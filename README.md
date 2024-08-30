### Magazin Componente PC
## Configurare & Instalare:
Asigurati-va ca aveti cea mai noua versiune de Python.
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

## Rolul aplicatiei

Aplicatia are rolul de a asigura administrarea eficientă al unui magazin online de componente pentru calculator.
Platforma cuprinde o metodă de autentificare pentru personalul magazinului precum și diverse pagini pentru a gestiona eficient comenzile sau inventarul magazinului.

## Tehnologii folosite

-Pentru partea de backend: Python impreuna cu framework-ul “Flask”.

-Pentru baza de date: SQL-Alchemy

-Pentru Front-end: HTML,CSS/Bootstrap,Javascript,Jquery.

## Prezentarea aplicatiei

### Pagina de autentificare

Accesul la platforma se va realiza prin intermediul paginii de logare, cu un fundal simplu si text usor de citit. Autentificarea se va realiza pe baza adresei de e-mail si a parolei, acestea fiind alese in timpul inregistrarii contului. 

![image](https://github.com/user-attachments/assets/d9428f0d-f881-423a-9f39-ae38286d919d)

### Pagina de inregistrare

In cazul in care nu exista un cont al administratorului, se poate realiza unul prin intermediul paginii de “Cont Nou” unde utilizatorul trebuie sa introducă Adresa de mail, Numele si parola. 

In realitate, aceasta pagina nu va putea fi accesibila decât personalului autorizat al magazinului.

![image](https://github.com/user-attachments/assets/ab4a1499-f5f0-4965-bccd-c17ec59f96bc)

### Pagina principala

Odată autentificat, utilizatorul va fi întâmpinat de pagina principala, alcătuita din meniul de navigație plasat in partea de sus a paginii, cu link-uri către paginile aplicației, un buton pentru delogarea din cont si o căsuță de căutare a produselor.

Putin mai jos avem un mesaj de întâmpinare alături de numele Utilizatorului, email-ul acestuia si data de astăzi plasata in partea dreapta.

Conținutul paginii este format din căsuțe cu diverse informații de baza precum comenzile recente, stocul de produse sau produsele cu stoc limitatFooter-ul conține diverse link-uri si un mesaj de copyright.

![image](https://github.com/user-attachments/assets/5ed97b50-27b9-4e92-8bc8-0c140654ade4)

### Pagina de vizualizare a inventarului

Pagina “vizualizare inventar” cuprinde un tabel cu elemente text usor de citit, pe un fundal inchis, cu produsele prezente in inventarul magazinului. 

Sunt prezente diverse informatii despre produsele respective iar pe ultima coloana avem butoane cu diverse actiuni pentru a modifica un produs sau a-l sterge.

![image](https://github.com/user-attachments/assets/f1aa492d-8b2f-479c-a0e0-992392711c85)

### Butoanele de pe pagina "Vizualizare Inventar"

La apsarea butonului de Optiuni Filtre, se va afisa o caseta modala cu diverse filtre pentru a facilita afisarea produselor.

La apasarea butonului “actiuni” in dreptul unui produs, se va afisa un submeniu cu optiunile de actualizare sau de stergere a produsului din baza de date.

La apasarea butonului de Stergere, utilizatorul va fi intampinat de un modal pentru a confirma stergerea produsului.

La apasarea butonului de Actualizare, se va afisa un modal cu diverse campuri pentru modificarea datelor produsului precum Marca,Modelul,Categoria,Pretul,Stocul sau Descrierea produsului respectiv.

In partea de jos a paginii avem butoanele de “Export Excel” respectiv “Import Excel”. 

La apăsarea butonului “Import Excel” utilizatorul va fi întâmpinat de un modal care explica modul de utilizare al acestei facilități. 

La apăsarea butonului “Export Excel”, utilizatorul poate sa exporteze Inventarul magazinului ori in fișier Excel ori in fișier CSV.

### Pagina "Adaugare Produs"

Pagina de adăugare al unui produs cuprinde câmpuri necesare acestuia precum Marca, Modelul, Categoria, Prețul, Stocul, Descrierea produsului si posibilitatea de a adăuga o poza pentru produsul respectiv.

Poza si descrierea pot fi vizualizate pentru fiecare produs in parte prin căutarea acestuia folosind căsuța text de pe pagina principala.

![image](https://github.com/user-attachments/assets/c6de0cf1-42c6-4323-8646-3371c6615c5b)

### Cautarea unui Produs

Căutarea unui produs se poate realiza folosind  căsuța text prezenta pe pagina principala a platformei.

Prin tastarea mărcii sau a modelului produsului, in partea dreapta a căsuței se vor afișa autosugestii de căutare a produsului iar prin apăsarea sugestiei, ori folosind tasta Enter sau click pe text-ul respectiv, se va afișa pagina produsului respectiv cu poza si descrierea acestuia.

Sunt prezente butoanele de actualizare sau de ștergere a produsului respectiv.

![image](https://github.com/user-attachments/assets/24fa8203-bb8c-4054-a21a-bfa290030007)

### Pagina "Istoric Comenzi"

Pagina “istoric comenzi” cuprinde un tabel cu coloanele: număr comanda, nume, email, telefon, data, produsele comandate alături de cantitatea comandata, starea comenzii si o coloana cu butoanele de acțiuni.

O comanda noua va avea starea “In Așteptare” iar cu ajutorul butoanelor de acțiuni, utilizatorul poate confirma o comandă sau o poate anula, apărând in coloana “stare” a comenzii respective “anulat” sau “confirmat”.

La confirmarea comenzii, va fi scăzut automat din stocul produselor respective cantitatea comandata de clientPentru demonstrație, au fost introduse manual in baza de date comenzi fictive.

![image](https://github.com/user-attachments/assets/88a2d12e-8ebc-4a2a-a47a-9241bc37659c)

### Butoanele de pe pagina "Istoric Comenzi"

La apăsarea butonului “acțiuni” in dreptul unei comenzi, va fi afișat un submeniu cu opțiunile de anulare respectiv de confirmare a comenzii.

La apăsarea butonului “Anulare comanda” va fi afișat un modal de confirmare si o căsuță text pentru introducerea motivului anularii.

La apăsarea butonului “Confirmare Comanda” va fi afișat un modal cu detaliile comenzii respective.


## Concluzii

Aplicația dezvoltată poate servi drept bază utilă pentru înființarea unui magazin online. 

Cu interfața sa ușor de utilizat, această platformă simplifică foarte mult gestionarea magazinului, oferind funcții avansate pentru modificarea inventarului, gestionarea comenzilor și asigurarea securității.
