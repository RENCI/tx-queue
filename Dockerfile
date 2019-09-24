FROM python:3-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY api/openAPI3/requirements.txt /usr/src/app/

RUN apk add gcc musl-dev
RUN pip3 install --no-cache-dir -r requirements.txt

COPY api/openAPI3 /usr/src/app
COPY txqueue /usr/src/app/txqueue
COPY config /usr/src/app/config
COPY entrypoint.py /usr/src/app

EXPOSE 8080

ENTRYPOINT ["gunicorn"]

CMD ["-w", "4", "-b", "0.0.0.0:8080", "-k", "gevent", "swagger_server:create_app()"]