#!/bin/bash

#this is the command for creating the docker image with the requirments
echo "--Started creating a docker image from the flask app--"
docker build -t flask_app . #this only needs to be run if the docker image is not already created

#this is the command for running the docker image on the port 3000
echo "Running webserver on http://localhost:3000/"
docker run -d -p 3000:5000 flask_app 

#docker stop <container_id>  # this will stop the container thats running