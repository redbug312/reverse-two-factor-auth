from flask import Blueprint, request, render_template, redirect, url_for, flash

from ..models import User, db


signup = Blueprint('signup', __name__)


@signup.route('/signup')
def index():
    return render_template('signup.pug', title='Sign Up')


@signup.route('/signup/redirect', methods=['POST'])
def result():
    # TODO merge into api.new_user
    username = request.form.get('username')
    password = request.form.get('password')
    if username is None or password is None:
        flash('You\'ve forgotten the username or password.')
        return redirect(url_for('signup.index'))
    if User.query.filter_by(username=username).first() is not None:
        flash('This username has been signed-up.')
        return redirect(url_for('signup.index'))
    user = User(username=username)
    user.hash_password(password)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('signin.index'), code=302)
