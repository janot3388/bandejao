
#######################################################
                         # IMPORT DE BIBLIOTECAS E FUNÇÕES
from flask import Flask, request, send_file, render_template
from flask_qrcode import QRcode
import qrcode, time, datetime



########################## COMENTAR CASO TESTAR QRCODE DIRETO SEM USAR DB !!
#from db import user      # Importa dados do usuario
#nome=user.nome, cpf=user.cpf, dre=user.dre



class QRCodeOBJ:                     # Classe geradora do QRcode
    def __init__(self,cpf,nome,dre):
        self.cpf = cpf
        self.nome = nome
        self.dre = dre
        self.qrdata = ("http://127.0.0.1:5000/lerQR/" + str(self.cpf) + "+" + str(self.dre) + "+" + self.nome + "/" )

    def qrmake(self):
        img = qrcode.make(self.qrdata)
        type(img)
        img.save("bandejao-main/bandejao copy/static/QRc.png")


###TESTE DE OBJ QRCODE
#p1 = QRCodeOBJ(cpf,nome,dre)
#p1.qrmake()


class Fila:                       # Classe geradora da fila de espera
    def __init__(self):
        pass


    def espera(self,h, m):        # Contador que simula tempo de espera da fila
        segundos = h * 60 + m     # OBS: UMA HORA É REPRESENTADA POR UM SEGUNDO
 
        while segundos > 0:
            # Timer representa tempo faltando, para exportar pro processamento
            timer = datetime.timedelta(seconds = segundos)

            # Espera um segundo enquanto conta um a menos na variável
            time.sleep(1)
            segundos -= 1
            
            if segundos == 15:
                
                filaquase = True
                print("A Fila esta quase acabando")

        filafim = True
        print("A fila acabou")

##### TESTE DA ESPERA
fila1 = Fila()
fila1.espera(0,20)