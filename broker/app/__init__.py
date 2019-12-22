from flask import Flask, render_template
from werkzeug.exceptions import HTTPException

from .models import db
from .views.api import auths
from .views.lookup import lookup

app = Flask(__name__, template_folder='templates')
app.jinja_env.add_extension('pypugjs.ext.jinja.PyPugJSExtension')
app.register_blueprint(auths)
app.register_blueprint(lookup)
app.config.from_pyfile('config.py')


@app.route('/')
def index():
    return render_template('welcome.pug', title='Welcome')


@app.errorhandler(HTTPException)
def handle_exception(error):
    title = 'Error %d' % error.code
    return render_template('error.pug', title=title, error=error), error.code


@app.before_first_request
def init():
    db.init_app(app)
    with app.app_context():
        db.create_all()
