def create_packet(source, destination, packet_type, sequence, message):
    return f"ROCS|{source}|{destination}|{packet_type}|{sequence}|{message}"


def parse_packet(packet):
    parts = packet.split("|")

    if len(parts) != 6:
        raise ValueError("Invalid ROCS packet")

    protocol, source, destination, packet_type, sequence, message = parts

    if protocol != "ROCS":
        raise ValueError("Not a ROCS packet")

    return {
        "source": source,
        "destination": destination,
        "type": packet_type,
        "sequence": int(sequence),
        "message": message
    }