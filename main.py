from app import create_app
from uvicorn import run


if __name__ == '__main__':
    run("main:create_app", reload=True, factory=True)
    