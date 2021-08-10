from tkinter import *

App = Tk()
App.geometry('300x250')
App['background']='black'
menu_ch = StringVar()
options = ['Red', 'White', 'Green', 'Pink', 'Purple']
#menu = OptionMenu(App, menu_ch, 'Red', 'White', 'Green', 'Pink', 'Purple')
menu = OptionMenu(App, menu_ch, *options)
menu.pack()
menu_ch.set('white')
def show():
    msg = Label(App, text='         ',background=(menu_ch.get()).lower())
    msg.pack()
B = Button(App, text='Show', command=show, background='white', foreground='black')
B.pack()
App.mainloop()