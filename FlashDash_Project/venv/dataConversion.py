import csv
import json

countries = []

with open('./data/country_data.csv', newline='') as csv_file:
    reader_csv = csv.reader(csv_file, delimiter=';')
    
    for row in reader_csv:
        country = {
            "country_code": row[0],
            "year": row[1],
            "percentage": row[2]
        }
        countries.append(country)

    # Convertendo a lista de dicionários para JSON
    json_paises = json.dumps(countries, indent=4)


export json_paises
