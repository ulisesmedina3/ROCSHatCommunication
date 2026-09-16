import threading

from rocs.packet import create_packet, parse_packet
from rocs.radio import SimulatedRadio


radio = SimulatedRadio(
    local_port=5005,
    remote_port=5006
)

sequence = 1


def receive_messages():
    while True:
        message = radio.receive()

        try:
            packet = parse_packet(message)

            if packet["destination"] == "ZERO":
                print(
                    f"\n[RECEIVED from {packet['source']}] "
                    f"{packet['message']}"
                )
                print("> ", end="", flush=True)

        except ValueError:
            print("\n[ERROR] Invalid ROCS packet")


receiver_thread = threading.Thread(
    target=receive_messages,
    daemon=True
)

receiver_thread.start()

print("ROCS Pi Zero online")
print("Type a message and press Enter.")
print("Type 'exit' to quit.\n")


while True:
    message = input("> ")

    if message.lower() == "exit":
        break

    packet = create_packet(
        source="ZERO",
        destination="PI4",
        packet_type="DATA",
        sequence=sequence,
        message=message
    )

    radio.send(packet)

    sequence += 1


radio.close()