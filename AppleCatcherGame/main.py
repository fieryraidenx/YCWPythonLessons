from turtle import *
from random import randint

#intialize window size and color
screenWidth, screenHeight = 800, 800
window = Screen()
window.title("Apple Catcher Game")
window.setup(width=screenWidth, height=screenHeight)
window.bgcolor("lightblue")

#add listeners
window.listen()

def setMovement(player, keyArray):
    '''bind movement to player based on keyArray(left, right, down, up)'''
    window.onkey(player.left, keyArray[0])
    window.onkey(player.right, keyArray[1])
    window.onkey(player.down, keyArray[2])
    window.onkey(player.up, keyArray[3])

class Food(Turtle):

    def __init__(self, imgPath, value):
        '''We will be initializing our food as a turtle, setting its image, setting its point value'''
        Turtle.__init__(self)
        self.value = value
        self.pu()
        window.addshape(imgPath)
        self.shape(imgPath)
        self.speed(0)
        self.teleport()
    
    def teleport(self):
        '''Go to a random spot on the Screen'''
        randX = randint(-screenWidth/2+25, screenWidth/2-25)
        randY = randint(-screenHeight/2+25, screenHeight/2-25)
        self.goto(randX, randY)



class Player(Turtle):
    score = 0

    def __init__(self, imgPath, name, keyArray):
        '''We will be initializing our players as a turtle and 
        accepting the parameters of the player image and name. We then
        add listeners on the turtle to give it movement'''
        Turtle.__init__(self)
        self.name = name
        self.pu()
        window.addshape(imgPath)
        self.shape(imgPath)
        self.speed(0)
        #set listeners up
        setMovement(self, keyArray)
    
    def right(self):
        self.setheading(0)
        self.forward(20)

    def up(self):
        self.setheading(90)
        self.forward(20)
       
    def left(self):
        self.setheading(180)
        self.forward(20)

    def down(self):
        self.setheading(270)
        self.forward(20)
        
    def checkCollisions(self, food):
        '''If the distance between this player and the food is close enough, move the food to
        a random location and increase this player's score by the food value'''
        if(self.distance(food) < 15):
            self.score += food.value
            food.teleport()

    def checkNearWall(self):
        '''Checks each side of the turtle to see if it is near to colliding with walls.
        If so, then bounce back'''
        EastEdge, WestEdge = screenWidth/2, -screenWidth/2
        if(self.xcor() > EastEdge - 10):
            self.left()

        if(self.xcor() < WestEdge + 10):
            self.right()

        northEdge, southEdge = screenHeight/2, -screenHeight/2
        if(self.ycor() > northEdge + 10):
            self.down()

        if(self.ycor() < southEdge - 10):
            self.up()



class Text(Turtle):
    score = 0

    def __init__(self, xPos , yPos, textColor):
        '''We will be creating a text turtle set at certain position to keep track of the score of both players'''
        Turtle.__init__(self)
        self.ht()
        self.pu()
        self.pencolor(textColor)
        self.goto(xPos, yPos)




#intialize sprites/turtles
foodlist = [Food("images/apple.gif", 1), Food("images/banana.gif", 2)]
playerlist = [Player("images/monkey.gif", "Monkey", ["Left", "Right", "Down", "Up"]), Player("images/farmer.gif", "Farmer", ["a", "d", "s", "w"])]
scorelist = []


#instantiate score turtles
nplayers = len(playerlist)
topRightXCoord = -screenWidth/2
for i in range(nplayers):
    #this is basically sectioning off the scores into equal parts across the top of the screen depending on the # of players
    sectionWidth = screenWidth/nplayers
    xPos = topRightXCoord + sectionWidth * i + 5
    scorelist.append(Text(xPos, screenHeight/2-50, "green"))

    #intialize the score to the screen
    text = "{} Score: 0".format(playerlist[i].name)
    scorelist[-1].write(text)




def endGame(pname):
    '''hides ALL turtles, then prints out a Game Over message'''

    #zip allows us to loop through 2 equal sized arrays at once
    for player, score in zip(playerlist, scorelist):
        player.reset()
        player.ht()
        score.reset()
        score.ht()
    for food in foodlist:
        food.reset()
        food.ht()
    
    #the final message
    gameOverText = Text(0, 0, "red")
    gameOverText.write("{} WINS!!!".format(pname), align="center", font="Arial 64")




#our game loop(not to be confused with turtle.mainloop())
runGame = True
while runGame:
    window.update()
    #check for collisions with food or wall
    for player in playerlist:
        player.checkNearWall()
        for food in foodlist:
            player.checkCollisions(food)

    
    #update score and check if game over(zip allows us to loop through 2 equal sized arrays at once)
    for player, scoreText in zip(playerlist, scorelist):
        #A score of 10 is the win condition
        if(player.score > 10):
            endGame(player.name)
            runGame = False
        if(player.score != scoreText.score):
            scoreText.score = player.score
            text = "{} Score: {}".format(player.name, player.score)
            #clear the previous score and write the new score
            scoreText.clear()
            scoreText.write(text)

    


mainloop()
