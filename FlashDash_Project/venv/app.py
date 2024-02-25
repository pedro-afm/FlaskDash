import dash
from dash import dcc, html
import plotly.graph_objs as go


# inicializando app Dash
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Interactive Map of Europe'),
    dcc.Graph(
        id='europe-map',
        figure={
            'data' : [
                go.Scattergeo(
                    lon=[-0.1276],
                    lat=[51.5072],
                    mode='markers',
                    marker=dict(size=10, color='red'),
                    text='London'
                )
            ],
            'layout': go.Layout(
                geo=dict(
                    scope='europe',
                    projection=dict(type='equirectangular'),
                    showland=True,
                    landcolor='rgb(217, 217, 217)',
                    countrycolor='rgb(255, 255, 255)'
                ),
                title='Map of Europe'
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)