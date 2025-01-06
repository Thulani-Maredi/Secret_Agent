# Program To write the initials of my name 
# Maredi Thulani 
# mrdthu003
# 23 April 2024

import turtle

turtle.shape("turtle")

# Make turtle to be at the centre
turtle.penup()
turtle.left(90)
turtle.forward(150)
turtle.right(90)

# Write the first initial "T" in pen color magenta
turtle.pendown()
turtle.pencolor("magenta")
turtle.back(200)
turtle.forward(100)
turtle.right(90)
turtle.forward(200)

# MOVE to wite the second initial
turtle.penup()
turtle.left(90)
turtle.forward(150)

# Write the second intial "M" but in the pen color red
turtle.pendown()
turtle.pencolor("red")
turtle.left(90)
turtle.forward(200)
turtle.right(150)
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.right(150)
turtle.forward(200)

turtle.exitonclick()
