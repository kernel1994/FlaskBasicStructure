from flask import Flask
from .api import api
from .admin import admin
from .home import home
from .main import main
# from flask.ext.mail import Mail
# from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug.utils import import_string
 
# mail = Mail()
# db = SQLAlchemy()

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
 
    # Load extensions
    # mail.init_app(app)
    # db.init_app(app)
 
    # Load blueprints
    app.register_blueprint(main)
    app.register_blueprint(api, url_prefix='/api')
    app.register_blueprint(admin, url_prefix='/admin')
    app.register_blueprint(home, url_prefix='/home')
 
    return app