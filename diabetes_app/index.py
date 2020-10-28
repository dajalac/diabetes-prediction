import dash_core_components as dcc
import dash_html_components as html
import dash_auth
from dash.dependencies import Input,Output


# connect to the main app file
from app import app
from app import server

# connect to two pages
from apps import graphs_info,diabetes_test

# to authentication
VALID_USERNAME_PASSWORD_PAIRS ={'hello':'world'}
auth = dash_auth.BasicAuth(app,VALID_USERNAME_PASSWORD_PAIRS)

app.layout = html.Div([
    html.Div([
        dcc.Link('Information | ', href='/apps/graphs_info'),
        dcc.Link('Diabetes test', href='/apps/diabetes_test')
    ],className='row'),
    dcc.Location(id = 'url',refresh=False,pathname ='/apps/graphs_info'),
    html.Div(id='page-content',children=[]) # every item in the pages will go inside []
])

@app.callback(Output(component_id='page-content',component_property='children'),
              [Input(component_id='url',component_property='pathname')])
def display_page(pathaneme):
    if pathaneme== '/apps/graphs_info':
        return graphs_info.layout

    if pathaneme == '/apps/diabetes_test':
        return diabetes_test.layout
    else:
        return "404 Page Error! Please choose a link" # you can put a page instead of this msg

if __name__ == '__main__':
    app.run_server(debug=True) #todo change to false to deploy