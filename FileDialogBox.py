from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

App = Tk()
App.title('App')
App.iconbitmap(r'iconss.ico')  # making a row string
def img_select():
    global img
    App.fname = filedialog.askopenfilename(initialdir = 'res', title= 'Select an image', filetypes= (('PNG Images','*.png' ),('ICON Files','*.ico'),('All files','*.*')))
    B.destroy()
    img = ImageTk.PhotoImage(Image.open(App.fname))
    lbl = Label(App, image=img)
    lbl.pack()
B = Button(App, text='View', command=img_select)
B.pack()
App.mainloop()