FROM node:latest

ENV DockerHOME=/home/app/frontend

RUN mkdir -p $DockerHOME

COPY . $DockerHOME

WORKDIR $DockerHOME

COPY .env.example .env

RUN npm install

RUN npm run build
