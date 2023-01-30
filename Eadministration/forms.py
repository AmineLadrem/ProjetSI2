from django.db.models import fields
from django import forms
from .models import *


class OfficierForm(forms.ModelForm):
 motpass = forms.CharField(widget=forms.PasswordInput)
 class Meta:
   model = Officier
   fields='__all__'

 

class NaissanceForm(forms.ModelForm):
 class Meta:
   model = Personne
   fields='__all__'

class NaissanceForm2(forms.ModelForm):
 class Meta:
   model = ActeNaissance
   fields='__all__'

class MariageForm(forms.ModelForm):
 class Meta:
   model = ActeMariage
   fields='__all__'

class DecesForm(forms.ModelForm):
  class Meta:
    model = ActeDeces
    fields='__all__'