from django.shortcuts import render

def home(request):
    return render(request, 'menu/home.html')

def cardapio(request):
    busca = request.GET.get('busca', '') #Pega o termo digitado na busca
    drinks = []
    if busca:
        url = f'https://www.thecocktaildb.com/api/json/v1/1/search.php?s={busca}'
        response = request.get(url)
        data = response.json()
        drinks = data.get('drinks', [])
    
    range_ingredientes = [str(i) for i in range(1,16)]
    
    return render(request, 'menu/cardapio.html', {
        'drinks' : drinks,
        'range_ingredientes' : range_ingredientes,
        'busca' : busca,
        'buscou' : bool(busca)
    })
