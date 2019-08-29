FROM python:3-alpine

RUN pip3 install redis rq

COPY worker/entrypoint.py entrypoint.py
COPY worker/start.py start.py
COPY utils.py utils.py

ENTRYPOINT ["python3", "start.py"]



