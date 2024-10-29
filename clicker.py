from tkinter import *
#says to import everything from tkinter

window=Tk()

window.geometry("300x300")

window.title("Button Clicker")

number=0


def ClickBtn():
    global number
    #shorcut to increase by 1
    number+=1
    #saying to change the text inside of the ShowInfo label
    ShowInfo["text"] = "You Clicked " + str(number) + " times."

#command tells it to execute which code when it is clicked
ClickingButton = Button(window,text="Click Me!", padx=30, pady=30, bg="gold", font=("Arial, 22"), command=ClickBtn)
ShowInfo = Label(window, text="message", font=("Arial, 20"), fg="purple", pady=20)
ClickingButton.pack()
ShowInfo.pack()
window.mainloop()