import tkinter as tk

window=tk.Tk()

#changes the title
window.title("Snake Game")

#to change the dimension
window.geometry("300x300")

#to make it non-resiable
#window.resizable(False,False)


#fg controls the font-color
#bg controls background color
label=tk.Label(window, text="hey guys", bg="lightgray",fg="yellow")
label.pack()

#activebg is the color when you click
#activefore the color of the text when you click
button=tk.Button(window, text="Click me", activebackground="lightblue", activeforeground="black")
button.pack()

#Create an Entry widget with selection colors
#text field
#color when you select
entry=tk.Entry(window, selectbackground="lightblue", selectforeground="yellow")
entry.pack()

#the widgets go above the mainloop
window.mainloop()