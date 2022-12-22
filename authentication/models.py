from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator, MinLengthValidator

# Create your models here.
class Usuario(AbstractUser):
    cpf = models.CharField(max_length=11, validators=[RegexValidator(regex="^[0-9]+$", message='Digite apenas números', code='nomatch'), MinLengthValidator(11)])
    telefone = models.CharField(max_length=16, blank=True, null=True, help_text='Digite o telefone do representante (00)0 0000-0000 (Opcional)')

    def is_representante(self):
        return self.groups.filter(name='Representante').exists()
  