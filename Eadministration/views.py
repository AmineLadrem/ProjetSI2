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
from django.http import FileResponse
import io 
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
import datetime
from datetime import datetime, date

from reportlab.lib.pagesizes import letter
# Create your views here.

def actenaisspdf(request):
  actenaiss= ActeNaissance()
  actenaiss= ActeNaissance.objects.get(pk=41638)
  buf=io.BytesIO()
  c=canvas.Canvas(buf,pagesize=letter, bottomup=0)
  textob=c.beginText()
  textob.setTextOrigin(inch,inch)
  textob.setFont("Helvetica",14)
  lines = [ ]
  lines.append("Commune : "+str(actenaiss.Commune))
  lines.append("Daira : "+str(actenaiss.Daira))
  lines.append("Wilaya : "+str(actenaiss.Wilaya))
  lines.append("                            Acte de naissance")
  lines.append("                            ")
  lines.append("                            ")
  lines.append("Numéro de l'acte : "+str(actenaiss.NumNaiss))
  lines.append("Numero de l'enregistrement : "+str(actenaiss.NumEnr))
  lines.append("Nom : "+str(actenaiss.Nom))
  lines.append("Prénom : "+str(actenaiss.Prenom))
  lines.append("Sexe : "+str(actenaiss.Sexe))
  lines.append("Date de naissance : "+str(actenaiss.DateNaiss))
  lines.append("Heure de naissance : "+str(actenaiss.HeureNaiss))
  lines.append("Lieu de naissance : "+str(actenaiss.LieuNaiss))
  lines.append("Les Parents sont :")
  lines.append(str(actenaiss.NomPrenomPere)+',Habite au'+str(actenaiss.Adresse)+',Profession :'+str(actenaiss.ProfessionPere)+',Né le :'+str(actenaiss.DateNaissPere)+',à :'+str(actenaiss.LieuNaissPere))
  lines.append(str(actenaiss.NomPrenomMere)+',Habite au :'+str(actenaiss.Adresse)+',Profession :'+str(actenaiss.ProfessionMere)+',Né le :'+str(actenaiss.DateNaissMere)+',à :'+str(actenaiss.LieuNaissMere))
  lines.append("Mention Marginale : "+str(actenaiss.MentionMarginale))
    
  
    

  for line in lines:
     textob.textLine(line)
  c.drawText(textob)
  c.showPage()
  c.save()
  buf.seek(0)
  return FileResponse(buf,as_attachment=True,filename='ActeDeNaissance.pdf')
 
def actemarpdf(request):
  actemar= ActeMariage()
  actemar= ActeMariage.objects.get(pk=21)
  buf=io.BytesIO()
  c=canvas.Canvas(buf,pagesize=letter, bottomup=0)
  textob=c.beginText()
  textob.setTextOrigin(inch,inch)
  textob.setFont("Helvetica",14)
  lines = [ ]
  lines.append("                            Acte de Mariage")
  lines.append("                            ")
  lines.append("                            ")
  lines.append("Numéro de l'acte : "+str(actemar.NumMariage))
  lines.append("Date de mariage : "+str(actemar.DateMar))
  lines.append("Lieu de mariage : "+str(actemar.LieuMar))
  lines.append("Numero de l'epoux : "+str(actemar.NumEpx))
  lines.append("Numero de l'epouse : "+str(actemar.NumEps))
  lines.append("Nom de l'epoux : "+str(actemar.NomEpx))
  lines.append("Prénom de l'epoux : "+str(actemar.PrenomEpx))
  lines.append("Nom de l'epouse : "+str(actemar.NomEps))
  lines.append("Prénom de l'epouse : "+str(actemar.PrenomEps))
  lines.append("Adresse de l'epoux : "+str(actemar.AdrEpx))
  lines.append("Adresse de l'epouse : "+str(actemar.AdrEps))
  lines.append("Profession de l'epoux : "+str(actemar.ProfessionEpx))
  lines.append("Profession de l'epouse : "+str(actemar.ProfessionEps))
  lines.append("Existance de contrat : "+str(actemar.ExistanceContrat))
  
    
  
    

  for line in lines:
     textob.textLine(line)
  c.drawText(textob)
  c.showPage()
  c.save()
  buf.seek(0)
  return FileResponse(buf,as_attachment=True,filename='ActeDeMariage.pdf')
 
    
  
    

