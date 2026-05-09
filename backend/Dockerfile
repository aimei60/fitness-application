#start with a Python image
FROM python:3.12-slim

#set working directory
WORKDIR /app

#install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

#copy the rest of the project
COPY . .

#expose FastAPI port documentation
EXPOSE 8000

#start gunicorn run the FastAPI app, use Uvicorn workers, and listen on port 8000
CMD ["gunicorn", "main:app", "-k", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:8000"]