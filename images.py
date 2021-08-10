from tkinter import *
from PIL import Image, ImageTk  # pip install pillow
App = Tk()
App.title('App')
App.iconbitmap(r'iconss.ico')  # making a row string

img = ImageTk.PhotoImage(Image.open(r'Img1.png'))
lbl = Label(App, image=img)
lbl.pack()

App.mainloop()