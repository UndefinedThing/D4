from PIL import ImageTk, Image

class Tour:
    """
        -image  
        -couleur
        -positionX
        -positionY
    """

    def __init__(self, couleur, positionX, positionY):
        image = Image.open('./image/'+couleur+'/tour.png')
        self.image = ImageTk.PhotoImage(image)
        self.couleur = couleur
        self.positionX = positionX
        self.positionY = positionY

class Cavalier:
    """
        -image  
        -couleur
        -positionX
        -positionY
    """

    def __init__(self, couleur, positionX, positionY):
        image = Image.open('./image/'+couleur+'/cavalier.png')
        self.image = ImageTk.PhotoImage(image)
        self.couleur = couleur
        self.positionX = positionX
        self.positionY = positionY

class Fou:
    """
        -image  
        -couleur
        -positionX
        -positionY
    """

    def __init__(self, couleur, positionX, positionY):
        image = Image.open('./image/'+couleur+'/fou.png')
        self.image = ImageTk.PhotoImage(image)
        self.couleur = couleur
        self.positionX = positionX
        self.positionY = positionY

class Reine:
    """
        -image  
        -couleur
        -positionX
        -positionY
    """

    def __init__(self, couleur, positionX, positionY):
        image = Image.open('./image/'+couleur+'/reine.png')
        self.image = ImageTk.PhotoImage(image)
        self.couleur = couleur
        self.positionX = positionX
        self.positionY = positionY

class Roi:
    """
        -image  
        -couleur
        -positionX
        -positionY
    """

    def __init__(self, couleur, positionX, positionY):
        image = Image.open('./image/'+couleur+'/roi.png')
        self.image = ImageTk.PhotoImage(image)
        self.couleur = couleur
        self.positionX = positionX
        self.positionY = positionY

class Pion:
    """
        -image  
        -couleur
        -positionX
        -positionY
    """

    def __init__(self, couleur, positionX, positionY):
        image = Image.open('./image/'+couleur+'/pion.png')
        self.image = ImageTk.PhotoImage(image)
        self.couleur = couleur
        self.positionX = positionX
        self.positionY = positionY