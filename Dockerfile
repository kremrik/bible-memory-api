FROM python:3.9-slim

# todo: create working dir
WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT uvicorn api.config.asgi:api --host 0.0.0.0 --port 8000 --reload
