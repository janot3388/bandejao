from ctypes.wintypes import LCTYPE
from operator import and_
from flask import render_template, request, redirect, url_for, flash, Flask
from db import s_in, s_up

#criando o site
app = Flask(__name__)
app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'


            #RENDERIZACAO DAS PAGINAS



# PAGINA DE ADMINISTRADOR E DEV
@app.route("/adm", methods=['POST','GET'])
def adm():
    from control import Fila, filaCT, filaCe, filaLe

    admin = Fila()
    acao = request.form.get('actionf') 

    print(filaCT),print(filaCe),print(filaLe)

    dre = "admin"
    lct = "ct"
    lce = "ce"
    lle = "le"

    print(acao) #INSERÇÃO MANUAL DE CLIENTES NAS FILAS

    if acao == 'cti':
        admin.entra(dre,lct)
    elif acao == 'ctd':
        admin.sai(lct)
    elif acao == 'cei':
        admin.entra(dre,lce)
    elif acao == 'ced':
        admin.sai(lce)
    elif acao == 'lei':
        admin.entra(dre,lle)
    elif acao == 'led':
        admin.sai(lle)



    return render_template("adm.html", ct=len(filaCT),ce=len(filaCe),le=len(filaLe))

#SEÇÃO QUE MOSTRA HISTÓRICO DE ACESSOS AO BENDEJAO
@app.route("/database")
def show():
    from db import admshow
    rows = admshow()
    print (rows)
    return render_template('database.html', rows=rows)


#rota padrão
@app.route("/")
def home():

    #todas as rotas de renderização possuem essa verificacao caso alguem esteja logado
    from db import user
    log=s_in(user.dre, user.senha)


    #carrega o template de home
    return render_template("home.html", log=log)

        #ROTAS DA NAVBAR

#visualizar o tempo de cada fila
@app.route("/fila")
def fila():

    from db import user
    log=s_in(user.dre, user.senha)

    #carrega o template de fila
    return render_template("fila.html", ct="55", central="75", letras="45", log=log)



#visualizar o cardapio do dia
@app.route("/cardapio")
def cardapio():

    from db import user
    log=s_in(user.dre, user.senha)

    #carrega o template de cardapio
    return render_template("cardapio.html", salad="alface e cenora", carne="churrasco misto", vegan="quiche", sobremesa="pera", log=log)


        #OPCOES DA BARRA DE TOPO

#ir para o login
@app.route("/sign_in")
def sign_in():

    from db import user


    log=s_in(user.dre, user.senha)

    #carrega o template de sign in
    return render_template("sign_in.html", log=log)

#ir para o cadastro
@app.route("/sign_up")
def sign_up():

    from db import user
    log=s_in(user.dre, user.senha)

    #carrega o template de sign up
    return render_template("sign_up.html", log=log)

#ir para o perfil
@app.route("/profile")
def profile():

    from db import user
    log=s_in(user.dre, user.senha)

    #carrega o template do perfil
    return render_template("profile.html", nome=user.nome, senha=user.senha, dre=user.dre, log=log)

#deslogar
@app.route("/logout")
def logout(): 

    from db import user

    #retira as credenciais do usuario atual de user
    user.logar("","","")

    return redirect(url_for('home'))

            #RECOLHENDO OS DADOS

#processa os dados para o login
@app.route("/sign_in", methods=['POST'])
def sign_in_post():
    

    dre = (request.form.get('DRE'))
    senha = (request.form.get('senha'))

    #login especial
    if dre == 'admin' and senha == 'admin':
        return redirect("/adm")

    #a utilização do comand int() será explicada no banco de dados
    dre=int(dre)
    senha=int(senha)


    #a função s_in retorna True caso os dados tenham correspondencia no banco de dados
    if s_in(dre, senha): 
        
        return redirect(url_for('home'))

    else:

        flash('credênciais não foram encontradas')

        return redirect(url_for('sign_in'))
    
#processa os dados para o cadastro
@app.route("/sign_up", methods=['POST'])
def sign_up_post():
    
    nome = request.form['nome']
    dre = request.form['DRE']
    senha = request.form['senha']

    #a função s_up retorna True caso os dados já não tenham uma instância no banco de dados
    if s_up(nome, dre, senha):

        return redirect(url_for('home'))

    else:

        flash('credênciais já estão cadastradas')

        return redirect(url_for('sign_up'))

#processa a escolha do bandejao a se entrar na fila
@app.route("/fila", methods=['POST'])
def entar_fila():
    from db import user
    log=s_in(user.dre, user.senha)
    global lugar
    
    lugar = (request.form.get('place'))

    #print (lugar)
    return redirect("/aguardando")


#renderiza a aba de espera antes da função
@app.route("/aguardando")
def switch():
    
    from db import user
    log=s_in(user.dre, user.senha)

    return render_template("aguardando.html",log=log)

#ENTRA NA FILA

@app.route("/aguardo")
def aguardar(): 

    from db import user
    from control import Fila
    global wait
    wait = Fila()
    
    user.lugar = lugar
    
    #wait.esperar(int(lugar))
    #print("$$$$$$$$$$$$")
   
    wait.entra(user.dre,user.lugar)
    return redirect("/aguardo2")

#SEGUNDA ABA PARA ESTADO DE LOOP ENQUANTO O CLIENTE NÃO ESTIVER NA SUA VEZ DA FILA
@app.route("/aguardo2")
def aguardar2():
    from db import user
    from control import Fila
    import time
    
    #CHECA SE POSIÇÃO É A PRIMEIRA
    Check = wait.check(user.dre,user.lugar)
    print(Check)

    #LOOP QUE ESPERA A VEZ
    while True:
        if Check == True:
            break
        else:
            time.sleep(2)
            return redirect("/aguardo2")

    return redirect("/qrcode") 
    



#renderiza a aba de geração do QRcode + função que gera o mesmo
@app.route("/qrcode")
def gerar_qr():

    from control import QRCodeOBJ
    from db import user
    log=s_in(user.dre, user.senha)
    
    # GERA QR
    link = QRCodeOBJ(user.senha,user.nome,user.dre)
    link.qrmake()

    #QUANDO QR CODE É GERADO, VAR CHAVE DO USUARIO É ATUALIZADA PARA AUTH FUTURA NA ENTRADA DO BANDEJAO
    user.chave = link.chave 



    return render_template("qrcode.html", log=log)



# ROTA DE LEITURA DO QR CODE

@app.route("/lerQR")
def leitura():

    from db import user
    from flask import request
    log=s_in(user.dre, user.senha)
    
#RECEBE VALORES DOS PARAMETROS DO LINK PERTENCENTE AO QRCODE
    senhal= request.args.get('senha')
    print(senhal)
    dreL= request.args.get('dre')
    print(dreL)
    nomeL = request.args.get('nome')
    print(nomeL)
    keyL = request.args.get('k')[0:-1]
    print(keyL)



# VALIDAÇÃO DO CLIENTE NO BANDEJAO, E ALOCAÇÃO DO MESMO NO HISTÓRICO DE ACESSOS

    if keyL == user.chave: #VALIDA AUTENTICIDADE DA CHAVE TEMPORARIA DO CLIENTE
        
        from db import alocar
        from control import filaCe,filaCT,filaLe,Fila

        alocar(senhal,nomeL,dreL)

        user.chave = 'expirado'
        
        delete = Fila()
        
        delete.sai(user.lugar)

        user.lugar = 'nada'

        return render_template("lerQR.html", log=log,)
    
    else:
        return render_template("badqr.html", log=log) #RETORNA QUE A CHAVE DE AUTH NÃO CONSTA




#rodar as rotas no site
app.run()
