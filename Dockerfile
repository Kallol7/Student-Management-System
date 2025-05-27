FROM python:3.12-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN python -m pip install --upgrade pip

COPY ./requirements.txt .

RUN python -m pip install --no-cache-dir -r requirements.txt && \
    python -m pip install --no-cache-dir gunicorn

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

EXPOSE 8000