from parser import parse_packet


def extract_packet_features(packet_details):
    """ Extract features from parsed packet details.    """     
    packet_features = {
        "source_mac": packet_details.get("source_mac"),
        "frame_type": packet_details.get("frame_type"),
        "frame_subtype": packet_details.get("frame_subtype"),
        "timestamp": packet_details.get("timestamp"),
        "is_management_frame": packet_details.get("frame_type") == "management",
        "is_deauthentication_frame": packet_details.get("frame_subtype") == "deauthentication"
    }
    return packet_features