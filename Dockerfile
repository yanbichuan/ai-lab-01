FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
COPY main.py .
ENTRYPOINT ["python","main.py"]