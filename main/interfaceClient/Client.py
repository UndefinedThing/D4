import interfaceClient
from interfaceClient.Network import Network
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from tkinter.simpledialog import *

from echec.classe.Plateau import Plateau

import re
import sys
import sched, time

mail_regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
n = Network()

conPassword = True
regPassword = True
regSamePassword = True

User = []
roomsList = []
inRoom = []
couleur = ""

class conRegPage:
    def __init__(self,root):
        self.root = root

        ############### INITIALIZING FRAMES IN WINDOW ###############
        # -> Connection frame
        self.connect = Frame(self.root)
        self.connect.grid(row=1, column=0, columnspan=2, sticky=(W,E), padx=20, pady=20)

        # -> Vertical Separator
        ttk.Separator(self.root, orient=VERTICAL).grid(column=2, row=1, rowspan=1, sticky=NS)

        # -> Register frame
        self.register = Frame(self.root)
        self.register.grid(row=1, column=3, columnspan=2, sticky=(W,E), padx=20, pady=20)

        ############### INITIALIZING FIELDS ###############
        # -> Connection and Register fields
        self.initConnect()
        self.initRegister()

        # -> Connection to the server status
        self.connection = Label(self.root)
        self.connection.grid(row=0, column=2, padx=20, pady=20)

        # -> Calls method to check if client is connected to server
        self.checkConn()

        # -> Initialize Quit button for client
        button_quit = Button(self.root, text="Quitter", command=self.connect.quit)
        button_quit.grid(row=2, column=2, padx=20, pady=20)

        # -> Save default background color in variable
        self.orig_color = button_quit.cget("background")

    ############### METHODS USED ###############
    def initConnect(self):
        Label(self.connect, text="Se connecter", font = "Verdana 16 bold").grid()

        self.connectError = Label(self.connect, state="disabled")
        self.connectError.grid()

        ############ LOGIN FORM ############
        Label(self.connect, text="Username").grid()

        self.username = Entry(self.connect, width=30)
        self.username.grid()

        Label(self.connect, text="Password").grid()

        self.password = Entry(self.connect, show="*", width=30)
        self.password.grid()
        
        self.connectPasswordShow = Label(self.connect, name="connectPassword", text="Montrer / Cacher")
        self.connectPasswordShow.grid()
        self.connectPasswordShow.bind("<Button-1>", lambda event: self.toggleShowField(event))

        ############# END FORM #############
        bouton_connect = Button(self.connect, text="Connexion", command=lambda:self.onClickConnect(self.username.get(), self.password.get()))
        bouton_connect.grid()

        self.user = Label(self.connect)
        self.user.grid()

    def initRegister(self) :
        Label(self.register, text="S'enregister", font = "Verdana 16 bold").grid()
        self.registerError = Label(self.register, state="disabled")
        self.registerError.grid()

        ############ LOGIN FORM ############
        # -> Mail address
        Label(self.register, text="Adresse mail :").grid()
        self.registerEmail = Entry(self.register, width=30)
        self.registerEmail.grid()
        
        # -> Username
        Label(self.register, text="Nom de compte").grid()
        self.registerUsername = Entry(self.register, width=30)
        self.registerUsername.grid()

        # -> Password
        Label(self.register, text="Mot de passe").grid()
        self.registerPassword = Entry(self.register, show="*", width=30)
        self.registerPassword.grid()

        self.registerPasswordShow = Label(self.register, name="registerPassword", text="Montrer / Cacher")
        self.registerPasswordShow.grid()
        self.registerPasswordShow.bind("<Button-1>", lambda event: self.toggleShowField(event))

        # -> Same password
        Label(self.register, text="Veuillez répéter le mot de passe").grid()
        self.registerSamePassword = Entry(self.register, show="*", width=30)
        self.registerSamePassword.grid()

        self.registerSamePasswordShow = Label(self.register, name="registerSamePassword", text="Montrer / Cacher")
        self.registerSamePasswordShow.grid()
        self.registerSamePasswordShow.bind("<Button-1>", lambda event: self.toggleShowField(event))

        ############# END FORM #############
        bouton_register = Button(self.register, text="Valider !", command=lambda:self.onClickRegister(self.registerEmail.get(), self.registerUsername.get(), self.registerPassword.get(), self.registerSamePassword.get()))
        bouton_register.grid()

        self.registerUser = Label(self.register)
        self.registerUser.grid()

    def checkConn(self):
        if ( n.send("isItWorking") is None ) :
            self.connection.configure(text="Pas connecté", bg="red")
            return False
        else :
            self.connection.configure(text="Connecté", bg="green")
            return True

    def toggleShowField(self, event):
        global conPassword, regPassword, regSamePassword

        if str(event.widget).split(".")[2] == "connectPassword" :
            if conPassword :
                self.password.configure(show="")
            else :
                self.password.configure(show="*")
            
            conPassword = not conPassword

        if str(event.widget).split(".")[2] == "registerPassword" :
            if regPassword :
                self.registerPassword.configure(show="")
            else :
                self.registerPassword.configure(show="*")
            
            regPassword = not regPassword

        if str(event.widget).split(".")[2] == "registerSamePassword" :
            if regSamePassword :
                self.registerSamePassword.configure(show="")
            else :
                self.registerSamePassword.configure(show="*")
            
            regSamePassword = not regSamePassword

    def onClickConnect(self, username, password) :
        try:
            if username is "" :
                self.username.configure(bg="red")
                self.password.configure(bg="white")
                raise Exception("Le username est vide")
            if password is "" :
                self.username.configure(bg="white")
                self.password.configure(bg="red")
                raise Exception("Le mot de passe est vide")

            self.username.configure(bg="white")
            self.password.configure(bg="white")

            data = "connect///"+username+"///"+password

            response = self.trySendServer(data)

            if response[0] == "500" or response[0] == "2" :
                showerror("Une erreur est survenue", response[1])
            elif response[0] == "3" :
                self.username.configure(bg="red")
                raise Exception("Aucun utilisateur ne correspond")
            else :
                response.pop(0)
                self.toMain(response)

        except Exception as e :
            self.connectError.configure(text=e, bg="red")
            print(e)

    def onClickRegister(self, email, username, password, samepassword) :
        try:
            # Champ manquant
            if email is "" or username is "" or password is "" or samepassword is "":
                raise Exception("Champ manquant")
            
            # Champ invalide
            if not re.search(mail_regex, email) :
                self.registerEmail.configure(bg="red")
                self.registerUsername.configure(bg="white")
                self.registerPassword.configure(bg="white")
                self.registerSamePassword.configure(bg="white")
                raise Exception("Adresse mail invalide (format : \"example.mail@mail.mail\"")
            if len(username) < 4 or len(username) > 16 :
                self.registerEmail.configure(bg="white")
                self.registerUsername.configure(bg="red")
                self.registerPassword.configure(bg="white")
                self.registerSamePassword.configure(bg="white")
                raise Exception("Le nom d'utilisateur doit contenir entre 4 et 16 caractères")
            if len(password) < 6 or len(password) > 16 :
                self.registerEmail.configure(bg="white")
                self.registerUsername.configure(bg="white")
                self.registerPassword.configure(bg="red")
                self.registerSamePassword.configure(bg="white")
                raise Exception("Le mot de passe doit contenir entre 6 et 16 caractères")
            if password != samepassword :
                self.registerEmail.configure(bg="white")
                self.registerUsername.configure(bg="white")
                self.registerPassword.configure(bg="red")
                self.registerSamePassword.configure(bg="red")
                raise Exception("Les mots de passes ne correspondent pas")

            self.registerEmail.configure(bg="white")
            self.registerUsername.configure(bg="white")
            self.registerPassword.configure(bg="white")
            self.registerSamePassword.configure(bg="white")

            data = "register///"+email+"///"+username+"///"+password
            response = self.trySendServer(data)

            if response[0] == "1" or response[0] == "2":
                self.registerError.configure(text=response[1], bg="red")
                self.registerUser.configure(text="", bg=self.orig_color)
            else :
                self.registerError.configure(text="", bg=self.orig_color)
                self.registerUser.configure(text="Votre compte a bien été créé !")
                time.sleep(2)
                response.pop(0)
                self.toMain(response)

        except Exception as e :
            self.registerError.configure(text=e, bg="red")
            print(e)

    def trySendServer(self, data):
        if self.checkConn():
            aled = n.send(data)
            if isinstance(aled, list):
                return aled
            else :
                return aled.split('///')
        else:
            return ["500","La connexion au serveur a échoué"]

    def toMain(self, userData):
        global User

        User = userData

        self.root.withdraw()
        main()

