import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from .home_callback import home_callback
from app import app

page_layout = {
               "padding": "1rem 1rem",
               "text-align": "justify",
               "text-justify":"inter-word",
               "font-family": "'Times New Roman', Times, serif",
               "background-color":"warning"}
fig_css = { "display": "block","margin-left": "auto", "margin-right": "auto", "width": "80%"}


layout = html.Div([
    dbc.Card([
      html.Br(),
      dbc.CardImg(src=app.get_asset_url('diabetes.jpg'),top=True, bottom= False,style=fig_css),
        html.Br(),
      dbc.CardBody([
        html.H4('What is diabetes?',style={'color':'#708090'}),
        html.P([' Diabetes is a chronic, metabolic disease in which the body does not properly'
                ' process food for use of energy. This condition elevates blood sugar levels which,'
                ' over time leads to heart attacks, blindness, kidney failure, stroke,'
                ' and other serious complications such as amputation of toe, foot, or legs.'
                ]),
        html.P(['They are two types of diabetes. Type 2 diabetes is the most common, which occurs when'
                ' the organism becomes resistant to insulin or does not produce enough insulin.'
                ' Type 1 diabetes is a chronic condition in which the pancreas makes none or a small amount of '
                'insulin by itself.  '
                ]),
        html.P(['According to World Health Organization (WHO) about 422 million people worldwide have diabetes'
                ' and 1.6 million deaths are directly attributed to disease each year.Unfortunately, diabetes'
                ' have a long asymptomatic phase, half of all people suffering from diabetes are undiagnosed because'
                ' of its long-term asymptomatic phase. The early diagnosis is important for a better treatment outcome. ']),
        html.H4('About our model',style={'color':'#708090'}),
        html.P(["The analysis and graphs were conducted based on questionnaires from the patients of Sylhet Diabetes "
               "Hospital in Sylhet, Bangladesh available ",
               html.A('here.',href='https://archive.ics.uci.edu/ml/datasets/Early+stage+diabetes+risk+prediction+dataset.')]),
        html.P(['This website is a tool to arise diabetes awareness which will allow you to check out some statistic '
                'related to the disease and also to take a virtual diabetes prediction test. Although our analysis were '
                'conducted with a high level technology (machine learning) our results does not substitute a doctor '
                'evaluation. Independently of the result, always consult your physician for a better evaluation. ']),

        dbc.Button("Statistics",id='statistics', color="success", className="mr-1",href='/apps/graphs_info_layout'),
        dbc.Button("Diabetes test", id='prediction',color="success", className="mr-1",
                   href='/apps/diabetes_prediction_layout'),
        html.P(""),
        html.P(['For more information check ',html.A('WHO',href='https://www.who.int/news-room/fact-sheets/detail/diabetes'),
                ' and ',
                html.A('CDC',href='https://www.cdc.gov/chronicdisease/resources/publications/factsheets/diabetes-prediabetes.htm')]),

        html.P(['Source:  World Health Organization (WHO) and Center of Disease Control and prevention (CDC)']),
      ]),
    ],color="warning",outline=True)
],style= page_layout)

layout2 = html.Div(id='redirection',children=[])

home_callback(app)

