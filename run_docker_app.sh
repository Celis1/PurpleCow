#!/bin/bash
echo "--Started creating a docker image from the flask app--"
docker build -t flask_app .

echo "Running webserver on http://localhost:3000/"
docker run -d -p 3000:5000 flask_app