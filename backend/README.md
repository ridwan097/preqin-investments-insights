# Preqin Fullstack Interview Task

## Overview

The bakend was built using **FastAPI** (Python) for the backend and **SQLite** as the database. The project is fully **Dockerized** to ensure a smooth setup and deployment.

## Setup Instructions

### 1️⃣ Prerequisites

Ensure you have the following installed:

- **Docker** ([Install Docker](https://docs.docker.com/get-docker/))
- **Docker Compose** ([Install Docker Compose](https://docs.docker.com/compose/install/))
- Alternatively, you can install ([Install Orbstack](https://docs.docker.com/compose/install/)) whcih includes docker and docker compose and is optimized for macOS

- (Optional) Python 3.9+ if running without Docker

---

### 2️⃣ Running the Application with Docker

#### **Step 1: Clone the Repository**

```sh
git clone https://github.com/ridwan097/preqin-investments-insights.git
cd preqin-fullstack-interview-task/backend
```

#### **Step 2: Build and Run the Docker Container**

```sh
docker-compose up --build
```

This will:

- Build the FastAPI application.
- Run the SQLite database setup automatically.
- Expose the FastAPI server at `http://127.0.0.1:8000`.

#### **Step 3: Verify API is Running**

Once the container is up, open:

- **Swagger UI** (API Documentation): [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc API Docs**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

### 3️⃣ Running the Application Without Docker (Manual Setup)

#### **Step 1: Create a Virtual Environment & Install Dependencies**

```sh
cd backend
python3.9 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate    # Windows
pip install -r requirements.txt
```

#### **Step 2: Set Up the Database**

```sh
python db/db.py
```

#### **Step 3: Start the FastAPI Server**

```sh
uvicorn main:app --reload
```

---

### 4️⃣ Testing the Endpoints

You can test the API using:

#### **1. Swagger UI (Browser)**

- Visit: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

#### **2. cURL (Terminal)**

```sh
curl -X 'GET' 'http://127.0.0.1:8000/investors' -H 'accept: application/json'
```

#### **3. Python Requests**

```python
import requests
BASE_URL = "http://127.0.0.1:8000"
response = requests.get(f"{BASE_URL}/investors")
print(response.json())
```

---

### 5️⃣ Stopping and Removing Containers

To stop the application, press **CTRL+C** or run:

```sh
docker-compose down
```

To remove all containers and volumes (reset database):

```sh
docker-compose down -v
```
