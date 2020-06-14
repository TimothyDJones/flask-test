# app/__init__.py

from flask import Flask

# Application initialization
app = Flask(__name__, instance_relative_config = True)

# Load the views
from app import views

# Load configuration
app.config.from_object('config')
