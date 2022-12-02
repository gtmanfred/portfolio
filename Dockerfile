FROM python:3.10

WORKDIR /srv
ENV PORT=8000

ADD files/run-server.sh /usr/local/bin/run-server
CMD ["run-server"]

ADD poetry.lock ./
ADD pyproject.toml ./
ADD asgi.py ./
COPY app ./app

RUN python3 -m pip install .
