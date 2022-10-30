import sqlite3


class User():

    def __init__(self, nome, dre, cpf):

        self.nome=nome
        self.dre=dre
        self.cpf=cpf

    #usado tanto para logar o usuario quanto para desloga-lo
    def logar(self, a, b, c):

        self.nome=a
        self.dre=b
        self.cpf=c

#inicia a variavel que determina o usuario logado
global user
user = User("","","")

#inicia o banco de dados
db = sqlite3.connect('db.sqlite') 
c = db.cursor()

c.execute('''
          CREATE TABLE IF NOT EXISTS alunos
          ([nome] STRING, [dre] STRING PRIMARY KEY, [cpf] STRING UNIQUE);
          ''')

db.commit()

#define a funcao para resgistrar um usuario no banco de dados
def s_up(nome, dre, cpf):

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
        c.execute("INSERT INTO alunos VALUES ('"+nome+"','"+dre+"','"+cpf+"')")

        db.commit()

        #define o usuario como logado
        user.logar( nome, dre, cpf)
        
        return True
    else:
        return False

#define a funcao de verificar se o usuario existe
def s_in(dre, cpf):

    #cria uma tupla para comparar com as tuplas do banco de dados
    test = (dre, cpf)

    db = sqlite3.connect('db.sqlite') 
    c = db.cursor()

    #cria uma lista com todos os usuarios do banco de dados
    users = c.execute("SELECT * FROM alunos").fetchall()

    db.commit()

    #procura uma correspondencia da trupla(test) no banco de dados
    for i in users:

        #compara o dre e o cpf
        if test==i[1:3]:

            #define o usuario logado
            user.logar( i[0], dre, cpf)
            
            return True
    return False