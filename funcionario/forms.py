from django import forms
from django.contrib.auth.models import User
from .models import Funcionario

class RegistroFuncionarioForm(forms.ModelForm):
    username = forms.CharField(label='Usuário')
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)
    nome_completo = forms.CharField(label='Nome completo')

    class Meta:
        model = User
        fields = ['username', 'password', 'nome_completo']
