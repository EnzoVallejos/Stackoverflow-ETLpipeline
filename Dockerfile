#this image i use for web scrappin
FROM python:3.8.6-buster

#i update the repositories
RUN apt-get update && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

#I set the workdir and install the libraries
WORKDIR /usr/src
COPY requirements.txt /usr/src
RUN pip install -r requirements.txt