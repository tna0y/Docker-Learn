FROM python:3.5

WORKDIR /app

ADD . /app

EXPOSE 8000
RUN pip install --trusted-host pypi.python.org -r requirements.txt
run python manage.py migrate

CMD ["python", "manage.py", "runserver","0.0.0.0:8000"]
