from datetime import datetime, timedelta
from flask_sqlalchemy import SQLAlchemy
from humanize import naturaldelta
from passlib.hash import hex_sha1

from .utils import random_icon


db = SQLAlchemy()


class Auth(db.Model):
    __table__name__ = 'auths'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(8), index=True)
    phone = db.Column(db.String(10))
    created_time = db.Column(db.DateTime, default=datetime.utcnow)

    def is_expired(self, duration=600):
        expired_time = self.created_time + timedelta(seconds=duration)
        return expired_time < datetime.utcnow()

    def expired_after(self, duration=600, humanize=True):
        expired_time = self.created_time + timedelta(seconds=duration)
        expired_delta = expired_time - datetime.utcnow()
        return 'expired' if expired_delta < timedelta() \
               else naturaldelta(expired_delta) if humanize \
               else str(expired_delta)

    def icons_token(self):
        seeds = [int(hex_sha1.hash(self.phone + str(n)), 16)
                 for n in range(3)]
        return [random_icon(seed) for seed in seeds]
