FROM metasploitframework/metasploit-framework:latest
# Install missing Dependencies.
RUN apk add --update \
    py-pip \
  && pip install virtualenv \
  && rm -rf /var/cache/apk/*
