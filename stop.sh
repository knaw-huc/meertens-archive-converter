#!/bin/bash

# docker kill $(docker ps -q)
docker-compose down
docker ps -a
