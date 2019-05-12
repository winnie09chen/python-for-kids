# Kaleidoscope.py
import random
import turtle
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
colors = ["red", "yellow", "blue", "green", "orange", "purple", "white", "gray"]
for n in range(50):
    sides = random.randint(3,8)
    angle = 360//sides+1
    thick = random.randint(1,6)
    # Generate spirals of random sizes/colors at random locations on the screen
    t.pencolor(random.choice(colors)) # Pick a random color from colors[]
    size = random.randint(10,40)      # Pick a random spiral size from 10 to 40
    # Generate a random (x,y) location on the screen
    x = random.randrange(0,turtle.window_width()//2)
    y = random.randrange(0,turtle.window_height()//2)
    # First spiral
    t.penup()
    t.setpos(x,y)
    t.pendown()
    for m in range(size):
        t.width(thick)
        t.forward(m*2)
        t.left(angle)
    # Second spiral
    t.penup()
    t.setpos(-x,y)
    t.pendown()
    for m in range(size):
        t.width(thick)
        t.forward(m*2)
        t.left(angle)
    # Third spiral
    t.penup()
    t.setpos(-x,-y)
    t.pendown()
    for m in range(size):
        t.width(thick)
        t.forward(m*2)
        t.left(angle)
    # Fourth spiral
    t.penup()
    t.setpos(x,-y)
    t.pendown()
    for m in range(size):
        t.width(thick)
        t.forward(m*2)
        t.left(angle)
    
    
    
