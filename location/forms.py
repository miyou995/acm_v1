from django import forms
from django.forms import ModelForm
from django.forms.models import inlineformset_factory, modelformset_factory
from location.models import Wilaya, Commune 

class WilayaForm(ModelForm) :
    class Meta: 
        model = Wilaya 
        fields = '__all__' 
        
class CommuneForm(ModelForm) :
    class Meta: 
        model = Commune 
        fields = '__all__' 

