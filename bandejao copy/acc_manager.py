from nav import app, User, db
from flask import render_template, request

@app.route("/sign_in", methods = ["POST"])
def sign_in_post():
    if request.method == "POST":
        DRE = request.form.get('DRE')
        CPF = request.form.get('CPF')
        remember = True if request.form.get('remember') else False

        user = User.query.filter_by(DRE=DRE).first()
    return render_template("home.html")