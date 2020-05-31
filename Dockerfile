FROM python:3.7
WORKDIR /work

RUN pip install \
    selenium \
    beautifulsoup4
