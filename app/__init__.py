from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
jwt = JWTManager(app)

from app import routes, models
