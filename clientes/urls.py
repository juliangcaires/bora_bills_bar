from django.urls import path
from .views import lista_clientes

urlpatterns= [
    path('ranking/', lista_clientes, name='ranking_clientes'),
]