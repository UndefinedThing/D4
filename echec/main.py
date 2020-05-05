from tkinter import *
from PIL import ImageTk, Image

window = Tk()
window.title("jeux d'echec")
window.geometry("1080x720")

plateau = []

plateau = Canvas(window, width =2000, height =2000, bg ='white')
plateau.delete(ALL)
plateau.pack()

for l in range(0, 10):
    for c in range(0, 10):
        if (l+c)%2 == 0:
            fill = 'white'
        else:
            fill = 'black'
        plateau.create_rectangle(l*50,c*50,l*50+50,c*50+50,fill=fill)

tour_blanc = Image.open('./image/blanc/tour.png')
tour_blanc = ImageTk.PhotoImage(tour_blanc)
tour_blanc.width()
plateau.create_image(0,0, image = tour_blanc )



window.mainloop()
