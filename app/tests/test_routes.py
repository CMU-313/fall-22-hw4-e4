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

def test_predict_study_route():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = "/predict_on_study"
    query_1 = {"G1":"18","G2":"9","failures":"4"}
    query_2 = {"F1":"3","G2":"17","failures":"2"}
    query_3 = {"G1":"3333","G2":"9","failures":"5"}

    response = client.get(url, query_string = query_1)
    assert response.status_code == 200

    response = client.get(url, query_string = "")
    assert response.status_code == 500

    response = client.get(url, query_string = query_2)
    assert response.status_code == 500

    response = client.get(url, query_string = query_3)
    assert response.status_code == 400
