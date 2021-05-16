#!/bin/bash
set -e


psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE USER bible_memory;
    GRANT ALL PRIVILEGES ON DATABASE bible_memory TO bible_memory;
EOSQL
