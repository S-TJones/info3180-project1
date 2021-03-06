
from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
# app.debug = True
# app.config['SECRET_KEY'] = 'Som3$ec5etK*y'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'driver://username:password@server/db'
# postgresql-animate-60902

db = SQLAlchemy(app)

app.config.from_object(Config)
from app import views, models