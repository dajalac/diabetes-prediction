import dash
from dash.dependencies import Input, Output
from datasets.data import create_diabetes_dataframe, create_rows_coordinates
import pandas as pd
import plotly.express as px


def graphs_callback(app):
    @app.callback(
        [Output(component_id='output_container', component_property='children'),
         Output(component_id='scatterplot', component_property='figure')],
        [Input(component_id='scatterplot_input', component_property='value')])
    def update_graph1(option_slct):
        container = "You selected: {}".format(option_slct)
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
        container = "You selected: {}".format(option_slct)
        dff = create_rows_coordinates().copy()
        fig = px.bar(pd.crosstab(dff[option_slct], dff['Diabetes']), barmode="group",
                     labels={'value': 'Number of individuals'})

        return container, fig

    @app.callback(
        [Output(component_id='output_container3', component_property='children'),
         Output(component_id='boxplot', component_property='figure')],
        [Input(component_id='boxplot_input', component_property='value')])
    def update_graph3(option_slct):
        container = "You selected: {}".format(option_slct)
        df = create_diabetes_dataframe().copy()
        # #get positive restults
        # df_positive = df.loc[df[option_slct]=='Yes']
        # #df_negative = df.loc[df[option_slct]=='No']
        #
        # df=df.loc[df['age']== df_positive]
        fig = px.box(df, x=option_slct, y='age')

        return container, fig