FROM python:latest

ADD consumer.py /consumer/

ADD requirements.txt /consumer/

WORKDIR /consumer/

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["consumer.py"]
