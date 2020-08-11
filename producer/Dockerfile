FROM python:latest

ADD producer.py /producer/

ADD requirements.txt /producer/

WORKDIR /producer/

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["producer.py"]
