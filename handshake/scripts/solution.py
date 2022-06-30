#!/usr/bin/python3
from scapy.all import *

DEFAULT = {
    'destination': ('10.222.1.2', 8998),  # SERVER default IP and PORT
    'source_port': 9999,  # Client port, can be anything in a valid range
}

def handShake(server_ip, server_port):
    i=IP()
    i.dst = server_ip   #atribui o IP do server
    i.display()         #mostra as infos no terminal 
    t=TCP()     
    t.port=server_port  #atribui a porta do server
    t.flags="S"         #atribui a flag Syn pro server
    t.display()         #mostra as infos no terminal

    sr1(i/t)            #envia o pacote i/t pro server e finaliza a conexão na primeira resposta

    t.flags= "A"        #atribui a flag Ack pro server como resposta ao que vem do syn
    t.seq = t.seq+1     #atribui + 1 a seq de t para responder ao server
    i.ack = i.ack+1     #atribui + 1 no ack de i para responder ao server
    sr1(i/t)            #envia o pacote i/t pro server e finaliza a conexão na primeira resposta

def main():
    """
    Change this method HOWEVER you want, remove prints, do clean, modular, reusable
    code. :D
    """
    server_ip, server_port = DEFAULT['destination']
    print("This is the entrypoint")
    print(f"Prepare handshake with {server_ip} on port {server_port}")
    handShake(server_ip, server_port)

if __name__ == "__main__":
    main()
