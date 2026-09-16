from rocs.packet import parse_packet
from rocs.radio import Radio


radio = Radio(simulate=True)

print("ROCS Pi 4 receiver ready...")
print("Waiting for transmission...\n")

message = radio.receive()

packet = parse_packet(message)

print("Packet received!")
print(f"Source:      {packet['source']}")
print(f"Destination: {packet['destination']}")
print(f"Message:     {packet['message']}")

radio.close()