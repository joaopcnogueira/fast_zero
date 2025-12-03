from pydantic import BaseModel


class Message(BaseModel):
    message: str


class Livro(BaseModel):
    titulo: str
    autor: str
    ano: int
    disponivel: bool
