from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

from .config.app import Config

app = Flask(__name__, template_folder='resources/views', static_folder='resources/static')
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)

from .pumpstation.pumps.controllers import pumps
from .pumpstation.main.controllers import main
from .pumpstation.auth.controllers import auth

"""
    [BUG] blueprint template_folder: https://stackoverflow.com/questions/7974771/flask-blueprint-template-folder
"""

app.register_blueprint(pumps)
app.register_blueprint(main)
app.register_blueprint(auth)

# app.url_map