# SpiralMyName.py - prints a colorful spiral of the user's name

import turtle               # Set up turtle graphics
t = turtle.Pen()
turtle.bgcolor("black")
colors = ["red", "yellow", "blue", "green", "orange", "purple", "white", "gray"]

# Ask the user's name using turtle's texttinput pop-up window
your_name = turtle.textinput("Enter your name", "What is your name?")
sides = int(turtle.numinput("Number of sides",
                             "How many sides do you want (1-8)?", 4, 1, 8))

# Draw a spiral of the name on the screen, written 150 times
for x in range(100):
    t.pencolor(colors[x%sides]) # Rotate through the four colors
    t.penup()               # Don't draw the regular spiral lines
    t.forward(x*2)          # Just move the turtle on the screen
    t.pendown()             # Write the user's name, bigger each time
    t.write(your_name, font = ("Arial", int( (x + sides) / sides), "bold") )
    t.right(360/sides+2)              # Turn left, just as in our other spirals
