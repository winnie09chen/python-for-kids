# ArrowDraw.py
import turtle
t = turtle.Pen()
t.speed(0)
t.turtlesize(2,2,2)
action_list = []
def up():
    t.forward(50)
    action_list.append('forward')
def left():
    t.left(90)
    action_list.append('left')
def right():
    t.right(90)
    action_list.append('right')
def undo():
    if len(action_list) > 0:
        action = action_list.pop()
        if action == 'forward':
            orig_color = t.pencolor()
            t.pencolor('white')
            t.backward(50)
            t.pencolor(orig_color)
        elif action == 'left':
            t.right(90)
        else:
            t.left(90)
turtle.onkeypress(undo, "Down")
turtle.onkeypress(up, "Up")
turtle.onkeypress(left, "Left")
turtle.onkeypress(right, "Right")
turtle.listen()
