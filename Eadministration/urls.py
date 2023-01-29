from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
path('connexion/',views.connexion),
path('register/',views.register),
path('homepage/',views.homepage),
path('inscription/',views.inscription),
path('etatcivil/',views.etatcivil),
path('actenaiss/',views.actenaiss),
path('actemariage/',views.actemariage),
path('actedeces/',views.actedeces),
path('etatcivil/',views.etatcivil),
path('ajoutnaiss/',views.ajoutnaiss),
path('ajoutmar/',views.ajoutmariage),
path('ajoutdeces/',views.ajoutdeces),
path('afficheractenaiss/',views.afficheractenaiss),
path('afficheractemar/',views.afficheractemar),
path('afficheractedeces/',views.afficheractedec),
path('index/',views.index),
]