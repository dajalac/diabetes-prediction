import dash
from dash.dependencies import Input, Output
import time
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from datasets.data import get_accuracy, get_model
import dash_html_components as html


def diabetes_test_callback(app):
    # callback for the buttons
    @app.callback(
        Output(component_id='tabs', component_property='active_tab'),
        [Input(component_id='next1', component_property='n_clicks'),
         Input(component_id='next_2', component_property='n_clicks'),
         Input(component_id='previous_2', component_property='n_clicks'),
         Input(component_id='previous3', component_property='n_clicks')])
    def update_tab(next1, next_2, previous_2, previous3):
        ctx = dash.callback_context
        pressed_btn = ctx.triggered[0]['prop_id'].split('.')[0]
        print(pressed_btn)

        if pressed_btn == 'next1':
            return "tab_2"
        if pressed_btn == 'next_2':
            print("next_tab2")
            return "tab_3"
        if pressed_btn == 'previous_2':
            print("p_tab2")
            return "tab_1"
        if pressed_btn == 'previous3':
            return "tab_2"
        else:
            return "tab_1"

    @app.callback(
        Output('test_result', 'children'),
        [Input('submit', 'n_clicks'), Input('age', 'value'),
         Input('urination', 'value'),
         Input('thirsty', 'value'), Input('weight_loss', 'value'),
         Input('weakness', 'value'), Input('eating', 'value'),
         Input('genital_thrush', 'value'), Input('visual_blurring', 'value'),
         Input('itching', 'value'), Input('irritability', 'value'),
         Input('delayed_healing', 'value'), Input('partial_paresis', 'value'),
         Input('muscle_stiffness', 'value'), Input('alopecia', 'value'),
         Input('obese', 'value'), ]
    )
    def show_test_result(clicks, age, urination, thirsty, weight_loss, weakness, eating,
                         genital_thrush, visual_blurring, itching, irritability, delayed_healing,
                         partial_paresis, muscle_stiffness, alopecia, obese):

        if clicks:
            start_time = time.time()
            attributes = [{'polyuria': urination, 'polydipsia': thirsty, 'sudden weight loss': weight_loss,
                           'weakness': weakness, 'polyphagia': eating, 'genital thrush': genital_thrush,
                           'visual blurring': visual_blurring, 'itching': itching, 'irritability': irritability,
                           'delayed healing': delayed_healing, 'partial paresis': partial_paresis,
                           'muscle stiffness': muscle_stiffness, 'alopecia': alopecia, 'obese': obese, 'c_age': age}]

            # trasforn dictionary into table
            user_input = pd.DataFrame.from_dict(attributes)

            # get accuracy
            accuracy = "The prediction model has a {}% of accuracy".format(round(get_accuracy() * 100, 2))

            # make prediction
            model = get_model()
            try:
                prediction = model.predict(user_input)
                prob = model.predict_proba(user_input)
                test_result = " "
                if prediction == [1]:
                    test_result = "According to our model you may have diabetes" \
                                  " ({}% probability)." \
                                  " Please schedule an  appointment with your doctor" \
                                  " for a better evaluation and instruction.".format(round(prob[0][1] * 100, 2))
                elif prediction == [0]:
                    test_result = "You probably don't have diabetes. " \
                                  "Keep up a good diet and regular physical activity."

                seconds = "Model calculated in -- %s seconds --" % round((time.time() - start_time), 2)

                return [html.H6(test_result),html.Br(),
                        html.P(accuracy, style={'color':'grey','font-size':'12px','margin':'0'}),
                        html.P(seconds,style={'color':'grey','font-size':'12px'})]
            except:
                error = html.H6("Please answer all the questions before hit submit", style= {'color':'red'})
                return error

