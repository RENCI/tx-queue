FROM python:3-alpine

RUN mkdir test
WORKDIR test

RUN pip3 install requests pytest redis rq

COPY test/test_txqueue.py test_txqueue.py
COPY utils.py utils.py
COPY test/entrypoint.py entrypoint.py
COPY test/entrypoint_exc.py entrypoint_exc.py

ENTRYPOINT ["pytest"]



