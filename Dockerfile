FROM kalilinux/kali-linux-docker
# Install missing Dependencies.
RUN apt-get update -y && apt-get dist-upgrade -y && apt-get autoremove -y && apt-get clean -y

RUN apt-get install -y kali-linux-top10 && apt-get install -y kali-linux-web

ENTRYPOINT ["bin/bash"]
