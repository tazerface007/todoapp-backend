from fastapi import APIRouter

todorouter = APIRouter(prefix='/api', tags=['todo'])

@todorouter.get('/todo')
def todohome():
    return {
        'message': 'To Do Home'
    }


@todorouter.get('/whattodo')
def whattodo():
    from app.database import SessionLocal
    from app.database.models.todo import Todo

    session = SessionLocal()

    response =session.query(Todo).all()


    for r in response:
        print(f'response: {r} ')

    return {
        'message': 'What to do?'
    }