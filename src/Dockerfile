FROM python:3.11

WORKDIR /usr/src/service

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . ./

EXPOSE 8000

ARG PG_DB_ARG
ARG PG_HOST_ARG
ARG PG_PORT_ARG
ARG PG_USER_ARG
ARG PG_PASS_ARG

ENV PG_DB $PG_DB_ARG
ENV PG_HOST $PG_HOST_ARG
ENV PG_PORT $PG_PORT_ARG
ENV PG_USER $PG_USER_ARG
ENV PG_PASS $PG_PASS_ARG

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port=8000"]
