#start with a Python image
FROM python:3.12-slim

#set working directory
WORKDIR /app

#install required system packages for psycopg2 and building dependencies, then clean up cache
RUN apt-get update && apt-get install -y --no-install-recommends build-essential libpq-dev && rm -rf /var/lib/apt/lists/*

#install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

#copy the rest of the project
COPY . .

#expose FastAPI port
EXPOSE 8000

#start gunicorn with uvicorn workers
CMD ["gunicorn", "main:app", "-k", "uvicorn.workers.UvicornWorker", "-w", "2", "-b", "0.0.0.0:8000", "--timeout", "60", "--access-logfile", "-", "--error-logfile", "-"]
