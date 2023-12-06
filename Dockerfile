FROM python:3.10

RUN mkdir /fastapi_smart

WORKDIR /fastapi_smart

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .


CMD gunicorn main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000

