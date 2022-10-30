
#######################################################
                         # IMPORT DE BIBLIOTECAS E FUNÇÕES
from flask import Flask, request, send_file, render_template
from flask_qrcode import QRcode
import qrcode, time, datetime



###################################################
from db import user      # Importa dados do usuario
nome=user.nome, cpf=user.cpf, dre=user.dre






class QRCodeOBJ:           # Classe geradora do QRcode
    def __init__(self,cpf,nome,dre):
        self.cpf = cpf
        self.nome = nome
        self.dre = dre
        self.qrdata = ("http://127.0.0.1:5000/lerQR/" + str(self.cpf) + "+" + str(self.dre) + "+" + self.nome + "/" )

    def qrmake(self):
        img = qrcode.make(self.qrdata)
        type(img)
        img.save("bandejao copy/static/QRc.png")


p1 = QRCodeOBJ(144934888400,"Janot_de_Carvalho",122072511)
p1.qrmake()


class Fila:
    def __init__(self):


        pass

    def espera(h, m):             # Contador que simula tempo de espera da fila
        segundos = h * 60 + m     # OBS: MINUTOS REAIS REPRESENTAM HORAS
 
        while segundos > 0:
 
            # Timer representa tempo faltando
            timer = datetime.timedelta(seconds = segundos)
        
            time.sleep(1)
            segundos -= 1
 
    print("cabou kk")
