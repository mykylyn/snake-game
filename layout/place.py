import tkinter as tk

window=tk.Tk()

frame=tk.Frame(master=window, width=150, height=150)
frame.pack()

label1=tk.Label(master=frame, text="I am at (0,9)", bg="red")
label1.place(x=0,y=9)

label2=tk.Label(master=frame, text="I am at (75,70)", bg="blue")
#isn't responsive
label2.place(x=70, y=75)

window.mainloop()