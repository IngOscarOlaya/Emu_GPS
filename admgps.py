from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QTextEdit
from PyQt5.QtCore import Qt, QTimer, QCoreApplication
from datetime import datetime
import serial

class admGPS(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: lightgrey; border: 2px solid white;")
        
        self.tramaText = QTextEdit()
        self.tramaText.setReadOnly(True)
        self.tramaText.setFontPointSize(12)
        
        stopButton = QPushButton("Stop")
        stopButton.setStyleSheet("background-color: lightgrey; font: bold 14px;")
        stopButton.clicked.connect(self.closeApp)
        
        adminLayout = QVBoxLayout(self)
        adminLayout.addWidget(self.tramaText)
        adminLayout.addWidget(stopButton, 0, Qt.AlignTop)
        adminLayout.addStretch()  # Empuja el botón hacia arriba
        
        # Configuración del puerto serial
        self.serial_port = serial.Serial(port='COM1', baudrate=4800, timeout=1)  # Cambia 'COM3' por el puerto correcto
        
        # Temporizador para actualizar la trama NMEA 0183
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateTrama)
        self.timer.start(100)  # 10 Hz (100 ms)
    
    def closeApp(self):
        self.serial_port.close()  # Cerrar el puerto serial al cerrar la aplicación
        QCoreApplication.instance().quit()

    def updateTrama(self):
        # Datos fijos para la trama
        lat = "1030.0000,N"  # Grados y minutos
        lon = "07530.0000,W"  # Grados y minutos
        speed = "000.0"  # Velocidad en nudos
        cog = "090.0"  # Rumbo en grados
        
        # Obtener la hora actual en formato HHMMSS
        current_time = datetime.now().strftime("%H%M%S")
        
        # Trama NMEA 0183 de ejemplo
        trama = f"$GPRMC,{current_time},A,{lat},{lon},{speed},{cog},270394,003.1,W*6A\r\n"
        
        # Mostrar la trama en el cuadro de texto, agregando la nueva trama al final
        self.tramaText.append(trama)
        
        # Hacer scroll automáticamente hasta la última trama añadida
        self.tramaText.verticalScrollBar().setValue(self.tramaText.verticalScrollBar().maximum())
        
        # Enviar la trama por el puerto serial
        self.serial_port.write(trama.encode('ascii'))
