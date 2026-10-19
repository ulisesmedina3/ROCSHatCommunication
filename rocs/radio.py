import socket
import serial


class SimulatedRadio:
    def __init__(self, local_port, remote_port, host="127.0.0.1"):
        self.host = host
        self.local_port = local_port
        self.remote_port = remote_port

        self.socket = socket.socket(
            socket.AF_INET,
            socket.SOCK_DGRAM
        )

        self.socket.bind(
            (self.host, self.local_port)
        )

    def send(self, message):
        self.socket.sendto(
            message.encode("utf-8"),
            (self.host, self.remote_port)
        )

        print(f"[SIMULATED RADIO] TX -> {message}")

    def receive(self):
        data, address = self.socket.recvfrom(1024)

        return data.decode("utf-8")

    def close(self):
        self.socket.close()

class LoRaRadio:
    """Communicate with the Waveshare SX1262 UART LoRa HAT."""

    def __init__(self, port="/dev/ttyUSB0", baudrate=9600):
        self.serial_connection = serial.Serial(
            port=port,
            baudrate=baudrate,
            timeout=0.2
        )

    def send(self, message):
        data = (message + "\n").encode("utf-8")
        self.serial_connection.write(data)
        self.serial_connection.flush()
        print(f"[LORA TX] {message}")

    def receive(self):
        data = self.serial_connection.readline()

        if data:
            return data.decode("utf-8", errors="replace").strip()

        return None

    def close(self):
        self.serial_connection.close()