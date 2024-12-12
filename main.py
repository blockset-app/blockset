from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from settings import main_settings


def get_application():
    _app = FastAPI(title=main_settings.PROJECT_NAME)

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        expose_headers=["X-query-size"],
    )

    return _app


app = get_application()
