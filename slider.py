from tkinter import *

App = Tk()
App.geometry('300x250')
App['background']='black'
sld_val = IntVar()
sld = Scale(App, from_=0, to=100, variable=sld_val, orient=HORIZONTAL, background='black' , foreground='white')
sld.pack()

def show():
    msg = Label(App, text=sld_val.get())
    msg.pack()

B = Button(App, text='Show', command=show, background='white', foreground='black')
B.pack()

App.mainloop()