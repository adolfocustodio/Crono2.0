from django import forms
from django.forms import ModelForm
from .models import Categoria


class CategoriaForm(ModelForm):
    
    class Meta:
        model = Categoria
        fields = ('nome',)
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'})
        }
