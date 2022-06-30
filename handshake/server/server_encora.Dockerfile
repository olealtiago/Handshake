FROM alpine:latest

WORKDIR /usr/src/app

RUN apk update
RUN apk add --no-cache python3 nmap
RUN alias python='python3'

COPY ./service.py .

EXPOSE 8998

CMD ["python3",  "-u", "./service.py"]

