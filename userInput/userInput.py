from tkinter import *

window=Tk()

label=Label(text="Enter your Name")
display=Label(text="")
entry=Entry()
window.geometry("300x300")
window.title("Button Clicker")


def Enter():
    name=entry.get()
    display["text"] = "Your name is "+ str(name)



Return = Button(window,text="Enter", padx=2, pady=2, bg="lightgreen", font=("Arial, 10"), command=Enter)

label.pack()
entry.pack()
Return.pack()
display.pack()


window.mainloop()