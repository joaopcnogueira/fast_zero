import os
from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app

client = TestClient(app)


def test_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}


def test_exercicio_ola_mundo_em_html():
    client = TestClient(app)

    response = client.get('/exercicio-html')

    assert response.status_code == HTTPStatus.OK
    assert '<h1> Olá Mundo! </h1>' in response.text


def test_read_root_html2():
    response = client.get('/exercicio-html2')
    assert response.status_code == HTTPStatus.OK
    assert response.headers['content-type'] == 'text/html; charset=utf-8'

    template_path = os.path.join('templates', 'exercicio-aula2.html')
    with open(template_path, 'r', encoding='utf-8') as file:
        expected_content = file.read()

    assert response.text == expected_content
