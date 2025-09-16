# Dockerized-Python-Web-App-with-SQLite
Create a complete web application with HTML/CSS frontend, Python backend, and SQLite database, all containerized with Docker.

Project Structure text
web-app/
├── app.py
├── requirements.txt
├── database.py
├── init_db.py
├── Dockerfile
├── docker-compose.yml
├── static/
│   └── style.css
└── templates/
    └── index.html


Create a project directory with "web-app"  and navigate to it
Build and run the Docker containers with command
"docker-compose build"
Run the build image with port to acces the service
"docker run -p 5000:5000 (image ID)"
access localhost "http://localhost:5000"
