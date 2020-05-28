from tkinter import *
from tkinter.messagebox import showinfo
import echec.classe
from echec.classe import Pieces
from PIL import ImageTk, Image

import pickle
from tkinter.messagebox import *
from tkinter.simpledialog import *

class Plateau:

    def __init__(self, window, couleur, netConn, username, room):
        self.window = window
        self.myCouleur = couleur
        self.n = netConn
        self.playerName = username
        self.room = room
        self.plateau = Canvas(window, width =400, height =400, bg ='white')
        self.quiJoue = "blanc"
        self.firstClick = True
        self.MortBlanc = {}
        self.MortNoir = {}
        #=================================================================BLANC===================================================================================
        
        "Tour"
        self.tourBA = Pieces.Pieces('tour', 'blanc', 25,25)
        self.tourBH = Pieces.Pieces('tour', 'blanc', 375,25)
        
        "Cavalier"
        self.cavalierBB = Pieces.Pieces('cavalier','blanc',75,25)
        self.cavalierBG = Pieces.Pieces('cavalier','blanc',325,25)
        
        "Fou"
        self.fouBC = Pieces.Pieces('fou','blanc',125,25)
        self.fouBF = Pieces.Pieces('fou','blanc',275,25)

        "Reine/Roi"
        self.reineB = Pieces.Pieces('reine','blanc',175,25)
        self.roiB = Pieces.Pieces('roi','blanc',225,25)

        "Pion"
        self.pionBA = Pieces.Pieces('pion','blanc',25,75)
        self.pionBB = Pieces.Pieces('pion','blanc',75,75)
        self.pionBC = Pieces.Pieces('pion','blanc',125,75)
        self.pionBD = Pieces.Pieces('pion','blanc',175,75)
        self.pionBE = Pieces.Pieces('pion','blanc',225,75)
        self.pionBF = Pieces.Pieces('pion','blanc',275,75)
        self.pionBG = Pieces.Pieces('pion','blanc',325,75)
        self.pionBH = Pieces.Pieces('pion','blanc',375,75)

        #=================================================================NOIR===================================================================================
    
        "Tour"
        self.tourNA = Pieces.Pieces('tour','noir', 25,375)
        self.tourNH = Pieces.Pieces('tour','noir', 375,375)

        "Cavalier"
        self.cavalierNB = Pieces.Pieces('cavalier','noir',75,375)
        self.cavalierNG = Pieces.Pieces('cavalier','noir',325,375)

        "Fou"
        self.fouNC = Pieces.Pieces('fou','noir',125,375);
        self.fouNF = Pieces.Pieces('fou','noir',275,375) 

        "Reine/Roi"
        self.reineN = Pieces.Pieces('reine','noir',175,375)
        self.roiN = Pieces.Pieces('roi','noir',225,375)

        "Pion"
        self.pionNA = Pieces.Pieces('pion','noir',25,325)
        self.pionNB = Pieces.Pieces('pion','noir',75,325)
        self.pionNC = Pieces.Pieces('pion','noir',125,325)
        self.pionND = Pieces.Pieces('pion','noir',175,325)
        self.pionNE = Pieces.Pieces('pion','noir',225,325)
        self.pionNF = Pieces.Pieces('pion','noir',275,325)
        self.pionNG = Pieces.Pieces('pion','noir',325,325)
        self.pionNH = Pieces.Pieces('pion','noir',375,325)
        
        #initialisation du dictionnaire du plateau
        self.dicoJeux = {0:self.tourBA,1:self.cavalierBB,2:self.fouBC,3:self.reineB,4:self.roiB,5:self.fouBF,6:self.cavalierBG,7:self.tourBH,
                         8:self.pionBA,9:self.pionBB,10:self.pionBC,11:self.pionBD,12:self.pionBE,13:self.pionBF,14:self.pionBG,15:self.pionBH,
                         48:self.pionNA,49:self.pionNB,50:self.pionNC,51:self.pionND,52:self.pionNE,53:self.pionNF,54:self.pionNG,55:self.pionNH,
                         56:self.tourNA,57:self.cavalierNB,58:self.fouNC,59:self.reineN,60:self.roiN,61:self.fouNF,62:self.cavalierNG,63:self.tourNH}
        for i in range(16,48):
            self.dicoJeux[i] = ' '

        #Liste des differente position avec coordonnées
        self.listPosition= []
        for y in range(0, 8):
            y = y*50+25
            for x in range(0, 8):
                x = x*50+25
                self.listPosition.append([x,y])
        self.pieceSelect = None

        #Création du plateau
        self.creationPlateau(self.dicoJeux)

    def change(self):
        if self.quiJoue == "blanc":
            self.quiJoue = "noir"
        else:
            self.quiJoue = "blanc"

    def select(self, event):
        if self.quiJoue != self.myCouleur:
            showinfo("aled", "c'est pas ton tour")
        else:
            x = event.x
            y = event.y
            x=event.x%50
            x=(event.x-x)+25
            y=event.y%50
            y=(event.y-y)+25
            listXY = [x,y]
            listXYR = [x,y,'red']
            listXYG = [x,y,'green']
            #Selection de la piece à déplacer
            if self.firstClick == True:
                self.pieceSelect = self.dicoJeux[self.listPosition.index(listXY)]
                if self.pieceSelect == " ":
                    pass
                elif self.pieceSelect.couleur != self.myCouleur:
                    showinfo("aled", "tu es les "+self.myCouleur)
                else:
                    lastItem = None
                    preshot = self.pieceSelect.preshot(self.dicoJeux, self.listPosition)
                    if preshot == None or not(preshot):
                        self.firstClick = True
                        showinfo("aled", "Vous ne pouvez pas déplacer cette piece")
                    else:
                        self.firstClick = False
                        for item in preshot:
                            self.plateau.create_rectangle(item[0]-25,item[1]-25,item[0]+25,item[1]+25,outline=item[2], width="5")
            
            #Selection de la case où déplacer la piece
            else:
                preshot = self.pieceSelect.preshot(self.dicoJeux, self.listPosition)
                if listXYR not in preshot and listXYG not in preshot:
                    pass
                else:
                    self.pieceSelect.setX(x)
                    self.pieceSelect.setY(y)
                    index = self.listPosition.index(listXY)
                    for key, value in self.dicoJeux.items():
                        if value == self.pieceSelect:
                            self.dicoJeux[key] = ' '
                        elif key == index:
                            if self.dicoJeux[key] == ' ':
                                pass
                            elif self.dicoJeux[key].couleur == "blanc":
                                self.MortBlanc[tuple([self.dicoJeux[key].positionX,self.dicoJeux[key].positionY])] = self.dicoJeux[key]
                            elif self.dicoJeux[key].couleur == "noir":
                                self.MortNoir[tuple([self.dicoJeux[key].positionX,self.dicoJeux[key].positionY])] = self.dicoJeux[key]
                            self.dicoJeux[key] = self.pieceSelect

                    self.creationPlateau()
                    self.firstClick = True                
                    if self.roiB in self.MortBlanc.values():
                        showinfo("aled", "le roi Blanc est mort")
                    elif self.roiN in self.MortNoir.values():
                        showinfo("aled", "le roi Noir est mort")
                    self.checkPion()
                    self.change()
                    

    def checkPion(self):
        aled = [0,1,2,3,4,5,6,7,63,62,61,60,59,58,57,56]
        for i in aled:
            if self.dicoJeux[i] != " " and self.dicoJeux[i].type == 'pion':
                self.aled = [self.dicoJeux[i].positionX, self.dicoJeux[i].positionY]
                self.plateau.destroy()
                self.mort = Canvas(self.window, width =400, height =400, bg ='grey')
                self.mort.pack()
                self.mort.bind('<Button-1>', self.changementPieces)
                if self.dicoJeux[i].couleur and self.quiJoue == "blanc":
                    for value in self.MortBlanc.values():
                        self.mort.create_image(
                            value.positionX ,
                            value.positionY, 
                            image = value.image)
                    break
                elif self.dicoJeux[i].couleur and self.quiJoue == "noir":
                    for value in self.MortNoir.values():
                        self.mort.create_image(
                            value.positionX ,
                            value.positionY, 
                            image = value.image)
                    break

    def changementPieces(self, event):
        x = event.x
        y = event.y
        x=event.x%50
        x=(event.x-x)+25
        y=event.y%50
        y=(event.y-y)+25
        listXY = tuple([x,y])
        if listXY in self.MortBlanc.keys():
            self.MortBlanc[listXY].positionX = self.aled[0]
            self.MortBlanc[listXY].positionY = self.aled[1]
            self.dicoJeux[self.listPosition.index(self.aled)] = self.MortBlanc[listXY]
            del self.MortBlanc[listXY]
            self.mort.destroy()
            self.plateau = Canvas(self.window, width =400, height =400, bg ='white')
            self.creationPlateau()

        elif listXY in self.MortNoir:
            self.MortNoir[listXY].positionX = self.aled[0]
            self.MortNoir[listXY].positionY = self.aled[1]
            self.dicoJeux[self.listPosition.index(self.aled)] = self.MortNoir[listXY]
            del self.MortNoir[listXY]
            self.mort.destroy()
            self.plateau = Canvas(self.window, width =400, height =400, bg ='white')
            self.creationPlateau()

    #Fonction pour creer le plateau
    def creationPlateau(self, newDico = None):
        self.plateau.delete(ALL)
        self.plateau.pack()
        self.plateau.bind('<Button-1>', self.select)

        for l in range(0, 8):
            for c in range(0, 8):
                if (l+c)%2 == 0:
                    fill = 'black'
                else:
                    fill = 'white'
                
                self.plateau.create_rectangle(l*50,c*50,l*50+50,c*50+50,fill=fill)
        
        for value in self.dicoJeux.values():
            if value == ' ':
                pass
            elif value.couleur == 'noir':
                self.plateau.create_text(
                    value.positionX ,
                    value.positionY, 
                    text = value.text,
                    font = "Arial 20 bold",
                    fill='red')
            elif value.couleur == 'blanc':
                self.plateau.create_text(
                    value.positionX ,
                    value.positionY, 
                    text = value.text,
                    font = "Arial 20 bold",
                    fill='green')

    def envoie(self):
        data = pickle.dumps(["dataGame", self.room, self.playerName, self.dicoJeux, self.quiJoue, self.MortBlanc, self.MortNoir])

        response = self.trySendServer(data)

        if response[0] == "500" :
            showerror("Une erreur est survenue", response[1])
        elif response[0] == "0":
            # TODO suite
            pass
        else :
            print("SOME ERROR OCCURED send")

    def recep(self):
        brut = self.n.client.recv(2048)
        try :
            data = pickle.loads(brut)
        except :
            data =  brut.decode()

        if data[0] == "0" and data[1] == "boardsInfo":
            # TODO
            pass

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
                