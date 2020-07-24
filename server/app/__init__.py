from flask import Flask, render_template, request, make_response, redirect, url_for, current_app
from flask_migrate import Migrate
from werkzeug.exceptions import HTTPException
from datetime import datetime, date, time
import random

from .models import User, db
from .views.api import users
from .views.signin import signin
from .views.signup import signup

app = Flask(__name__, template_folder='templates')
app.jinja_env.add_extension('pypugjs.ext.jinja.PyPugJSExtension')
app.register_blueprint(users)
app.register_blueprint(signin)
app.register_blueprint(signup)
app.config.from_pyfile('instance/default.py')
app.config.from_pyfile('instance/development.py', silent=True)

migrate = Migrate(app, db)


@app.route('/')
def index():
    quotes = current_app.config['QUOTES']
    token = request.cookies.get('token')
    if token is None or User.verify_auth_token(token) is None:
        return render_template('welcome.pug', title='Welcome')
    today = datetime.combine(date.today(), time.min)
    random.seed(today.timestamp())
    quote = random.choice(quotes)
    return render_template('home.pug', title='Home', quote=quote)


@app.route('/logout')
def logout():
    res = make_response(redirect(url_for('index'), code=302))
    res.set_cookie('token', '')
    return res


@app.errorhandler(HTTPException)
def handle_exception(error):
    title = 'Error %d' % error.code
    return render_template('error.pug', title=title, error=error), error.code


@app.before_first_request
def init():
    db.init_app(app)
    with app.app_context():
        db.create_all()
