#!/usr/bin/env bash
podman pod create --name postgresql -p 5434:5432
podman run --name db --pod=postgresql --detach \
-e LC_ALL=C.UTF-8 \
-e POSTGRES_DB=database_name \
-e POSTGRES_USER=postgresql_username \
-e POSTGRES_PASSWORD=postgresql_password \
--mount "type=bind,source=./.pgdata,destination=/var/lib/postgresql/data,relabel=shared" \
postgres:latest
