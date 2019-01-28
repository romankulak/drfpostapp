FROM python:3.7.2-slim-stretch

ARG DEMO

WORKDIR /app

COPY . /app/

RUN pip install -r requirements.txt

RUN python manage.py migrate

# Populate with predefined data for demo purpose
RUN if [ "x$DEMO" = "x" ] ; then \
    echo Skipping Loading Fixtures... ; \
    else \
    python manage.py loaddata users.json posts.json; fi

EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000