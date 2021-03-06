import dash_core_components as dcc
import dash_html_components as html
import dash_auth
from dash.dependencies import Input,Output
import dash_bootstrap_components as dbc

# connect to the main app file
from app import app
from app import server

# connect to two pages
from apps import graphs_info_layout,diabetes_prediction_layout,home_page_layout

# to authentication
VALID_USERNAME_PASSWORD_PAIRS ={'hello':'world'}
auth = dash_auth.BasicAuth(app,VALID_USERNAME_PASSWORD_PAIRS)

link_style = {'font-weight': 'bold', 'color': 'white'}
app.layout = html.Div([
   dbc.Nav(
            [
                dbc.NavLink("Home", href="/apps/home_layout", style=link_style),
                dbc.NavLink("Statistics", href="/apps/graphs_info_layout",style=link_style),
                dbc.NavLink( "Prediction test", href="/apps/diabetes_prediction_layout",style=link_style),
            ], style={"background": "#20B2AA", "height":"50px"}
        ),
    dcc.Location(id = 'url',refresh=False,pathname ='/apps/home_page_layout.py'),
    html.Div(id='page-content',children=[]), # every item in the pages will go inside []
])

@app.callback(Output(component_id='page-content',component_property='children'),
              [Input(component_id='url',component_property='pathname')])
def display_page(pathaneme):
    if pathaneme == '/apps/graphs_info_layout':
        return graphs_info_layout.layout

    if pathaneme == '/apps/diabetes_prediction_layout':
        return diabetes_prediction_layout.layout
    else:
        return home_page_layout.layout # you can put a page instead of this msg

if __name__ == '__main__':
    app.run_server(debug=True) #todo change to false to deploy