FROM python:3.9-slim

# todo: create working dir
WORKDIR /app

ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT uvicorn \
    api.config.asgi:api \
    --host 0.0.0.0 \
    --port 8000 \
    --log-level info \
    --reload
