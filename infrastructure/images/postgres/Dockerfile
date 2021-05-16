FROM postgres:13.3

ARG postgres_user
ARG postgres_password
ARG postgres_db

ENV POSTGRES_USER="$postgres_user"
ENV POSTGRES_PASSWORD="$postgres_password"
ENV POSTGRES_DB="$postgres_db"

COPY ./docker-entrypoint-initdb.d /docker-entrypoint-initdb.d
