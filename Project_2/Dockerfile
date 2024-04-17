FROM python:latest

WORKDIR /api_demo

COPY ./demo_api.py .

RUN pip install requests

CMD [ "python3", "demo_api.py" ]