class mainPage:
    def __init__(self,root):
        self.root = root

        ############### Init frames info + rooms ###############
        # -> User's info
        self.user = Frame(self.root)
        self.user.grid(row=1, column=0, columnspan=2, sticky=(W,E), padx=20, pady=20)

        # -> Vertical Separator
        ttk.Separator(self.root, orient=VERTICAL).grid(column=2, row=1, rowspan=1, sticky=NS)

        # -> Room's frame
        self.rooms = Frame(self.root)
        self.rooms.grid(row=1, column=3, columnspan=2, sticky=(W,E), padx=20, pady=20)

        ############### Fill previously created frames ###############
        self.initUser()
        self.initRooms()
        
        # -> Initialize Disconnect button for client
        button_disc = Button(self.root, text="Déconnecter", command=lambda : self.quitter('disc'))
        button_disc.grid(row=3, column=1, padx=20, pady=20)

        # -> Initialize Quit button for client
        button_quit = Button(self.root, text="Quitter", command=lambda : self.quitter('quit'))
        button_quit.grid(row=3, column=2, padx=20, pady=20)

        button_ref_room = Button(self.root, text="Rafraichir", command=lambda : self.initRooms())
        button_ref_room.grid(row=3, column=3, padx=20, pady=20)
        button_room = Button(self.root, text="+", command=lambda : self.createRoom( askstring("Input", "Quel nom à la room ?", parent=self.root) ))
        button_room.grid(row=3, column=4, padx=20, pady=20)

        # -> Save default background color in variable
        self.orig_color = button_quit.cget("background")

    def initUser(self) :
        ############# User's info #############
        # -> Account label
        Label(self.user, text="Compte", font = "Verdana 16 bold").grid()

        # -> Email
        Label(self.user, text="Adresse mail :").grid()
        Label(self.user, text=User[1]).grid()
        
        # -> Username
        Label(self.user, text="Nom de compte").grid()
        Label(self.user, text=User[2]).grid()

    def initRooms(self) :
        global roomsList

        for element in self.rooms.winfo_children() :
            element.destroy()

        ############# User's info #############
        # -> Rooms label
        Label(self.rooms, text="Rooms", font = "Verdana 16 bold").grid()

        # -> Room's list
        self.roomsList = Canvas(self.rooms, width=360, height=100, background="white", scrollregion=(0,0,0,0))
        self.roomsList.grid_columnconfigure(5)
        self.roomsList.grid()

        # -> Receive rooms
        response = self.trySendServer("getRooms///raw")

        if response[0] == "500" :
            showerror("Une erreur est survenue", response[1])
        else :
            try :
                roomsList = response[1:][0]
            except :
                Label(self.rooms, text="No rooms :(").grid()
        
        # -> Utils call rooms => return rooms[]
        if not roomsList :
            Label(self.rooms, text="No rooms :(").grid()
        else :
            for room in roomsList:
                button = Button(self.roomsList, name=room[0], width=64, text=room[0])
                button.bind("<Button-1>", lambda event: self.joinRoom(event))
                button.grid()

        self.roomsList.configure(scrollregion=self.roomsList.bbox("all"))

    def joinRoom(self, event):
        global inRoom

        data = "joinRoom///"+str(event.widget).split('.')[len(str(event.widget).split('.'))-1]+"///"+User[2]

        response = self.trySendServer(data)

        if response[0] == "500" :
            showerror("Une erreur est survenue", response[1])
        elif response[0] == "0":
            inRoom = response[1:]
            self.root.withdraw()
            main()
        else :
            print("SOME ERROR OCCURED")

    def createRoom(self, name):
        global inRoom

        if not name:
            showerror("Une erreur est survenue", "Impossible de créer une room sans nom")
        else :
            data = "createRoom///"+name+"///"+User[2]

            response = self.trySendServer(data)

            if response[0] == "500" :
                showerror("Une erreur est survenue", response[1])
            elif response[0] == "0":
                inRoom = response[1:]
                self.root.withdraw()
                main()
            else :
                print("SOME ERROR OCCURED")

            self.initRooms()

    def checkConn(self):
        if (n.send("isItWorking") is None ) :
            return False
        else :
            return True

    def trySendServer(self, data):
        if self.checkConn():
            aled = n.send(data)
            if isinstance(aled, list):
                return aled
            else :
                return aled.split('///')
        else:
            return ["500","La connexion au serveur a échoué"]

    def quitter(self, com):
        global User

        User = []
        self.root.destroy()

        if com == "disc" : main();
        if com == "quit" : sys.exit();

