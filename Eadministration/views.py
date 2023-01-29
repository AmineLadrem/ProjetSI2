from ctypes import sizeof
import datetime
from tarfile import ExtractError
from django.shortcuts import render, redirect
from .forms import *
from .models import *
import random
import datetime
from django.db.models import Count
from django.utils import timezone

# Create your views here.


def connexion(request):
    global mat
    global officier
    mat = request.POST.get('uname')
    motpass = request.POST.get('psw')
    error = 0
    if Officier.objects.filter(IDF_Officier=mat, motpass=motpass).exists():
        error = 1
        officier = Officier.objects.get(IDF_Officier=mat)
        return render(request, "EtatCivil.html", {"officier": officier})
    else:
        error = -1
    print(error)
    return render(request, "Connexion.html", {"error": error})


def deconnexion(request):
    return render(request, "homepage.html")


def register(request):
    if request.method == 'POST':
        form = OfficierForm(request.POST)
        if form.is_valid():
            form.save()
            msg = "Votre compte a été crée avec succès"
            return render(request, "register.html", {"form": form, "message": msg})


def homepage(request):
    return render(request, "Homepage.html")


def inscription(request):
    return render(request, "register.html")


def etatcivil(request):
    return render(request, "EtatCivil.html")


def actenaiss(request):
    return render(request, "ActeDeNaiss.html", {"officier": officier})


def actemariage(request):
    return render(request, "ActeDeMarriage.html", {"officier": officier})


def actedeces(request):
    return render(request, "ActeDeDeces.html", {"officier": officier})


def etatcivil(request):
    return render(request, "EtatCivil.html")

def ajoutdeces(request):
    changee=False
    form = DecesForm(request.POST)
    actedeces= ActeDeces()
    personne= Personne()
    reg= Registre()
    if request.method == 'POST':
     NumPersonne= request.POST.get('NumPersonne')
     DateDeces= request.POST.get('DateDeces')
     print(int(DateDeces[:4]))
     AnneeDeces = int(DateDeces[:4])
     HeureDeces= request.POST.get('HeureDeces')
     LieuDeces= request.POST.get('LieuDeces')
    

     if Personne.objects.filter(pk=NumPersonne).exists():
        personne = Personne.objects.get(pk=NumPersonne)
        Personne.objects.filter(pk=NumPersonne).update(EtatCivil='Deces')
        changee=True
     if Registre.objects.filter(TypeReg='Deces',AnneeReg=AnneeDeces).exists() :
        reg= Registre.objects.get(TypeReg='Deces',AnneeReg=AnneeDeces)
     reg= Registre.objects.get(TypeReg='Deces',AnneeReg=AnneeDeces)
     
     actedeces=ActeDeces(DateDeces=DateDeces,HeureDeces=HeureDeces,LieuDeces=LieuDeces,EtatCivil=personne,NumReg=reg)
    actedeces.save()
    msg="L'acte de deces a été ajouté avec succès ✔️"


    return render(request, "AjouteDeces.html", {"form": form, "officier": officier , "msg":msg,"changee":changee})

