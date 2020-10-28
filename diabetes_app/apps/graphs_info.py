from datasets.data import create_diabetes_dataframe, create_rows_coordinates
from dash.dependencies import Input,Output
import plotly.express as px
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
from app import app

layout= html.Div([
    html.Div([
        html.H1("my first try", style={'text-aling': 'center'}),

        dcc.Dropdown(id="scatterplot_input",
                     options=[
{'label': "Alopecia (baldeness)", 'value': 'alopecia'},
                         {'label': "Delayed Healing", 'value': 'delayed healing'},
                         {'label': "Irritability", 'value': 'irritability'},
                         {'label': "Muscle Stiffness", 'value': 'muscle stiffness'},
                         {'label': "Obesity", 'value': 'obesity'},
                         {'label': "Polyphagia (Excessive Hunger)", 'value': 'polyphagia'},
                         {'label': "Polyuria", 'value': 'polyuria'},
                         {'label': "Sudden Weight Loss", 'value': 'sudden weight loss'},
                         {'label': "Visual Blurring", 'value': 'visual blurring'}],
                     multi=False,
                     value='obesity',
                     style={'width': '40%'}
                     ),
        html.Div(id='output_container', children=[]),
        html.Br(),
        dcc.Graph(id='scatterplot', figure={})
    ]),

    html.Div([

        html.H3('bar plot graph test'),
        dcc.Dropdown(id="bar_chart_input",
                     options=[
                         {'label': "Alopecia (baldeness)", 'value': 'alopecia'},
                         {'label': "Delayed Healing", 'value': 'delayed healing'},
                         {'label': "Irritability", 'value': 'irritability'},
                         {'label': "Muscle Stiffness", 'value': 'muscle stiffness'},
                         {'label': "Obesity", 'value': 'obesity'},
                         {'label': "Polyphagia (Excessive Hunger)", 'value': 'polyphagia'},
                         {'label': "Polyuria", 'value': 'polyuria'},
                         {'label': "Sudden Weight Loss", 'value': 'sudden weight loss'},
                         {'label': "Visual Blurring", 'value': 'visual blurring'}],
                     multi=False,
                     value='obesity',
                     style={'width': '40%'}
                     ),
        html.Div(id='output_container2', children=[]),
        html.Br(),
        dcc.Graph(id='Barplot', figure={})
    ]),
    html.Div([
        html.H3('Age plot'),
        dcc.Dropdown(id="boxplot_input",
                     options=[
                         {'label': "Female", 'value': 'Female'},
                         {'label': "Male", 'value': 'Male'}],
                     multi=False,
                     value='Female',
                     style={'width': '40%'}
                     ),
        html.Div(id='output_container3', children=[]),
        html.Br(),
        dcc.Graph(id='boxplot', figure={})
    ])
])

@app.callback(
        [Output(component_id='output_container', component_property='children'),
         Output(component_id='scatterplot', component_property='figure')],
        [Input(component_id='scatterplot_input', component_property='value')])
def update_graph1(option_slct):
        container = "The age selected by user was: {}".format(option_slct)
        dff = create_rows_coordinates().copy()
        # dff = dff.loc[dff['c_age'] == option_slct]
        # dff=dff[option_slct]
        fig = px.scatter(dff, x='0', y='1', color='Diabetes', symbol=option_slct,
                         title='Multiple Correspondence Analysis (MCA)',
                         labels={'0': 'Component 0 (22.2% inertia)',
                                 '1': 'Component 1 (12.74% inertia)',
                                 })
        fig.update_traces(marker=dict(size=10))
        symbols = {'Positive, Yes': 'circle',
                   'Positive, No': 'square',
                   'Negative, Yes': 'circle-open',
                   'Negative, No': 'square-open'}
        for i, d in enumerate(fig.data):
            fig.data[i].marker.symbol = symbols[fig.data[i].name]

        return container, fig

@app.callback(
        [Output(component_id='output_container2', component_property='children'),
         Output(component_id='Barplot', component_property='figure')],
        [Input(component_id='bar_chart_input', component_property='value')])
def update_graph2(option_slct):
        container = "The attribute selected by user was: {}".format(option_slct)
        dff = create_rows_coordinates().copy()
        fig = px.bar(pd.crosstab(dff[option_slct], dff['Diabetes']), barmode="group",
                     labels={'value': 'Number of individuals'})

        return container, fig

@app.callback(
         [Output(component_id='output_container3', component_property='children'),
         Output(component_id='boxplot', component_property='figure')],
        [Input(component_id='boxplot_input', component_property='value')])
def update_graph3(option_slct):
        container = "The gender selected by user was: {}".format(option_slct)
        df = create_diabetes_dataframe().copy()
        df=df.loc[df['Gender']==option_slct]
        fig = px.box(df, x='Diabetes',y='Age')
        return container, fig