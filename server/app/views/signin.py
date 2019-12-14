from flask import Blueprint, request, render_template, redirect, url_for, make_response, g, flash

from ..models import auth


signin = Blueprint('signin', __name__)


@signin.route('/signin')
def index():
    return render_template('signin.pug', title='Login')


@signin.route('/signin/redirect', methods=['POST'])
def result():
    username = request.form.get('username')
    password = request.form.get('password')
    if username is None or password is None:
        flash('You\'ve forgotten the username or password.')
        return redirect(url_for('signin.index'))
    if not auth.verify_password_callback(username, password):
        flash('You\'ve mistyped the username or password.')
        return redirect(url_for('signin.index'))
    res = make_response(redirect(url_for('index'), code=302))
    res.set_cookie('token', g.user.generate_auth_token())
    return res
