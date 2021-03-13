# Fetch Rewards: Text Similarity

> A Django web application to find similarity between different text samples.
> This application is containerized and uploaded to DockerHub.

## Table of contents

* General Info
* Instructions To Run
* Application Screenshots
* Technologies
* Algorithms

## General Info

The web application implements different algorithms to find the similarity score between text samples. The algorithms
implemented use the built-in data structures and do not rely on any external library. User can select the algorithms of
their choice from the menu and find out how different techniques score the text.

## Instructions To Run

1. Setup [docker engine/desktop](https://docs.docker.com/engine/) on your local system.
2. Run the following docker commands:
    1. `docker pull yashchitre03/text-similarity`
    2. `docker run -p 8000:8000 yashchitre03/text-similarity`
3. Open your local browser and visit port 8000 on your localhost (or whichever port you chose when running the command).

The command 2.i pulls the docker image from DockerHub, while the command 2.ii creates a container based on that
image, binds the port from host system to container, and runs the container. The host port can be anything, 
but the container port should be 8000 (as this port is exposed in the Dockerfile).

## Application Screenshots

## Technologies

* Python 3 programming language
* Django 3 web framework
* Bulma CSS framework
* Docker Engine

## Algorithms

* Jaccard Index
* Cosine Similarity
* Dice's Coefficient
* Overlap Coefficient