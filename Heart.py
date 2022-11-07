#Neeraj Gupta
#Draw Heart

import turtle as tu
tu.bgcolor("white")
tu.color("black","red")
def go(x,y):
	tu.penup()
	tu.goto(x,y)
	tu.pendown()
tu.width(4)
tu.seth(45)
tu.begin_fill()
tu.forward(250)
tu.circle(125,180)
tu.right(90)
tu.circle(125,180)
tu.forward(250)
tu.end_fill()

tu.color("white")
go(0,210)
tu.write("I Lovo You",font=("Times New Roman",10,"bold"),align="center")
tu.hideturtle()

tu.done()