class gamePage:
    def __init__(self,root):
        global inRoom

        self.root = root

        if inRoom[1] == "1" :
            Label(self.root, text="En attente d'un second joueur\n" + str(inRoom[0]), font = "Verdana 16 bold").grid(padx=20, pady=20)
            data = n.client.recv(2048).decode()
            if data == "GOGOGO":
                self.loadGame()
        else :
            self.loadGame()

        button_quit = Button(self.root, text="Quitter", command=lambda : self.quitRoom())
        button_quit.grid()

        # -> Save default background color in variable
        self.orig_color = self.root.cget("background")
    
    def loadGame(self) :
        global inRoom, User, couleur
        data = "whoAmI///"+inRoom[0]+"///"+User[2]

        response = self.trySendServer(data)

        if response[0] == "500" :
            showerror("Une erreur est survenue", response[1])
        elif response[0] == "0":
            couleur = response[1]

            self.root.destroy()

            main()
        else :
            print("SOME ERROR OCCURED on LOAD")

    def quitRoom(self) :
        global inRoom
        data = "quitRoom///"+inRoom[0]+"///"+User[2]

        response = self.trySendServer(data)

        if response[0] == "500" :
            showerror("Une erreur est survenue", response[1])
        elif response[0] == "0":
            inRoom = []
            self.root.destroy()
            main()
        else :
            print("SOME ERROR OCCURED quit")

    def checkConn(self):
        if (n.send("isItWorking") is None ) :
            return False
        else :
            return True

    def trySendServer(self, data):
        if self.checkConn():
            aled = n.send(data)
            if isinstance(aled, list):
                return aled
            else :
                return aled.split('///')
        else:
            return ["500","La connexion au serveur a échoué"]

def main():
    global inRoom, couleur

    root = Tk()
    root.title("D4 Client")

    if not User:
        root.geometry('680x460')
        conRegPage(root)
    elif User and not inRoom :
        root.geometry('980x440')
        mainPage(root)
    elif User and inRoom and not couleur:
        root.geometry('660x660')
        gamePage(root)
    elif User and inRoom and couleur:
        root.geometry('660x660')
        Plateau(root, couleur, n, User[2], inRoom[0])
    else :
        print("aled")
        sys.exit()

    root.mainloop()
