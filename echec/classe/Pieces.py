from PIL import ImageTk, Image

class Pieces:
    """
        -image  
        -type
        -couleur
        -positionX
        -positionY
    """

    def __init__(self, type, couleur, positionX, positionY):
        image = Image.open('./image/'+couleur+'/'+type+'.png')
        self.image = ImageTk.PhotoImage(image)
        self.couleur = couleur
        self.type = type
        self.positionX = positionX
        self.positionY = positionY
    
    def setX(self, newX):
        self.positionX = newX
    
    def setY(self, newY):
        self.positionY = newY
    
    def preshot(self, dicoJeux, listPosition):
        #verif Pion
        if self.type == "pion":
            if self.couleur == "blanc":
                if (self.positionY == 75):
                    res = [[self.positionX, self.positionY+50],[self.positionX, self.positionY+100]]
                    for i in range(len(res)):
                        if dicoJeux[listPosition.index(res[i])] == " ":
                            res[i].append('green')
                        elif dicoJeux[listPosition.index(res[i])].couleur == self.couleur:
                            del res[i]
                        else:
                            del res[i+1]
                            res[i].append('red')
                            break
                else:
                    res = [[self.positionX, self.positionY+50]]
                    if dicoJeux[listPosition.index(res[0])] == " ":
                        res[0].append('green')
                    elif dicoJeux[listPosition.index(res[0])].couleur == self.couleur:
                        del res[0]
                    else:
                        del res[0]
                        res[0].append('red')

            else:
                if (self.positionY == 325):
                    res = [[self.positionX, self.positionY-50],[self.positionX, self.positionY-100]]
                    for i in range(len(res)):
                        if dicoJeux[listPosition.index(res[i])] == " ":
                            res[i].append('green')
                        elif dicoJeux[listPosition.index(res[i])].couleur == self.couleur:
                            del res[i]
                        else:
                            res[i].append('red')
                else:
                    res = [[self.positionX, self.positionY-50]]
                    if dicoJeux[listPosition.index(res[0])] == " ":
                        res[0].append('green')
                    elif dicoJeux[listPosition.index(res[0])].couleur == self.couleur:
                        del res[0]
                    else:
                        res[0].append('red')
            
            return res #return

        #verif Tour
        elif self.type == "tour":
            res = []
            Droite = False
            Gauche = False
            Bas = False
            Haut = False
            
            for i in range(1,8): 
                if Droite == False:
                    aled = [self.positionX+i*50, self.positionY]
                    if aled in listPosition :
                        if dicoJeux[listPosition.index(aled)] == " ":
                            aled.append('green')
                            res.append(aled)
                        elif dicoJeux[listPosition.index(aled)].couleur == self.couleur:
                            Droite = True 
                        else:
                            Droite = True 
                            aled.append('red')
                            res.append(aled)
                            
                if Gauche == False:
                    aled = [self.positionX-i*50, self.positionY]
                    if aled in listPosition :
                        if dicoJeux[listPosition.index(aled)] == " ":
                            aled.append('green')
                            res.append(aled)
                        elif dicoJeux[listPosition.index(aled)].couleur == self.couleur:
                            Gauche = True 
                        else:
                            Gauche = True 
                            aled.append('red')
                            res.append(aled)

                if Bas == False:
                    aled = [self.positionX, self.positionY+i*50]
                    if aled in listPosition :
                        if dicoJeux[listPosition.index(aled)] == " ":
                            aled.append('green')
                            res.append(aled)
                        elif dicoJeux[listPosition.index(aled)].couleur == self.couleur:
                            Bas = True 
                        else:
                            Bas = True 
                            aled.append('red')
                            res.append(aled)

                if Haut == False:
                    aled = [self.positionX, self.positionY-i*50]
                    if aled in listPosition :
                        if dicoJeux[listPosition.index(aled)] == " ":
                            aled.append('green')
                            res.append(aled)
                        elif dicoJeux[listPosition.index(aled)].couleur == self.couleur:
                            Haut = True 
                        else:
                            Haut = True 
                            aled.append('red')
                            res.append(aled)
            return res

        #verif Cavalier
        elif self.type == "cavalier":
            res=[]
            aled = [[self.positionX+100, self.positionY+50],
                    [self.positionX+100, self.positionY-50],
                    [self.positionX-100, self.positionY+50],
                    [self.positionX-100, self.positionY-50],
                    [self.positionX+50, self.positionY+100],
                    [self.positionX+50, self.positionY-100],
                    [self.positionX-50, self.positionY+100],
                    [self.positionX-50, self.positionY-100]]
            for item in aled:
                if item in listPosition :
                    if dicoJeux[listPosition.index(item)] == " ":
                        item.append('green')
                        res.append(item)
                    elif dicoJeux[listPosition.index(item)].couleur == self.couleur:
                        pass
                    else:
                        item.append('red')
                        res.append(item)

            return res
        
        #verif Fou
        elif self.type == "fou":
            res = []
            DBD = False # Diagonal Bas Droite
            DHG = False # Diagonal Haut Gauche
            DHD = False # Diagonal Haut Droite
            DBG = False # Diagonal Bas gGauche
            
            for i in range(1,8): 
                if DBD == False:
                    aled = [self.positionX+i*50, self.positionY+i*50]
                    if aled in listPosition :
                        if dicoJeux[listPosition.index(aled)] == " ":
                            aled.append('green')
                            res.append(aled)
                        elif dicoJeux[listPosition.index(aled)].couleur == self.couleur:
                            DBD = True 
                        else:
                            DBD = True
                            aled.append('red')
                            res.append(aled)
                            
                if DHG == False:
                    aled = [self.positionX-i*50, self.positionY-i*50]
                    if aled in listPosition :
                        if dicoJeux[listPosition.index(aled)] == " ":
                            aled.append('green')
                            res.append(aled)
                        elif dicoJeux[listPosition.index(aled)].couleur == self.couleur:
                            DHG = True 
                        else:
                            DHG = True 
                            aled.append('red')
                            res.append(aled)

                if DHD == False:
                    aled = [self.positionX+i*50, self.positionY-i*50]
                    if aled in listPosition :
                        if dicoJeux[listPosition.index(aled)] == " ":
                            aled.append('green')
                            res.append(aled)
                        elif dicoJeux[listPosition.index(aled)].couleur == self.couleur:
                            DHD = True 
                        else:
                            DHD = True
                            aled.append('red')
                            res.append(aled)

                if DBG == False:
                    aled = [self.positionX-i*50, self.positionY+i*50]
                    if aled in listPosition :
                        if dicoJeux[listPosition.index(aled)] == " ":
                            aled.append('green')
                            res.append(aled)
                        elif dicoJeux[listPosition.index(aled)].couleur == self.couleur:
                            DBG = True 
                        else:
                            DBG = True
                            aled.append('red')
                            res.append(aled)
            return res
        
        #verif reine
        elif self.type == "reine":
            res = []
            Droite = False
            Gauche = False
            Bas = False
            Haut = False
            DBD = False # Diagonal Bas Droite
            DHG = False # Diagonal Haut Gauche
            DHD = False # Diagonal Haut Droite
            DBG = False # Diagonal Bas gGauche

            for i in range(1,8):
                #Vertical/horizontal ---------------------------------------------------------------------------------
                if Droite == False:
                    aled = [self.positionX+i*50, self.positionY]
                    if aled in listPosition :
                        if dicoJeux[listPosition.index(aled)] == " ":
                            aled.append('green')
                            res.append(aled)
                        elif dicoJeux[listPosition.index(aled)].couleur == self.couleur:
                            Droite = True 
                        else:
                            Droite = True
                            aled.append('red')
                            res.append(aled)
                            
                if Gauche == False:
                    aled = [self.positionX-i*50, self.positionY]
                    if aled in listPosition :
                        if dicoJeux[listPosition.index(aled)] == " ":
                            aled.append('green')
                            res.append(aled)
                        elif dicoJeux[listPosition.index(aled)].couleur == self.couleur:
                            Gauche = True 
                        else:
                            Gauche = True 
                            aled.append('red')
                            res.append(aled)

                if Bas == False:
                    aled = [self.positionX, self.positionY+i*50]
                    if aled in listPosition :
                        if dicoJeux[listPosition.index(aled)] == " ":
                            aled.append('green')
                            res.append(aled)
                        elif dicoJeux[listPosition.index(aled)].couleur == self.couleur:
                            Bas = True 
                        else:
                            Bas = True 
                            aled.append('red')
                            res.append(aled)

                if Haut == False:
                    aled = [self.positionX, self.positionY-i*50]
                    if aled in listPosition :
                        if dicoJeux[listPosition.index(aled)] == " ":
                            aled.append('green')
                            res.append(aled)
                        elif dicoJeux[listPosition.index(aled)].couleur == self.couleur:
                            Haut = True 
                        else:
                            Haut = True 
                            aled.append('red')
                            res.append(aled)

                #Diagonal ------------------------------------------------------------------------------------
                if DBD == False:
                    aled = [self.positionX+i*50, self.positionY+i*50]
                    if aled in listPosition :
                        if dicoJeux[listPosition.index(aled)] == " ":
                            aled.append('green')
                            res.append(aled)
                        elif dicoJeux[listPosition.index(aled)].couleur == self.couleur:
                            DBD = True 
                        else:
                            DBD = True 
                            aled.append('red')
                            res.append(aled)
                            
                if DHG == False:
                    aled = [self.positionX-i*50, self.positionY-i*50]
                    if aled in listPosition :
                        if dicoJeux[listPosition.index(aled)] == " ":
                            aled.append('green')
                            res.append(aled)
                        elif dicoJeux[listPosition.index(aled)].couleur == self.couleur:
                            DHG = True 
                        else:
                            DHG = True 
                            aled.append('red')
                            res.append(aled)

                if DHD == False:
                    aled = [self.positionX+i*50, self.positionY-i*50]
                    if aled in listPosition :
                        if dicoJeux[listPosition.index(aled)] == " ":
                            aled.append('green')
                            res.append(aled)
                        elif dicoJeux[listPosition.index(aled)].couleur == self.couleur:
                            DHD = True 
                        else:
                            DHD = True 
                            aled.append('red')
                            res.append(aled)

                if DBG == False:
                    aled = [self.positionX-i*50, self.positionY+i*50]
                    if aled in listPosition :
                        if dicoJeux[listPosition.index(aled)] == " ":
                            aled.append('green')
                            res.append(aled)
                        elif dicoJeux[listPosition.index(aled)].couleur == self.couleur:
                            DBG = True 
                        else:
                            DBG = True 
                            aled.append('red')
                            res.append(aled)
            return res
            
        
        #verif Roi
        elif self.type == "roi":
            res = []
            aled = [[self.positionX+50, self.positionY],
                    [self.positionX-50, self.positionY],
                    [self.positionX, self.positionY-50],
                    [self.positionX, self.positionY+50],
                    [self.positionX+50, self.positionY+50],
                    [self.positionX-50, self.positionY-50],
                    [self.positionX+50, self.positionY-50],
                    [self.positionX-50, self.positionY+50]]
            for item in aled:
                if item in listPosition :
                    if dicoJeux[listPosition.index(item)] == " ":
                        item.append('green')
                        res.append(item)
                    elif dicoJeux[listPosition.index(item)].couleur == self.couleur:
                        pass
                    else:
                        item.append('red')
                        res.append(item)
            return res
        return None
            