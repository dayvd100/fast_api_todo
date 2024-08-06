from http import HTTPStatus

from fastapi import FastAPI

from routers import auth, todo, users
from schemas.schemas import Message

app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(todo.router)


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'This is the home'}
