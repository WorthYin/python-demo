FROM python:3.6.5-alpine3.7

WORKDIR /usr/src/app

RUN mkdir -p /var/log/gunicorn && \
    pip install --no-cache-dir gunicorn && \
    pip install --no-cache-dir flask

COPY . /usr/src/app

ENV PORT 8000
EXPOSE 8000 

CMD ["/usr/local/bin/gunicorn", "-w", "2", "-b", ":8000", "python-demo:app"]

