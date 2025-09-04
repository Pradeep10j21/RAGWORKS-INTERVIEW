# Backend Engineer Assessment Projects (Problem 1 to 3)

This repository contains solutions for the **Backend Engineer Technical Assessment**, including Problem 1, Problem 2, and Problem 3. Each project uses **Python 3.11**, **FastAPI**, **PostgreSQL**, and **Redis** (Problem 3 uses full dockerized infrastructure).  

---

## Table of Contents

1. [Project Overview](#project-overview)  
2. [Prerequisites](#prerequisites)  
3. [Project Setup](#project-setup)  
4. [Running Each Problem](#running-each-problem)  
5. [Common Errors and Fixes](#common-errors-and-fixes)  
6. [Testing](#testing)  
7. [Submission Guidelines](#submission-guidelines)  

---

## Project Overview

- **Problem 1**: Basic Python backend logic implementation.  
- **Problem 2**: Intermediate Python API project using FastAPI.  
- **Problem 3**: Full backend microservice with **FastAPI**, **PostgreSQL**, and **Redis** integration.  

All projects are organized under:  
```
backend-engineer/
├─ problem-1/
├─ problem-2/
├─ problem-3/
└─ docker-compose/
```

---

## Prerequisites

Ensure the following are installed on your machine:

- [Python 3.11](https://www.python.org/downloads/)  
- [Docker & Docker Compose](https://docs.docker.com/get-docker/)  
- [Git](https://git-scm.com/)  

---

## Project Setup

### 1. Clone Repository

```bash
git clone <your-forked-repo-url>
cd backend-engineer
```

### 2. Create Virtual Environment (for local Python projects)

```bash
python -m venv venv311
source venv311/bin/activate   # Linux/Mac
venv311\Scripts\activate      # Windows PowerShell
```

### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt   # Each problem has its own requirements.txt
```

---

## Running Each Problem

### Problem 1 & 2 (Local Python / FastAPI)

1. Navigate to the problem directory:  
   ```bash
   cd problem-1   # or problem-2
   ```

2. Run the FastAPI app (if applicable):  
   ```bash
   uvicorn main:app --reload
   ```

3. Visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

### Problem 3 (Dockerized with PostgreSQL & Redis)

#### 1. Navigate to docker-compose folder

```bash
cd docker-compose
```

#### 2. Start Infrastructure

```bash
./start-backend.sh   # Includes Postgres & Redis services
```

> This script will:  
> - Build Docker images  
> - Start FastAPI, PostgreSQL, and Redis containers  

#### 3. Navigate to Problem 3 directory

```bash
cd ../problem-3
```

#### 4. Run FastAPI in Docker

```bash
docker-compose up
```

#### 5. Visit the API

Open your browser: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## Common Errors and Fixes

### 1. FastAPI 404 Not Found

- **Cause**: Trying to access `/` endpoint which is not defined.  
- **Fix**: Check `main.py` for available endpoints or use `/docs` to test.

```
http://127.0.0.1:8000/docs
```

---

### 2. PostgreSQL Connection Errors

```
asyncpg.exceptions.InvalidPasswordError
ConnectionRefusedError: [Errno 111]
```

- **Cause**: FastAPI tries to connect before PostgreSQL is ready or password mismatch.  
- **Fix**:  
  - Ensure `POSTGRES_PASSWORD` in `docker-compose.yml` matches FastAPI settings.  
  - Use `depends_on` in `docker-compose.yml`:
    ```yaml
    fastapi_app:
      depends_on:
        - postgres_db
        - redis_cache
    ```
  - Add a `wait-for.sh` script to delay FastAPI start until PostgreSQL is ready.

---

### 3. Redis Not Connecting

- **Cause**: Container not fully started or wrong host/port.  
- **Fix**: Ensure FastAPI uses `redis_cache:6379` as host and port in Docker network.

---

### 4. Docker Version Warnings

```
the attribute `version` is obsolete, it will be ignored
```

- **Cause**: Docker Compose v2 ignores `version` key in YAML.  
- **Fix**: Remove the `version` line from `docker-compose.yml`.

---

## Testing

- Use **Swagger UI** to test all endpoints:  
  ```
  http://127.0.0.1:8000/docs
  ```
- For automated tests (if included):
  ```bash
  pytest
  ```


---

### Notes

- All database credentials are **configurable in `.env` or docker-compose.yml`**.  
- Redis and Postgres containers **persist data** in Docker volumes.  
- Always **stop containers** after use:  
  ```bash
  docker-compose down -v
  ```

