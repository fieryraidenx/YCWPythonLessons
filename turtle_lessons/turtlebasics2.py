from turtle import *

t = Turtle()
scoreT = Turtle()

#Toggling the turtle's visibility
t.hideturtle()
scoreT.hideturtle()

#Changing the turtle's pen color
t.pencolor("red")
t.fd(100)

#changing fill color
t.fillcolor("blue")

#start and end fill
t.begin_fill()
t.circle(25)
t.end_fill()


#Write text to the screen
scoreT.color("green")
scoreT.write("This is a Test!!!", align="right", font=("Arial", 32, "normal"))


#Clear screen AND reset all turtles(a complete wipe basically)
t.clear()

mainloop()