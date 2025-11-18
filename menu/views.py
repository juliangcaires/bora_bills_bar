import requests

from django.shortcuts import render #reder renderização

def cardapio(request):
  busca = request.GET.get('busca', '') #pega o termo digitado
  drinks = []
  if busca:
    url = f'https://www.thecocktaildb.com/api/json/v1/1/search.php?s={busca}'
    response = requests.get(url)
    data = response.json()
    drinks = data.get('drinks', [])

  range_ingedientes = [str(i) for i in range(1,16)] #1 a 15

  return render(requests, 'menu/cardapio.html', { 
  'drinks' : drinks,
  "range_ingredientes" : range_ingedientes,
  'busca'  : busca,
  'buscou' : bool(busca), #define se o usuário buscou algo
})

# Create your views here.
def home(request):
  return render (request, 'menu/home.html')
