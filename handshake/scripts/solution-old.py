#!/usr/bin/python3
from scapy.all import *

DEFAULT = {
    'destination': ('10.222.1.2', 8998),  # SERVER default IP and PORT
    'source_port': 9999,  # Client port, can be anything in a valid range
}


def main():
    """
    Change this method HOWEVER you want, remove prints, do clean, modular, reusable
    code. :D
    """
    server_ip, server_port = DEFAULT['destination']
    print("This is the entrypoint")
    print(f"Prepare handshake with {server_ip} on port {server_port}")


if __name__ == "__main__":
    main()
