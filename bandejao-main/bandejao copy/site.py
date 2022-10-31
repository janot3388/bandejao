from flask import render_template, request, redirect, url_for, flash, Flask
from db import s_in, s_up

#criando o site
app = Flask(__name__)
app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'

            #RENDERIZACAO DAS PAGINAS

#ainda a implementar
@app.route("/adm")
def adm():
    return render_template("adm.html")

#rota padrão
@app.route("/")
def home():

    #todas as rotas de renderização possuem essa verificacao caso alguem esteja logado
    from db import user
    log=s_in(user.dre, user.cpf)

    #carrega o template de home
    return render_template("home.html", log=log)

        #ROTAS DA NAVBAR

#visualizar o tempo de cada fila
@app.route("/fila")
def fila():

    from db import user
    log=s_in(user.dre, user.cpf)

    #carrega o template de fila
    return render_template("fila.html", ct="55", central="75", letras="45", log=log)

#visualizar o cardapio do dia
@app.route("/cardapio")
def cardapio():

    from db import user
    log=s_in(user.dre, user.cpf)

    #carrega o template de cardapio
    return render_template("cardapio.html", salad="alface e cenora", carne="churrasco misto", vegan="quiche", sobremesa="pera", log=log)


        #OPCOES DA BARRA DE TOPO

#ir para o login
@app.route("/sign_in")
def sign_in():

    from db import user
    log=s_in(user.dre, user.cpf)

    #carrega o template de sign in
    return render_template("sign_in.html", log=log)

#ir para o cadastro
@app.route("/sign_up")
def sign_up():

    from db import user
    log=s_in(user.dre, user.cpf)

    #carrega o template de sign up
    return render_template("sign_up.html", log=log)

#ir para o perfil
@app.route("/profile")
def profile():

    from db import user
    log=s_in(user.dre, user.cpf)

    #carrega o template do perfil
    return render_template("profile.html", nome=user.nome, cpf=user.cpf, dre=user.dre, log=log)

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
    
    #a utilização do comand int() será explicada no banco de dados
    dre = int (request.form.get('DRE'))
    cpf = int (request.form.get('CPF'))

    #a função s_in retorna True caso os dados tenham correspondencia no banco de dados
    if s_in(dre, cpf): 
        
        return redirect(url_for('home'))

    else:

        flash('credênciais não foram encontradas')

        return redirect(url_for('sign_in'))
    
#processa os dados para o cadastro
@app.route("/sign_up", methods=['POST'])
def sign_up_post():
    
    nome = request.form['nome']
    dre = request.form['DRE']
    cpf = request.form['CPF']

    #a função s_up retorna True caso os dados já não tenham uma instância no banco de dados
    if s_up(nome, dre, cpf):

        return redirect(url_for('home'))

    else:

        flash('credênciais já estão cadastradas')

        return redirect(url_for('sign_up'))

#processa a escolha do bandejao a se entrar na fila
@app.route("/fila", methods=['POST'])
def entar_fila():
    from db import user
    log=s_in(user.dre, user.cpf)
    global lugar
    
    lugar = (request.form.get('place'))
    int(lugar)

    #print (lugar)
    return redirect("/aguardando")


#renderiza a aba de espera antes da função
@app.route("/aguardando")
def switch():
    
    from db import user
    log=s_in(user.dre, user.cpf)

    return render_template("aguardando.html",log=log)

#inicia a função de espera
@app.route("/aguardo")
def aguardar(): 

    from control import Fila
    wait = Fila()
    wait.esperar(int(lugar))
    print("$$$$$$$$$$$$")


    return redirect("/qrcode")

#renderiza a aba de geração do QRcode + função que gera o mesmo
@app.route("/qrcode")
def gerar_qr():

    from control import QRCodeOBJ
    from db import user
    log=s_in(user.dre, user.cpf)
    
    codigo = QRCodeOBJ(user.cpf,user.nome,user.dre)
    codigo.qrmake()

    return render_template("qrcode.html", log=log)


################################

@app.route("/lerQR")
def leitura():

    from db import user
    from flask import request
    log=s_in(user.dre, user.cpf)
    

    cpfL= request.args.get('cpf')
    print(cpfL)
    dreL= request.args.get('dre')
    print(dreL)
    nomeL = request.args.get('nome')
    print(nomeL)
    keyL = request.args.get('k')[0:-1]
    print(keyL)


    return render_template("lerQR.html", log=log)






#rodar as rotas no site
app.run()
