from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}


def test_livros_deve_retornar_ok_e_lista_de_livros():
    client = TestClient(app)

    response = client.get('/livros')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == [
        {
            'titulo': '1984',
            'autor': 'George Orwell',
            'ano': 1949,
            'disponivel': True,
        },
        {
            'titulo': 'O Senhor dos Anéis',
            'autor': 'J.R.R. Tolkien',
            'ano': 1954,
            'disponivel': False,
        },
        {
            'titulo': 'Dom Casmurro',
            'autor': 'Machado de Assis',
            'ano': 1899,
            'disponivel': True,
        },
    ]


def test_ola_mundo():
    client = TestClient(app)

    response = client.get('/ola')

    assert response.status_code == HTTPStatus.OK
    assert 'Olá Mundo!' in response.text
