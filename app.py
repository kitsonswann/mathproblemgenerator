from dash import Dash, html, dcc, callback, Output, Input, State
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from worksheetgenerator.helpers import generate_table_rows, load_images

IMAGES = load_images()

app = Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)

app.layout = html.Div([
        dbc.Row(
            dbc.Col(
                [
                    dbc.Row(dbc.Col(html.Div(html.Button('Generate Problem Set', id='generate-submit', n_clicks=0)))),
                    dbc.Row(dbc.Col(html.Div(html.H1(children='Paw Patrol Kumon', style={'textAlign':'center'})))),
                    dbc.Row(dbc.Col(html.Div(id='mathtable', children=[], className='responsive-table'))),
                ]
            )
        )
])

@callback(
    Output('mathtable', 'children'),
    Input('generate-submit', 'n_clicks'),
    prevent_initial_call=True
)
def update_output(n_clicks):
    if n_clicks:
        return generate_table_rows(IMAGES)

if __name__ == '__main__':
    app.run(debug=True)
