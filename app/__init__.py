from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_mail import Mail
from .config import Config



app = Flask(__name__)



app.config.from_object(Config)

csrf = CSRFProtect(app)
mail = Mail(app)

from . import views
