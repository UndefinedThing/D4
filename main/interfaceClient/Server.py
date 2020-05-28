from _thread import *
from interfaceClient.db_dialog import *

import select
import socket
import sys
import pickle
import interfaceClient.utils as utl
from interfaceClient.utils import Room, Player

player_list = {}

def threaded_client(conn: socket):
    global player_list

    conn.send(str.encode("Connected"))
    dbConn = create_connection(r"interfaceClient\\projetBdd.db")

    print(checkConn(dbConn))

    while True:
        try:
            reply = ""
            data = conn.recv(2048) # <- ERROR

            try:
                treated = pickle.loads(data)
            except :
                reply = data.decode("utf-8")
                treated = reply.split("///") # <- Split request using defined separator to use headers

            if treated[0] == "isItWorking" :
                conn.send(str.encode("1"))

            if treated[0] == "register" :
                registerString = userRegister(dbConn, treated[1], treated[2], treated[3])
                registerTable = registerString.split("///")

                if registerTable[0] == "0":
                    player_list[registerTable[3]] = Player(registerTable[3], conn)

                conn.send(str.encode(registerString))

            if treated[0] == "connect" : 
                connectString = usersConnection(dbConn, treated[1], treated[2])
                connectTable = connectString.split("///")

                if connectTable[0] == "0":
                    print("va pas la")
                    player_list[connectTable[3]] = Player(connectTable[3], conn)

                conn.send(str.encode(connectString))

            if treated[0] == "createRoom" :
                try :
                    # create room
                    if utl.createRoom(str(treated[1])).split("///")[0] == "0" :
                        # userName join room
                        utl.getObjRoom(treated[1]).addPlayer(player_list.get(treated[2]))

                    res = "0" + "///" + utl.getObjRoom(treated[1]).name + "///" + str(len(utl.getObjRoom(treated[1]).players))

                    conn.send(str.encode(res))
                except Error as e:
                    print('Some error occured line 33 : ', e)

            if treated[0] == "getRooms" :
                res = ["0", utl.getRooms()]
                roomsList = pickle.dumps(res)
                conn.send(roomsList)

            if treated[0] == "joinRoom" :
                if utl.getObjRoom(treated[1]).addPlayer(player_list.get(treated[2])).split('///')[0] == "1" :
                    utl.getObjRoom(treated[1]).players[0].socket.sendall(str.encode("GOGOGO"))

                res = "0" + "///" + utl.getObjRoom(treated[1]).name + "///" + str(len(utl.getObjRoom(treated[1]).players))
                conn.send(str.encode(res))

            if treated[0] == "quitRoom" :
                if utl.getObjRoom(treated[1]).removePlayer(player_list.get(treated[2])) :
                    conn.send(str.encode("0///La room a été quittée"))
                else :
                    conn.send(str.encode("1///La room a été quittée"))

            if treated[0] == "whoAmI" :
                conn.send(str.encode(utl.getObjRoom(treated[1]).whichColor(player_list.get(treated[2]))))

            if treated[0] == "dataGame" :
                for user in utl.getObjRoom(treated[1]).players:
                    if player_list.get(treated[2]) != user :
                        res = ["0", "boardsInfo", treated[3], treated[4], treated[5], treated[6]]
                        gameInfos = pickle.dumps(res)
                        utl.getObjRoom(treated[1]).players[0].socket.sendall(gameInfos)

            if not data:
                print("Disconnected")
                break
            else:
                print("Received: ", reply)
                print("Sending : ", reply)

            print("================ END REQUEST ================\n=============================================")

            # conn.sendall(str.encode(reply))
        except Exception as e:
            print(e)
            break

    print("Lost connection")
    conn.close()

def main():
    server = "192.168.0.46"
    port = 61825

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        s.bind((server, port))
    except socket.error as e:
        str(e)

    s.listen(10)
    print("Waiting for a connection, Server Started")

    while True:
        conn, addr = s.accept()
        print("Connection from :", addr)
        print(conn)

        conn.settimeout(1800)

        start_new_thread(threaded_client, (conn,))
