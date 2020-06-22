# Basic Flask
Simple and Basic Flask App

## Setup

    python3 -m venv venv
    . venv/bin/activate # Please use `. venv/bin/activate.fish` if you are using fish
    python3 setup.py test

## Run

    python3 setup.py install
    FLASK_ENV=development FLASK_APP=engine flask run

## Run via Docker

    docker build -t basic-flask .
    docker run -p 5000:5000 basic-flask
