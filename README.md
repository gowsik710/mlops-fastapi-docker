🚀 End-to-End MLOps Model Deployment

This project demonstrates a junior–associate level MLOps workflow, where a machine learning model is trained, deployed as a REST API, containerized using Docker, and automatically deployed to the cloud using CI/CD.

The main goal of this project is to convert a notebook-based ML model into a production-style service that can be accessed through an API and updated automatically when code changes.

📌 Project Workflow

Train a machine learning model in Jupyter Notebook

Save the trained model as model.joblib

Create REST APIs using FastAPI

Validate input data using Pydantic

Dockerize the application

Push code to GitHub

Automatically build and deploy using Render (CI/CD)

Test live endpoints

🌐 API Endpoints
GET /health

Checks if the application is running

Returns application status

POST /predict

Accepts input feature values

Returns prediction from the trained model

🛠 Tools & Technologies Used

Python

Scikit-learn

FastAPI

Pydantic

Docker

GitHub

Render (Cloud Deployment)

CI/CD (Auto-deploy on Git push)

🎯 What This Project Demonstrates

End-to-end ML deployment

API-based model serving

Docker containerization

Cloud deployment

CI/CD automation

Production-style ML workflow
