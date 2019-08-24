FROM kalilinux/kali-linux-docker

# updates, install metasploit, run postgresql services and create initial db
RUN apt-get -y update && apt-get -y dist-upgrade && // 
    apt-get -y install metasploit-framework && //
    apt-get clean && //
    service postgresql start && //
    msfdb init

RUN apt-get install -y kali-linux-top10 && apt-get install -y kali-linux-web

ENTRYPOINT ["bin/bash"]
