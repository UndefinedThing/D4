from tkinter import *
import classe
from classe import Pieces
from PIL import ImageTk, Image


class Plateau:
    """
        -plateau
    """

    def __init__(self, window):
        self.firstClick = True
        self.plateau = Canvas(window, width =400, height =400, bg ='white')
        self.plateau.delete(ALL)
        self.plateau.pack()
        for l in range(0, 8):
            for c in range(0, 8):
                if (l+c)%2 == 0:
                    fill = 'black'
                else:
                    fill = 'white'
                self.plateau.create_rectangle(l*50,c*50,l*50+50,c*50+50,fill=fill)

        "=================================================================BLANC==================================================================================="
        
        "Tour"
        self.tourBA = Pieces.Pieces('tour', 'blanc', 25,25); self.plateau.create_image(self.tourBA.positionX ,self.tourBA.positionY, image = self.tourBA.image )
        self.tourBH = Pieces.Pieces('tour', 'blanc', 375,25); self.plateau.create_image(self.tourBH.positionX ,self.tourBH.positionY, image = self.tourBH.image )
        
        "Cavalier"
        self.cavalierBB = Pieces.Pieces('cavalier','blanc',75,25); self.plateau.create_image(self.cavalierBB.positionX ,self.cavalierBB.positionY, image = self.cavalierBB.image )
        self.cavalierBG = Pieces.Pieces('cavalier','blanc',325,25); self.plateau.create_image(self.cavalierBG.positionX ,self.cavalierBG.positionY, image = self.cavalierBG.image )
        
        "Fou"
        self.fouBC = Pieces.Pieces('fou','blanc',125,25); self.plateau.create_image(self.fouBC.positionX ,self.fouBC.positionY, image = self.fouBC.image )
        self.fouBF = Pieces.Pieces('fou','blanc',275,25); self.plateau.create_image(self.fouBF.positionX ,self.fouBF.positionY, image = self.fouBF.image )

        "Reine/Roi"
        self.reineB = Pieces.Pieces('reine','blanc',175,25); self.plateau.create_image(self.reineB.positionX ,self.reineB.positionY, image = self.reineB.image )
        self.roiB = Pieces.Pieces('roi','blanc',225,25); self.plateau.create_image(self.roiB.positionX ,self.roiB.positionY, image = self.roiB.image )

        "Pion"
        self.pionBA = Pieces.Pieces('pion','blanc',25,75); self.plateau.create_image(self.pionBA.positionX ,self.pionBA.positionY, image = self.pionBA.image)
        self.pionBB = Pieces.Pieces('pion','blanc',75,75); self.plateau.create_image(self.pionBB.positionX ,self.pionBB.positionY, image = self.pionBB.image)
        self.pionBC = Pieces.Pieces('pion','blanc',125,75); self.plateau.create_image(self.pionBC.positionX ,self.pionBC.positionY, image = self.pionBC.image)
        self.pionBD = Pieces.Pieces('pion','blanc',175,75); self.plateau.create_image(self.pionBD.positionX ,self.pionBD.positionY, image = self.pionBD.image)
        self.pionBE = Pieces.Pieces('pion','blanc',225,75); self.plateau.create_image(self.pionBE.positionX ,self.pionBE.positionY, image = self.pionBE.image)
        self.pionBF = Pieces.Pieces('pion','blanc',275,75); self.plateau.create_image(self.pionBF.positionX ,self.pionBF.positionY, image = self.pionBF.image)
        self.pionBG = Pieces.Pieces('pion','blanc',325,75); self.plateau.create_image(self.pionBG.positionX ,self.pionBG.positionY, image = self.pionBG.image)
        self.pionBH = Pieces.Pieces('pion','blanc',375,75); self.plateau.create_image(self.pionBH.positionX ,self.pionBH.positionY, image = self.pionBH.image)

        "=================================================================NOIR==================================================================================="
    
        "Tour"
        self.tourN1 = Pieces.Pieces('tour','noir', 25,375); self.plateau.create_image(self.tourN1.positionX ,self.tourN1.positionY, image = self.tourN1.image )
        self.tourN2 = Pieces.Pieces('tour','noir', 375,375); self.plateau.create_image(self.tourN2.positionX ,self.tourN2.positionY, image = self.tourN2.image )

        "Cavalier"
        self.cavalierN1 = Pieces.Pieces('cavalier','noir',75,375); self.plateau.create_image(self.cavalierN1.positionX ,self.cavalierN1.positionY, image = self.cavalierN1.image )
        self.cavalierN2 = Pieces.Pieces('cavalier','noir',325,375); self.plateau.create_image(self.cavalierN2.positionX ,self.cavalierN2.positionY, image = self.cavalierN2.image )

        "Fou"
        self.fouN1 = Pieces.Pieces('fou','noir',125,375); self.plateau.create_image(self.fouN1.positionX ,self.fouN1.positionY, image = self.fouN1.image )
        self.fouN2 = Pieces.Pieces('fou','noir',275,375); self.plateau.create_image(self.fouN2.positionX ,self.fouN2.positionY, image = self.fouN2.image )

        "Reine/Roi"
        self.reineN = Pieces.Pieces('reine','noir',175,375); self.plateau.create_image(self.reineN.positionX ,self.reineN.positionY, image = self.reineN.image )
        self.roiN = Pieces.Pieces('roi','noir',225,375); self.plateau.create_image(self.roiN.positionX ,self.roiN.positionY, image = self.roiN.image )

        "Pion"
        self.pionNA = Pieces.Pieces('pion','noir',25,325); self.plateau.create_image(self.pionNA.positionX ,self.pionNA.positionY, image = self.pionNA.image)
        self.pionNB = Pieces.Pieces('pion','noir',75,325); self.plateau.create_image(self.pionNB.positionX ,self.pionNB.positionY, image = self.pionNB.image)
        self.pionNC = Pieces.Pieces('pion','noir',125,325); self.plateau.create_image(self.pionNC.positionX ,self.pionNC.positionY, image = self.pionNC.image)
        self.pionND = Pieces.Pieces('pion','noir',175,325); self.plateau.create_image(self.pionND.positionX ,self.pionND.positionY, image = self.pionND.image)
        self.pionNE = Pieces.Pieces('pion','noir',225,325); self.plateau.create_image(self.pionNE.positionX ,self.pionNE.positionY, image = self.pionNE.image)
        self.pionNF = Pieces.Pieces('pion','noir',275,325); self.plateau.create_image(self.pionNF.positionX ,self.pionNF.positionY, image = self.pionNF.image)
        self.pionNG = Pieces.Pieces('pion','noir',325,325); self.plateau.create_image(self.pionNG.positionX ,self.pionNG.positionY, image = self.pionNG.image)
        self.pionNH = Pieces.Pieces('pion','noir',375,325); self.plateau.create_image(self.pionNH.positionX ,self.pionNH.positionY, image = self.pionNH.image)
        
        self.dicoJeux = {0:self.tourBA,1:self.cavalierBB,2:self.fouBC,3:self.reineB,4:self.roiB,5:self.fouBF,6:self.cavalierBG,7:self.tourBH,
                         8:self.pionBA,9:self.pionBB,10:self.pionBC,11:self.pionBD,12:self.pionBE,13:self.pionBF,14:self.pionBG,15:self.pionBH,
                         48:self.pionBA,49:self.pionBB,50:self.pionBC,51:self.pionBD,52:self.pionBE,53:self.pionBF,54:self.pionBG,55:self.pionBH,
                         56:self.tourBA,57:self.cavalierBB,58:self.fouBC,59:self.reineB,60:self.roiB,61:self.fouBF,62:self.cavalierBG,63:self.tourBH}
        for i in range(16,48):
            self.dicoJeux[i] = ' '
        
        print(self.dicoJeux)

        self.listPosition= []
        for y in range(0, 8):
            y = y*50+25
            for x in range(0, 8):
                x = x*50+25
                self.listPosition.append([x,y])

        print(self.listPosition)
        self.pieceSelect = None


    def select(self, event):
        if self.firstClick == True:
            self.firstClick = False
            x = event.x
            y = event.y
            x=event.x%50
            x=(event.x-x)+25
            y=event.y%50
            y=(event.y-y)+25
            listXY = [x,y]
            self.pieceSelect = self.dicoJeux[self.listPosition.index(listXY)]
            print(self.pieceSelect.type)
        else:
            x = event.x
            y = event.y
            x=event.x%50
            x=(event.x-x)+25
            y=event.y%50
            y=(event.y-y)+25
            listXY = [x,y]
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
            pass
        
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
                print("ok")
            else:
                self.plateau.create_image(
                    value.positionX ,
                    value.positionY, 
                    image = value.image)
        print(self.dicoJeux)

                
                