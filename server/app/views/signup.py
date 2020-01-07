from flask import Blueprint, request, render_template, redirect, url_for, flash, current_app
from random import randint

from ..models import User, db


signup = Blueprint('signup', __name__)


@signup.route('/signup')
def index():
    code = 831194  # randint(100000, 999999)
    brokers = current_app.config['BROKERS']
    recaptcha = current_app.config['RECAPTCHA_SITEKEY']
    return render_template('signup.pug', title='Sign Up', code=code,
                           brokers=brokers, recaptcha=recaptcha)


@signup.route('/signup/redirect', methods=['POST'])
def result():
    username = request.form.get('username')
    password = request.form.get('password')
    badges = request.form.get('badges')
    if username is None or password is None:
        flash('You\'ve forgotten the username, password.', 'error')
        return redirect(url_for('signup.index'))
    if User.query.filter_by(username=username).first() is not None:
        flash('This username has been signed-up.', 'error')
        return redirect(url_for('signup.index'))
    user = User(username=username, badges=badges)
    user.hash_password(password)
    db.session.add(user)
    db.session.commit()
    flash('You\'ve successfully registered! Welcome!', 'success')
    return redirect(url_for('signin.index'))
