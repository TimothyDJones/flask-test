# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

from config import app_config

# Database initialization
db = SQLAlchemy()

login_manager = LoginManager()

# Application initialization
def create_app(config_name):
	app = Flask(__name__, instance_relative_config = True)
	# Load configuration
	app.config.from_object(app_config[config_name])
	app.config.from_pyfile('config.py')
	db.init_app(app)

	login_manager.init_app(app)
	login_manager.login_message = "Please log in to access this page."
	login_manager.login_view = "auth.login"

	migrate = Migrate(app, db)

	from app import models

	# Temporary route
	@app.route("/")
	def hello_world():
		return "Hello, world!"

	return app


# Load the views
# from app import views


