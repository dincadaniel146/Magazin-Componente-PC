from flask import Blueprint,render_template,request,flash
from flask_login import login_required, current_user
from .models import Produse
from . import db



views = Blueprint('views', __name__)


@views.route('/',methods=['GET','POST'])
@login_required
def home():
    return render_template("index.html",user=current_user)
@views.route('/incarcarestoc',methods=['GET','POST'])
def incarcarestoc():
  if request.method== 'POST':
    cod3=request.form.get('cod3')
    stoc2=request.form.get('stoc2')
    db.session.query(Produse)\
       .filter(Produse.cod == cod3)\
       .update({Produse.stoc: Produse.stoc + stoc2})
    db.session.commit()
    flash('Stoc incarcat!', category='success')
  return render_template("incarcare_stoc.html",user=current_user)
@views.route('/vanzareprodus', methods=['GET','POST'])
def vanzare():
  if request.method== 'POST':
    cod2=request.form.get('cod2')
    stoc1=request.form.get('stoc1')
    db.session.query(Produse)\
       .filter(Produse.cod == cod2)\
       .update({Produse.stoc: Produse.stoc - stoc1})
    db.session.commit()
    flash('Stoc vandut!', category='success')
  return render_template("vanzare.html",user=current_user)
@views.route('/adaugareprodus', methods=['GET', 'POST'])
def adaugare():
    if request.method== 'POST':
       marca=request.form.get('marca')
       model=request.form.get('model')
       pret=request.form.get('pret')
       cod=request.form.get('cod')
       stoc=request.form.get('stoc')
       taraprovenienta=request.form.get('taraprovenienta')
       categorie=request.form.get('categorie')
       if len(marca) <1:
         flash('Numele marcii trebuie sa fie mai mare de 1 caracter.', category='error')
       elif len(model) <2:
         flash('Numele modelului trebuie sa fie mai mare de 2 caractere.', category='error')
       elif len(pret) <1:
         flash('Pretul trebuie sa fie mai mare de 1.', category='error')
       elif len(taraprovenienta) <2:
         flash('Numele tarii proveniente trebuie sa fie mai mare de 2 caractere.', category='error')
       else:
        produs_nou=Produse(marca=marca,model=model,pret=pret,cod=cod,stoc=stoc,taraprovenienta=taraprovenienta,categorie=categorie)
        db.session.add(produs_nou)
        db.session.commit()
        flash('Produs adaugat!', category='success')

    return render_template("adaugare.html",user=current_user)
@views.route('/stergereprodus', methods=['GET', 'POST'])
def stergere():
  if request.method== 'POST':
   cod1=request.form.get('cod1')
   Produse.query.filter(Produse.cod==cod1).delete()
   db.session.commit()
   flash('Produs Sters !',category='success')
  return render_template("stergere.html",user=current_user)
@views.route('/vizualizare',methods=['GET','POST'])
def vizualizare():
  if request.method == "GET":
   
   return render_template("vizualizare.html",query=Produse.query.all(),user=current_user)

   
