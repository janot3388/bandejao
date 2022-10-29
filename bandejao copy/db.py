from flask import render_template, Flask, request, redirect, url_for, flash
import sqlite3


app = Flask(__name__)

app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'

db = sqlite3.connect('db.sqlite') 
c = db.cursor()

c.execute('''
          CREATE TABLE IF NOT EXISTS alunos
          ([nome] STRING, [dre] STRING PRIMARY KEY, [cpf] STRING UNIQUE);
          ''')

db.commit()


def s_up(nome, dre, cpf):

    db = sqlite3.connect('db.sqlite') 
    c = db.cursor()
    reg = c.execute("SELECT [nome] FROM alunos where cpf = '"+cpf+"'").fetchall()
    db.commit()
    
    if len(reg)==0:
    
        db = sqlite3.connect('db.sqlite') 
        c = db.cursor()
        c.execute("INSERT INTO alunos VALUES ('"+nome+"','"+dre+"','"+cpf+"')")
        db.commit()

        print (201)
        return True
    else:
        flash('credênciais já estão cadastradas')
        return False
        
def s_in(dre, cpf):
    test = (dre, cpf)

    db = sqlite3.connect('db.sqlite') 
    c = db.cursor()
    users = c.execute("SELECT * FROM alunos").fetchall()
    db.commit()

    for i in users:
        if test==i[1:3]:
            return True
    flash('credênciais não foram encontradas')
    return False