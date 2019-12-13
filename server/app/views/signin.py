from flask import Blueprint, abort, request, jsonify, render_template

from ..models import auth


signin = Blueprint('signin', __name__)


@signin.route('/signin')
def index():
    return render_template('signin.html')


@signin.route('/signin/redirect', methods=['POST'])
def result():
    username = request.form.get('username')
    password = request.form.get('password')
    if username is None or password is None:
        abort(400)    # missing arguments
    if not auth.verify_password_callback(username, password):
        abort(400)    # failed authen
    return jsonify({'success': True}), 201
