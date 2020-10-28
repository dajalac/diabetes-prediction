from dash.dependencies import Input,Output
import plotly.express as px
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from app import app
#app.css.append_css({'external_url': 'https://codepen.io/amyoshino/pen/jzXypZ.css'})

layout = html.Div([
    dbc.Tabs(id='tabs',active_tab='tab_1',children=[
        dbc.Tab(tab_id='tab_1',label='1',children=[
            dbc.Container([
                dbc.Row([
                    dbc.Col(html.Div(html.H4("are you obese?"))),
                    dbc.Col([
                        dcc.RadioItems(options=[
                                    {'label': 'Yes', 'value': 1},
                                    {'label': 'No', 'value': 0}])
                    ]) ]),
                dbc.Row([
                    dbc.Col(html.Div(html.H4("are you obese?"))),
                    dbc.Col([
                        dcc.RadioItems(options=[
                                    {'label': 'Yes', 'value': 1},
                                    {'label': 'No', 'value': 0}])
                    ]),
                dbc.Button(id='btn1',children='Next')
            ])
        ],fluid= True)
    ])
    ]),
   dbc.Container([
        dbc.Row([
            dbc.Col(html.Div(html.H4("are you obese?"))),
            dbc.Col([
                dcc.RadioItems(options=[
                            {'label': 'Yes', 'value': 1},
                            {'label': 'No', 'value': 0}])
            ])
        ]),
        dbc.Row([
            dbc.Col(html.Div(html.H4("are you obese?"))),
            dbc.Col([
                dcc.RadioItems(options=[
                            {'label': 'Yes', 'value': 1},
                            {'label': 'No', 'value': 0}])
            ])
        ]),
       dbc.Row([
            dbc.Col(html.Div(html.H4("are you obese?"))),
            dbc.Col([
                dcc.RadioItems(options=[
                            {'label': 'Yes', 'value': 1},
                            {'label': 'No', 'value': 0}])
            ])
        ]),
       dbc.Row([
            dbc.Col(html.Div(html.H4("are you obese?"))),
            dbc.Col([
                dcc.RadioItems(options=[
                            {'label': 'Yes', 'value': 1},
                            {'label': 'No', 'value': 0}])
            ])
        ]),
       dbc.Row([
            dbc.Col(html.Div(html.H4("are you obese?"))),
            dbc.Col([
                dcc.RadioItems(options=[
                            {'label': 'Yes', 'value': 1},
                            {'label': 'No', 'value': 0}])
            ])
        ])

   ])
])

# def layout( ):
#     test= dbc.FormGroup([
#         dbc.Label("Are you obese?", html_for="example-radios-row", width=2),
#         dbc.Col(
#             dbc.RadioItems(
#                 id='test',
#                 options=[
#                     {'label': 'Yes', 'value': 1},
#                      {'label': 'No', 'value': 0},],), width=10,),
#     ], row=True)
#     form = dbc.Form(test)
#     return form