from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()

def create_app(test_config=None):
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    if not test_config:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('RENDER_DATABASE')
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('TEST_DATABASE')
    
    #import models here
    from app.models.planet import Planet
    
    db.init_app(app)
    migrate.init_app(app, db)

    #add our planets blueprint
    from flask import Blueprint
    from .routes import planets_bp

    app.register_blueprint(planets_bp)
    
    return app