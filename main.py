import os
from tkinter import *


#Games
def redlightgreen():
    os.system('python redlightgreen.py')

def snake():
    os.system('python snake.py')

def spaceinvadors():
    os.system('python Space+Hand.py')

#main screen
def main_screen():
    global main_screen
    screen = Tk()
    screen.geometry("1300x700")
    screen.title("Pixel Wall")
    bg = PhotoImage(file="PW22.png")

    # Show image using label
    #label1 = Label(screen, image=bg)
    #label1.place(x=0, y=0)

    Label(text="Pixel Wall", bg="grey", width="300", font=("Calibri", 13)).pack()

    # Add buttons
    button1 = Button(screen, text="Game1", command=snake)
    button1.pack(pady=20)

    button2 = Button(screen, text="Game2", command=redlightgreen)
    button2.pack(pady=20)

    button3 = Button(screen, text="Game3", command=spaceinvadors)
    button3.pack(pady=20)

    #EXIT
    button3 = Button(screen, text="EXIT")
    button3.pack(pady=20)

    screen.mainloop()


main_screen()
