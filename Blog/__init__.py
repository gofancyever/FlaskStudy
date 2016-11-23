from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import config
from flask_migrate import Migrate
from flask_script import Manager

app = Flask(__name__)
app.config.from_object(config)

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)

from Blog import views

