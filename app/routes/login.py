from fastapi import APIRouter

login_router = APIRouter(prefix='/login', tags=['login'])

@login_router.get('/')
def loginHome():
    return {
        'message': 'login home'
    }