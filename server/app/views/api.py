from flask import Blueprint, abort, request, jsonify, g, url_for, render_template
from flask_httpauth import HTTPBasicAuth

from ..models import User, db


auth = HTTPBasicAuth()
users = Blueprint('users', __name__, template_folder='templates')


@auth.verify_password
def verify_password(username_or_token, password):
    # first try to authenticate by token
    user = User.verify_auth_token(username_or_token)
    if not user:
        # try to authenticate with username/password
        user = User.query.filter_by(username=username_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True


@users.route('/api/users', methods=['POST'])
def new_user():
    if request.content_type == 'application/json':
        username = request.json.get('username')
        password = request.json.get('password')
    elif request.content_type == 'application/x-www-form-urlencoded':
        username = request.form.get('username')
        password = request.form.get('password')
    else:
        abort(400)    # invalid content type
    if username is None or password is None:
        abort(400)    # missing arguments
    if User.query.filter_by(username=username).first() is not None:
        abort(400)    # existing user
    user = User(username=username)
    user.hash_password(password)
    db.session.add(user)
    db.session.commit()
    return (jsonify({'username': user.username}), 201,
            {'Location': url_for('users.get_user', id=user.id, _external=True)})


@users.route('/api/users/<int:id>')
def get_user(id):
    user = User.query.get(id)
    if not user:
        abort(400)
    return jsonify({'username': user.username})


@users.route('/api/token')
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token(600)
    return jsonify({'token': token.decode('ascii'), 'duration': 600})


@users.route('/api/resource')
@auth.login_required
def get_resource():
    return jsonify({'data': 'Hello, %s!' % g.user.username})


@users.route('/login')
def login():
    return render_template('login.html')
