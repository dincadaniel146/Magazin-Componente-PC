from flask import Blueprint,render_template,request,flash
from flask_login import login_required, current_user
from datetime import datetime
from .models import Produse
from . import db
import locale
from sqlalchemy import or_
from flask import jsonify
from werkzeug.utils import secure_filename

views = Blueprint('views', __name__)

UPLOAD_FOLDER = '/produse_img'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}



@views.route('/',methods=['GET','POST'])
@login_required
def home():
    success_message = request.args.get('success_message')
    if success_message:
        flash(success_message, category='success')
    locale.setlocale(locale.LC_TIME, 'ro_RO')           
    return render_template("index.html",user=current_user,data=datetime.now().strftime('%A %d %B %Y'),numar_total_produse=Produse.query.count(),numar_stoc_total=int(db.session.query(db.func.sum(Produse.stoc)).scalar()),stoc_limitat=Produse.query.filter(Produse.stoc < 10).count())
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Define the upload file route
@views.route('/upload', methods=['POST'])
def upload_file():
    if 'product_image' not in request.files:
        flash('No file part')
        return redirect(request.url)
    
    file = request.files['product_image']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        flash('File uploaded successfully')
        # Redirect to the add product page with the filename
        return redirect(url_for('views.adaugare', filename=filename))
    else:
        flash('Invalid file type')
        return redirect(request.url)

@views.route('/adaugareprodus', methods=['GET', 'POST'])
@login_required  
def adaugare():
    if request.method == 'POST':
        marca = request.form.get('marca')
        model = request.form.get('model')
        pret = request.form.get('pret')
        stoc = request.form.get('stoc')
        descriere = request.form.get('descriere')
        categorie = request.form.get('categorie')
        image_filename = request.form.get('filename')  # Get the filename from the form
        
        if len(marca) < 1:
            flash('Numele marcii trebuie sa fie mai lung de 1 caracter.', category='error')
        elif len(model) < 2:
            flash('Numele modelului trebuie sa fie mai lung de 2 caractere.', category='error')
        elif len(pret) < 1:
            flash('Pretul trebuie sa fie un numar valid.', category='error')
        else:
            # Create the new product instance with the image filename
            produs_nou = Produse(marca=marca, model=model, pret=pret, stoc=stoc, descriere=descriere, categorie=categorie, imagine=image_filename)
            db.session.add(produs_nou)
            db.session.commit()
            flash('Produs adaugat!', category='success')
            return render_template("adaugare.html", user=current_user)
    
    # For GET requests or if there are form validation errors, return the template
    return render_template("adaugare.html", user=current_user)

@views.route('/stergereprodus', methods=['POST'])
@login_required  
def stergere():
  if request.method== 'POST':
   cod=request.form.get('cod-stergere')
   Produse.query.filter(Produse.cod==cod).delete()
   db.session.commit()
   flash('Produs Sters !',category='success')
  return render_template("vizualizare.html",
                               query=Produse.query.all(),
                               user=current_user,
                               numar_produse=Produse.query.count(),
                               data=datetime.now().strftime('%A %d %B %Y'))
@views.route('/vizualizare', methods=['GET', 'POST'])
@login_required  
def vizualizare():
    if request.method == "GET":  
        # Fetch all Produse objects and render the template
        return render_template("vizualizare.html",
                               query=Produse.query.all(),
                               user=current_user,
                               numar_produse=Produse.query.count(),
                               data=datetime.now().strftime('%A %d %B %Y'))
    
    if request.method == 'POST':
        cod = request.form.get('cod')
        marca = request.form.get('marca')
        model = request.form.get('model')
        pret = request.form.get('pret')
        stoc = request.form.get('stoc')
        descriere = request.form.get('descriere')
        categorie = request.form.get('categorie')

        # Validate the input fields
        if len(marca) < 1:
            flash('Numele marcii trebuie sa fie mai lung de 1 caracter.', category='error')
        elif len(model) < 2:
            flash('Numele modelului trebuie sa fie mai lung de 2 caractere.', category='error')
        elif len(pret) < 1:
            flash('Pretul trebuie sa fie un numar valid.', category='error')
        else:
            # Fetch the Produs object based on the provided cod
            produs = Produse.query.filter_by(cod=cod).first()
            if produs:
                # Update the Produs object with the new data
                produs.marca = marca
                produs.model = model
                produs.pret = pret
                produs.stoc = stoc
                produs.descriere = descriere
                produs.categorie = categorie
                db.session.commit()
                flash('Produs actualizat!', category='success')
            else:
                flash('Eroare: Produsul nu există!', category='error')
    
    # Render the template after handling the POST request
    return render_template("vizualizare.html",
                               query=Produse.query.all(),
                               user=current_user,
                               numar_produse=Produse.query.count(),
                               data=datetime.now().strftime('%A %d %B %Y'))

@views.route('/search', methods=['GET'])
@login_required
def search():
    query = request.args.get('query')
    # Adjust the filter to search by 'model' instead of 'id'
    produse_query = Produse.query.filter(or_(Produse.model.like(f'%{query}%'),Produse.marca.like(f'%{query}%'))).all()
    # Modify the suggestions to include both 'marca' and 'model'
    suggestions = [{'cod': product.cod, 'marca': product.marca, 'model': product.model} for product in produse_query]
    return jsonify({'suggestions': suggestions})


@views.route('/produs/<int:product_cod>', methods=['GET', 'POST'])
@login_required  
def vizualizare_produs(product_cod):
    if request.method == "GET":  
        # Fetch the Produs object by ID
        produs = Produse.query.get(product_cod)  
        return render_template("produs.html", user=current_user, product=produs)

    if request.method == 'POST':
        cod = request.form.get('cod')
        marca = request.form.get('marca')
        model = request.form.get('model')
        pret = request.form.get('pret')
        stoc = request.form.get('stoc')
        descriere = request.form.get('descriere')
        categorie = request.form.get('categorie')

        # Validate the input fields
        if len(marca) < 1:
            flash('Numele marcii trebuie sa fie mai lung de 1 caracter.', category='error')
        elif len(model) < 2:
            flash('Numele modelului trebuie sa fie mai lung de 2 caractere.', category='error')
        elif len(pret) < 1:
            flash('Pretul trebuie sa fie un numar valid.', category='error')
        else:
            # Fetch the Produs object based on the provided cod
            produs = Produse.query.filter_by(cod=cod).first()
            if produs:
                # Update the Produs object with the new data
                produs.marca = marca
                produs.model = model
                produs.pret = pret
                produs.stoc = stoc
                produs.descriere = descriere
                produs.categorie = categorie
                db.session.commit()
                flash('Produs actualizat!', category='success')
            else:
                flash('Eroare: Produsul nu există!', category='error')
        
    produs = Produse.query.get(product_cod)
    return render_template("produs.html",product=produs)
@views.route('/modal-produs/<int:produs_cod>', methods=['GET','POST'])
@login_required
def modal_produs(produs_cod):
    produs = Produse.query.get(produs_cod)
    if produs:
        produs_data = {
            'cod': produs.cod,
            'marca': produs.marca,
            'model': produs.model,
            'categorie': produs.categorie,
            'pret': produs.pret,
            'stoc': produs.stoc,
            'descriere': produs.descriere
        }
        return jsonify(produs_data)
    else:
        return jsonify({'error': 'Produsul nu a fost gasit!'}), 404



   
