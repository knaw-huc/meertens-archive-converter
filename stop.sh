#!/bin/bash

# docker kill $(docker ps -q)
docker kill phpmyadmin
docker kill web
docker kill db
docker container prune -f
docker ps -a
