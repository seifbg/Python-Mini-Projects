from tkinter import *
import random


#Create Object
game = Tk()

#Game Values
game_values = {
    "0": "Rock",
    "1": "Paper",
    "2": "Scissor"
}

#Functions that we will use later in code
def disable_game():
    rock_button["state"] = "disabled"
    paper_button["state"] = "disabled"
    scissor_button["state"] = "disabled"


def reset_game():
    rock_button["state"] = "active"
    paper_button["state"] = "active"
    scissor_button["state"] = "active"
    player_label.config(text="Player")
    result_label.config(text="")
    computer_label.config(text="Computer")
def isrock():
    gamerand = game_values[str(random.randint(0, 2))]
    if gamerand == "Rock":
        result = "Draw!"
    elif gamerand == "Paper":
        result = "Lost!"
    else:
        result = "Won!"
    player_label.config(text="Rock")
    computer_label.config(text=gamerand)
    result_label.config(text=result)
    disable_game()

def ispaper():
    gamerand = game_values[str(random.randint(0, 2))]
    if gamerand == "Paper":
        result = "Draw!"
    elif gamerand == "Rock":
        result = "Won!"
    else:
        result = "Lost!"
    player_label.config(text="Paper")
    computer_label.config(text=gamerand)
    result_label.config(text=result)
    disable_game()

def isscissor():
    gamerand = game_values[str(random.randint(0, 2))]
    if gamerand == "Scissor":
        result = "Draw!"
    elif gamerand == "Paper":
        result = "Won!"
    else:
        result = "Lost!"
    player_label.config(text="Scissor")
    computer_label.config(text=gamerand)
    result_label.config(text=result)
    disable_game()

#Application Geometry & Title
game.geometry("300x300")
game.title("Rock Paper Scissor")
game.resizable(height=FALSE,width=FALSE)

#Labels, Frames & Buttons
head_label = Label(game,text="Rock Paper Scissor",fg="Brown",font=("Arial", 20)).pack(pady=20)
frame = Frame(game)
frame.pack()
player_label = Label(frame,text="Player",font=10,fg="Green")
vs_label= Label(frame,text="VS",font="normal 10 bold")
computer_label = Label(frame, text="Computer", font=10,fg="Blue")

player_label.pack(side=LEFT)
vs_label.pack(side=LEFT)
computer_label.pack()

result_label = Label(game,text="",font="normal 20 bold",bg="White",width=15,borderwidth=2,relief="solid")
result_label.pack(pady=20)

frame1 = Frame(game)
frame1.pack()

rock_button = Button(frame1,text="Rock",fg="Black",width=5,command=isrock)
paper_button = Button(frame1,text="Paper",fg="Black",width=5,command=ispaper)
scissor_button = Button(frame1,text="Scissor",fg="Black",width=5,command=isscissor)

rock_button.pack(side=LEFT,padx=10)
paper_button.pack(side=LEFT,padx=10)
scissor_button.pack(padx=10)

reset_button = Button(game,text="Reset Game",fg="Red",width=10,command=reset_game)
reset_button.pack(pady=10)

Copyright = Label(game,text="Made by SEIFEDDINE BEN GHARBIA")
Copyright.pack(pady=10)

#Main loop
game.mainloop()
