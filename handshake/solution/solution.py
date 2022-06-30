#!/usr/bin/python3
from scapy.all import *

DEFAULT = {
   'destination': ('10.222.1.2', 8998),  # SERVER default IP and PORT
   'source_port': 9999,  # Client port, can be anything in a valid range
}

def Ip_Server(server_ip):
    i=IP()
    i.dst = server_ip
    return i

def Tcp_Server(server_port, source_port):
    t=TCP()
    t.dport = server_port
    t.sport = source_port
    t.seq=100
    return t

def Send_Syn(ip, tcp):
    tcp.flags="S"
    return sr1(ip/tcp)

def Send_Ack(ip, tcp, resp_Syn):
    tcp.ack=resp_Syn.seq+1
    tcp.seq=tcp.seq+1
    tcp.flags="A"
    return sr1(ip/tcp)

def Hand_Shake(server_ip, server_port, source_port):
    ip=Ip_Server(server_ip)
    tcp=Tcp_Server(server_port, source_port)
    resp_Syn=Send_Syn(ip, tcp)
    resp_ack=Send_Ack(ip, tcp, resp_Syn)
    return resp_ack

def main():
    """
    Change this method HOWEVER you want, remove prints, do clean, modular, reusable
    code. :D
    """
    server_ip, server_port = DEFAULT['destination']
    source_port=DEFAULT['source_port']

    print("This is the entrypoint")
    print(f"Prepare handshake with {server_ip} on port {server_port}")
    retorno = Hand_Shake(server_ip, server_port, source_port)
    print(retorno.show())
    

if __name__ == "__main__":
    main()
