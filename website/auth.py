from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db   ##means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Parola incorecta.', category='error')
        else:
            flash('Adresa de mail invalida.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        Nume = request.form.get('Nume')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Adresa de mail are un cont asociat.', category='error')
        elif len(email) < 4:
            flash('Adresa de mail trebuie sa contina cel putin 4 caractere.', category='error')
        elif len(Nume) < 2:
            flash('Numele trebuie sa contina cel putin 2 caractere.', category='error')
        elif password1 != password2:
            flash('Parolele nu se potrivesc.', category='error')
        elif len(password1) < 7:
            flash('Parola trebuie sa contina cel putin 7 caractere.', category='error')
        else:
            new_user = User(email=email, Nume=Nume, password=generate_password_hash(password1))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Contul a fost inregistrat cu succes !', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)