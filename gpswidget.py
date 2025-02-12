from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QFont
from datetime import datetime

class GPSWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        main_layout = QVBoxLayout(self)
        
        # First quadrant
        self.quadrant1 = QWidget()
        self.quadrant1.setStyleSheet("background-color: lightgrey; border: 2px solid white;")
        quadrant1_layout = QHBoxLayout(self.quadrant1)
        
        self.dateTimeLabel = QLabel()
        self.dateTimeLabel.setFont(QFont("Arial", 24))
        self.gpsLabel = QLabel("GPS CEDNAV")
        self.gpsLabel.setFont(QFont("Arial", 24))
        
        quadrant1_layout.addWidget(self.dateTimeLabel, 0, Qt.AlignLeft)
        quadrant1_layout.addWidget(self.gpsLabel, 0, Qt.AlignRight)
        
        # Second quadrant
        self.quadrant2 = QWidget()
        self.quadrant2.setStyleSheet("background-color: lightgrey; border: 2px solid white;")
        quadrant2_layout = QVBoxLayout(self.quadrant2)
        
        self.latitudeLabel = QLabel("Latitud: 10° 24.00' N")  # Coordenadas de Cartagena
        self.latitudeLabel.setFont(QFont("Arial", 24))
        self.longitudeLabel = QLabel("Longitud: 75° 30.00' W")  # Coordenadas de Cartagena
        self.longitudeLabel.setFont(QFont("Arial", 24))
        
        quadrant2_layout.addWidget(self.latitudeLabel)
        quadrant2_layout.addWidget(self.longitudeLabel)
        
        # Third quadrant
        self.quadrant3 = QWidget()
        self.quadrant3.setStyleSheet("background-color: lightgrey; border: 2px solid white;")
        quadrant3_layout = QHBoxLayout(self.quadrant3)
        
        self.speedLabel = QLabel("Speed: 0 Knt")
        self.speedLabel.setFont(QFont("Arial", 24))
        self.cogLabel = QLabel("COG: 090°")
        self.cogLabel.setFont(QFont("Arial", 24))
        
        quadrant3_layout.addWidget(self.speedLabel, 0, Qt.AlignLeft)
        quadrant3_layout.addWidget(self.cogLabel, 0, Qt.AlignRight)
        
        # Adding quadrants to the main layout
        main_layout.addWidget(self.quadrant1, 1)
        main_layout.addWidget(self.quadrant2, 3)
        main_layout.addWidget(self.quadrant3, 1)
        
        # Timer for date and time updates
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateDateTime)
        self.timer.start(1000)  # Update every second
        
        # Initial updates
        self.updateDateTime()
    
    def updateDateTime(self):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.dateTimeLabel.setText(current_time)
