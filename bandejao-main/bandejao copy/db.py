import datetime
import sqlite3


class User():

    def __init__(self, nome, dre, senha):

        self.nome=nome
        self.dre=dre
        self.senha=senha
        self.chave = "nada"      
        self.lugar= "nada"

    #usado tanto para logar o usuario quanto para desloga-lo
    def logar(self, a, b, c):

        self.nome=a
        self.dre=b
        self.senha=c

#inicia a variavel que determina o usuario logado
global user
user = User("","","")

#inicia o banco de dados
db = sqlite3.connect('db.sqlite') 
c = db.cursor()


######### CRIEI TABLE QUE LISTA ALUNOS QUE ENTRARAM NO BANDEJÃO + HORARIO EM QUE ENTRARAM (DELETA SE DER MERDA)
c.execute('''
          CREATE TABLE IF NOT EXISTS alunos
          ([nome] STRING, [dre] STRING PRIMARY KEY, [senha] STRING UNIQUE);
          ''')

c.execute('''
          CREATE TABLE IF NOT EXISTS alocados
          ([nome] STRING, [dre] STRING , [senha] STRING, [tempo] TEXT PRIMARY KEY);
          ''')


db.commit()

#define a funcao para resgistrar um usuario no banco de dados
def s_up(nome, dre, senha):

    db = sqlite3.connect('db.sqlite') 
    c = db.cursor()

    #procura se ja existe um usuario com aquele dre, sendo que o dre e a chave primaria
    reg = c.execute("SELECT [nome] FROM alunos where dre = '"+dre+"'").fetchall()

    db.commit()
    
    #caso nao ache nenhum o resultado sera uma lista de zero elementos
    if len(reg)==0:
    
        db = sqlite3.connect('db.sqlite') 
        c = db.cursor()

        #inclui o novo usuario no banco de dados
        c.execute("INSERT INTO alunos VALUES ('"+nome+"','"+dre+"','"+senha+"')")

        db.commit()

        #define o usuario como logado
        user.logar( nome, dre, senha)
        
        return True
    else:
        return False

#define a funcao de verificar se o usuario existe
def s_in(dre, senha):

    #cria uma tupla para comparar com as tuplas do banco de dados
    test = (dre, senha)

    db = sqlite3.connect('db.sqlite') 
    c = db.cursor()

    #cria uma lista com todos os usuarios do banco de dados
    users = c.execute("SELECT * FROM alunos").fetchall()

    db.commit()

    #procura uma correspondencia da trupla(test) no banco de dados
    for i in users:

        #compara o dre e o senha
        if test==i[1:3]:

            #define o usuario logado
            user.logar( i[0], dre, senha)
            
            return True
    return False


############## FUNÇÃO QUE INSERE ALUNOS QUE ENTRARAM NO BANDEJÃO NO X DIA E HORA, NO DB alocados
def alocar(senha,nome,dre):
    db = sqlite3.connect('db.sqlite') 
    c = db.cursor()
    tempo = str(datetime.datetime.now())

    c.execute("INSERT INTO alocados VALUES ('"+nome+"','"+dre+"','"+senha+"','"+tempo+"')")

    db.commit()

'''
def admprint():
    db = sqlite3.connect('db.sqlite') 
    c = db.cursor()
    c.execute("SELECT * FROM alocados")  

    for row in c:
    
        print(row)
'''

def admshow(): #EXPORTA O HISTÓRICO DE ACESSOS AO BANDEJAO PARA EXIBIR NA PAGINA ADMINISTRATIVA
    conn = sqlite3.connect('db.sqlite')
    c = conn.cursor()
    c.execute('SELECT nome, dre, senha, tempo FROM alocados')    
    rows = c.fetchall()
    return rows