from flask import Flask

from app.handlers.routes import configure_routes

def test_base_route():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/'

    response = client.get(url)

    assert response.status_code == 200
    assert response.get_data() == b'try the predict route it is great!'

def test_correctAcceptance():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predit&studyTime?=4&failures?=1&internet=true'

    response = client.get(url)

    assert response.status_code == 200
    assert response.get_data() == {true}

def test_correctDenial():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predit&studyTime?=0&failures?=8&internet=false'

    response = client.get(url)

    assert response.status_code == 200
    assert response.get_data() == {false}