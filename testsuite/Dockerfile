FROM python:3.11

WORKDIR /usr/src/testsuite

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

ARG SERVICE_URL_ARG
ENV SERVICE_URL $SERVICE_URL_ARG
