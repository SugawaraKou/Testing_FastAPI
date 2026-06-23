#!/bin/bash

git pull

docker kill test_fastapi
docker rm test_fastapi
docker rmi test_fastapi_img

docker build -t test_fastapi_img .
docker run -d -p 8080:9999 --name test_fastapi test_fastapi_img