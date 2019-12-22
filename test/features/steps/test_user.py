import pytest
import threading
import requests
from wsgiref.simple_server import make_server
from pytest_bdd import scenarios, given, when, then, parsers

from server.app import app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.sqlite'


scenarios('../user.feature')


@pytest.fixture
def fixture():
    class Context():
        pass
    context = Context()
    context.server = make_server('0.0.0.0', 5000, app)
    context.thread = threading.Thread(target=context.server.serve_forever)
    context.thread.start()
    yield context
    context.server.shutdown()
    context.thread.join()


@given(parsers.parse('I am the user {username}'))
def get_user(fixture, username):
    fixture.user = username


@given(parsers.parse('I have signed up with password {password}'))
def sign_up(fixture, password):
    url = 'http://%s:%d' % fixture.server.server_address + '/api/users'
    json = {'username': fixture.user, 'password': password}
    requests.post(url, json=json)
    fixture.auth = (fixture.user, password)


@when('I want to retreive my resource')
def retrieve_resource(fixture):
    url = 'http://%s:%d' % fixture.server.server_address + '/api/resource'
    fixture.response = requests.get(url, auth=fixture.auth)


@then('I should see success message')
def see_success_message(fixture):
    assert fixture.response.status_code < 400
