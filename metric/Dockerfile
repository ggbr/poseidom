FROM ubuntu:latest
MAINTAINER fnndsc "ggbr@eu.aa"

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip
ADD . /app
WORKDIR /app
RUN pip3 install --no-cache-dir -r requirements.txt

CMD [ "python3", "app.py" ]
