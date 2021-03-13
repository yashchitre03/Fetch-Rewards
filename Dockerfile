FROM python:3-alpine

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . app
WORKDIR /app

EXPOSE 8080

ENTRYPOINT ["python", "manage.py"]
CMD ["runserver"]