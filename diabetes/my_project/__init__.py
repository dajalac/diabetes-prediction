from flask import Flask
from config import Config
import dash


#def create_app():
    # server = Flask(__name__)
    # server.config.from_object(Config)
    # register_blueprints(server)
    # register_dash_app(server)
    # server.run(debug=True)
    #return server


def register_blueprints(server):
    from my_project.router import server_bp
    server.register_blueprint(server_bp)

def register_dash_app(app):
    from my_project.home_dash.layout import layout
    from my_project.home_dash.callbacks import register_callbacks
    dash_app = dash.Dash(__name__,
                         server=app,
                         url_base_pathname='/home/')
    with app.app_context():
        #dash_app.title = 'Dashapp 1'
        dash_app.layout = layout
        register_callbacks(dash_app)

#to rum
server = Flask(__name__)
server.config.from_object(Config)
register_blueprints(server)
register_dash_app(server)
server.run(debug=True)

