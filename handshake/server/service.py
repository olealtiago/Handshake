#!/usr/bin/env python

import socket


def create_connection(with_connection: (str, int)) -> socket.socket:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(with_connection)
    s.listen(1)
    return s


def listen_for_message(connection_info: (socket.socket, str)):
    conn, addr = connection_info
    with conn:
        print(f'Connected to {addr}')
        while True:
            data = conn.recv(1024)
            if not data:
                break
            msg = f'{data.decode()}'
            print(f'Received: {msg}', end='')
            # conn.send(str.encode(msg))


def main(connection: (str, int)):
    with create_connection(connection) as s:
        print(f'Socket is listening on {CONNECTION[0]}:{CONNECTION[1]}')
        while True:
            client = s.accept()
            listen_for_message(client)
            print(f'Connection to {client[1]} has been dropped')


if __name__ == "__main__":
    hostname = socket.gethostname()
    CONNECTION = (socket.gethostbyname(hostname), 8998)
    main(CONNECTION)
