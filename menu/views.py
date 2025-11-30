import requests
from django.shortcuts import render
from api.utils import previsao_tempo, obter_lat_lon_por_cidade


# ----------------------------
# HOME – Previsão do tempo
# ----------------------------
def home(request):
    cidade = request.GET.get('cidade', 'São Paulo').strip()

    # Se a cidade existir, buscar coordenadas
    latitude, longitude = obter_lat_lon_por_cidade(cidade) if cidade else (-23.5505, -46.6333)

    clima = None

    if latitude and longitude:
        weather = previsao_tempo(latitude, longitude)

        if weather:
            temp = weather.get('temperature')
            wind = weather.get('windspeed')
            weathercode = weather.get('weathercode')

            descricao = {
                0: "céu limpo ☀️",
                1: "principalmente limpo ⛅",
                2: "parcialmente nublado",
                3: "nublado ☁️",
                45: "neblina",
                48: "gelo/neblina ❄️",
                51: "chuvisco leve",
                53: "chuvisco moderado",
                55: "chuvisco denso",
                61: "chuva leve",
                63: "chuva moderada",
                65: "chuva intensa ⛈️",
                80: "aguaceiro leve",
                81: "aguaceiro moderado",
                82: "aguaceiro forte ⛈️",
            }.get(weathercode, "indefinido")

            clima = f"{descricao}, {temp}°C, vento {wind}km/h"
        else:
            clima = "Cidade não encontrada."

    return render(request, 'menu/home.html', {
        'cidade': cidade,
        'clima': clima
    })


# ----------------------------
# CARDÁPIO – Drinks API
# ----------------------------
def cardapio(request):
    busca = request.GET.get('busca', '').strip()
    drinks = []

    if busca:
        url = f'https://www.thecocktaildb.com/api/json/v1/1/search.php?s={busca}'
        response = requests.get(url)
        data = response.json()
        drinks = data.get('drinks', [])

    range_ingredientes = [str(i) for i in range(1, 16)]

    return render(request, 'menu/cardapio.html', {
        'drinks': drinks,
        'range_ingredientes': range_ingredientes,
        'busca': busca,
        'buscou': bool(busca),
    })
