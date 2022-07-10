#!/usr/bin/python3
from scapy.all import *

DEFAULT = {
   'destination': ('10.222.1.2', 8998),  # SERVER default IP and PORT
   'source_port': 9999,  # Client port, can be anything in a valid range
}

#inicializar um obj "connection"
#atribuir valores do default
#chamar metodo "connect"
#chamar metodo "sendmessage" (enviar 5 mensagens diferentes)
#chamar metodo "disconnect"
#sair do programa
def main():



# ------------------
    i=IP()
    i.dst="10.222.1.2"
    i.display() 
    t=TCP()
    t.dport=8998
    t.sport=9999
    t.flags="S"
    t.display()
    resposta=sr1(i/t) 
    t.flags="A"
    t.ack=resposta.seq+1	
    t.seq=1
    send(i/t)

    mensagem="teste\r\n"

    # for vez in range (1, 5):
    t.flags="PA"
    resposta=sr1(i/t/mensagem)
    t.seq+=len(mensagem)

    t.flags="FA"
    resposta=sr1(i/t)
    t.flags="A"
    t.seq=resposta.ack
    t.ack=resposta.seq+1
    send(i/t)

# ------------------

if __name__ == "__main__":
    main()
