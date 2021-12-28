import turtle
san= turtle.Turtle()
san.color('red','yellow')
# san.size(6)
san.pensize(1)
# san.penup()
san.speed(15)
san.begin_fill()
for i in range(54):
    san.forward(200)
    san.left(190)
san.end_fill()
san.pendown()
san.forward(200)
san.begin_fill()
for i in range(54):
    san.forward(200)
    san.left(190)
san.end_fill()
# san.forward(100)
# san.left(90)
# san.forward(100)
# san.left(90)
# san.forward(100)
# san.left(90
# san.end_fill()ain
turtle.done()