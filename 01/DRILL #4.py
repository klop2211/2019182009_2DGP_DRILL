import turtle

count = 4;
while count > 0:
    turtle.forward(500)
    turtle.left(90)
    count -= 1
while count < 4:
    turtle.forward(100)
    if count % 2 == 0:
        turtle.setheading(90)
    else:
        turtle.setheading(270)
    turtle.forward(500)
    turtle.setheading(0)
    count += 1
turtle.forward(100)
turtle.setheading(90)
while count > 0:
    turtle.forward(100)
    if count % 2 == 0:
        turtle.setheading(180)
    else:
        turtle.setheading(0)
    turtle.forward(500)
    turtle.setheading(90)
    count -= 1

