import dataConversion
import json

json_countries = json.loads(dataConversion.json_paises)

with open('./data/coordenadas.json', 'r') as file:
    coord = json.load(file)
#print(coord)
# json que ira receber os dados combinados
coordinates_countries = []

for country in json_countries:
    if country["country_code"] in coord:
        country["coordinates"] = coord[country["country_code"]]
        coordinates_countries.append(country)
    else:
        print(f"Coordinates did not found for this country")

print(coordinates_countries)