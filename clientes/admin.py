from django.contrib import admin
from .models import Cliente
# Register your models here.

@admin.register(Cliente)#decorator
class Clientes(admin.ModelAdmin):
  list_display = ('nome', 'email', 'data_cadastro', 'pontos')
  search_fields = ('nome', 'email')
  list_filter = ('data_cadastro',)

#depois no terminal rode
