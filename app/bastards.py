import uuid

from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles


def _register_bastards(app):
    app.mount('/static', StaticFiles(directory='app/static', html=True))
    app.get('/bastards/', response_class=HTMLResponse)(bastards_page)
    app.get('/bastards/{character_id}', response_class=HTMLResponse)(bastards_page)


def bastards_page():
    return FileResponse('app/html/bastards.html')
