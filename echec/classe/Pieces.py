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
