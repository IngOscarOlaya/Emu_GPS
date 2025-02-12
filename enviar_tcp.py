import socket
import time
from datetime import datetime

def main():
    tcp_ip = "127.0.0.1"  # Dirección IP de destino
    tcp_port = 5005       # Puerto de destino
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Crear socket TCP
    sock.connect((tcp_ip, tcp_port))  # Conectar al servidor TCP

    while True:
        # Datos fijos para la trama
        lat = "1030.0000,N"  # Grados y minutos
        lon = "07530.0000,W"  # Grados y minutos
        speed = "000.0"  # Velocidad en nudos
        cog = "090.0"  # Rumbo en grados

        # Obtener la hora actual en formato HHMMSS
        current_time = datetime.now().strftime("%H%M%S")

        # Trama NMEA 0183 de ejemplo
        trama = f"$GPRMC,{current_time},A,{lat},{lon},{speed},{cog},270394,003.1,W*6A\r\n"

        # Enviar la trama por TCP
        sock.sendall(trama.encode('ascii'))
        print(f"Mensaje enviado: {trama}")

        time.sleep(1)  # Esperar 1 segundo antes de enviar el siguiente mensaje

if __name__ == "__main__":
    main()
