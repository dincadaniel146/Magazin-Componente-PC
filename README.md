### Magazin Componente PC
## Configurare & Instalare:
Asigurati-va ca aveti cea mai noua versiune de Python:
```
> git clone https://github.com/dincadaniel146/Magazin-Componente-PC
> pip install -r dependente.txt
```
## Pentru a rula aplicatia:
```
python main.py
```
## Viualizarea aplicatiei:
```
Accesati http://127.0.0.1:5000
```



## Prezentare generala:
- Aplicatia are rolul de a asigura gestiunea unui magazin de componente hardware.
- Pentru baza de date,se utilizeaza modulul 'SQL Alchemy'
- Pentru partea de Back-end se utilizeaza modulul 'Flask'
- Aplicatia foloseste Bootstrap pentru o experienta placuta in utilizare
- In fisierul __init__.py vom importa modulul Flask si definim functia
“create_app” care ne va ajuta sa initializam aplicatia.
- In fisierul main.py vom importa din pachetul “website” functia
create_app care ne va ajuta sa rulam aplicatia flask.
- In fisierul views.py vom stoca rutele standard ale website-ului
nostru.Importam “Blueprint” din modulul flask care ne va ajuta sa
organizam rutele site-ului.
- In folderul template vom crea fisierele HTML pentru fiecare dintre
paginile necesare aplicatiei, index.html reprezinta pagina principala,iar
base.html este un model sablon pentru toate paginile pe care le vom
crea,acesta contine bara de navigatie si logo-ul,prezent pe toate paginile
HTML pe care le vom folosi.
- In Flask vom folosi un “engine” pentru sabloane web numit “Jinja” care
ne ajuta sa folosim cod similar cu Python in fisierul nostru HTML.
- In base.html avem elemente CSS care ajuta site-ul sa arate mai elegant
si mai placut de folosit,precum si elemente JavaScript care ajuta la
functionarea corespunzatoare a animatiilor si a butoanelor.
- In fisierul models.py vom avea modelul bazei noastre de date cu toate
coloanele care trebuie completate cand introducem o componenta in
magazin.
