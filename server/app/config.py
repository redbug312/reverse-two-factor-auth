SECRET_KEY = 'the quick brown fox jumps over the lazy dog'

SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_TRACK_MODIFICATIONS = True

BROKERS = [
    {'phone': '0900000000', 'name': 'Foo', 'url': 'http://localhost:5001/'},
    {'phone': '0900000001', 'name': 'Bar', 'url': 'http://localhost:5002/'},
]
