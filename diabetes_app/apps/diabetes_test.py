from dash.dependencies import Input,Output
import plotly.express as px
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from app import app
#app.css.append_css({'external_url': 'https://codepen.io/amyoshino/pen/jzXypZ.css'})

from .callbacks import diabetes_test_callback

layout = html.Div([
    dbc.Tabs(id='tabs',active_tab='tab_1',children=[
        dbc.Tab(tab_id='tab_1',label='1',children=[
dbc.Container([
                dbc.Col(html.Div(html.H5("1. Which category below includes your age? "))),
                dbc.Col([
                    dcc.RadioItems(id='age',options=[{'label': 'Less than 30 years old', 'value': 2},
                                            {'label': 'Between 30 and 59 years old', 'value': 0},
                                            {'label': 'More than 59 years old','value':1}])
                    ]),
                 dbc.Col(html.Div(html.H5("2. Gender"))),
                  dbc.Col([
                    dcc.RadioItems(id='gender', options=[{'label': 'Female', 'value': 0}, {'label': 'Male', 'value': 1}])
                    ]),
                dbc.Col(html.Div(html.H5("3. Have you been experiencing polyuria (excessive urination)?"))),
                  dbc.Col([
                    dcc.RadioItems(id='urination', options=[{'label': 'Yes', 'value': 1}, {'label': 'No', 'value': 0}])
                    ]),
                dbc.Col(html.Div(html.H5("4. Have you been experiencing excessively thirsty?"))),
                  dbc.Col([
                    dcc.RadioItems(id='thirsty',options=[{'label': 'Yes', 'value': 1}, {'label': 'No', 'value': 0}])
                    ]),
                dbc.Col(html.Div(html.H5("5. Have you been experiencing sudden weight loss?"))),
                  dbc.Col([
                    dcc.RadioItems(id='weight_loss',options=[{'label': 'Yes', 'value': 1}, {'label': 'No', 'value': 0}])
                    ]),
                dbc.Col(html.Div(html.H5("6. Have you been experiencing weakness?"))),
                  dbc.Col([
                    dcc.RadioItems(id='weakness',options=[{'label': 'Yes', 'value': 1}, {'label': 'No', 'value': 0}])
                    ]),
                html.Br(),
                dbc.Button("Next", id='next1',color="success", className="mr-1")
                # dbc.Col(dbc.Button(id='btn1',children='Previous'),className="mr-1"),
                # dbc.Col(dbc.Button(id='btn1',children='Next'),className="mr-1")
                #dbc.Button(id='btn1',children='Next')
            ],fluid=True)
        ]),
        dbc.Tab(tab_id='tab_2',label='2',children=[
            dbc.Container([
                dbc.Col(html.Div(html.H5("7. Have you been experiencing polyphagia (excessive eating)? "))),
                dbc.Col([
                  dcc.RadioItems(id='eating', options=[{'label': 'Yes', 'value': 1}, {'label': 'No', 'value': 0}])
                    ]),
                 dbc.Col(html.Div(html.H5("8. Have you been experiencing genital thrush (candidiasis) ?"))),
                  dbc.Col([
                    dcc.RadioItems(id='genital_thrush',options=[{'label': 'Yes', 'value': 1}, {'label': 'No', 'value': 0}])
                    ]),
                dbc.Col(html.Div(html.H5("9. Have you been experiencing visual blurring ?"))),
                  dbc.Col([
                    dcc.RadioItems(id='visual_blurring', options=[{'label': 'Yes', 'value': 1}, {'label': 'No', 'value': 0}])
                    ]),
                dbc.Col(html.Div(html.H5("10. Have you been experiencing body itching ?"))),
                  dbc.Col([
                    dcc.RadioItems(id='itching',options=[{'label': 'Yes', 'value': 1}, {'label': 'No', 'value': 0}])
                    ]),
                dbc.Col(html.Div(html.H5("11. Have you been experiencing irritability?"))),
                  dbc.Col([
                    dcc.RadioItems(id='irritability',options=[{'label': 'Yes', 'value': 1}, {'label': 'No', 'value': 0}])
                    ]),
                dbc.Col(html.Div(html.H5("12. Have you been experiencing delayed wound healing?"))),
                  dbc.Col([
                    dcc.RadioItems(id='delayed_healing',options=[{'label': 'Yes', 'value': 1}, {'label': 'No', 'value': 0}])
                    ]),
                html.Br(),
                dbc.Button("Previous",id='previous_2', color="success", className="mr-1"),
                dbc.Button("Next", id='next_2',color="success", className="mr-1")
            ],fluid=True)
        ]),
        dbc.Tab(tab_id='tab_3',label='3',children=[
            dbc.Container([
                dbc.Col(html.Div(html.H5("13. Have you been experiencing partial paresis ? "))),
                dbc.Col([
                  dcc.RadioItems(id='partial_paresis', options=[{'label': 'Yes', 'value': 1}, {'label': 'No', 'value': 0}])
                    ]),
                 dbc.Col(html.Div(html.H5("14. Have you been experiencing muscle stiffness?"))),
                  dbc.Col([
                    dcc.RadioItems(id='muscle_stiffness',options=[{'label': 'Yes', 'value': 1}, {'label': 'No', 'value': 0}])
                    ]),
                dbc.Col(html.Div(html.H5("15. Have you been experiencing alopecia (Sudden hair loss , baldness) ?"))),
                  dbc.Col([
                    dcc.RadioItems(id='alopecia', options=[{'label': 'Yes', 'value': 1}, {'label': 'No', 'value': 0}])
                    ]),
                dbc.Col(html.Div(html.H5("16. Are you obese?"))),
                  dbc.Col([
                    dcc.RadioItems(id='obese',options=[{'label': 'Yes', 'value': 1}, {'label': 'No', 'value': 0}])
                    ]),
                html.Br(),
                dbc.Button("Previous",id='previous3', color="success", className="mr-1"),
                dbc.Button("Submit", id='submit',color="success", className="mr-1")
            ],fluid=True)
        ])
    ]),
      html.Div(id='test_result', children=[])
    ])
