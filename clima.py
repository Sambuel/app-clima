import requests
from colorama import Fore,Style

print(Fore.GREEN + "Hola este es un software que te ayuda a saber el clima de la ciudad que quieras" + Style.RESET_ALL)
ciudad = input("Ingresa la ciudad: ")

respuesta = requests.get(
    "https://geocoding-api.open-meteo.com/v1/search",
    params={"name":ciudad,"count":1}
) 

datos = respuesta.json()
diccionario_ciudad = datos["results"][0]
latitud = diccionario_ciudad["latitude"]
longitud= diccionario_ciudad["longitude"]


buscar_clima = requests.get(
    "https://api.open-meteo.com/v1/forecast",
    params={"latitude": latitud, "longitude": longitud, "current_weather": True}
)

datos_dos = buscar_clima.json()

temperatura_al_momento = datos_dos["current_weather"]["temperature"]
velocidad_viento = datos_dos["current_weather"]["windspeed"]
codigo_numerico = datos_dos["current_weather"]["weathercode"]

"""
La tabla oficial (WMO) tiene códigos como:
0 → Despejado
1, 2, 3 → Principalmente despejado / Parcialmente nublado / Nublado
45, 48 → Niebla
51, 53, 55 → Llovizna
61, 63, 65 → Lluvia
71, 73, 75 → Nieve
95 → Tormenta
"""

codigos = {
    0:"despejado",
    1:"Principalmente Despejado",
    2:"Parcialmente nublado",
    3:"Nublado",
    45:"Niebla",
    48:"Niebla",
    51:"Llovizna",
    53:"Llovizna",
    55:"Llovizna",
    61:"Lluvia",
    63:"Lluvia",
    65:"Lluvia",
    71:"Nieve",
    73:"Nieve",
    75:"Nieve",
    80:"Chubasco ligero",
    81:"Chubasco moderado",
    82:"chubasco violento",
    95:"Tormenta",

}

descripcion = codigos.get(codigo_numerico,"error del clima")
print(descripcion)
print(f"La velocidad del viento es de {velocidad_viento}")
print(f"La temperatura de {ciudad} es de {temperatura_al_momento}")
