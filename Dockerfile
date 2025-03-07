FROM python:3.9-slim

WORKDIR /

COPY requirements.txt .

RUN apt-get update && apt-get install -y libpq-dev gcc \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["python", "app.py"]