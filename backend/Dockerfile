FROM python:3.8

WORKDIR /usr/src/app
ENV ENVIRONMENT=PROD

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["gunicorn"]
CMD ["--bind=0.0.0.0:5000", "app:app"]