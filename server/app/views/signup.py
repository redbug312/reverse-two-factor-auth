from flask import Blueprint, abort, request, jsonify, render_template

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
        abort(400)    # missing arguments
    if User.query.filter_by(username=username).first() is not None:
        abort(400)    # existing user
    user = User(username=username)
    user.hash_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({'success': True}), 201
