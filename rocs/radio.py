import socket
import serial


class Radio:
    def __init__(
        self,
        port="/dev/serial0",
        baudrate=9600,
        simulate=False,
        host="127.0.0.1",
        udp_port=5005
    ):
        self.port = port
        self.baudrate = baudrate
        self.simulate = simulate
        self.host = host
        self.udp_port = udp_port

        self.serial_connection = None
        self.socket = None

        if self.simulate:
            self.socket = socket.socket(
                socket.AF_INET,
                socket.SOCK_DGRAM
            )
        else:
            self.serial_connection = serial.Serial(
                port=self.port,
                baudrate=self.baudrate,
                timeout=1
            )

    def send(self, message):
        if self.simulate:
            self.socket.sendto(
                message.encode("utf-8"),
                (self.host, self.udp_port)
            )

            print(f"[SIMULATED RADIO] TX -> {message}")
            return

        data = (message + "\n").encode("utf-8")
        self.serial_connection.write(data)

    def receive(self):
        if self.simulate:
            self.socket.bind(
                (self.host, self.udp_port)
            )

            data, address = self.socket.recvfrom(1024)

            return data.decode("utf-8")

        if self.serial_connection.in_waiting > 0:
            data = self.serial_connection.readline()

            return data.decode("utf-8").strip()

        return None

    def close(self):
        if self.serial_connection:
            self.serial_connection.close()

        if self.socket:
            self.socket.close()