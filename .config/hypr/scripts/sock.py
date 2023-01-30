import socket
import os
import sys

HYPER_SOCKET = os.environ.get('HYPRLAND_INSTANCE_SIGNATURE')
socket_path = f"/tmp/hypr/{HYPER_SOCKET}/.socket2.sock"

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(socket_path)

sock.listen

while True:
    connection, address = sock.accept()

    while True:
        data = connection.recv(16)
        if data:
            print(f"Recieved: ", data)
