from fastapi.staticfiles import StaticFiles

from ..utils.spa import SinglePageApp


def _register_bastards(app):
    app.mount('/bastards/', app=SinglePageApp(directory='app/bastards/static', html=True))
