from django.shortcuts import render
from .models import Cliente

def lista_clientes(request):
    clientes = Cliente.objects.order_by('-pontos', 'nome')
    return render(request, 'clientes/lista_clientes.html', 
        {'clientes' : clientes})