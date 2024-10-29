from tkinter import *
import random


gameWidth=600
gameHeight=600
speed=500
spaceSize=50
bodyParts=3
foodColor='#eb4034'
snakeColor="#069116"
backColor='#000000'

class Snake:
    def __init__(self):
        self.body_size=bodyParts
        self.coordinates=[]
        self.squares=[]

        for i in range(0, bodyParts):
            self.coordinates.append([0,0])

        for x,y in self.coordinates:
            square=canvas.create_rectangle(x,y, x+spaceSize, y+spaceSize, fill=snakeColor, tag="snake")
            self.squares.append(square)

class Food:
    #food object
    def __init__(self):
        x=random.randint(0, int((gameWidth/spaceSize)-1))*spaceSize
        y=random.randint(0, int((gameHeight/spaceSize)-1))*spaceSize

        self.coordinates =[x,y]

        canvas.create_oval(x,y, x+spaceSize, y+spaceSize, fill=foodColor, tag="food")

def next_turn(snake, food):
    x, y=snake.coordinates[0]

    if direction =="up":
        y-=spaceSize
    elif direction == "down":
        y+=spaceSize
    elif direction == "left":
        x-=spaceSize
    elif direction == "right":
        x+=spaceSize

    snake.coordinates.insert(0,(x,y))
    

    square=canvas.create_rectangle(x,y, x+spaceSize, y+spaceSize, fill=snakeColor)
    snake.squares.insert(0, square)

    if x== food.coordinates[0] and y==food.coordinates[1]:
        global score

        score+=1
        label.config(text="Score:{}".format(score))
        canvas.delete("food")
        food=Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_coll(snake):
        game_over()
    else:
        window.after(speed, next_turn, snake, food)


def change_dir(new_direction):
    global direction

    if new_direction =="left":
        if direction !="right":
            direction=new_direction

    elif new_direction =="right":
        if direction !="left":
            direction=new_direction
    
    elif new_direction =="up":
        if direction !="down":
            direction=new_direction
    
    elif new_direction =="down":
        if direction !="up":
            direction=new_direction

def check_coll(snake):
    x,y=snake.coordinates[0]

    if x<0 or x>=gameWidth:
        #print("Game Over")
        return True

    elif y<0 or y>=gameHeight:
        #print("Game Over")
        return True

    for body_part in snake.coordinates[1:]:
        if x== body_part[0] and y == body_part[1]:
            return True

    return False

def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=('consolas', 70), text="Game Over", fill="red", tag="gameover")

window=Tk()
window.title("Snake Game")
window.resizable(False,False)

score=0
direction='down'

label=Label(window, text="Score:{}".format(score),font=('consolas',40))
label.pack()

canvas= Canvas(window, bg=backColor, height=gameHeight, width=gameWidth)
canvas.pack()

window.update()
window_width=window.winfo_width()
window_height=window.winfo_height()
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()

x=int((screen_width/2)-(window_width/2))
y=int((screen_height/2)-(window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")


#This is where you look for keypresses and changes direction based of that
window.bind('<Left>', lambda event: change_dir('left'))
window.bind('<Right>', lambda event: change_dir('right'))
window.bind('<Up>', lambda event: change_dir('up'))
window.bind('<Down>', lambda event: change_dir('down'))



snake= Snake()
food= Food()
next_turn(snake, food)

window.mainloop()