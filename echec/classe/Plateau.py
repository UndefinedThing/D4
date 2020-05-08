from tkinter import *
import classe
from classe import Pieces
from PIL import ImageTk, Image


class Plateau:
    """
        -plateau
    """

    def __init__(self, window):
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
        self.tourBA = Pieces.Tour('blanc', 25,25); self.plateau.create_image(self.tourBA.positionX ,self.tourBA.positionY, image = self.tourBA.image )
        self.tourBH = Pieces.Tour('blanc', 375,25); self.plateau.create_image(self.tourBH.positionX ,self.tourBH.positionY, image = self.tourBH.image )
        
        "Cavalier"
        self.cavalierBB = Pieces.Cavalier('blanc',75,25); self.plateau.create_image(self.cavalierBB.positionX ,self.cavalierBB.positionY, image = self.cavalierBB.image )
        self.cavalierBG = Pieces.Cavalier('blanc',325,25); self.plateau.create_image(self.cavalierBG.positionX ,self.cavalierBG.positionY, image = self.cavalierBG.image )
        
        "Fou"
        self.fouBC = Pieces.Fou('blanc',125,25); self.plateau.create_image(self.fouBC.positionX ,self.fouBC.positionY, image = self.fouBC.image )
        self.fouBF = Pieces.Fou('blanc',275,25); self.plateau.create_image(self.fouBF.positionX ,self.fouBF.positionY, image = self.fouBF.image )

        "Reine/Roi"
        self.reineB = Pieces.Reine('blanc',175,25); self.plateau.create_image(self.reineB.positionX ,self.reineB.positionY, image = self.reineB.image )
        self.roiB = Pieces.Roi('blanc',225,25); self.plateau.create_image(self.roiB.positionX ,self.roiB.positionY, image = self.roiB.image )

        "Pion"
        self.pionBA = Pieces.Pion('blanc',25,75); self.plateau.create_image(self.pionBA.positionX ,self.pionBA.positionY, image = self.pionBA.image)
        self.pionBB = Pieces.Pion('blanc',75,75); self.plateau.create_image(self.pionBB.positionX ,self.pionBB.positionY, image = self.pionBB.image)
        self.pionBC = Pieces.Pion('blanc',125,75); self.plateau.create_image(self.pionBC.positionX ,self.pionBC.positionY, image = self.pionBC.image)
        self.pionBD = Pieces.Pion('blanc',175,75); self.plateau.create_image(self.pionBD.positionX ,self.pionBD.positionY, image = self.pionBD.image)
        self.pionBE = Pieces.Pion('blanc',225,75); self.plateau.create_image(self.pionBE.positionX ,self.pionBE.positionY, image = self.pionBE.image)
        self.pionBF = Pieces.Pion('blanc',275,75); self.plateau.create_image(self.pionBF.positionX ,self.pionBF.positionY, image = self.pionBF.image)
        self.pionBG = Pieces.Pion('blanc',325,75); self.plateau.create_image(self.pionBG.positionX ,self.pionBG.positionY, image = self.pionBG.image)
        self.pionBH = Pieces.Pion('blanc',375,75); self.plateau.create_image(self.pionBH.positionX ,self.pionBH.positionY, image = self.pionBH.image)

        "=================================================================NOIR==================================================================================="
    
        "Tour"
        self.tourN1 = Pieces.Tour('noir', 25,375); self.plateau.create_image(self.tourN1.positionX ,self.tourN1.positionY, image = self.tourN1.image )
        self.tourN2 = Pieces.Tour('noir', 375,375); self.plateau.create_image(self.tourN2.positionX ,self.tourN2.positionY, image = self.tourN2.image )

        "Cavalier"
        self.cavalierN1 = Pieces.Cavalier('noir',75,375); self.plateau.create_image(self.cavalierN1.positionX ,self.cavalierN1.positionY, image = self.cavalierN1.image )
        self.cavalierN2 = Pieces.Cavalier('noir',325,375); self.plateau.create_image(self.cavalierN2.positionX ,self.cavalierN2.positionY, image = self.cavalierN2.image )

        "Fou"
        self.fouN1 = Pieces.Fou('noir',125,375); self.plateau.create_image(self.fouN1.positionX ,self.fouN1.positionY, image = self.fouN1.image )
        self.fouN2 = Pieces.Fou('noir',275,375); self.plateau.create_image(self.fouN2.positionX ,self.fouN2.positionY, image = self.fouN2.image )

        "Reine/Roi"
        self.reineN = Pieces.Reine('noir',175,375); self.plateau.create_image(self.reineN.positionX ,self.reineN.positionY, image = self.reineN.image )
        self.roiN = Pieces.Roi('noir',225,375); self.plateau.create_image(self.roiN.positionX ,self.roiN.positionY, image = self.roiN.image )

        "Pion"
        self.pionNA = Pieces.Pion('noir',25,325); self.plateau.create_image(self.pionNA.positionX ,self.pionNA.positionY, image = self.pionNA.image)
        self.pionNB = Pieces.Pion('noir',75,325); self.plateau.create_image(self.pionNB.positionX ,self.pionNB.positionY, image = self.pionNB.image)
        self.pionNC = Pieces.Pion('noir',125,325); self.plateau.create_image(self.pionNC.positionX ,self.pionNC.positionY, image = self.pionNC.image)
        self.pionND = Pieces.Pion('noir',175,325); self.plateau.create_image(self.pionND.positionX ,self.pionND.positionY, image = self.pionND.image)
        self.pionNE = Pieces.Pion('noir',225,325); self.plateau.create_image(self.pionNE.positionX ,self.pionNE.positionY, image = self.pionNE.image)
        self.pionNF = Pieces.Pion('noir',275,325); self.plateau.create_image(self.pionNF.positionX ,self.pionNF.positionY, image = self.pionNF.image)
        self.pionNG = Pieces.Pion('noir',325,325); self.plateau.create_image(self.pionNG.positionX ,self.pionNG.positionY, image = self.pionNG.image)
        self.pionNH = Pieces.Pion('noir',375,325); self.plateau.create_image(self.pionNH.positionX ,self.pionNH.positionY, image = self.pionNH.image)
        
