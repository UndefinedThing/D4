import socket
from _thread import *
import sys
from server_db_dialog import *

def threaded_client(conn):
    conn.send(str.encode("Connected"))

    # connexion db
    dbConn = create_connection(r"projetBdd.db")

    print(checkConn(dbConn))

    while True:
        try:
            reply = ""
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            treated = reply.split("/")

            if treated[0] == "connect" :
                conn.send(str.encode(usersConnection(dbConn, treated[1], treated[2])))
            if treated[0] == "register" :
                conn.send(str.encode(userRegister(dbConn, treated[1], treated[2], treated[3])))
            if not data:
                print("Disconnected")
                break
            else:
                print("Received: ", reply)
                print("Sending : ", reply)

            # conn.sendall(str.encode(reply))
        except Exception as e:
            print(e)
            break

    print("Lost connection")
    conn.close()

server = "localhost"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

while True:
    conn, addr = s.accept()
    print("Connection from :", addr)

    start_new_thread(threaded_client, (conn,))
