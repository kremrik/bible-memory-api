#!/usr/bin/env bash


docker build \
    -t bible-memory-db \
    --build-arg postgres_user="$POSTGRES_USER" \
    --build-arg postgres_password="$POSTGRES_PASSWORD" \
    --build-arg postgres_db="$POSTGRES_DB" \
    .
