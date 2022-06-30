FROM alpine:latest

WORKDIR /usr/src/app

RUN apk update
RUN apk add --no-cache python3 py-pip tcpdump vim iptables
RUN pip3 install scapy
RUN alias python='python3'

COPY ./entrypoint.sh /

ENTRYPOINT ["/entrypoint.sh"]