def ajoutmariage(request):
    form = MariageForm(request.POST)
    actemar= ActeMariage()
    if request.method == 'POST':
     DateMar = request.POST.get('DateMar')
     print(int(DateMar[:4]))
     AnneeMar = int(DateMar[:4])
     LieuMar = request.POST.get('LieuMar')
     NumEpx= request.POST.get('NumEpx')
     NumEps= request.POST.get('NumEps')

     if Personne.objects.filter(NumEnr=NumEpx).exists() :
        Personne.objects.filter(NumEnr=NumEpx).update(EtatCivil='Marie')
        pere= Personne.objects.get(NumEnr=NumEpx)
        NomEpx= pere.Nom
        PrenomEpx= pere.Prenom
        DateNaissEpx= pere.DateNaiss
        LieuNaissEpx= pere.LieuNaiss
        ProfessionEpx= pere.Profession
        AdresseEpx= pere.Adresse
        print(NomEpx, PrenomEpx, DateNaissEpx, LieuNaissEpx, ProfessionEpx, AdresseEpx)

     if Personne.objects.filter(NumEnr=NumEps).exists() :
        Personne.objects.filter(NumEnr=NumEps).update(EtatCivil='Mariee')
        mere= Personne.objects.get(NumEnr=NumEps)
        NomEps= mere.Nom    
        PrenomEps= mere.Prenom
        DateNaissEps= mere.DateNaiss
        LieuNaissEps= mere.LieuNaiss
        ProfessionEps= mere.Profession
        AdresseEps= mere.Adresse
        print(NomEps, PrenomEps, DateNaissEps, LieuNaissEps, ProfessionEps, AdresseEps)    
   
     if Registre.objects.filter(TypeReg='Mariage',AnneeReg=AnneeMar).exists() :
        reg= Registre.objects.get(TypeReg='Mariage',AnneeReg=AnneeMar)
     reg= Registre.objects.get(TypeReg='Mariage',AnneeReg=AnneeMar)
     ExistanceContrat= request.POST.get('ExistanceContrat')

     
     actemar=ActeMariage(DateMar=DateMar,LieuMar=LieuMar,NumEpx=NumEpx,NumEps=NumEps,NomEpx=NomEpx,PrenomEpx=PrenomEpx,NomEps=NomEps,PrenomEps=PrenomEps,ProfessionEpx=ProfessionEpx,ProfessionEps=ProfessionEps,AdrEpx=AdresseEps,AdrEps=AdresseEps,ExistanceContrat=ExistanceContrat,NumReg=reg)
     actemar.save()


    return render(request, "AjouteMar.html", {"form": form, "officier": officier})

def ajoutnaiss(request):
    ajouter=False
    personal_number = ""
    for i in range(9):
        personal_number += str(random.randint(0, 9))
    form = NaissanceForm(request.POST)
    personne= Personne()
    actenaiss= ActeNaissance()
    Commune=officier.IDF_Bureau.Commune
    Daira=officier.IDF_Bureau.Daira
    Wilaya=officier.IDF_Bureau.Wilaya
    if request.method == 'POST':
     personne = Personne()
     pere= Personne()
     mere= Personne()
     actenaiss= ActeNaissance()
     form = NaissanceForm(request.POST)
     N_Personnel=   personal_number
     Nom = request.POST.get('Nom')
     Prenom = request.POST.get('Prenom')
     Sexe = request.POST.get('Sexe')
     DateNaiss = request.POST.get('DateNaiss')
     AnneeNaiss = int(DateNaiss[:4])
     HeureNaiss = request.POST.get('HeureNaiss')
     LieuNaiss = request.POST.get('LieuNaiss')
     EtatCivil = request.POST.get('EtatCivil')
     Adresse = request.POST.get('Adresse')
     Profession = request.POST.get('Profession')
     NumPere = request.POST.get('NumPere')
     NumMere = request.POST.get('NumMere')


     if Personne.objects.filter(pk=NumPere).exists():
        print("pere existe")
        pere = Personne.objects.get(pk=NumPere)
        Nompere= pere.Nom
        Prenompere= pere.Prenom
        DateNaisspere= pere.DateNaiss
        LieuNaisspere= pere.LieuNaiss
        Professionpere= pere.Profession
        Adressepere= pere.Adresse

        
    
     if Personne.objects.filter(pk=NumMere).exists():
      print("mere existe")
      mere = Personne.objects.get(pk=NumMere)
      Nommere= mere.Nom
      Prenommere= mere.Prenom
      DateNaissmere= mere.DateNaiss
      LieuNaissmere= mere.LieuNaiss
      Professionmere= mere.Profession
      Adressemere= mere.Adresse

      
     if Registre.objects.filter(TypeReg='Naissance',AnneeReg=AnneeNaiss).exists() :
      reg= Registre.objects.get(TypeReg='Naissance',AnneeReg=AnneeNaiss)
     reg= Registre.objects.get(TypeReg='Naissance',AnneeReg=AnneeNaiss)
    
     personne = Personne(N_Personnel=N_Personnel, Nom=Nom, Prenom=Prenom, Sexe=Sexe, DateNaiss=DateNaiss, LieuNaiss=LieuNaiss, HeureNaiss=HeureNaiss, EtatCivil=EtatCivil, Adresse=Adresse, Profession=Profession, NumPere=pere.NumEnr, NumMere=mere.NumEnr,NumReg=reg)
     personne.save()
     personne= Personne.objects.get(N_Personnel=N_Personnel)
     actenaiss=ActeNaissance(NumNaiss=personne.NumEnr,Nom=Nom,Prenom=Prenom,Sexe=Sexe,DateNaiss=DateNaiss,HeureNaiss=HeureNaiss,LieuNaiss=LieuNaiss,Commune=Commune,Daira=Daira,Wilaya=Wilaya,NomPrenomPere=Nompere+" "+Prenompere,NomPrenomMere=Nommere+" "+Prenommere,ProfessionPere=Professionpere,ProfessionMere=Professionmere,LieuNaissPere=LieuNaisspere,LieuNaissMere=LieuNaissmere,DateNaissPere=DateNaisspere,DateNaissMere=DateNaissmere,Adresse=Adressepere,MentionMarginale=" ",NumEnr=personne,NumReg=reg)
     actenaiss.save()
     ajouter= True
    msg1="L'acte de naissance a été ajouté avec succès✔️"
    msg2="L'acte de naissance n'a pas été ajouté ❌, Veuillez vérifier les données saisies"
     
 

    return render(request, "AjouteNaiss.html", {"form": form, "officier": officier , "ajouter": ajouter, "msg1": msg1, "msg2": msg2})


