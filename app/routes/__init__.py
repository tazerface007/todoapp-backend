from fastapi import APIRouter
from app.routes.todo import todorouter
from app.routes.login import login_router

router = APIRouter(tags=['home'])

router.include_router(todorouter)
router.include_router(login_router)


@router.get('/')
def home():
    return {
        'message': 'Welcome to home'
    }

