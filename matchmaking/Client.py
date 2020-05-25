from Network import Network
import select
import socket
import sys
from utils import Room, Hall, Player
import utils

n = Network()
server_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_connection.connect((n.server, n.port))


def prompt():
    print('>', end=' ', flush=True)


msg_prefix = ''

socket_list = [server_connection]
print(socket_list)

while True:
    read_sockets, write_sockets, error_sockets = select.select(
        socket_list, [], [])
    for s in read_sockets:
        if s is server_connection:  # incoming message
            msg = s.recv(4096)
            if not msg:
                print("Server down!")
                sys.exit(2)
            else:
                if msg == utils.QUIT_STRING.encode():
                    sys.stdout.write('Bye\n')
                    sys.exit(2)
                else:
                    sys.stdout.write(msg.decode())
                    if 'Please tell us your name' in msg.decode():
                        msg_prefix = 'name: '  # identifier for name
                    else:
                        msg_prefix = ''
                    prompt()
                    input()

        else:
            msg = msg_prefix + sys.stdin.readline()
            server_connection.sendall(msg.encode())
