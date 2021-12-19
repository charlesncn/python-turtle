import turtle
import time

t = turtle. Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.pencolor('green')

a = 0
b = 0

t.speed(890900)
t.penup()
t.goto(0, 200)
t.pendown()

while True:
	t.forward(a)
	t.right(b)
	a+=3
	b+=1
	
	pen1 = t.Turtle()
	pen1.color("red")
	pen1.speed(10000)

	def draw_square():
		for side in range(4):
			pen1.forward(120)
			pen1.right(190)
            
            for side in range(4):
            	pen1.forward(50)
                pen1.right(190)
                
    pen1.penup()
	pen1.back(20)
	pen1.pendown()

	for square in range(80):
		draw_square()
        pen1.forward(50)
        pen1.left(50)
        

	if(b == 180):
		time.sleep(30)
		break
	t.hideturtle()
turtle.done()
