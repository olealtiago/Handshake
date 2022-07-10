#!/usr/bin/python3
from scapy.all import *

class Tcp:
    def __init__(self, dst, dport, sport):
        self.i=IP()
        self.i.dst=dst
        self.t=TCP()
        self.t.sport=sport
        self.t.dport=dport
        self.resposta=None

    def Send_sin(self):
        self.t.flags='S'
        self.resposta=sr1(self.i/self.t) 

    def Send_ack(self, ack, seq):
        self.t.flags='A'
        self.t.ack=ack
        self.t.seq=seq
        send(self.i/self.t)

    def Connect(self):
        self.Send_sin()
        self.Send_ack(self.resposta.seq+1, 1)
    
    def Send_message(self, message):
        self.t.flags="PA"
        self.resposta=sr1(self.i/self.t/message)
        self.t.seq+=len(message)

    def Disconnect(self):
        self.t.flags="FA"
        self.resposta=sr1(self.i/self.t)
        self.Send_ack(self.resposta.seq+1, self.resposta.ack)


connexao1=Tcp('10.222.1.2', 8998, 9999)

connexao1.Connect()
connexao1.Send_message("teste1")
connexao1.Send_message("teste2")
connexao1.Send_message("teste3")
connexao1.Send_message("teste4")
connexao1.Send_message("teste5")
connexao1.Disconnect()
