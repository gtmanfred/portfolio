import uuid

from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from .templating import templates
from .characters import CharacterGenerator


def _register_bastards(app):
    app.mount('/static', StaticFiles(directory='app/static', html=True))
    app.get('/bastards/', response_class=HTMLResponse)(bastards_page_new)
    app.get('/bastards/{character_id}', response_class=HTMLResponse)(bastards_page)


def bastards_page_new(request: Request, commoner: bool = False, extra_classes: bool = False):
    character_id = uuid.uuid4()
    data = templates.TemplateResponse('bastards.html', {
        'c': CharacterGenerator.create(seed=character_id, commoner=commoner, extra_classes=extra_classes).dict(),
        'character_id': character_id,
        'create': True,
        'request': request,
    })
    return data


def bastards_page(request: Request, character_id: uuid.UUID, commoner: bool = False, extra_classes: bool = False):
    data = templates.TemplateResponse('bastards.html', {
        'c': CharacterGenerator.create(seed=character_id, commoner=commoner, extra_classes=extra_classes).dict(),
        'character_id': character_id,
        'create': False,
        'request': request,
    })
    return data
