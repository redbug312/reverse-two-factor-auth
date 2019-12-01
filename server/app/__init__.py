import os
from flask import Flask

from .models import db
from .views.api import users

app = Flask(__name__, template_folder='templates')
app.register_blueprint(users)
app.config.from_object('config')

# https://stackoverflow.com/a/19438054
db.init_app(app)
with app.app_context():
    db.create_all()
