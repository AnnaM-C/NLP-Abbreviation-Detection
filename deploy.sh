#!/bin/bash
set -e

git pull origin main
docker-compose down
docker compose up --build