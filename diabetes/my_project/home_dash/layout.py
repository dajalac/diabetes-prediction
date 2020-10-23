import dash_core_components as dcc
import dash_html_components as html

# plotly dash layout
layout = html.Div([
    html.H1("my first try", style = {'text-aling':'center'}),

    dcc.Dropdown(id="select_age",
                 options = [
                     {'label':"less than 30 years old", 'value':'young adult'},
                     {'label':"between 30 and 60 years old", 'value':'adult'},
                     {'label':"more than 60 years old", 'value':'young adult'}],
                 multi = False,
                 style = {'width':'40%'}
                 ),
    html.Div(id='output_container', children=[]),
    html.Br(),

    dcc.Graph(id='scatterplot', figure={})
    ])