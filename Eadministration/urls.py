from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
path('connexion/',views.connexion),
path('connexionmaire/',views.connexionmaire), 
path('gererofficier/',views.gererofficier), 
path('ajoutofficier/',views.ajoutofficier), 
path('register/',views.register),
path('homepage/',views.homepage),
path('inscription/',views.inscription),
path('etatcivil/',views.etatcivil),
path('actenaiss/',views.actenaiss , name="ActeNaiss"),
path('actemariage/',views.actemariage,name="ActeMar"),
path('actedeces/',views.actedeces,name="ActeDeces"),
path('etatcivil/',views.etatcivil),
path('ajoutnaiss/',views.ajoutnaiss),
path('ajoutmar/',views.ajoutmariage),
path('ajoutdeces/',views.ajoutdeces),
path('afficheractenaiss/',views.afficheractenaiss),
path('afficheractemar/',views.afficheractemar),
path('afficheractedeces/',views.afficheractedec),
path('searchactenaiss/',views.searchactenaiss),
path('searchactemar/',views.searchactemar),
path('searchactedeces/',views.searchactedeces),
path('searchactenaiss/modifiernaiss/<int:NumNaiss>',views.modifieractenaiss),
path('searchactemar/modifiermar/<int:NumMariage>',views.modifieractemar),
path('searchactedeces/modifierdeces/<int:NumDeces>',views.modifieractedeces),
path('actenaisspdf/',views.actenaisspdf , name='actenaisspdf'),
path('actemarpdf/',views.actemarpdf , name='actemarpdf'),
path('actedecespdf/',views.actedecespdf , name='actedecespdf'),

path('index/',views.index),
]