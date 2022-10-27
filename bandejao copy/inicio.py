from flask import render_template, Flask
from flask_login import LoginManager, UserMixin, login_required

app = Flask(__name__)



@app.route("/")
def home():
    return render_template("home.html")

@app.route("/fila")
def fila():
    return render_template("fila.html")



@app.route("/profile")
@login_required
def profile():
    return render_template("profile.html")

@app.route("/cardapio")
def cardapio():
    return render_template("cardapio.html")

@app.route("/sign_in")
def sign_in():
    return render_template("sign_in.html")

@app.route("/sign_up")
def sign_up():
    return render_template("sign_up.html")




app.run()