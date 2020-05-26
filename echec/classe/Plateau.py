from tkinter import *
from tkinter.messagebox import showinfo
import classe
from classe import Pieces
from PIL import ImageTk, Image
from collections import OrderedDict


class Plateau:
    """
        -plateau
    """

    def __init__(self, window):
        self.window = window
        self.firstClick = True
        self.plateau = Canvas(window, width =400, height =400, bg ='white')
        self.plateau.delete(ALL)
        self.plateau.pack()
        self.quiJoue = "blanc"

        for l in range(0, 8):
            for c in range(0, 8):
                if (l+c)%2 == 0:
                    fill = 'black'
                else:
                    fill = 'white'
                self.plateau.create_rectangle(l*50,c*50,l*50+50,c*50+50,fill=fill)

        "=================================================================BLANC==================================================================================="
        
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

        "=================================================================NOIR==================================================================================="
    
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
        
        self.dicoJeux = {0:self.tourBA,1:self.cavalierBB,2:self.fouBC,3:self.reineB,4:self.roiB,5:self.fouBF,6:self.cavalierBG,7:self.tourBH,
                         8:self.pionBA,9:self.pionBB,10:self.pionBC,11:self.pionBD,12:self.pionBE,13:self.pionBF,14:self.pionBG,15:self.pionBH,
                         48:self.pionNA,49:self.pionNB,50:self.pionNC,51:self.pionND,52:self.pionNE,53:self.pionNF,54:self.pionNG,55:self.pionNH,
                         56:self.tourNA,57:self.cavalierNB,58:self.fouNC,59:self.reineN,60:self.roiN,61:self.fouNF,62:self.cavalierNG,63:self.tourNH}
        for i in range(16,48):
            self.dicoJeux[i] = ' '


        self.listPosition= []
        for y in range(0, 8):
            y = y*50+25
            for x in range(0, 8):
                x = x*50+25
                self.listPosition.append([x,y])
        self.pieceSelect = None
        self.creationPlateau(self.dicoJeux)

    def change(self):
        if self.quiJoue == "blanc":
            self.quiJoue = "noir"
        else:
            self.quiJoue = "blanc"

    def select(self, event):
        x = event.x
        y = event.y
        x=event.x%50
        x=(event.x-x)+25
        y=event.y%50
        y=(event.y-y)+25
        listXY = [x,y]
        listXYR = [x,y,'red']
        listXYG = [x,y,'green']
        if self.firstClick == True:
            self.pieceSelect = self.dicoJeux[self.listPosition.index(listXY)]
            if self.pieceSelect == " ":
                pass
            elif self.pieceSelect.couleur != self.quiJoue:
                showinfo("aled", "c'est pas ton tour")
            else:
                lastItem = None
                preshot = self.pieceSelect.preshot(self.dicoJeux, self.listPosition)
                if preshot == None or not(preshot):
                    self.firstClick = True
                    showinfo("aled", "Vous ne pouvez pas jouer cette piece")
                else:
                    self.firstClick = False
                    for item in preshot:
                        self.plateau.create_rectangle(item[0]-25,item[1]-25,item[0]+25,item[1]+25,outline=item[2], width="5")
        else:
            preshot = self.pieceSelect.preshot(self.dicoJeux, self.listPosition)
            if listXYR not in preshot and listXYG not in preshot:
                print('mauvaise case')
                pass
            else:
                self.pieceSelect.setX(x)
                self.pieceSelect.setY(y)
                index = self.listPosition.index(listXY)
                for key, value in self.dicoJeux.items():
                    if value == self.pieceSelect:
                        self.dicoJeux[key] = ' '
                    elif key == index:
                        self.dicoJeux[key] = self.pieceSelect

                self.creationPlateau()
                self.firstClick = True
                roiFound = False
                for key, value in self.dicoJeux.items():
                    if value == self.roiN:
                        roiFound = True
                
                if roiFound == False:
                    showinfo("aled", "le roi est mort")
                self.change()
        
    def creationPlateau(self, newDico = None):
        self.plateau.delete(ALL)
        self.plateau.pack()

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
            else:
                self.plateau.create_image(
                    value.positionX ,
                    value.positionY, 
                    image = value.image)

                
                