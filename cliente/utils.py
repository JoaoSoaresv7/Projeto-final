import requests
import math

def obter_coordenadas(endereco, api_key):
    try:
        url = f"https://api.opencagedata.com/geocode/v1/json?q={endereco}&key={api_key}"
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()
        if dados['results']:
            lat = dados['results'][0]['geometry']['lat']
            lon = dados['results'][0]['geometry']['lng']
            return (lat, lon)
        else:
            return None
    except requests.exceptions.RequestException:
        return None

def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)
    a = math.sin(delta_phi / 2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c
