from flask import Blueprint, abort, request, jsonify, g, url_for

from ..models import User, db, auth


users = Blueprint('users', __name__)


@users.route('/api/users', methods=['POST'])
def new_user():
    username = request.json.get('username')
    password = request.json.get('password')
    if username is None or password is None:
        abort(401)    # missing arguments
    if User.query.filter_by(username=username).first() is not None:
        abort(401)    # existing user
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
        abort(401)
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
