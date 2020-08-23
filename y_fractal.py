import turtle as t
t.screensize(800,800)
a = t.Turtle()

a.left(90)
a.penup()
a.backward(100)
a.pendown()
a.speed(100)

def y_fractal(length):		
	if(length<10):	
		return
	else:
		a.forward(length)
		a.left(30)
		y_fractal(3*length/4)	
		a.right(60)
		y_fractal(3*length/4)
		a.left(30)
		a.backward(length)

y_fractal(100)

t.mainloop()
