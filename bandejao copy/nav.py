from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from inicio import app

db = SQLAlchemy()

db.init_app(app)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    DRE = db.Column(db.String(9), unique=True)
    CPF = db.Column(db.String(11))
    name = db.Column(db.String(100))