# RosetteGoneWild.py
import turtle
t = turtle.Pen()
turtle.bgcolor("black")

# Ask the user for the number of circles in their rosette, default to 6
number_of_circles = 18
t.pencolor("yellow")
for x in range(number_of_circles):
    t.circle(80)
    t.left(360/number_of_circles)
t.pencolor("orange")
for x in range(number_of_circles):
    t.circle(130)
    t.left(360/number_of_circles)
