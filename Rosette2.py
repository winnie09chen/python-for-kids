# Rosette.py
import turtle
t = turtle.Pen()
colors = ["red", "pink", "blue", "purple", "yellow", "green"]
for x in range (6):
    t.pencolor(colors[x%6])
    t.circle(100)
    t.left(60)
