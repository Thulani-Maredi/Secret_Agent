# Drawing a turtle using different turtle function
# mrdthu003
# 01 August 2024

import turtle

t = turtle
t.speed(3)
t.mode("logo")
t.shape("turtle")

# face turtle in correct position
t.setheading(90)
# Draw the shell (pentagon)  
t.fillcolor("brown")  
t.begin_fill()  
for _ in range(5):
    t.forward(150)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(150)
    t.right(90)
    t.forward(50)
    t.right(90) 
    t.forward(150)  
    t.right(72)  
t.end_fill()  
  
# Draw the head (oval) 

t.forward(100)
t.left(90)
t.fillcolor("green")  
t.begin_fill()  
t.circle(30, 180)  
t.end_fill()  
  
# Draw the eyes (circles)  
t.penup()  
t.goto(50, 20)  
t.pendown()  
t.fillcolor("black")  
t.begin_fill()  
t.circle(5)  
t.end_fill()  
  
t.penup()  
t.goto(80, 20)  
t.pendown()  
t.fillcolor("black")  
t.begin_fill()  
t.circle(5)  
t.end_fill()
t.penup()

# Write message above turtle
t.goto(-50, 100)  
turtle.write("Hello, my name is Thulani the Turtle", align='left', font=('Arial', 14, 'normal'))
t.hideturtle()
t.done()


  




