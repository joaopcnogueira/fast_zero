import os
from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fast_zero.schemas import Message

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}


@app.get('/exercicio-html', response_class=HTMLResponse)
def read_root_html():
    return """
    <html>
        <head>
            <title> Nosso olá mundo! </title>
        </head>
        <body>
            <h1> Olá Mundo! </h1>
        </body>
    </html>"""


@app.get('/exercicio-html2', response_class=HTMLResponse)
def read_root_html2():
    template_path = os.path.join('templates', 'exercicio-aula2.html')
    with open(template_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    return HTMLResponse(content=html_content)
