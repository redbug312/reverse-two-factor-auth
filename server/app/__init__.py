from flask import Flask, render_template, request, make_response, redirect, url_for
from werkzeug.exceptions import HTTPException

from .models import User, db
from .views.api import users
from .views.signin import signin
from .views.signup import signup

app = Flask(__name__, template_folder='templates')
app.jinja_env.add_extension('pypugjs.ext.jinja.PyPugJSExtension')
app.register_blueprint(users)
app.register_blueprint(signin)
app.register_blueprint(signup)
app.config.from_pyfile('config.py')


@app.route('/')
def index():
    token = request.cookies.get('token')
    if token is None or User.verify_auth_token(token) is None:
        return render_template('welcome.pug', title='Welcome')
    return render_template('home.pug', title='Home')


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
