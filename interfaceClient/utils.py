import socket

roomList = []

class Room:
    def __init__(self, name):
        self.players = []  # a list of sockets
        self.name = name

    def addPlayer(self, from_player):
        msg = self.name + " welcomes: " + from_player.name + '\n'
        for player in self.players:
            player.socket.sendall(msg.encode())

    def broadcast(self, from_player, msg):
        msg = from_player.name.encode() + b":" + msg
        for player in self.players:
            player.socket.sendall(msg)

    def remove_player(self, player):
        self.players.remove(player)
        leave_msg = player.name.encode() + b"has left the room\n"
        self.broadcast(player, leave_msg)

def createRoom(name) :
    if getRoom(name) != None :
        return "11///Une room de ce nom existe déjà"
    else :
        try :
            if "///" in name or "." in name :
                raise Exception("12///Nom de room invalide")
            new_room = Room(name)
            roomList.append(new_room)
            return "0///La room a été créée"
        except Exception as e:
            if "12" in e.split("///")[0] :
                return e
            return "13///Une erreur est survenue"

def getRoom(searchName):
    for room in roomList :
        if room.name == searchName :
            return [room.name, room.players]

    return None

def getRooms():
    global roomList
    res = []
    for room in roomList:
        res.append([room.name,room.players])   
    return res