diabetes_test_callback(app)
# @app.callback(
#         Output(component_id='tabs', component_property='active_tab'),
#         [Input(component_id='next1', component_property='n_clicks')])
# def update_graph3(clicks):
#     if clicks:
#         return "tab_2"
#     else:
#         return "tab_1"

   # dbc.Container([
   #      dbc.Row([
   #          dbc.Col(html.Div(html.H4("are you obese?"),style={"border":"2px black solid"})),
   #          dbc.Col([
   #              dcc.RadioItems(options=[
   #                          {'label': 'Yes', 'value': 1},
   #                          {'label': 'No', 'value': 0}])
   #          ])
   #      ]),
   #      dbc.Row([
   #          dbc.Col(html.Div(html.H4("are you obese?"))),
   #          dbc.Col([
   #              dcc.RadioItems(options=[
   #                          {'label': 'Yes', 'value': 1},
   #                          {'label': 'No', 'value': 0}])
   #          ])
   #      ]),
   #     dbc.Row([
   #          dbc.Col(html.Div(html.H4("are you obese?"))),
   #          dbc.Col([
   #              dcc.RadioItems(options=[
   #                          {'label': 'Yes', 'value': 1},
   #                          {'label': 'No', 'value': 0}])
   #          ])
   #      ]),
   #     dbc.Row([
   #          dbc.Col(html.Div(html.H4("are you obese?"))),
   #          dbc.Col([
   #              dcc.RadioItems(options=[
   #                          {'label': 'Yes', 'value': 1},
   #                          {'label': 'No', 'value': 0}])
   #          ])
   #      ]),
   #     dbc.Row([
   #          dbc.Col(html.Div(html.H4("are you obese?"))),
   #          dbc.Col([
   #              dcc.RadioItems(options=[
   #                          {'label': 'Yes', 'value': 1},
   #                          {'label': 'No', 'value': 0}])
   #          ])
   #      ])
   #
   # ])
# ])

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