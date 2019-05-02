# PolygonOrRosette.py
import turtle
t = turtle.Pen()
turtle.bgcolor("black")
t.pencolor("red")
# Ask the user for the number of sides of circles, default to 6
number = int(turtle.numinput("Number of sides of circles",
            "How many sides of circles in your shape?", 6))
# Ask the user whether they want a polygon or rosette
shape = turtle.textinput("Which shape do you want?",
                         "Enter 'p' for polygon of 'r' for rosette:")
for x in range(number):
    if shape == 'r':         # User selected rosette
        t.circle(100)
    else:                   # Default to polygon
        t.forward(150)
    t.left(360/number)
