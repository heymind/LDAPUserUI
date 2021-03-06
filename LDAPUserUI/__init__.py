import datetime
from flask import Flask
import sys,os

sys.path.append(os.path.dirname(__file__))

from config import ConfigClass
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config.from_object(ConfigClass)


with app.app_context():
    from my_user_manager import MyUserManager
    from models import User
    user_manager = MyUserManager(app,SQLAlchemy(),User)

    import routes
