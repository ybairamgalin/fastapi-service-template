FROM python:3.11

WORKDIR /usr/src/testsuite

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.testsuite.txt

CMD ["pytest", "."]
