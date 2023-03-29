#!/bin/bash

# Build the Docker image
docker build -t $1 ./

# Start the Docker container
docker run --env-file='.env' -p 8000:8000 $1
