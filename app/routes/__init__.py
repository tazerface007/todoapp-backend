from fastapi import APIRouter
from app.routes.todo import todorouter

router = APIRouter(tags=['home'])

router.include_router(todorouter)


@router.get('/')
def home():
    return {
        'message': 'Welcome to home'
    }

