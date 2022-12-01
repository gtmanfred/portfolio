import json
import os
from typing import Optional
from urllib.request import Request
from urllib.request import urlopen
from uuid import UUID

import bugsnag
from bugsnag.asgi import BugsnagMiddleware
from fastapi import FastAPI

from .config import Config
from .utils.plugin import find_modules
from .utils.plugin import import_string


def _register_handlers(app: FastAPI, location: str) -> None:
    for module in find_modules(location, recursive=True):
        version = module.rsplit('.', 2)[-2]
        router = import_string(import_name=f'{module}:router', silent=True)
        if router is not None:
            app.include_router(router, prefix=f'/api/{version}')


def _register_bugsnag(app: FastAPI) -> FastAPI:
    bugsnag.configure(
        api_key = Config.BUGSNAG_API_KEY,
        project_root = os.getcwd(),
    )

    # Wrap your ASGI app with Bugsnag
    return BugsnagMiddleware(app)


def create_app():
    app = FastAPI()

    _register_handlers(app, 'app.handlers')
    app = _register_bugsnag(app)

    return app
