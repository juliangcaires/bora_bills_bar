from django.urls import path
from .views import home, cardapio



urlpatterns = [
    path('', home, name='home'),
    path('cardapio/', cardapio, name='cardapio'),
]

