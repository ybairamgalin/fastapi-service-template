FROM python:3.11

WORKDIR /usr/src/service

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.service.txt

CMD ["uvicorn", "main:app"]
