import turtle
turtle.shape("turtle")
turtle.mode("logo")

sides = int(input("Enter the number of sides:\n"))
length = int(input("Enter the length of sides:\n"))
num = 360/sides
rep = int(input("Enter number of reapeted sides:\n"))
for n in range(rep):
 turtle.left(num)
 for i in range(sides):
    turtle.forward(length)
    turtle.right(num)
    
turtle.exitonclick()