def afficheractenaiss(request):
    Existe=False
    actenaiss= ActeNaissance()
    if request.method == 'POST':
        NumNaiss = request.POST.get('NumNaiss')
        if ActeNaissance.objects.filter(pk=NumNaiss).exists():
            Existe=True
            print("Existe")
            actenaiss= ActeNaissance.objects.get(pk=NumNaiss)
            print(actenaiss.HeureNaiss)
            
    return render(request, "AffichageActeNaiss.html", {"officier": officier , "actenaiss": actenaiss})    

def afficheractemar(request):
 Error=False
 msg=''
 try:   
    
    actemar= ActeMariage()
    epoux= Personne()
    epouse= Personne()
    if request.method == 'POST':
        NumMar = request.POST.get('NumMar')
        if ActeMariage.objects.filter(pk=NumMar).exists():
            Existe=True
            print("Existe")
            actemar= ActeMariage.objects.get(pk=NumMar)
        epoux= Personne.objects.get(pk=actemar.NumEpx)
        epouse= Personne.objects.get(pk=actemar.NumEps) 
 except Exception as e:
  Error=True
  print("Personne n'existe pas") 
  msg="Personne n'existe pas"    
 return render(request, "AffichageActeMar.html", {"officier": officier , "actemar": actemar , "epoux": epoux , "epouse": epouse , "msg": msg , "Error": Error})    

def afficheractedec(request):
    Existe=False
    actdec= ActeDeces()
    if request.method == 'POST':
        NumDec = request.POST.get('NumDec')
        if ActeDeces.objects.filter(pk=NumDec).exists():
            Existe=True
            print("Existe")
            actdec= ActeDeces.objects.get(pk=NumDec)

            
    return render(request, "AffichageActeDeces.html", {"officier": officier , "actdec": actdec}) 

def index(request):
 labels = []
 data = []

 
    
 return render(request, "index.html" , {"labels": labels, "data": data})