FROM metasploitframework/metasploit-framework:latest
RUN apk add --update --no-cache netcat-openbsd bash enum4linux && rm -rf /var/cache/apk/* 
