from flask import render_template, request, redirect, url_for, flash
from db import app, s_in, s_up
#Renderização das paginas

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/fila")
def fila():
    return render_template("fila.html")

@app.route("/cardapio")
def cardapio():
    return render_template("cardapio.html")

@app.route("/sign_in")
def sign_in():
    flash("")
    return render_template("sign_in.html")

@app.route("/sign_up")
def sign_up():
    flash ("")
    return render_template("sign_up.html")

#Processamento de dados

@app.route('/sign_in', methods=['POST'])
def sign_in_post():
    
    dre = int (request.form.get('DRE'))
    cpf = int (request.form.get('CPF'))

    if s_in(dre, cpf): 
        return redirect(url_for('home_'))
    else:
        return redirect(url_for('sign_in'))
    

@app.route('/sign_up', methods=['POST'])
def sign_up_post():
    
    nome = request.form['nome']
    dre = request.form['DRE']
    cpf = request.form['CPF']

    if s_up(nome, dre, cpf):
        
        
        return redirect(url_for('home_'))
    else:
        
        return redirect(url_for('sign_up'))


@app.route("/home")
def home_():
    return render_template("home2.html")

@app.route("/filal")
def fila_():
    return render_template("fila2.html")

@app.route("/cardapiol")
def cardapio_():
    return render_template("cardapio2.html")


@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/logout")
def logout(): 
    return redirect(url_for('home'))


@app.route("/filal", methods=["POST"])
def entar_fila():
    if request.button:
        print ("foi")

app.run()
