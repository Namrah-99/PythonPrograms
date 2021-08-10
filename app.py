from tkinter import *
from random import randint,choice, sample

App = Tk() # This Tk() class would create app window
#App.title('Random Number Generator')
App.title('Element Picker')
#App.geometry('350x200')
App.geometry('300x150')
App['background']='black'
# Need to create class of label
#Display = Label(App, text='Application Window')
#Display.pack()  # This is to jot Display down into our application
#-------------------------------------------------------------------
#def show_msg():
#    msg = Label(App, text='Have a nice day!')
#    msg.pack()
#B = Button(App, text='Click', command=show_msg)  # Function call only takes name ( No need to suffix it with parenthesis )
#B.pack()
#-------------------------------------------------------------------

#def show_msg():
#    msg = Label(App, text=randint(1,100))
#    msg.pack()
#B = Button(App, text='Generate', command=show_msg)  # Function call only takes name ( No need to suffix it with parenthesis )
#B.pack()
#-------------------------------------------------------------------
#inp = Entry(App)
#inp.pack()
#def pick():
#    INP = (inp.get().split(','))
#    ms = Label(App, text=choice(INP))
#    ms.pack()
#B = Button(App, text='Choose', command=pick)
#B.pack()
#quitB = Button(App, text='Cancel', command=App.quit)
#quitB.pack()

#---------USING GRID SYSTEM TO PLACE WIDGETS/states/Theme colors and fonts/Adding color theme(Hex codes)/ Styling widgets appearance using relief parameter----------------------------------
inp = Entry(App,background = 'white', foreground = 'black')
inp.grid(row=0,column=0,columnspan=2,padx=25,pady=5)

no_choice = IntVar()
# Check Button
#chk = Checkbutton(App, text='Double', variable=no_choice , onvalue=2, offvalue=1)
#chk.deselect()
#chk.grid(row=1,column=0,columnspan=2,padx=25,pady=5)

# Radio Button
#rb1 = Radiobutton(App, text='1', variable=no_choice, value='1')
#rb2 = Radiobutton(App, text='2', variable=no_choice, value='2')
#rb1.grid(row=1,column=0)
#rb2.grid(row=1,column=1)
#rb1.select()
# Slider
sld = Scale(App, from_=1,to=5,variable=no_choice,orient=HORIZONTAL)
sld.grid(row=1,column=0,columnspan=2,padx=25,pady=5)

def pick():
    INP = (inp.get().split(','))

    #if no_choice.get() == 2:
    #    ele = sample(INP,2)
    #    chois = 'Choice : ' + str(ele[0]) + ' ' + str(ele[1])
    #else:
    #    chois = 'Choice : ' + str(choice(INP))
    # for slider the above if condition will be changed
    if no_choice.get() != 1:
        ele = sample(INP,no_choice.get())
        lbl = ''
        for e in ele:
            lbl += ' '+e
        chois = 'Choice :' + str(lbl)
    else:
        chois = 'Choice : ' + str(choice(INP))
    #chois = 'Choice : ' + str(choice(INP))
    OutWin = Toplevel()
    OutWin.title('Output')
    ms = Label(OutWin, text=chois, font=('Courier',12), background = 'white', foreground = 'black', relief='flat', width=25, borderwidth=2)
    # ms width will be set to 25 in case of slider else 13
    ms.grid(row=3,column=0,columnspan=2,padx=25,pady=5)

    if quitB['state'] == DISABLED:   # quitB is a dictionary value inside our globals with the key 'state'
        quitB['state'] = NORMAL

B = Button(App, text='Choose', command=pick,background = 'white', foreground = 'black', relief='raised', borderwidth=3)
B.grid(row=2,column=0,padx=25,pady=5)

quitB = Button(App, text='Cancel', command=App.quit, state = DISABLED, background = 'white', foreground = 'black',relief='raised', borderwidth=3)
quitB.grid(row=2,column=1,padx=25,pady=5)

# Hex codes :
# relief = ['raised','sunken','groove','flat','ridge']

#-------------------------------------------------------------------

App.mainloop()  # This is to display our application window
