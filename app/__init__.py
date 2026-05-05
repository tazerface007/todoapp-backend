from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from .routes import router
from app.middlewares.middleware import MyCustomMiddleware


async def custom_404_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=404,
        content={'error':'Not found'}
    )

def create_app()->FastAPI:
    app = FastAPI()
    app.include_router(router=router)
    app.add_middleware(MyCustomMiddleware)
    app.add_exception_handler(404,custom_404_handler)
    return app