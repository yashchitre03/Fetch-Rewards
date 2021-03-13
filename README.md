# Fetch Rewards: Text Similarity

> A Django web application to find similarity between different text samples.
> This application is containerized and uploaded to DockerHub.

## Table Of Contents

* [General Info](#general-info)
* [Instructions To Run](#instructions-to-run)
* [Project Structure](#project-structure)
* [Application Screenshots](#application-screenshots)
* [Technologies](#technologies)
* [Algorithms](#algorithms)

## General Info

The web application implements different algorithms to find the similarity score between text samples. The algorithms
implemented use the built-in data structures and do not rely on any external library. User can select the algorithms of
their choice from the menu and find out how different techniques score the text.

Before applying the algorithms, some pre-processing is performed on the data samples. The text is converted to lower
case as case should not affect the meaning of the text. Then all punctuations are removed from the text. Suppose a text
is 'hey ! ! !', then after tokenization (converting sentence to list of words), the three exclamation marks would be
considered as three separate tokens. But, they do not add any meaning to the text. Finally, any non-alphabetical data
(like numbers) is removed from the text.

This text is internally represented as a vector of numbers for ease in mathematical calculations in various algorithms.

## Instructions To Run

1. Setup [docker engine/desktop](https://docs.docker.com/engine/) on your local system.
2. To run, execute the command: `docker run -d -p 8000:8000 yashchitre03/text-similarity`
3. Open your local browser and visit  `localhost:8000` to interact with the front-end.
4. To stop, execute the command: `docker container stop [container-id]`

The command 2 pulls the docker image from DockerHub, creates a container based on that image,
binds the port from host system to container, and runs the container in a detached mode. The host port can be anything,
but the container port should be `8000` (as this port is exposed in the Dockerfile).

## Project Structure

The project consists of the following files and directories:

1. Directories
    * Fetch_Rewards - Contains the config and settings files for the Django web application.
    * similarity - An app that defines views, forms, and algorithms for the text similarity task.
    * templates - Contains HTML files.
    * README_images - Image data for the README.md file.
2. Files
    * README.md - Project documentation.
    * .gitignore - Build and IDE files to ignore in git repository.
    * requirements.txt - Python packages required for the project.
    * manage.py - Django task for running project related commands.
    * Dockerfile - Script for project containerization.

## Application Screenshots

* Main page (top)
  ![Main page (top)](https://github.com/yashchitre03/Fetch-Rewards/blob/main/README_images/main-1.png)

* Main page (bottom)
  ![Main page (bottom)](https://github.com/yashchitre03/Fetch-Rewards/blob/main/README_images/main-2.png)

* Result page
  ![Result page](https://github.com/yashchitre03/Fetch-Rewards/blob/main/README_images/res.png)

## Technologies

* Programming language
    * [Python 3 programming language](https://www.python.org/)

* Frameworks
    * [Django 3 web framework](https://www.djangoproject.com/)
    * [Bulma CSS framework](https://bulma.io/)

* Tools
    * [Docker Engine](https://docs.docker.com/engine/)
    * [git scm](https://git-scm.com/)

* IDE
    * [Jetbrains Pycharm](https://www.jetbrains.com/pycharm/)

## Algorithms

The following algorithms were used for text similarity detection:

* [Jaccard Index](https://en.wikipedia.org/wiki/Jaccard_index)
* [Cosine Similarity](https://en.wikipedia.org/wiki/Cosine_similarity)
* [Dice's Coefficient](https://en.wikipedia.org/wiki/S%C3%B8rensen%E2%80%93Dice_coefficient)
* [Overlap Coefficient](https://en.wikipedia.org/wiki/Overlap_coefficient)