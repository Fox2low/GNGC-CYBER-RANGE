import time
import threading
import socket
import sys

# Global variable to control packet transmission
transmit_packet = False

def send_udp_packet(ip, port, message):
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.sendto(message.encode(), (ip, port))
    udp_socket.close()

def send_udp_packet_periodically(ip, port, message, interval):
    global transmit_packet

    while transmit_packet:
        send_udp_packet(ip, port, message)
        time.sleep(interval)

if __name__ == "__main__":
    target_ip = "127.0.0.1"  # Replace this with the destination IP address
    target_port = 12345      # Replace this with the destination port
    message_to_send = "Hello!"
    interval_seconds = 30    # Packet transmission interval in seconds

    if len(sys.argv) != 2 or sys.argv[1] not in ["on", "off"]:
        print("Usage: python script_name.py [on|off]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "on":
        if not transmit_packet:
            transmit_packet = True
            print("UDP packet transmission started!")
            threading.Thread(target=send_udp_packet_periodically, args=(target_ip, target_port, message_to_send, interval_seconds), daemon=True).start()
        else:
            print("UDP packet transmission is already on!")
    elif command == "off":
        if transmit_packet:
            transmit_packet = False
            print("UDP packet transmission turned off.")
        else:
            print("UDP packet transmission is already off.")
    else:
        print("Invalid command. Usage: python script_name.py [on|off]")
        sys.exit(1)

    while transmit_packet:
        time.sleep(1)