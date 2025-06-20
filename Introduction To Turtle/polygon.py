import turtle

turtle.Screen().bgcolor("Grey")
turtle.Screen().setup(300,400)
polygon = turtle.Turtle()

num_sides = 7
side_length = 60

angle = 360./num_sides

for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)

turtle.done()