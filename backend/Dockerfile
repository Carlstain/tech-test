FROM python:3.10   

ENV DockerHOME=/home/app/backend

ENV POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_VIRTUALENVS_IN_PROJECT=false \
    POETRY_NO_INTERACTION=1

ENV PATH="$PATH:$POETRY_HOME/bin"

RUN mkdir -p $DockerHOME 

COPY . $DockerHOME  

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

RUN pip install --upgrade pip

RUN curl -sSL https://install.python-poetry.org | python3 -

WORKDIR $DockerHOME

COPY .env.example .env

RUN poetry install --only main
RUN pip install gunicorn

EXPOSE 8000  

# CMD poetry run python manage.py migrate

# CMD poetry run python manage.py runserver
