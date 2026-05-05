from fastapi import APIRouter

todorouter = APIRouter(tags=['todo'])

@todorouter.get('/api/todo/')
def todohome():
    return {
        'message': 'To Do Home'
    }