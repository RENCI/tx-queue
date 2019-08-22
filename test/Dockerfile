FROM python:3-alpine

RUN mkdir test
WORKDIR test

RUN pip3 install requests pytest redis rq

COPY test_txqueue.py test_txqueue.py
COPY entrypoint.py entrypoint.py

ENTRYPOINT ["pytest"]



