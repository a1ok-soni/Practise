from fastapi import FastAPI

from practise.api.routes import router as api_router


def create_app():
    app = FastAPI()
    app.include_router(api_router)
    return app
