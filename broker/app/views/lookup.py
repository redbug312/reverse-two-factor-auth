from flask import Blueprint, request, render_template, redirect, url_for

from ..models import Auth


lookup = Blueprint('lookup', __name__)


@lookup.route('/lookup')
def index():
    code = request.args.get('code')
    if code is None:
        return redirect(url_for('index'))
    return redirect(url_for('lookup.result', code=code))


@lookup.route('/lookup/<string:code>')
def result(code):
    query = Auth.query.filter_by(code=code).order_by(Auth.created_time.desc())
    auths = [{'user': auth.icons_token(), 'expired': auth.expired_after()}
             for auth in query.all()  # if not auth.is_expired()]
             ]
    return render_template('lookup.pug', title=code, auths=auths)
