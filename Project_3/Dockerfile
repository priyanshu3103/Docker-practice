FROM python:latest

WORKDIR /sql

COPY ./sql_demo.py .
COPY ./servers.txt .

RUN pip install pymysql
RUN pip install cryptography

CMD [ "python3", "sql_demo.py" ]