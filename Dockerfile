FROM python:latest

RUN apt-get update && apt-get install && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /code
COPY . .

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

RUN useradd -ms /bin/bash docker_user && \
    chown docker_user --recursive .

USER docker_user

ENTRYPOINT [ "sh", "./entrypoint.sh" ]