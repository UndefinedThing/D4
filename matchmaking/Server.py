import select
import socket
import sys
import pdb
from utils import Hall, Room, Player
import utils


server = "localhost"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

listen_sock = utils.create_socket((server, port))

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")


hall = Hall()
connection_list = []
connection_list.append(listen_sock)


while True:
    conn, addr = s.accept()
    print("Connected to ", addr)

    # Player.fileno()
    read_players, write_players, error_sockets = select.select(
        connection_list, [], [])
    for player in read_players:
        if player is listen_sock:  # new connection, player is a socket
            new_socket, add = player.accept()
            new_player = Player(new_socket)
            connection_list.append(new_player)
            hall.welcome_new(new_player)

        else:  # new message
            msg = player.socket.recv(4096)
            if msg:
                msg = msg.decode().lower()
                hall.handle_msg(player, msg)
            else:
                player.socket.close()
                connection_list.remove(player)

    for sock in error_sockets:  # close error sockets
        sock.close()
        connection_list.remove(sock)
