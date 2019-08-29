FROM python:3-alpine

RUN pip3 install redis rq docker pytest

RUN mkdir test
WORKDIR test

COPY worker/entrypoint.py entrypoint.py
COPY worker/start.py start.py
COPY utils.py utils.py
COPY worker/test/test_txqueue_worker.py test_txqueue_worker.py

ENTRYPOINT ["pytest"]