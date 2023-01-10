FROM ubuntu
COPY . /app
WORKDIR /app
CMD node garden.py