#!/usr/bin/python3
from multiprocessing import connection
from scapy.all import *

# connectio_tcp = None

class Tcp:
    def __init__(self, dst, dport, sport):
        self.i = IP()
        self.i.dst = dst
        self.t = TCP()
        self.t.sport = sport
        self.t.dport = dport
        self.resposta = None

    def Send_sin(self):
        self.t.flags = 'S'
        self.resposta = sr1(self.i/self.t) 

    def Send_ack(self, ack, seq):
        self.t.flags = 'A'
        self.t.ack = ack
        self.t.seq = seq
        send(self.i/self.t)

    def Connect(self):
        self.Send_sin()
        self.Send_ack(self.resposta.seq+1, 1)
    
    def Send_message(self, message):
        self.t.flags = "PA"
        self.resposta = sr1(self.i/self.t/message)
        self.t.seq += len(message)

    def Disconnect(self):
        self.t.flags = "FA"
        self.resposta = sr1(self.i/self.t)
        self.Send_ack(self.resposta.seq+1, self.resposta.ack)

# def Conection():
ip = input("Digite o Ip que deseja conectar:\t")
dport = int(input("Digite a porta TCP de destino:\t"))
sport = int(input("Digite a porta TCP de origem:\t"))
connection_tcp = Tcp(ip, dport, sport)
connection_tcp.Connect()

while(True):
    opc = input("Digite a opcao que deseja:\n d = Desconectar \n s = Enviar mensagem) ")
    if(opc == 'd'):
        connection_tcp.Disconnect()
        break
    elif(opc == 's'):
        msg = input("Digite a mensagem a ser enviada:\n")
        connection_tcp.Send_message(msg)
    else:
        print('Opcao invalida\n')