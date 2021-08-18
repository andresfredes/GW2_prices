from flask import Flask
from flask_bootstrap import Bootstrap
import config

bootstrap = Bootstrap()

def create_app():
    app = Flask(__name__)
    load_config(app)
    bootstrap.init_app(app)
    return app

def load_config(app):
    if app.config["ENV"] == "production":
        app.config.from_object(config.ProductionConfig)
    elif app.config["ENV"] == "testing":
        app.config.from_object(config.TestingConfig)
    else:
        app.config.from_object(config.DevelopmentConfig)

app = create_app()

from prices import views