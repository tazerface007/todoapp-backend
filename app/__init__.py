from fastapi import FastAPI, Request
from fastapi.middleware.cors  import CORSMiddleware
from fastapi.responses import JSONResponse
from .routes import router
from app.middlewares.middleware import MyCustomMiddleware
from app.middlewares._hp_middleware import HighPerformanceMiddleware
from app.database import Base, engine
from app.database.models.todo import Todo

async def custom_404_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=404,
        content={'error':'Not found'}
    )

def create_app()->FastAPI:
    app = FastAPI(root_path='/api')
    app.include_router(router=router)
    app.add_middleware(HighPerformanceMiddleware, 
        exclude_paths={"/login", "/login/", "/.well-known/appspecific/com.chrome.devtools.json"}                   
    )
    app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
    Base.metadata.create_all(bind=engine)
    # app.add_middleware(MyCustomMiddleware)
    app.add_exception_handler(404,custom_404_handler)
    return app