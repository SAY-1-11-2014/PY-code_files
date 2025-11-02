import turtle
a = turtle.Screen()
a.bgcolor("red")
a.setup(1000, 900)
turtle.title("Welcome to my project")
draw = turtle.Turtle()
for i in range(4):
    draw.forward(90)
    draw.left(90)