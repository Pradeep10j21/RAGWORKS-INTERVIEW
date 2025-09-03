FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y build-essential libpq-dev && rm -rf /var/lib/apt/lists/*

# copy requirements from project root (context is now backend-engineer/)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy only problem-1 code into container
COPY problems/problem-1/ .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
