from tkinter import *

App = Tk()
App.geometry('300x250')

chois = StringVar()
rb1 = Radiobutton(App, text='Option 1', variable=chois, value='RB1 Selected')
rb2 = Radiobutton(App, text='Option 2', variable=chois, value='RB2 Selected')
rb1.deselect()
rb2.deselect()
rb1.pack()
rb2.pack()

def show():
    msg = Label(App, text=chois.get())
    msg.pack()

B = Button(App, text='Show', command=show)
B.pack()

App.mainloop()