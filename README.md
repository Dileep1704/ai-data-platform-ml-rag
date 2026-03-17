# AI Data Platform with ML & RAG

## Overview

This project is a scalable AI-powered data platform that supports data ingestion, machine learning predictions, and retrieval-augmented querying. It demonstrates how modern backend systems integrate ML models, databases, and APIs in a production-style environment.

## Features

* REST APIs using FastAPI
* ML model deployment (prediction API)
* RAG-based query system
* PostgreSQL for structured data storage
* MongoDB for unstructured data storage
* Dockerized services for scalability

## Tech Stack

* Backend: FastAPI (Python)
* Machine Learning: Scikit-learn
* Databases: PostgreSQL, MongoDB
* DevOps: Docker
* Data Processing: Pandas

## API Endpoints

* POST /ingest → Store data
* POST /predict → ML predictions
* GET /rag → Query system

## How to Run

### 1. Clone repository

git clone https://github.com/your-username/ai-data-platform-ml-rag.git
cd ai-data-platform-ml-rag

### 2. Install dependencies

pip install -r requirements.txt

### 3. Run Docker (DBs)

docker-compose up -d

### 4. Run backend

python -m uvicorn backend.main:app --reload

### 5. Open API docs

http://127.0.0.1:8000/docs

## Future Improvements

* Deploy on AWS
* Add authentication
* Add frontend dashboard

## Author

Dileep Tallamapuram
