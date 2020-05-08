from tkinter import *
from PIL import ImageTk, Image
import classe
from classe import Plateau

window = Tk()
window.title("jeux d'echec")
window.geometry("1080x720")

plateau = Plateau.Plateau(window)



window.mainloop()
