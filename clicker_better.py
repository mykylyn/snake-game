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
    ShowInfo["text"] = "You Clicked " + str(number) + " times."
    
    if number>5:
        Btn5.pack()
        
        

def ClickBtn5():
    global number
    #shorcut to increase by 1
    number+=5
    ShowInfo["text"] = "You Clicked " + str(number) + " times."

    if number>20:
        Btn20.pack()


#command tells it to execute which code when it is clicked
ClickingButton = Button(window,text="+1", padx=50, pady=50, bg="gold", font=("Arial, 22"), command=ClickBtn)
ShowInfo = Label(window, text="message", font=("Arial, 20"), fg="purple", pady=20)

Btn5 = Button(window,text="Increase by 5", padx=50, pady=50, bg="gold", font=("Arial, 22"), command=ClickBtn5)
Btn20 = Button(window,text="Increase by 20", padx=50, pady=50, bg="gold", font=("Arial, 22"), command=ClickBtn5)
ClickingButton.pack()
ShowInfo.pack()
window.mainloop()