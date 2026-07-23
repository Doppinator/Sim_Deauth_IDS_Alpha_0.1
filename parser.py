def parse_packet(raw_packet):
    """ Parse a raw network packet and extract its details.
    
    Args:
        raw_packet (bytes): The raw network packet data.
    
    Returns:
        dict: A dictionary containing the parsed packet details.
    """
    # Placeholder for packet parsing logic
    packet_details = {
        "source_mac": "00:1A:2B:3C:4D:5E",
        "destination_mac": "5E:4D:3C:2B:1A:00",
        "protocol": "TCP",
        "type": "data"
    }
    return packet_details