# SpiralMyName.py - prints a colorful spiral of the user's name

import turtle               # Set up turtle graphics
t = turtle.Pen()
turtle.bgcolor("black")
colors = ["red", "yellow", "blue", "green",]

# Ask the user's name using turtle's texttinput pop-up window
your_name = "Boo"
sides = 4
# Draw a spiral of the name on the screen, written 150 times
x = 0
while x < 100 :
    t.pencolor(colors[x%4]) # Rotate through the four colors
    t.penup()               # Don't draw the regular spiral lines
    t.forward(x*4)          # Just move the turtle on the screen
    t.pendown()             # Write the user's name, bigger each time
    t.write(your_name, font = ("Arial", int( (x + sides) / sides), "bold") )
    t.right(360/sides+2)              # Turn left, just as in our other spirals
    x = x + 1
