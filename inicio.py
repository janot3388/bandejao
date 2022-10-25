from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/cardapio")
def cardapio():
    return render_template("cardapio.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/fila")
def fila():
    return render_template("fila.html")

app.run()
