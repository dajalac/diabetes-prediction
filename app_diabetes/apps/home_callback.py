from dash.dependencies import Input, Output
import dash
from .graphs_info_layout import layout as statistic_layout
from .diabetes_prediction_layout import layout as test_layout



def home_callback(app):
    @app.callback(
        Output(component_id='redirection', component_property='children'),
        [Input(component_id='statistics', component_property='n_clicks'),
         Input(component_id='prediction', component_property='n_clicks')])
    def update_page(precition, statistic):
        ctx = dash.callback_context
        pressed_btn = ctx.triggered[0]['prop_id'].split('.')[0]

        if pressed_btn == 'statistics':
            return statistic_layout
        if pressed_btn == 'prediction':
            return test_layout
