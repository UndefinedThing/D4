import socket

roomList = []

MAX_CLIENTS = 30


def create_socket(address):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.setblocking(0)
    s.bind(address)
    s.listen(MAX_CLIENTS)
    print("Now listening at ", address)
    return s


class Player(object):
    def __init__(self, name, sock):
        self.socket = sock
        self.name = name

    def fileno(self):
        return self.socket.fileno()


class Room(object):
    def __init__(self, name):
        self.players = []  # a list of Players
        self.name = name   # room's name
        self.history = []  # room's message history

    def addPlayer(self, addedPlayer):
        for player in self.players:
            if player.name == addedPlayer.name:
                return "Already in"

        try:
            self.players.append(addedPlayer)
            return "0///Le joueur a bien été ajouté"
        except Exception as e:
            print(e)
            return "22///Une erreur est survenue"

    def removePlayer(self, player):
        try:
            self.players.remove(player)
            return True
        except Exception as e:
            print(e)
            return "22///Une erreur est survenue"

    def welcome_new(self, from_player):
        msg = "Welcomes to " + from_player.name + 'in' + self.name + '\n'
        self.history.append(msg)
        return self.history

    def broadcast(self, from_player, msg):
        msg = from_player.name + ":" + msg
        self.history.append(msg)
        return self.history


def createRoom(name):
    if getRoom(name) != None:
        return "11///Une room de ce nom existe déjà"
    else:
        try:
            if "///" in name or "." in name:
                raise Exception("12///Nom de room invalide")
            new_room = Room(name)
            roomList.append(new_room)
            return "0///La room a été créée"
        except Exception as e:
            if "12" in e.split("///")[0]:
                return e
            return "13///Une erreur est survenue"


def getRoom(searchName):
    for room in roomList:
        if room.name == searchName:
            print(room.players)
            return [room.name, room.players]

    return None


def getObjRoom(searchName):
    for room in roomList:
        if room.name == searchName:
            return room

    return None


def getRooms():
    global roomList
    res = []
    for room in roomList:
        res.append([room.name, len(room.players)])
    return res
