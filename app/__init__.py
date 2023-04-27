from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


def create_app(test_config=None):
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    #connects SQL to our Database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/hello_books_development'
    #add our planets blueprint
    from flask import Blueprint
    from .routes import planets_bp

    app.register_blueprint(planets_bp)
    
    return app