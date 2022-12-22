from django.forms import ModelForm
from django.contrib.auth import forms
from authentication.forms import UserCreationForm, UserChangeForm
from gestao_de_doacoes.models import Familia, IntegranteFamiliar, Entidade, Usuario, Item, Doacao, ItensDoacao


class FamilyForm(ModelForm):
    class Meta:
        model = Familia
        fields = '__all__'


class FamilyMemberForm(ModelForm):
    class Meta:
        model = IntegranteFamiliar
        fields = '__all__'


class DonationForm(ModelForm):
    class Meta:
        model = Doacao
        fields = '__all__'

class EntityForm(ModelForm):
    class Meta:
        model = Entidade
        fields = '__all__'

class UserForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'cpf', 'email', 'telefone']

class ChangeUser(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'cpf', 'email', 'telefone']
