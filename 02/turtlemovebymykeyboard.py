Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> def drill_movew():
	turtle.setheading(90)
	turtle.forward(50)
	turtle.stamp()

>>> def drill_movea():
	turtle.setheading(180)
	turtle.forward(50)
	turtle.stamp()

	
>>> def drill_moves():
	turtle.setheading(270)
	turtle.forward(50)
	turtle.stamp()

>>> def drill_moved():
	turtle.setheading(0)
	turtle.forward(50)
	turtle.stamp()

	
>>> turtle.onkey(drill_movew, 'w')
>>> turtle.onkey(drill_movea, 'a')
>>> turtle.onkey(drill_moves, 's')
>>> turtle.onkey(drill_moved, 'd')
>>> turte.listen()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    turte.listen()
NameError: name 'turte' is not defined
>>> turtle.listen()
>>> def restart():
	turtle.reset()

	
>>> turtle.shape('turtle')
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    turtle.shape('turtle')
  File "<string>", line 5, in shape
turtle.Terminator
>>> turtle.shape('turtle')
>>> turtle.shape('turtle')
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    turtle.shape('turtle')
  File "<string>", line 5, in shape
turtle.Terminator
>>> turtle.onkey(restart,'Escape')
>>> turtle.shape('turtle')
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    turtle.shape('turtle')
  File "<string>", line 5, in shape
turtle.Terminator
>>> turtle.shape('turtle')
>>> turtle.onkey(drill_movew, 'w')
>>> turtle.onkey(drill_movea, 'a')
>>> turtle.onkey(drill_moves, 's')
>>> turtle.onkey(drill_moved, 'd')
>>> turtle.onkey(restart,'Escape')
>>> turtle.listen()
>>> Exception ignored in: 