import serial


class Radio:
    def __init__(self, port="/dev/serial0", baudrate=9600, simulate=False):
        self.port = port
        self.baudrate = baudrate
        self.simulate = simulate
        self.serial_connection = None

        if not self.simulate:
            self.serial_connection = serial.Serial(
                port=self.port,
                baudrate=self.baudrate,
                timeout=1
            )

    def send(self, message):
        if self.simulate:
            print(f"[SIMULATED RADIO] TX -> {message}")
            return

        data = (message + "\n").encode("utf-8")
        self.serial_connection.write(data)

    def receive(self):
        if self.simulate:
            return None

        if self.serial_connection.in_waiting > 0:
            data = self.serial_connection.readline()
            return data.decode("utf-8").strip()

        return None

    def close(self):
        if self.serial_connection:
            self.serial_connection.close()