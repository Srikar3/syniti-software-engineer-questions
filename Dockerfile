FROM python:3.8
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
CMD pytest --cov-config=.coveragerc --cov-report term --cov=. test.py
