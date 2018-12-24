FROM metasploitframework/metasploit-framework:latest
FROM alpine:latest

RUN apk add --update --no-cache netcat-openbsd bash && rm -rf /var/cache/apk/* 
