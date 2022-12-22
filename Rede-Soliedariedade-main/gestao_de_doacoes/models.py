from django.db import models
from authentication.models import Usuario
from django.core.validators import RegexValidator, MinLengthValidator
from datetime import datetime, date

# Create your models here.
class Familia(models.Model):
    chefe_da_familia = models.CharField(max_length=200, help_text='Digite o nome do chefe da família')
    cpf = models.CharField(max_length=11, validators=[RegexValidator(regex="^[0-9]+$", message='Digite apenas números', code='nomatch'), MinLengthValidator(11)], help_text='Digite o cpf do chefe da família')
    endereco = models.CharField(max_length=200, help_text='Digite o endereço do chefe da família', verbose_name='endereço')
    telefone1 = models.CharField(max_length=16, help_text='Digite o telefone principal do chefe da família', verbose_name='telefone principal')
    telefone2 = models.CharField(max_length=16, blank=True, null=True, help_text='Digite o telefone secundário do chefe da família (opcional)', verbose_name='telefone secundário')
    data_cadastro = models.DateField(auto_now_add=True, verbose_name='data de cadastro')

    class Meta:
        ordering = ['id']
        verbose_name = 'Família'
        verbose_name_plural = 'Famílias'

    def __str__(self):
        return self.chefe_da_familia


class IntegranteFamiliar(models.Model):
    chefe_da_familia = models.ForeignKey(Familia, on_delete=models.CASCADE, help_text='Selecione o chefe da família')
    nome = models.CharField(max_length=200, help_text='Digite o nome do integrante da família')
    cpf = models.CharField(max_length=11, validators=[RegexValidator(regex="^[0-9]+$", message='Digite apenas números', code='nomatch'), MinLengthValidator(11)], help_text='Digite o cpf do integrante da família')
    telefone = models.CharField(max_length=16, help_text='Digite o telefone do membro da família', verbose_name='telefone')
    data_cadastro = models.DateField(auto_now_add=True, verbose_name='data de cadastro')

    class Meta:
        ordering = ['nome']
        verbose_name = 'Integrante de família'
        verbose_name_plural = 'Integrantes de famílias'

    def __str__(self):
        return self.chefe_da_familia.chefe_da_familia


class Entidade(models.Model):
    nome_fantasia = models.CharField(max_length=200, help_text='Digite o nome-fantasia da entidade')
    cnpj = models.CharField(max_length=14, validators=[RegexValidator(regex="^[0-9]+$", message='Digite apenas números', code='nomatch'), MinLengthValidator(14)], help_text='Digite o cnpj da entidade')
    endereco = models.CharField(max_length=200, help_text='Digite o email da entidade', verbose_name = 'endereço')
    telefone = models.CharField(max_length=16, blank=True, null=True, help_text='Digite o telefone da entidade (00)0 0000-0000 (Opcional)')
    email = models.EmailField(help_text='Digite o email da entidade')
    representante = models.ForeignKey(Usuario, on_delete=models.CASCADE, help_text='Selecione o representante da entidade')
    data_cadastro = models.DateField(auto_now_add=True, verbose_name='data de cadastro')
    
    class Meta:
        ordering = ['nome_fantasia']
        verbose_name = 'Entidade'
        verbose_name_plural = 'Entidades'

    def __str__(self):
        return self.nome_fantasia


class Item(models.Model):
    nome = models.CharField(max_length=200, help_text='Digite o nome do item')

    class Meta:
        ordering = ['nome']
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'

    def __str__(self):
        return self.nome


class Doacao(models.Model):
    chefe_da_familia = models.ForeignKey(Familia, on_delete=models.CASCADE, help_text='Selecione o chefe da família')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, help_text='Selecione o usuário representante', verbose_name="usuário")
    data = models.DateField(help_text='Informe a data da doação')
    justificativa = models.TextField(max_length=200, blank=True, null=True, help_text='Digite a justificativa da doação')
    data_cadastro = models.DateField(auto_now_add=True, verbose_name='data de cadastro')

    class Meta:
        ordering = ['data']
        verbose_name = 'Doação'
        verbose_name_plural = 'Doações'

    def __str__(self):
        return f"Doação para {self.chefe_da_familia.chefe_da_familia} feita em {self.data.strftime('%d/%m/%Y')}"


class ItensDoacao(models.Model):
    doacao = models.ForeignKey(Doacao, on_delete=models.CASCADE, help_text='Selecione a doação')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, help_text='Selecione o item')
    quantidade = models.PositiveIntegerField(help_text='Digite a quantidade do item selecionado')
    
    class Meta:
        ordering = ['doacao']
        verbose_name = 'Item de doação'
        verbose_name_plural = 'Itens de doações'
    
    def __str__(self):
        return f"Item da doação para {self.doacao.chefe_da_familia.chefe_da_familia} feita em {self.doacao.data.strftime('%d/%m/%Y')}"
    