def actedecespdf(request):
  actedeces= ActeDeces()
  actedeces= ActeDeces.objects.get(pk=30)
  buf=io.BytesIO()
  c=canvas.Canvas(buf,pagesize=letter, bottomup=0)
  textob=c.beginText()
  textob.setTextOrigin(inch,inch)
  textob.setFont("Helvetica",14)
  lines = [ ]
  lines.append("                            Acte de Deces")
  lines.append("                            ")
  lines.append("                            ")
  lines.append("Numéro de l'acte : "+str(actedeces.NumDeces))
  lines.append("Nom : "+str(actedeces.EtatCivil.Nom))
  lines.append("Prneom : "+str(actedeces.EtatCivil.Prenom))
  lines.append("Sexe : "+str(actedeces.EtatCivil.Sexe))
  lines.append("Date de deces : "+str(actedeces.DateDeces))
  lines.append("Heure de deces : "+str(actedeces.HeureDeces))
  lines.append("Lieu de deces : "+str(actedeces.LieuDeces))
  lines.append("Date de Naissance : "+str(actedeces.EtatCivil.DateNaiss))
  lines.append("Lieu de Naissance : "+str(actedeces.EtatCivil.LieuNaiss))
  lines.append("Etat Civil : "+str(actedeces.EtatCivil.EtatCivil))

    
  
    

  for line in lines:
     textob.textLine(line)
  c.drawText(textob)
  c.showPage()
  c.save()
  buf.seek(0)
  return FileResponse(buf,as_attachment=True,filename='ActeDeDeces.pdf')
 

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

def connexionmaire(request):
    global mat
    global maire
    mat = request.POST.get('uname')
    motpass = request.POST.get('psw')
    error = 0
    if Maire.objects.filter(IDF_Maire=mat, motpass=motpass).exists():
        error = 1
        maire = Maire.objects.get(IDF_Maire=mat)
        return render(request, "Maire.html", {"maire": maire})
    else:
        error = -1
    print(error)
    return render(request, "ConnexionMaire.html", {"error": error})

def gererofficier(request):

    officiers = list(Officier.objects.filter(IDF_Bureau=maire.IDF_Bureau))
    return render(request, "GererOfficier.html", {"officiers": officiers , "maire": maire})


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
    msg=''
    form = DecesForm(request.POST)
    actedeces= ActeDeces()
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
          if ActeDeces.objects.filter(EtatCivil=personne).exists():
            msg="Cette personne a déjà un acte de deces"
          else:
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
     AnneeNaiss=request.POST.get('AnneeNaiss')
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
    
     personne = Personne(N_Personnel=N_Personnel, Nom=Nom, Prenom=Prenom, Sexe=Sexe, DateNaiss=DateNaiss,AnneeNaiss=AnneeNaiss, LieuNaiss=LieuNaiss, HeureNaiss=HeureNaiss, EtatCivil=EtatCivil, Adresse=Adresse, Profession=Profession, NumPere=pere.NumEnr, NumMere=mere.NumEnr,NumReg=reg)
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
    msg1=''
    msg2=''
    actenaiss= ActeNaissance()
    if request.method == 'POST':
        NumNaiss = request.POST.get('NumNaiss')
        if ActeNaissance.objects.filter(pk=NumNaiss).exists():
            Existe=True
            actenaiss= ActeNaissance.objects.get(pk=NumNaiss)
            msg1= "L'acte de naissance Existe✔️"
        else:
            msg2= "L'acte de naissance n'existe pas ❌"    
                      
    return render(request, "AffichageActeNaiss.html", {"officier": officier , "actenaiss": actenaiss , "Existe": Existe , "msg1": msg1, "msg2": msg2})    

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
    msg1=''
    msg2=''
    actdec= ActeDeces()
    if request.method == 'POST':
        NumDec = request.POST.get('NumDec')
        print(NumDec)
        if Personne.objects.filter(pk=NumDec,EtatCivil='Deces').exists():
            personne= Personne.objects.get(pk=NumDec,EtatCivil='Deces')
            Existe=True
            print("Existe")
            actdec= ActeDeces.objects.get(EtatCivil=personne)
            msg1= "L'acte de deces Existe✔️"
        else:
            msg2= "L'acte de deces n'existe pas ❌"     
    return render(request, "AffichageActeDeces.html", {"officier": officier , "actdec": actdec, "Existe": Existe , "msg1": msg1, "msg2": msg2}) 

