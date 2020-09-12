from turtle import *

class ShapeTurtle(Turtle):
    '''We inherit the properties of the Turtle class to create our own Shape Turtle''' 

    def __init__(self, color):
        '''we will use the Turtle's init method, but also change the turtle to hidden and change pen/fill color to what the person desires'''
        Turtle.__init__(self)
        self.ht()
        self.pencolor(color)
        self.fillcolor(color)

    def square(self, l):
        '''Drawing a square(properties: same length on all 4 sides and 4 90 deg angles) and filling it'''
        self.begin_fill()
        for i in range(4):
            self.fd(l)
            self.rt(90)
        self.end_fill()

    def circle(self, r):
        '''here we are redefining the circle method the turtle has in order to make it fill as well'''
        self.begin_fill()
        #we use the super method to reference the ORIGINAL circle method
        super(ShapeTurtle, self).circle(r)
        self.end_fill()

    def rectangle(self, l, w):
        '''Drawing a rectangle(properties: 2 sides with sidelength l and 2 sides with 
        side length w (4 90 deg angles)) and filling it'''
        self.begin_fill()
        for i in range(1, 5):
            #if i is odd, use length, if i is even, use width
            if(i % 2 == 0):
                self.fd(l)
            else:
                self.fd(w)
            self.rt(90)
        self.end_fill()

    def flower(self, r, fnum):
        '''Drawing a flower by using fnum amount of circles with r radius'''
        turnrate = 360/fnum # a flower needs to be 360deg(a circle), so we are seeing by how much we need to turn for each circle
        for i in range(fnum):
            t.fd(r/8) # to add a little hole in the middle to look like an actual flower
            self.begin_fill()
            self.circle(r)
            self.rt(turnrate)
            self.end_fill()





t = ShapeTurtle("red")
t.square(100)
t.pu()
t.goto(100, 100)
t.pd()
t.circle(80)
t.pu()
t.goto(-100, -100)
t.pd()
t.rectangle(50, 150)
t.clear()
t.speed(0)
t.flower(40, 6)

#The challenge is now to come up with at least two simple shapes(oval, triangle, semicircle) and one complex shape(star, pentagon, cube, a better flower)

mainloop()