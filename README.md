Flask App - CI and CI using Github Actions
A minimal Flask web application built for learning containerization using Github Action and deployment to Self Hosted Runner.

Python Flask Docker:

Tech Stack-
Component	Technology:
Framework	Flask 3.1.1
Runtime	Python 3.14
Container	Docker (python-slim)

Deploy in Github Actions (Self Hosted Runner):
Project Structure
flask-app-Github Action
app.py                 
# Flask app with routes

run.py                 
# Entry point (host 0.0.0.0, port 80)

requirements.txt       
# Python dependencies

templates/
   index.html         
   # Landing page
   
Dockerfile             
# Simple single-stage build

Quick Start
Run locally
pip install -r requirements.txt
python run.py
App runs at http://localhost:80.

Run with Docker
Simple build:

docker build -t flask-app .
docker run -p 80:80 flask-app:

docker build -f Dockerfile -t flask-app .
docker run -p 80:80 flask-app
Dockerfiles Explained
Simple (Dockerfile)
Single-stage build using python:3.14-slim. Straightforward — copies everything, installs dependencies, runs the app. Good for development and learning.

Route	Method	Description
/	GET	Landing page
/health	GET	Health check (returns Server is up and running)