def searchactenaiss(request):
  if request.method == 'POST':
         NumActe = request.POST.get('actenaiss')
         if ActeNaissance.objects.filter(pk=NumActe).exists():
            url = 'modifiernaiss/' +NumActe
            return redirect(url)

  return render(request, "searchactenaiss.html", {"officier": officier})

def searchactemar(request):
   if request.method == 'POST':
         NumActe = request.POST.get('actemar')
         if ActeMariage.objects.filter(pk=NumActe).exists():
            url = 'modifiermar/' +NumActe
            return redirect(url)
   return render(request, "searchactemar.html", {"officier": officier})

def searchactedeces(request):
    if request.method == 'POST':
         NumActe = request.POST.get('actedeces')
         if ActeDeces.objects.filter(pk=NumActe).exists():
            url = 'modifierdeces/' +NumActe
            return redirect(url)
    return render(request, "searchactedeces.html", {"officier": officier})

def modifieractenaiss(request , NumNaiss):
    Actes=ActeNaissance.objects.get(NumNaiss=NumNaiss)
    if request.method == 'POST':
     form= NaissanceForm2(request.POST, instance=Actes)
     if form.is_valid():
            form.save()
            return redirect('ActeNaiss')
    else:
     form = NaissanceForm2(instance=Actes)        
    return render(request, "ModifierActeNaiss.html", {'form': form, 'officier':officier})

def modifieractemar(request , NumMariage):
    Actes=ActeMariage.objects.get(NumMariage=NumMariage)
    if request.method == 'POST':
     form= MariageForm(request.POST, instance=Actes)
     if form.is_valid():
            form.save()
            return redirect('ActeMar')
    else:
     form = MariageForm(instance=Actes)        
    return render(request, "ModifierActeMar.html", {'form': form , 'officier':officier})

def modifieractedeces(request , NumDeces):
    Actes=ActeDeces.objects.get(NumDeces=NumDeces)
    if request.method == 'POST':
     form= DecesForm(request.POST, instance=Actes)
     if form.is_valid():
            form.save()
            return redirect('ActeDeces')
    else:
     form = DecesForm(instance=Actes)        
    return render(request, "ModifierActeDeces.html", {'form': form, 'officier':officier})

def ajoutofficier(request):
    officier=Officier()
    form = OfficierForm()
    if request.method == 'POST':
        form = OfficierForm(request.POST)
        if form.is_valid():
         print("valid")
         form.save()
    return render(request, 'AjouteOfficier.html', {'form': form, 'maire':maire})

def index(request):
 naiss = Personne.objects.values("AnneeNaiss").annotate(nombre=Count("AnneeNaiss"))
 NumMaj=0
 NumMin=0
 actenaiss=Personne.objects.all()

 for acte in actenaiss:
    if date.today().year-int(acte.AnneeNaiss)>18:
        NumMaj=NumMaj+1;
    else:
        NumMin=NumMin+1;
   
 return render(request, "Stats.html" , {"naiss": naiss , "NumMaj": NumMaj , "NumMin": NumMin ,"officier": officier})