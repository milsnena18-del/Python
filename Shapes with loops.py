import turtle
screen=turtle.Screen()
screen.bgcolor("light blue")
pen=turtle.Turtle()
pen.color("purple")
for i in range(9):
    pen.forward(80)
    pen.left(360/9)

screen.mainloop()





