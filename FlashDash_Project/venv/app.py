# Importando os módulos necessários do Dash e do Plotly
import dash
from dash import dcc, html
import plotly.graph_objs as go

# Importando os dados dos países do arquivo coordinatesConversion.py
import coordinatesConversion

# Obtendo os dados dos países
country_data = coordinatesConversion.coordinates_countries

# Calculando as coordenadas de longitude e latitude de cada país
lons = [country["coordinates"]["coordinates"][1] for country in country_data]
lats = [country["coordinates"]["coordinates"][0] for country in country_data]

# Calculando os limites do mapa
lon_min = min(lons)
lon_max = max(lons)
lat_min = min(lats)
lat_max = max(lats)

# Margem adicional para evitar que os marcadores fiquem muito na borda do mapa
margin = 1  # graus de latitude/longitude

# Ajustando os limites com uma margem
lon_range = [lon_min - margin, lon_max + margin]
lat_range = [lat_min - margin, lat_max + margin]

# Inicializando o aplicativo Dash
app = dash.Dash(__name__)

# Criando uma lista para armazenar os marcadores dos países
markers = []

# Criando os marcadores para cada país
for country in country_data:
    percentage = float(country["percentage"].replace(",", "."))
    marker_text = f"{country["coordinates"]["name"]}<br>" \
                  f"Percentage: {100 * percentage:.2f}%<br>" \
                  f"Code: {country["country_code"]}"

    markers.append(
        go.Scattergeo(
            lon=[country["coordinates"]["coordinates"][1]],
            lat=[country["coordinates"]["coordinates"][0]],
            mode='markers',
            text=[marker_text],
            showlegend=False,  # Oculta a legenda do gráfico,
            hoverinfo='text'
        )
    )

# Configurando o layout da aplicação Dash
app.layout = html.Div([
    html.H1('Approximated estimates for the share of gross final consumption of renewable energy sources, 2022'),  # Título da página
    dcc.Graph(
        id='europe-map',
        style={'height': '90vh', 'width': '100%'},  # Estilo do gráfico
        figure={
            'data': markers,  # Dados (marcadores dos países)
            'layout': go.Layout(
                geo=dict(
                    scope='europe',  # Escopo do mapa (Europa)
                    projection=dict(type='mercator'),  # Projeção Mercator
                    showland=True,  # Mostra a terra
                    landcolor='rgb(240, 240, 240)',  # Cor da terra
                    countrycolor='rgb(204, 204, 204)',  # Cor dos países
                    coastlinecolor='rgb(138, 138, 138)',  # Cor das linhas costeiras
                    showocean=True,  # Mostra o oceano
                    oceancolor='rgb(204, 255, 255)',  # Cor do oceano
                    showlakes=True,  # Mostra os lagos
                    lakecolor='rgb(204, 255, 255)',  # Cor dos lagos
                    fitbounds='locations',  # Ajusta os limites do mapa com base nas coordenadas dos países
                    lonaxis=dict(range=lon_range),  # Limites do eixo de longitude
                    lataxis=dict(range=lat_range)  # Limites do eixo de latitude
                ),
                title='Map of Europe',  # Título do gráfico
                margin={'l': 0, 'r': 0, 't': 30, 'b': 0}  # Margens do gráfico
            )
        }
    )
])

# Executando o aplicativo Dash
if __name__ == '__main__':
    app.run_server(debug=True)
