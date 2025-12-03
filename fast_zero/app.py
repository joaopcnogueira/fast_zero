from http import HTTPStatus

from fastapi import FastAPI

from fast_zero.schemas import Livro, Message

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}


@app.get('/livros', status_code=HTTPStatus.OK, response_model=list[Livro])
def read_livros():
    livros = [
        Livro(titulo='1984', autor='George Orwell', ano=1949, disponivel=True),
        Livro(
            titulo='O Senhor dos Anéis',
            autor='J.R.R. Tolkien',
            ano=1954,
            disponivel=False,
        ),
        Livro(
            titulo='Dom Casmurro',
            autor='Machado de Assis',
            ano=1899,
            disponivel=True,
        ),
    ]
    return livros


@app.get('/ola', status_code=HTTPStatus.OK)
def ola_mundo():
    return 'Olá Mundo!'
