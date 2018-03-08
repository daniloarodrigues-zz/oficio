from django import forms
from django.forms import DateInput, HiddenInput
from oficio.models import Oficio


class FormOficio(forms.ModelForm):
    error = 'Erro'
    class Meta:
        model = Oficio
        fields = ['orgao','numero', 'data', 'para', 'cargo_para', 'assunto', 'texto']
        widgets = {
            'data': DateInput(attrs={'class':'data'}),

        }