# Ashley Stone
# 07/05/2026
# P4LAB1
# This program uses turtle graphics, a while loop,
# and a for loop to draw a house.

import turtle

# Create window
window = turtle.Screen()
window.bgcolor("lightblue")

# Create turtle
pen = turtle.Turtle()
pen.color("purple")
pen.pensize(4)
pen.speed(5)

# Draw square using a for loop

for side in range(4):
    pen.forward(150)
    pen.left(90)


# Move turtle to draw roof

pen.penup()
pen.goto(0, 150)
pen.pendown()


# Draw triangle roof using a while loop

count = 0

while count < 3:
    pen.forward(150)
    pen.left(120)
    count += 1


# Hide turtle
pen.hideturtle()

# Keep window open
window.mainloop()