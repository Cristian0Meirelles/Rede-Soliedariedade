# Generated by Django 4.0.1 on 2022-01-16 16:06

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Doacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(help_text='Informe a data da doação')),
                ('justificativa', models.TextField(blank=True, help_text='Digite a justificativa da doação', max_length=200, null=True)),
                ('data_cadastro', models.DateField(auto_now_add=True, verbose_name='data de cadastro')),
            ],
            options={
                'verbose_name': 'Doação',
                'verbose_name_plural': 'Doações',
                'ordering': ['data'],
            },
        ),
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chefe_da_familia', models.CharField(help_text='Digite o nome do chefe da família', max_length=200)),
                ('cpf', models.CharField(help_text='Digite o cpf do chefe da família', max_length=11, validators=[django.core.validators.RegexValidator(code='nomatch', message='Digite apenas números', regex='^[0-9]+$'), django.core.validators.MinLengthValidator(11)])),
                ('endereco', models.CharField(help_text='Digite o endereço do chefe da família', max_length=200, verbose_name='endereço')),
                ('telefone1', models.CharField(help_text='Digite o telefone principal do chefe da família', max_length=16, verbose_name='telefone principal')),
                ('telefone2', models.CharField(blank=True, help_text='Digite o telefone secundário do chefe da família (opcional)', max_length=16, null=True, verbose_name='telefone secundário')),
                ('data_cadastro', models.DateField(auto_now_add=True, verbose_name='data de cadastro')),
            ],
            options={
                'verbose_name': 'Família',
                'verbose_name_plural': 'Famílias',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Digite o nome do item', max_length=200)),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Itens',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='ItensDoacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField(help_text='Digite a quantidade do item selecionado')),
                ('doacao', models.ForeignKey(help_text='Selecione a doação', on_delete=django.db.models.deletion.CASCADE, to='gestao_de_doacoes.doacao')),
                ('item', models.ForeignKey(help_text='Selecione o item', on_delete=django.db.models.deletion.CASCADE, to='gestao_de_doacoes.item')),
            ],
            options={
                'verbose_name': 'Item de doação',
                'verbose_name_plural': 'Itens de doações',
                'ordering': [],
            },
        ),
        migrations.CreateModel(
            name='IntegranteFamiliar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Digite o nome do integrante da família', max_length=200)),
                ('cpf', models.CharField(help_text='Digite o cpf do integrante da família', max_length=11, validators=[django.core.validators.RegexValidator(code='nomatch', message='Digite apenas números', regex='^[0-9]+$'), django.core.validators.MinLengthValidator(11)])),
                ('telefone', models.CharField(help_text='Digite o telefone do membro da família', max_length=16, verbose_name='telefone')),
                ('data_cadastro', models.DateField(auto_now_add=True, verbose_name='data de cadastro')),
                ('chefe_da_familia', models.ForeignKey(help_text='Selecione o chefe da família', on_delete=django.db.models.deletion.CASCADE, to='gestao_de_doacoes.familia')),
            ],
            options={
                'verbose_name': 'Integrante de família',
                'verbose_name_plural': 'Integrantes de famílias',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Entidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_fantasia', models.CharField(help_text='Digite o nome-fantasia da entidade', max_length=200)),
                ('cnpj', models.CharField(help_text='Digite o cnpj da entidade', max_length=14, validators=[django.core.validators.RegexValidator(code='nomatch', message='Digite apenas números', regex='^[0-9]+$'), django.core.validators.MinLengthValidator(14)])),
                ('endereco', models.CharField(help_text='Digite o email da entidade', max_length=200, verbose_name='endereço')),
                ('telefone', models.CharField(blank=True, help_text='Digite o telefone da entidade (00)0 0000-0000 (Opcional)', max_length=16, null=True)),
                ('email', models.EmailField(help_text='Digite o email da entidade', max_length=254)),
                ('data_cadastro', models.DateField(auto_now_add=True, verbose_name='data de cadastro')),
                ('representante', models.ForeignKey(help_text='Selecione o representante da entidade', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Entidade',
                'verbose_name_plural': 'Entidades',
                'ordering': ['nome_fantasia'],
            },
        ),
        migrations.AddField(
            model_name='doacao',
            name='chefe_da_familia',
            field=models.ForeignKey(help_text='Selecione o chefe da família', on_delete=django.db.models.deletion.CASCADE, to='gestao_de_doacoes.familia'),
        ),
        migrations.AddField(
            model_name='doacao',
            name='usuario',
            field=models.ForeignKey(help_text='Selecione o usuário representante', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='usuário'),
        ),
    ]
