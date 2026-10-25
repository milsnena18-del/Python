import turtle
screen=turtle.Screen()
screen.bgcolor("light yellow")
pen=turtle.Turtle()
pen.color("pink")
pen.speed(0)
pen.width(4)
for i in range(5):
    for i in range(8):
        pen.forward(80)
        pen.left(360/8)
    pen.left(360/5)



 