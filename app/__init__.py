from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
manager = Manager(app)

from app import views,models