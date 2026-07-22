FROM python:3.12-alpine3.24

WORKDIR /app

COPY app/ ./app/

EXPOSE 8000

CMD ["python", "app/main.py"]