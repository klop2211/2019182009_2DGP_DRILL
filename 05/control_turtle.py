import turtle

def move_w():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()

def move_a():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()
    
def move_s():
    turtle.setheading(270)
    turtle.forward(50)
    turtle.stamp()
    
def move_d():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()


def reset():
    turtle.reset()

turtle.shape('turtle')
turtle.onkey(move_w, 'w')
turtle.listen()
turtle.onkey(move_a, 'a')
turtle.listen()
turtle.onkey(move_s, 's')
turtle.listen()
turtle.onkey(move_d, 'd')
turtle.listen()
turtle.onkey(reset, 'Escape')
turtle.listen()
