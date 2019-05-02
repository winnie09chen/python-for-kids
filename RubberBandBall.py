import turtle
turtle.delay(0)
turtle.speed(0)
turtle.tracer(0, 0)
t = turtle.Pen()
turtle.bgcolor("black")
# You can choose between 2 and 6 sides for some cool shapes!
sides = eval(input("Enter a number of sides between 2 and 6: "))
colors = ["red", "yellow", "blue", "orange", "green", "purple"]
for x in range(360):
    t.pencolor(colors[x%sides])
    t.forward(x * 3/sides + x)
    t.left(360/sides + 1)
    t.width(x*sides/200)
    t.left(90)
input("Do you want to close? ")          
