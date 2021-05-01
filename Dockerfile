FROM python:3.8-slim-buster

COPY calculator.py /

CMD [ "python", "calculator.py"]
