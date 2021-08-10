# Dice Roller
from tkinter import *

App = Tk()
App.title("Dice Roller")
App['background']='black'
# Dice unicode characters dictionary
Dice = {
    0 : '🎲',
    1 : '⚀',
    2 : '⚁',
    3 : '⚂',
    4 : '⚃',
    5 : '⚄',
    6 : '⚅'
}

# First dice character to show when the app starts
lbl = Label(App, text=Dice[0], font=('Times', 100), foreground='white',background='black')
lbl.grid(row=0, column=0, padx=40)


# Choose number from 1 - 6 randomly and display it
def roll():
    from random import randint
    dice_choice = randint(1, 6)

    dice_lbl = Label(App, text=Dice[dice_choice], font=('Times', 100), width=2, foreground='white',background='black')
    dice_lbl.grid(row=0, column=0, padx=40)


# Roll button
roll_button = Button(App, text='Roll', command=roll,background = 'white', foreground = 'black',relief='raised')
roll_button.grid(pady=10)

App.mainloop()