Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> turtle.forward(100)
>>> turtle.reset()
>>> test = 100
>>> line = 100
>>> for k in range(5):
	turtle.penup()
	turtle.goto(0,-test)
	test = test-100
	turtle.pendown()
	for i in range(5):
		turtle.forward(line)
		for j in range(4):
			turtle.left(90)
			turtle.forward(line)

			
>>> 
