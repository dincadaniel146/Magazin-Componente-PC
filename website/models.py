from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Produse(db.Model):
    cod=db.Column(db.Integer,primary_key=True,autoincrement=True)
    marca=db.Column(db.String(150))
    model=db.Column(db.String(150))
    pret=db.Column(db.Integer)
    descriere=db.Column(db.String(150))
    stoc=db.Column(db.Integer)
    categorie=db.Column(db.String(150))
    imagine=db.Column(db.String(255),nullable=True)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    Nume = db.Column(db.String(150))


