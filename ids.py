from capture import capture_packet
from parser import parse_packet

def start_ids():
    # Start the IDS system
    print("Starting Intrusion Detection System...")
    # Add logic to initialize and run the IDS
    raw_packet = capture_packet()
    parsed_packet = parse_packet(raw_packet)
    # Display the parsed packet details
    print(f"Captured Packet: {parsed_packet}")
    pass