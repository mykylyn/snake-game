from tkinter import *
import random

window=Tk()

intro=Label(text="Rock Paper Scissor")
description=Label(text="Enter Rock, Paper, Scissors:")
possible_actions=["rock", "paper", "scissors"]
computer_action=random.choice(possible_actions)


computer=Label(text="")
user=Label(text="")

display=Label(text="")
entry=Entry()
window.geometry("300x300")
window.title("Rock Paper Scissor")


message="none"
user_action=""

def Check():
    global message
    global user_action
    user_action=entry.get()


    if user_action==computer_action:
        message=f"Both player selected {user_action}. It's a tie!"
        #print(f"Both player selected {user_action}. It's a tie!")
    elif user_action =="rock":
        if computer_action == "scissors":
            message="Rock smashes scissors! You win!"
            #print("Rock smashes scissors! You win!")
        else:
            message="Paper covers rock! You lose."
            #print("Paper covers rock! You lose.")

    elif user_action =="paper":
        if computer_action =="rock":
            message="Paper covers the rock! You win!"
            #print("Paper covers the rock! You win!")
        else:
            message="Scissors cuts paper! You lose"
            #print("Scissors cuts paper! You lose")

    elif user_action == "scissors":
        if computer_action=="paper":
            message="Scissors cuts paper! You win!"
            #print("Scissors cuts paper! You win!")

        else:
            message="Rock smashes scissors! You lose."
            #print("Rock smashes scissors! You lose.")
def Enter():
    global computer_action
    global user_action
    Check()
    computer["text"]="The computer choose "+computer_action
    user["text"]="The user choose "+user_action
    display["text"] = message
    computer_action=random.choice(possible_actions)



Return = Button(window,text="Enter", padx=2, pady=2, bg="lightgreen", font=("Arial, 10"), command=Enter)


#fill tells to fill all that parts
#also use expand=True to make it even more responsive
#fill=BOTH. to fill the x and y
#can use place insead of pack


intro.pack(fill=X)
description.pack(fill=X)
entry.pack(fill=X, side=BOTTOM)
Return.pack(fill=X, side=BOTTOM)
computer.pack(fill=X, side=BOTTOM)
user.pack(fill=X, side=BOTTOM)
display.pack(fill=X, side=BOTTOM)


window.mainloop()