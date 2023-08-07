from tkinter import *
from PIL import  ImageGrab

root = Tk()


def capture():


    im = ImageGrab.grab((100, 50, 1500, 1080))
    im.show('mypic.png')


canvas = Canvas(root, bg='red')
canvas.pack(padx=10, pady=10)

e = Entry(root)

canvas.create_window(canvas.canvasx(100), canvas.canvasy(100), window=e)

Button(root, text='Click a pic', command=capture).pack()

root.mainloop()

