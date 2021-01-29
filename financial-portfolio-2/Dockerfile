FROM python:3.8

ADD . /code

WORKDIR /code

RUN apt-get update && \
  apt-get install -y \
  g++ \
  make \
  cmake \
  unzip \
  libcurl4-openssl-dev

RUN pip install -r requirements.txt
RUN pip install awslambdaric boto3

ENTRYPOINT [ "python", "-m", "awslambdaric" ]
CMD [ "finport.portfolio_handler" ]
