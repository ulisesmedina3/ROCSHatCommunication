from rocs.packet import create_packet
from rocs.radio import Radio


radio = Radio(simulate=True)

packet = create_packet(
    source="ZERO",
    destination="PI4",
    message="Hello from Pi Zero"
)

radio.send(packet)
radio.close()