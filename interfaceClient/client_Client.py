from client_Network import Network
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import re

import sched, time

mail_regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
n = Network()

conPassword = True
regPassword = True
regSamePassword = True

User = []

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

        # -> Aled
        self.button1 = Button(self.root, text='New Window', width=25, command=self.new_window)
        self.button1.grid()
        # -> Initialize Quit button for client
        button_quit = Button(self.root, text="Quitter", command=self.connect.quit)
        button_quit.grid(row=2, column=2, padx=20, pady=20)

        # -> Save default background color in variable
        self.orig_color = button_quit.cget("background")

    ############### METHODS USED ###############
    def initConnect(self):
        Label(self.connect, text="Se connecter").grid()

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
        Label(self.register, text="S'enregister").grid()

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
        if (n.getPos() is None) :
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

            if response[0] == "500" :
                showerror("Une erreur est survenue", response[1])
            else :
                print(response)

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
                self.registerUser.configure(text="Votre compte a bien été créé !\n Vous pouvez maintenant vous connecter")

        except Exception as e :
            self.registerError.configure(text=e, bg="red")
            print(e)

    def trySendServer(self, data):
        if self.checkConn():
            aled = n.send(data)
            return aled.split('///')
        else:
            return ["500","La connexion au serveur a échoué"]

    def new_window(self):
        global User

        User = [1,2,3]

        self.root.withdraw()
        main()

class mainPage:
    def __init__(self,root):
        self.root = root

        Label(self.root, text="Nom de compte").grid()
        
        # -> Initialize Disconnect button for client
        button_quit = Button(self.root, text="Quitter", command=lambda : self.quitter())
        button_quit.grid(row=2, column=2, padx=20, pady=20)

        # -> Initialize Quit button for client
        button_quit = Button(self.root, text="Quitter", command=lambda : self.quitter())
        button_quit.grid(row=2, column=2, padx=20, pady=20)

        # -> Save default background color in variable
        self.orig_color = button_quit.cget("background")

    def quitter(self):
        global User

        User = []
        self.root.destroy()
        main()

def main():
    root = Tk()
    root.title("D4 Client")

    if not User:
        root.geometry('680x440')
        app = conRegPage(root)
    else :
        root.geometry('980x440')
        app = mainPage(root)
        
    root.mainloop()

if __name__ == "__main__":
    main()