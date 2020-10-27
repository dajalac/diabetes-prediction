import dash_core_components as dcc
import dash_html_components as html

# plotly dash layout

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
