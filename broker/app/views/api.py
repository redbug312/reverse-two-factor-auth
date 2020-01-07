from flask import Blueprint, abort, request, jsonify

from ..models import Auth, db


auths = Blueprint('auths', __name__)


@auths.route('/api/auths', methods=['POST'])
def new_auth():
    code = request.json.get('code')
    phone = request.json.get('phone')
    if code is None or phone is None:
        abort(401)  # missing arguments
    auth = Auth(code=code, phone=phone)
    db.session.add(auth)
    db.session.commit()
    return (jsonify({'code': auth.code, 'phone': auth.phone}), 201)


@auths.route('/api/auths/<string:code>')
def get_auths(code):
    query = Auth.query.filter_by(code=code).order_by(Auth.created_time.desc())
    auths = [{'badges': auth.get_badges(),
              'digits': auth.phone[-3:],
              'expired': auth.expired_after()}
             for auth in query.all() if not auth.is_expired()]
    return jsonify({'auths': auths})
