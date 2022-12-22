from django.contrib import admin
from .models import Familia, IntegranteFamiliar, Entidade, Item, ItensDoacao, Doacao

@admin.register(Familia)
class FamiliaAdmin(admin.ModelAdmin):
    list_display = ('chefe_da_familia', 'endereco', 'telefone1')
    list_filter = ('chefe_da_familia', 'endereco')


@admin.register(IntegranteFamiliar)
class IntegranteFamiliarAdmin(admin.ModelAdmin):
    list_display = ('chefe_da_familia', 'nome')
    list_filter = ('chefe_da_familia__chefe_da_familia', 'nome')


@admin.register(Entidade)
class EntidadeAdmin(admin.ModelAdmin):
    list_display = ('nome_fantasia', 'email', 'telefone')
    list_filter = ('nome_fantasia', 'email')

admin.site.register(Item)

@admin.register(ItensDoacao)
class ItensDoacaoAdmin(admin.ModelAdmin):
    list_display = ('doacao', 'item', 'quantidade')
    list_filter = ('doacao', 'item')

@admin.register(Doacao)
class DoacaoAdmin(admin.ModelAdmin):
    list_display = ('chefe_da_familia', 'usuario', 'data')
    list_filter = ('chefe_da_familia__chefe_da_familia', 'usuario__username', 'data')