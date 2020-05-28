from PIL import ImageTk, Image

import echec

import os

class Pieces:
    """
        -image  
        -type
        -couleur
        -positionX
        -positionY
    """

    def __init__(self, type, couleur, positionX, positionY):
        print('getcwd:      ', os.getcwd())
        print('__file__:    ', __file__)
        print("111111111111111111111111111111111")
        print('./echec/image/'+couleur+'/'+type+'.png')
        image = Image.open('./echec/image/'+couleur+'/'+type+'.png')
        print("222222222222222222222222222222222")
        self.image = ImageTk.PhotoImage(image)
        print("333333333333333333333333333333333")
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
            res = []
            temp = []
            if self.couleur == "blanc":
                temp = [[self.positionX, self.positionY+50],[self.positionX, self.positionY+100], [self.positionX+50, self.positionY+50],[self.positionX-50, self.positionY+50]]
            else:
                temp = [[self.positionX, self.positionY-50],[self.positionX, self.positionY-100], [self.positionX+50, self.positionY-50],[self.positionX-50, self.positionY-50]]

            devant = False
            if temp[0] in listPosition:
                if (self.positionY == 75 or self.positionY == 325):
                        if dicoJeux[listPosition.index(temp[0])] == " ":
                            temp[0].append('green')
                            res.append(temp[0])
                        elif dicoJeux[listPosition.index(temp[0])].couleur == self.couleur:
                            devant = True
                        else:
                            devant = True

                        if devant == True:
                            pass
                        else:
                            if temp[1] in listPosition and dicoJeux[listPosition.index(temp[1])] == " ":
                                temp[1].append('green')
                                res.append(temp[1])
                            elif temp[1] in listPosition and dicoJeux[listPosition.index(temp[1])].couleur == self.couleur:
                                pass
                            else:
                                pass
                else:
                    if dicoJeux[listPosition.index(temp[0])] == " ":
                        temp[0].append('green')
                        res.append(temp[0])
                    elif dicoJeux[listPosition.index(temp[0])].couleur == self.couleur:
                        pass
                    else:
                        pass
            
            for i in range(2,4):
                if temp[i] in listPosition:
                    if dicoJeux[listPosition.index(temp[i])] == " " or dicoJeux[listPosition.index(temp[i])].couleur == self.couleur:
                        pass
                    else:
                        temp[i].append('red')
                        res.append(temp[i])

                        
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
                    temp = [self.positionX+i*50, self.positionY]
                    if temp in listPosition :
                        if dicoJeux[listPosition.index(temp)] == " ":
                            temp.append('green')
                            res.append(temp)
                        elif dicoJeux[listPosition.index(temp)].couleur == self.couleur:
                            Droite = True 
                        else:
                            Droite = True 
                            temp.append('red')
                            res.append(temp)
                            
                if Gauche == False:
                    temp = [self.positionX-i*50, self.positionY]
                    if temp in listPosition :
                        if dicoJeux[listPosition.index(temp)] == " ":
                            temp.append('green')
                            res.append(temp)
                        elif dicoJeux[listPosition.index(temp)].couleur == self.couleur:
                            Gauche = True 
                        else:
                            Gauche = True 
                            temp.append('red')
                            res.append(temp)

                if Bas == False:
                    temp = [self.positionX, self.positionY+i*50]
                    if temp in listPosition :
                        if dicoJeux[listPosition.index(temp)] == " ":
                            temp.append('green')
                            res.append(temp)
                        elif dicoJeux[listPosition.index(temp)].couleur == self.couleur:
                            Bas = True 
                        else:
                            Bas = True 
                            temp.append('red')
                            res.append(temp)

                if Haut == False:
                    temp = [self.positionX, self.positionY-i*50]
                    if temp in listPosition :
                        if dicoJeux[listPosition.index(temp)] == " ":
                            temp.append('green')
                            res.append(temp)
                        elif dicoJeux[listPosition.index(temp)].couleur == self.couleur:
                            Haut = True 
                        else:
                            Haut = True 
                            temp.append('red')
                            res.append(temp)
            return res

        #verif Cavalier
        elif self.type == "cavalier":
            res=[]
            temp = [[self.positionX+100, self.positionY+50],
                    [self.positionX+100, self.positionY-50],
                    [self.positionX-100, self.positionY+50],
                    [self.positionX-100, self.positionY-50],
                    [self.positionX+50, self.positionY+100],
                    [self.positionX+50, self.positionY-100],
                    [self.positionX-50, self.positionY+100],
                    [self.positionX-50, self.positionY-100]]
            for item in temp:
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
                    temp = [self.positionX+i*50, self.positionY+i*50]
                    if temp in listPosition :
                        if dicoJeux[listPosition.index(temp)] == " ":
                            temp.append('green')
                            res.append(temp)
                        elif dicoJeux[listPosition.index(temp)].couleur == self.couleur:
                            DBD = True 
                        else:
                            DBD = True
                            temp.append('red')
                            res.append(temp)
                            
                if DHG == False:
                    temp = [self.positionX-i*50, self.positionY-i*50]
                    if temp in listPosition :
                        if dicoJeux[listPosition.index(temp)] == " ":
                            temp.append('green')
                            res.append(temp)
                        elif dicoJeux[listPosition.index(temp)].couleur == self.couleur:
                            DHG = True 
                        else:
                            DHG = True 
                            temp.append('red')
                            res.append(temp)

                if DHD == False:
                    temp = [self.positionX+i*50, self.positionY-i*50]
                    if temp in listPosition :
                        if dicoJeux[listPosition.index(temp)] == " ":
                            temp.append('green')
                            res.append(temp)
                        elif dicoJeux[listPosition.index(temp)].couleur == self.couleur:
                            DHD = True 
                        else:
                            DHD = True
                            temp.append('red')
                            res.append(temp)

                if DBG == False:
                    temp = [self.positionX-i*50, self.positionY+i*50]
                    if temp in listPosition :
                        if dicoJeux[listPosition.index(temp)] == " ":
                            temp.append('green')
                            res.append(temp)
                        elif dicoJeux[listPosition.index(temp)].couleur == self.couleur:
                            DBG = True 
                        else:
                            DBG = True
                            temp.append('red')
                            res.append(temp)
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
                    temp = [self.positionX+i*50, self.positionY]
                    if temp in listPosition :
                        if dicoJeux[listPosition.index(temp)] == " ":
                            temp.append('green')
                            res.append(temp)
                        elif dicoJeux[listPosition.index(temp)].couleur == self.couleur:
                            Droite = True 
                        else:
                            Droite = True
                            temp.append('red')
                            res.append(temp)
                            
                if Gauche == False:
                    temp = [self.positionX-i*50, self.positionY]
                    if temp in listPosition :
                        if dicoJeux[listPosition.index(temp)] == " ":
                            temp.append('green')
                            res.append(temp)
                        elif dicoJeux[listPosition.index(temp)].couleur == self.couleur:
                            Gauche = True 
                        else:
                            Gauche = True 
                            temp.append('red')
                            res.append(temp)

                if Bas == False:
                    temp = [self.positionX, self.positionY+i*50]
                    if temp in listPosition :
                        if dicoJeux[listPosition.index(temp)] == " ":
                            temp.append('green')
                            res.append(temp)
                        elif dicoJeux[listPosition.index(temp)].couleur == self.couleur:
                            Bas = True 
                        else:
                            Bas = True 
                            temp.append('red')
                            res.append(temp)

                if Haut == False:
                    temp = [self.positionX, self.positionY-i*50]
                    if temp in listPosition :
                        if dicoJeux[listPosition.index(temp)] == " ":
                            temp.append('green')
                            res.append(temp)
                        elif dicoJeux[listPosition.index(temp)].couleur == self.couleur:
                            Haut = True 
                        else:
                            Haut = True 
                            temp.append('red')
                            res.append(temp)

                #Diagonal ------------------------------------------------------------------------------------
                if DBD == False:
                    temp = [self.positionX+i*50, self.positionY+i*50]
                    if temp in listPosition :
                        if dicoJeux[listPosition.index(temp)] == " ":
                            temp.append('green')
                            res.append(temp)
                        elif dicoJeux[listPosition.index(temp)].couleur == self.couleur:
                            DBD = True 
                        else:
                            DBD = True 
                            temp.append('red')
                            res.append(temp)
                            
                if DHG == False:
                    temp = [self.positionX-i*50, self.positionY-i*50]
                    if temp in listPosition :
                        if dicoJeux[listPosition.index(temp)] == " ":
                            temp.append('green')
                            res.append(temp)
                        elif dicoJeux[listPosition.index(temp)].couleur == self.couleur:
                            DHG = True 
                        else:
                            DHG = True 
                            temp.append('red')
                            res.append(temp)

                if DHD == False:
                    temp = [self.positionX+i*50, self.positionY-i*50]
                    if temp in listPosition :
                        if dicoJeux[listPosition.index(temp)] == " ":
                            temp.append('green')
                            res.append(temp)
                        elif dicoJeux[listPosition.index(temp)].couleur == self.couleur:
                            DHD = True 
                        else:
                            DHD = True 
                            temp.append('red')
                            res.append(temp)

                if DBG == False:
                    temp = [self.positionX-i*50, self.positionY+i*50]
                    if temp in listPosition :
                        if dicoJeux[listPosition.index(temp)] == " ":
                            temp.append('green')
                            res.append(temp)
                        elif dicoJeux[listPosition.index(temp)].couleur == self.couleur:
                            DBG = True 
                        else:
                            DBG = True 
                            temp.append('red')
                            res.append(temp)
            return res
            
        
        #verif Roi
        elif self.type == "roi":
            res = []
            temp = [[self.positionX+50, self.positionY],
                    [self.positionX-50, self.positionY],
                    [self.positionX, self.positionY-50],
                    [self.positionX, self.positionY+50],
                    [self.positionX+50, self.positionY+50],
                    [self.positionX-50, self.positionY-50],
                    [self.positionX+50, self.positionY-50],
                    [self.positionX-50, self.positionY+50]]
            for item in temp:
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
            