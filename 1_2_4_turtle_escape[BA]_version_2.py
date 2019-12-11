#import turtle and set its speed and pensize
import turtle as trtl 
franklin = trtl.Turtle()
franklin.speed(0)
franklin.pensize(5)
crash = trtl.Turtle()
crash.shape("turtle")

#import 
# om function so you can randomize maze and colors
import random

#name parts of your maze
wall_size = 20
gap_size = 50
counter = 25
franklin.penup()

#define a thing to make a barrier
def make_barrier():
    franklin.left(90)
    franklin.forward(40)
    franklin.back(40)
    franklin.right(90)

#define a thing to create door
def make_door():
    franklin.penup()
    franklin.forward(gap_size)
    franklin.pendown()

# define a movements for moveable turtle
def go_left():
    crash.setheading(180)
    crash.forward(10)
def go_right():
    crash.setheading(0)
    crash.forward(10)
def go_up():
    crash.setheading(270)
    crash.forward(10)
def go_down():
    crash.setheading(90)
    crash.forward(10)
# create maze and hide your moving turtle
crash.ht()
while (counter >= 0):
    if counter < 21:
        #randomize gap and wall placement
        door = random.randint(gap_size, wall_size - gap_size)
        barrier = random.randint(gap_size, wall_size - gap_size)

        #make colors to be randomly chosen have your walls become those colors
        rad_colors = ["silver", "dark grey", "grey", "dim grey", "black", "light slate grey", "slate grey", "navy", "medium blue", "deep sky blue", "dodger blue", "dark turquoise", "deep pink", "pale violet red", "hot pink", "dark magenta", "medium violet red", "dark violet", "indigo", "medium purple", "chocolate", "sienna", "maroon", "firebrick", "lime", "crimson", "brown", "orange red", "lawn green", "forest green", "dark sea green"]
        color = random.choice(rad_colors)
        franklin.pencolor(color)
        franklin.pendown()

        #based on what is drawn first draw things in a certain order
        if (door > barrier):
            franklin.forward(barrier)
        #make sure it doesnt draw barrier on the last or first few lines in maze
            if (counter <= 19):
                if (counter >= 1):
                    make_barrier()
            franklin.forward(door-barrier)
        #make sure it doesn't create a door on the outer walls of the maze
            if (counter >= 4):
                make_door()
            else:
                franklin.forward(gap_size)
            franklin.forward(wall_size-door-gap_size)
            franklin.left(90)

        
        else:
            franklin.forward(door)
        #make sure it doesn't create a door on the outer walls of the maze
            if (counter >= 3):
                make_door()
            else:
                franklin.forward(gap_size)
            franklin.forward(barrier-door-gap_size)
        #make sure it doesnt draw barrier on the last or first few lines in maze
            if (counter <= 19):
                if (counter >= 1):
                    make_barrier()
            franklin.forward(wall_size-barrier)
            franklin.left(90)
    wall_size += 20
    counter -= 1 

#hide turtle so that the turtle that drew the maze is gone
franklin.ht()

# move your navigator turtle to were the begining of the maze is
xor = franklin.xcor()
yor = franklin.ycor()
crash.penup()
crash.goto(xor,yor)
crash.setheading(90)
crash.forward(20)
crash.left(90)
crash.showturtle()
crash.pendown()

wn = trtl.Screen()
wn.onkeypress(go_down, "Up")
wn.onkeypress(go_up, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")
wn.listen()


#keep the maze on the screen
 
wn.mainloop()
