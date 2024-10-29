from tkinter import *
import random

#the dimensions of your screen
gameWidth=600
gameHeight=600
#higher number will make you snake go faster
#Sets the delay (in milliseconds) between game updates (or frames). Lower values make the snake move faster.
speed=500
#this will change the size of the snake
spaceSize=50
#inital size of the snake
bodyParts=3
#color of the food
foodColor='#eb4034'
#color of the snake
snakeColor="#069116"
#color of the background
backColor='#000000'

#Snake class
class Snake:
    #creating a new object
    #initilizes a new snake
    def __init__(self):
        self.body_size=bodyParts
        #stores the coordinates of the snakes segments
        # A list that will store each segment’s coordinates, starting with each segment at (0,0) initially.
        self.coordinates=[]
        #holds the reference to the rectangles that make up the snake
        self.squares=[]

        #need more explanation
        for i in range(0, bodyParts):
            #add inital parts of the body
            #. It then populates the coordinates list with the BODY_SIZE number of [0, 0]
            #  elements, and uses a loop to create the BODY_SIZE number of rectangles on a canvas
            #  object using the create_rectangle method, with the upper-left corner at (x, y) and 
            # the lower-right corner at (x + SPACE_SIZE, y + SPACE_SIZE)
            self.coordinates.append([0,0])

        #Adds each segment's coordinates (initially [0, 0]), placing them at the top-left corner.
        for x,y in self.coordinates:
            #each of the rectangles is drawn here
            square=canvas.create_rectangle(x,y, x+spaceSize, y+spaceSize, fill=snakeColor, tag="snake")
            # adding each reactangle to the square list. this is the snakes body
            self.squares.append(square)

class Food:
    #food object. initilize food
    def __init__(self):
        #makes the foods position at randion locations within the screen also it make sures the values
        #are intergers
        #This gives the number of potential grid cells in the horizontal and vertical directions.
        #By subtracting 1, the random value stays within the grid cells and does not exceed the game boundary.
        # * spaceSize Converts it to pixel coordinates
        x=random.randint(0, int((gameWidth/spaceSize)-1))*spaceSize 
        y=random.randint(0, int((gameHeight/spaceSize)-1))*spaceSize

        #set the coordinates of the food
        self.coordinates =[x,y]

        #then draw that on the screen
        #set coordinates and specify the sizes
        canvas.create_oval(x,y, x+spaceSize, y+spaceSize, fill=foodColor, tag="food")

#two arguments snake, food
def next_turn(snake, food):
    #the x and y we will use later on
    #getting the x and y of the snakes head
    x, y=snake.coordinates[0]

    #changing the direction of the snake based of the 
    #Adjusts the head position of the snake based on the current direction.
    if direction =="up":
        #spaceSize sort up represent the each cell in the screen
        y-=spaceSize
    elif direction == "down":
        y+=spaceSize
    elif direction == "left":
        x-=spaceSize
    elif direction == "right":
        x+=spaceSize

    
    #Inserts the new head position at the front of the coordinates list.
    #This makes the first segment of the snake move to this new position, while the rest of the segments shift to follow the head.
    #The new x and y coordinates are then inserted at the beginning of the coordinates list of the snake object.
    snake.coordinates.insert(0,(x,y))
    
    #Creates a rectangle at the new head position and adds it to the squares list.
    #A new square is created on the canvas at the updated position of the head
    #The new rectangle with new postion is added to square list
    square=canvas.create_rectangle(x,y, x+spaceSize, y+spaceSize, fill=snakeColor)
    snake.squares.insert(0, square)


    #Checks to see if it is eating the food

    #    Creates a rectangle at the new head position and adds it to the squares list.
    # Checks if the snake's head coordinates match the food coordinates. If they match, the score is increased, and a new food item is created. If not, the tail of the snake is removed, maintaining the same length.
    if x== food.coordinates[0] and y==food.coordinates[1]:
        global score

        score+=1
        #update score
        label.config(text="Score:{}".format(score))
        #the old food is deleted
        canvas.delete("food")
        #new food is displayed on the canvas
        food=Food()
    else:
        #If the snake did not eat food, the last segment (tail) is removed:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    #Calls check_coll() to see if the snake has collided with itself or the borders of the window. If so, game_over() is called.
    if check_coll(snake):
        game_over()
    else:
        #Uses window.after() to call next_turn again after the specified speed.
        #At the end of next_turn, the function calls itself with a delay set by the speed variable:
        #This creates a continuous loop where next_turn updates the snake’s position at regular intervals, making it appear as though the snake is moving forward automatically.
        window.after(speed, next_turn, snake, food)


def change_dir(new_direction):
    #Changes the direction of the snake based on key presses, ensuring the snake cannot reverse direction directly (e.g., it can't go left if it's currently going right).
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
    #x and y coordinates of the head of the snake (the first element in the coordinates list of the snake object).
    x,y=snake.coordinates[0]
    #Checks if the snake's head goes out of bounds (negative coordinates or exceeding the width/height).
    #x coordinate is less than zero or greater than or equal to the value 
    # of the WIDTH constant, or if the y coordinate is less than zero or greater than or
    #  equal to the value of the HEIGHT constant
    if x<0 or x>=gameWidth:
        #print("Game Over")
        return True

    elif y<0 or y>=gameHeight:
        #print("Game Over")
        return True
    #Iterates through the rest of the snake's body to check if the head has collided with any part of its own body
    #for loop to iterate over the elements of the coordinates list of the snake object,
    #  starting from the second element (snake.coordinates[1:]).
    #the function checks if the x and y coordinates of the element are the same as the x and y coordinates 
    # of the head of the snake
    for body_part in snake.coordinates[1:]:
        if x== body_part[0] and y == body_part[1]:
            return True
    #or else return false saying it has not collided
    return False

#Clears the canvas and displays a "Game Over" message in the center of the window.
def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=('consolas', 70), text="Game Over", fill="red", tag="gameover")

#Tk object and setting the window title. It then initializes the score to zero and the direction of the snake to ‘down’.
window=Tk()
window.title("Snake Game")
window.resizable(False,False)

score=0

#by default the snake moves downward since that what we set here 
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

#Runs the next_turn function
next_turn(snake, food)

window.mainloop()