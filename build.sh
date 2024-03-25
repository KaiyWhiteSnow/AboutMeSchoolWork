#!/bin/bash

docker compose down

cp .env src/.env
docker compose up --build