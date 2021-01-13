FROM python:3.7

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

COPY . /challenge

WORKDIR /challenge

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["runner.py"]