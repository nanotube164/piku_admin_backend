#python version
FROM python:3.9
#This is mainly for monitoring logs that let us know whatever is happening
ENV PYTHONUNBUFFED 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app

#CMD python manage.py runserver 0.0.0.0:8000
#CMD python consumer.py