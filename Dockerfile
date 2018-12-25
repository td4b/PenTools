FROM metasploitframework/metasploit-framework:latest

RUN apk add --update \
    netcat-openbsd \
    bash \
    python \
    python-dev \
    py-pip \
    build-base \
  && pip install virtualenv \
  && rm -rf /var/cache/apk/*
