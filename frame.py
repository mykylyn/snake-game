import tkinter as tk


#Frame are basically containers for other widgets
#Frame becomes master attribute


#multiple effects
#tk.FLAT
#tk.SUNKEM
#tk.RAISED
#tk.GROOVE
#tk.RIDGE

window=tk.Tk()

frame_a=tk.Frame()
frame_b=tk.Frame()

label_a=tk.Label(master=frame_a, text="I am inside A", relief=tk.GROOVE)
label_a.pack()
label_b=tk.Label(master=frame_b, text="I am inside B")
label_b.pack()


#can change the order
frame_a.pack()
frame_b.pack()

window.mainloop()