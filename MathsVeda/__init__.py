from flask import Flask





def create_app():

    app = Flask(__name__)

    from .main import main as main_blueprint
    from .handle_exceptions import handle_exceptions as h_e_blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(h_e_blueprint)

    return app
