from django.db import models

# Create your models here.
   

class Pays(models.Model):
    IDF_Pays=models.IntegerField(primary_key=True)
    Pays=models.CharField(max_length=50)

class Consulat(models.Model):
    IDF_Consulate=models.IntegerField(primary_key=True)
    Consulat=models.CharField(max_length=50)
    Ville=models.CharField(max_length=50,null=True)
    IDF_Pays=models.ForeignKey("Pays",on_delete=models.CASCADE)

class AgentDiplomatique(models.Model):
    IDF_Agent=models.IntegerField(primary_key=True)
    Nom=models.CharField(max_length=50)
    Prenom=models.CharField(max_length=50)
    motpass=models.CharField(max_length=16)
    IDF_Consulat=models.ForeignKey("Consulat",on_delete=models.CASCADE)

class Bureau(models.Model):
    IDF_Bureau=models.IntegerField(primary_key=True)
    Commune=models.CharField(max_length=50)
    Daira=models.CharField(max_length=50)
    Wilaya=models.CharField(max_length=50)
    

class Officier(models.Model):
    IDF_Officier=models.IntegerField(primary_key=True)
    Nom=models.CharField(max_length=50)
    Prenom=models.CharField(max_length=50)
    DatePrise=models.DateField()
    motpass=models.CharField(max_length=16)
    IDF_Bureau=models.ForeignKey("Bureau",on_delete=models.CASCADE)

class Maire(models.Model):
    IDF_Maire=models.IntegerField(primary_key=True)
    Nom=models.CharField(max_length=50)
    Prenom=models.CharField(max_length=50)
    DatePrise=models.DateField()
    IDF_Bureau=models.ForeignKey("Bureau",on_delete=models.CASCADE)

class Personne(models.Model):
    NumEnr=models.AutoField(primary_key=True)
    N_Personnel=models.IntegerField( null=True)
    Nom=models.CharField(max_length=50,null=True)
    Prenom=models.CharField(max_length=50,null=True)
    Sexe=models.CharField(max_length=1,null=True)
    DateNaiss=models.DateField( null=True)
    HeureNaiss=models.TimeField( null=True)
    LieuNaiss=models.CharField(max_length=50,null=True)
    EtatCivil=models.CharField(max_length=50,null=True)
    Adresse=models.CharField(max_length=50,null=True)
    Profession=models.CharField(max_length=50, null=True)
    NumPere=models.IntegerField(null=True)
    NumMere=models.IntegerField(null=True)
    NumReg=models.ForeignKey("Registre",on_delete=models.CASCADE, null=True)

class ActeNaissance(models.Model):
    NumNaiss=models.IntegerField(primary_key=True)
    Nom=models.CharField(max_length=50, null=True)
    Prenom=models.CharField(max_length=50, null=True)
    Sexe=models.CharField(max_length=1, null=True)
    DateNaiss=models.DateField( null=True)
    HeureNaiss=models.TimeField( null=True)
    LieuNaiss=models.CharField(max_length=50, null=True)
    Commune=models.CharField(max_length=50, null=True)
    Daira=models.CharField(max_length=50, null=True)
    Wilaya=models.CharField(max_length=50, null=True)
    NomPrenomPere=models.CharField(max_length=50, null=True)
    NomPrenomMere=models.CharField(max_length=50, null=True)
    ProfessionPere=models.CharField(max_length=50, null=True)
    ProfessionMere=models.CharField(max_length=50, null=True)
    LieuNaissPere=models.CharField(max_length=50, null=True)
    LieuNaissMere=models.CharField(max_length=50, null=True)
    DateNaissPere=models.DateField( null=True)
    DateNaissMere=models.DateField( null=True)
    Adresse=models.CharField(max_length=50, null=True)
    MentionMarginale=models.CharField(max_length=200, null=True)
    NumEnr=models.ForeignKey("Personne",on_delete=models.CASCADE, null=True)
    NumReg=models.ForeignKey("Registre",on_delete=models.CASCADE, null=True)

class ActeMariage(models.Model):
    NumMariage=models.IntegerField(primary_key=True)
    DateMar=models.DateField(null=True)
    LieuMar=models.CharField(max_length=50)
    NumEpx=models.IntegerField(null=True)
    NumEps=models.IntegerField(null=True)
    NomEpx=models.CharField(max_length=50)
    PrenomEpx=models.CharField(max_length=50)
    NomEps=models.CharField(max_length=50)
    PrenomEps=models.CharField(max_length=50)
    AdrEpx=models.CharField(max_length=50)
    AdrEps=models.CharField(max_length=50)
    ProfessionEpx=models.CharField(max_length=50)
    ProfessionEps=models.CharField(max_length=50)
    ExistanceContrat=models.CharField(max_length=100)
    NumReg=models.ForeignKey("Registre",on_delete=models.CASCADE)

class ActeDeces(models.Model):
    NumDeces=models.AutoField(primary_key=True)
    DateDeces=models.DateField(null=True)
    HeureDeces=models.TimeField( null=True)
    LieuDeces=models.CharField(max_length=50 , null=True)
    EtatCivil=models.ForeignKey("Personne",on_delete=models.CASCADE , null=True)
    NumReg=models.ForeignKey("Registre",on_delete=models.CASCADE , null=True)


class Registre(models.Model):
  NumReg=models.IntegerField(primary_key=True)
  TypeReg=models.CharField(max_length=50)
  AnneeReg=models.IntegerField()
  NbrActe=models.IntegerField(null=True)
  Bureau=models.ForeignKey("Bureau",on_delete=models.CASCADE)


