#how to import turtle
from turtle import *

#how to name your turtle
t = Turtle()

#making your turtle go forward
t.fd(50)

#making your turtle turn to the right
t.rt(90)

#when your turtle moves now, it wont draw anything
t.pu()

#making your turtle move backwards
t.bk(150)

#making your turtle turn to the left
t.lt(90)

#when your turtle moves now, it can draw
t.pd()

#move your turtle to an x and y position on the grid
t.goto(-100, -100)

#without this, the screen will close once all events are done(this keeps the window open)
mainloop()
