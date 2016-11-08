FROM ubuntu

RUN mkdir /webapp
COPY zipcount.py webapp

RUN apt-get update && \
    apt-get install -y python-pip curl && \
    pip install CherryPy && \
    apt-get autoclean -y

WORKDIR /webapp
CMD ["python", "zipcount.py"]
