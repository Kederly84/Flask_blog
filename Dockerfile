FROM python:3.11.2-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY run.py run.py
COPY .env .env
COPY blog ./blog
COPY wsgi.py wsgi.py

EXPOSE 5000

CMD ["python3", "run.py"]
