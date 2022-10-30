from flask import Flask, request, send_file, render_template
from flask_qrcode import QRcode
import qrcode


from db import user      #importa dados do usuario
nome=user.nome, cpf=user.cpf, dre=user.dre

class QRCodee:           #classe geradora do QRcode
    def __init__(self,cpf,nome,dre):
        self.cpf = cpf
        self.nome = nome
        self.dre = dre
        self.qrdata = ("http://127.0.0.1:5000/lerQR/" + str(self.cpf) + "+" + str(self.dre) + "+" + self.nome + "/" )

    def qrmake(self):
        img = qrcode.make(self.qrdata)
        type(img)
        img.save("bandejao copy/static/QRc.png")


p1 = QRCodee(144934888400,"Janot_de_Carvalho",122072511)
p1.qrmake()