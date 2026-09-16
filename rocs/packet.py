def create_packet(source, destination, message):
    packet = f"ROCS|{source}|{destination}|{message}"
    return packet


def parse_packet(packet):
    parts = packet.split("|")

    if len(parts) != 4:
        raise ValueError("Invalid ROCS packet")

    protocol = parts[0]
    source = parts[1]
    destination = parts[2]
    message = parts[3]

    if protocol != "ROCS":
        raise ValueError("Not a ROCS packet")

    return {
        "source": source,
        "destination": destination,
        "message": message
    }