import turtle
import random
import math
import winsound

#functions for player movement
def move_left():
    x=player.xcor()-30
    if x<=-280:
        x=-280
    player.setx(x)

def move_right():
    x=player.xcor()+30
    if x>=280:
        x=280
    player.setx(x)
    
def move_up():
    y=player.ycor()+50
    if y>=280:
        y=280
    player.sety(y)

def move_down():
    y=player.ycor()-50
    if y<=-280:
        y=-280
    player.sety(y)

#making bullet function
def fire_bullet():
    winsound.PlaySound("laser.wav",winsound.SND_ASYNC)
    x=player.xcor()
    y=player.ycor()+30
    bullet.setposition(x,y)
    bullet.showturtle()


#setting up window
window=turtle.Screen()
window.setup(width=700,height=700)
window.bgcolor("black")
window.bgpic("background.gif")
window.title("SPACE INVADERS")

#drawing border
border=turtle.Turtle()
border.speed(0)
border.color("grey")
border.up()
border.setposition(300,300)
border.down()
border.pensize(5)

for side in range(4):
    border.right(90)
    border.forward(600)
border.hideturtle()

#register shape
turtle.register_shape("player.gif")
turtle.register_shape("invader.gif")
turtle.register_shape("coin.gif")


#create the player turtle
player=turtle.Turtle()
player.shape("player.gif")
player.up()
player.speed(0)
player.setposition(0,-260)

#create the player bullet
bullet=turtle.Turtle()
bullet.shape("triangle")
bullet.shapesize(0.5,0.5)
bullet.color("yellow")
bullet.setheading(90)
bullet.up()
bullet.hideturtle()
bullet.speed(0)
bullet.setposition(500,500)


#create the coins
coin1=turtle.Turtle()
coin1.shape("coin.gif")
coin1.up()
coin1.speed(0)
coin1.setposition(random.randint(-280,280),270)

coin2=turtle.Turtle()
coin2.shape("coin.gif")
coin2.up()
coin2.speed(0)
coin2.setposition(random.randint(-280,280),270)

coin3=turtle.Turtle()
coin3.shape("coin.gif")
coin3.up()
coin3.speed(0)
coin3.setposition(random.randint(-280,280),270)

coin4=turtle.Turtle()
coin4.shape("coin.gif")
coin4.up()
coin4.speed(0)
coin4.setposition(random.randint(-280,280),270)

coin5=turtle.Turtle()
coin5.shape("coin.gif")
coin5.up()
coin5.speed(0)
coin5.setposition(random.randint(-280,280),270)

#create the invaders
invader1=turtle.Turtle()
invader1.shape("invader.gif")
invader1.up()
invader1.speed(0)
invader1.setposition(random.randint(-280,280),270)

invader2=turtle.Turtle()
invader2.shape("invader.gif")
invader2.up()
invader2.speed(0)
invader2.setposition(random.randint(-280,280),270)

invader3=turtle.Turtle()
invader3.shape("invader.gif")
invader3.up()
invader3.speed(0)
invader3.setposition(random.randint(-280,280),270)

invader4=turtle.Turtle()
invader4.shape("invader.gif")
invader4.up()
invader4.speed(0)
invader4.setposition(random.randint(-280,280),270)

invader5=turtle.Turtle()
invader5.shape("invader.gif")
invader5.up()
invader5.speed(0)
invader5.setposition(random.randint(-280,280),270)



#score board
score=0
score_pen=turtle.Turtle()
score_pen.speed(0)
score_pen.color("grey")
score_pen.up()
score_pen.setposition(-300,310)
score_pen.write("Score: %s"%score)
score_pen.hideturtle()



#linking player with keyboard
turtle.listen()
turtle.onkey(move_left,"Left")
turtle.onkey(move_right,"Right")
turtle.onkey(move_up,"Up")    
turtle.onkey(move_down,"Down")
turtle.onkey(fire_bullet,"space")

#Game loop
while True:
#bullet firing speed and movement
    bullet.forward(20)
    
#Invader movement
    invader1.forward(5)
    invader2.forward(5)
    invader3.forward(5)
    invader4.forward(5)
    invader5.forward(5)
    if (invader1.xcor()>280)|(invader2.xcor()>280)|(invader3.xcor()>280)|(invader4.xcor()>280)|(invader5.xcor()>280):
        invader1.right(90)
        invader1.forward(50)
        invader1.right(90)
        invader1.forward(2)

        invader2.right(90)
        invader2.forward(50)
        invader2.right(90)
        invader2.forward(25)

        invader3.right(90)
        invader3.forward(50)
        invader3.right(90)
        invader3.forward(2)

        invader4.right(90)
        invader4.forward(50)
        invader4.right(90)
        invader4.forward(2)

        invader5.right(90)
        invader5.forward(50)
        invader5.right(90)
        invader5.forward(2)
        
    elif (invader1.xcor()<-280)|(invader2.xcor()<-280)|(invader3.xcor()<-280)|(invader4.xcor()<-280)|(invader5.xcor()<-280):
        invader1.left(90)
        invader1.forward(50)
        invader1.left(90)
        invader1.forward(2)

        invader2.left(90)
        invader2.forward(50)
        invader2.left(90)
        invader2.forward(2)

        invader3.left(90)
        invader3.forward(50)
        invader3.left(90)
        invader3.forward(2)

        invader4.left(90)
        invader4.forward(50)
        invader4.left(90)
        invader4.forward(2)

        invader5.left(90)
        invader5.forward(50)
        invader5.left(90)
        invader5.forward(2)

#distance between bullet and invaders        
    distance1= math.sqrt(math.pow(bullet.xcor()-invader1.xcor(),2)+math.pow(bullet.ycor()-invader1.ycor(),2))
    distance2= math.sqrt(math.pow(bullet.xcor()-invader2.xcor(),2)+math.pow(bullet.ycor()-invader2.ycor(),2))
    distance3= math.sqrt(math.pow(bullet.xcor()-invader3.xcor(),2)+math.pow(bullet.ycor()-invader3.ycor(),2))
    distance4= math.sqrt(math.pow(bullet.xcor()-invader4.xcor(),2)+math.pow(bullet.ycor()-invader4.ycor(),2))
    distance5= math.sqrt(math.pow(bullet.xcor()-invader5.xcor(),2)+math.pow(bullet.ycor()-invader5.ycor(),2))

#bullet collision
    if distance1<25:
        winsound.PlaySound("explosion-e+b.wav",winsound.SND_ASYNC)
        score+=10
        score_pen.clear()
        score_pen.write("Score: %s"%score)
        bullet.setposition(500,500)
        bullet.hideturtle()
        invader1.hideturtle()
        invader1.showturtle()
        x=random.randint(-280,280)
        invader1.setposition(x,280)

    elif distance2<25:
        winsound.PlaySound("explosion-e+b.wav",winsound.SND_ASYNC)
        score+=10
        score_pen.clear()
        score_pen.write("Score: %s"%score)
        bullet.setposition(500,500)
        bullet.hideturtle()
        invader2.hideturtle()
        invader2.showturtle()
        x=random.randint(-280,280)
        invader2.setposition(x,280)

    elif distance3<25:
        winsound.PlaySound("explosion-e+b.wav",winsound.SND_ASYNC)
        score+=10
        score_pen.clear()
        score_pen.write("Score: %s"%score)
        bullet.setposition(500,500)
        bullet.hideturtle()
        invader3.hideturtle()
        invader3.showturtle()
        x=random.randint(-280,280)
        invader3.setposition(x,280)

    elif distance4<25:
        winsound.PlaySound("explosion-e+b.wav",winsound.SND_ASYNC)
        score+=10
        score_pen.clear()
        score_pen.write("Score: %s"%score)
        bullet.setposition(500,500)
        bullet.hideturtle()
        invader4.hideturtle()
        invader4.showturtle()
        x=random.randint(-280,280)
        invader4.setposition(x,280)

    elif distance5<25:
        winsound.PlaySound("explosion-e+b.wav",winsound.SND_ASYNC)
        score+=10
        score_pen.clear()
        score_pen.write("Score: %s"%score)
        bullet.setposition(500,500)
        bullet.hideturtle()
        invader5.hideturtle()
        invader5.showturtle()
        x=random.randint(-280,280)
        invader5.setposition(x,280)


#distance between player and invaders
    distancep1= math.sqrt(math.pow(player.xcor()-invader1.xcor(),2)+math.pow(player.ycor()-invader1.ycor(),2))
    distancep2= math.sqrt(math.pow(player.xcor()-invader2.xcor(),2)+math.pow(player.ycor()-invader2.ycor(),2))
    distancep3= math.sqrt(math.pow(player.xcor()-invader3.xcor(),2)+math.pow(player.ycor()-invader3.ycor(),2))
    distancep4= math.sqrt(math.pow(player.xcor()-invader4.xcor(),2)+math.pow(player.ycor()-invader4.ycor(),2))
    distancep5= math.sqrt(math.pow(player.xcor()-invader5.xcor(),2)+math.pow(player.ycor()-invader5.ycor(),2))


#player collision
    if (distancep1<35)|(distancep2<35)|(distancep3<35)|(distancep4<35)|(distancep5<35):
        winsound.PlaySound("explosion-e+p.wav",winsound.SND_ALIAS)
        break

#distance between coins and bullet
    distancec1= math.sqrt(math.pow(bullet.xcor()-coin1.xcor(),2)+math.pow(bullet.ycor()-coin1.ycor(),2))
    distancec2= math.sqrt(math.pow(bullet.xcor()-coin2.xcor(),2)+math.pow(bullet.ycor()-coin2.ycor(),2))
    distancec3= math.sqrt(math.pow(bullet.xcor()-coin3.xcor(),2)+math.pow(bullet.ycor()-coin3.ycor(),2))
    distancec4= math.sqrt(math.pow(bullet.xcor()-coin4.xcor(),2)+math.pow(bullet.ycor()-coin4.ycor(),2))
    distancec5= math.sqrt(math.pow(bullet.xcor()-coin5.xcor(),2)+math.pow(bullet.ycor()-coin5.ycor(),2))
#coin collection
    if distancec1<20:
        winsound.PlaySound("coin.wav",winsound.SND_ASYNC)
        score+=5
        score_pen.clear()
        score_pen.write("Score: %s"%score)
        bullet.setposition(500,500)
        bullet.hideturtle()
        coin1.hideturtle()
        coin1.setposition(-500,500)

    elif distancec2<20:
        winsound.PlaySound("coin",winsound.SND_ASYNC)
        score+=5
        score_pen.clear()
        score_pen.write("Score: %s"%score)
        bullet.setposition(500,500)
        bullet.hideturtle()
        coin2.hideturtle()
        coin2.setposition(-500,500)

    elif distancec3<20:
        winsound.PlaySound("coin.wav",winsound.SND_ASYNC)
        score+=5
        score_pen.clear()
        score_pen.write("Score: %s"%score)
        bullet.setposition(500,500)
        bullet.hideturtle()
        coin3.hideturtle()
        coin3.setposition(-500,500)

    elif distancec4<20:
        winsound.PlaySound("coin.wav",winsound.SND_ASYNC)
        score+=5
        score_pen.clear()
        score_pen.write("Score: %s"%score)
        bullet.setposition(500,500)
        bullet.hideturtle()
        coin4.hideturtle()
        coin4.setposition(-500,500)

    elif distancec5<20:
        winsound.PlaySound("coin.wav",winsound.SND_ASYNC)
        score+=5
        score_pen.clear()
        score_pen.write("Score: %s"%score)
        bullet.setposition(500,500)
        bullet.hideturtle()
        coin5.hideturtle()
        coin5.setposition(-500,500)


#invader crosses boundary
    if (invader1.ycor()<-270)|(invader2.ycor()<-270)|(invader3.ycor()<-270)|(invader4.ycor()<-270)|(invader5.ycor()<-270):
  
        break

#limiting bullet in boundary
    if bullet.ycor()>=290:
        bullet.setposition(500,500)

#Game over screen
invader1.hideturtle()
invader2.hideturtle()
invader3.hideturtle()
invader4.hideturtle()
invader5.hideturtle()
coin1.hideturtle()
coin2.hideturtle()
coin3.hideturtle()
coin4.hideturtle()
coin5.hideturtle()
player.hideturtle()
bullet.hideturtle()
window.bgpic("end.gif")
score_pen.setposition(-70,-60)
score_pen.clear()
score_pen.color("yellow")
score_pen.write("Score: %s"%score,font=("elephant",20))
winsound.PlaySound("gameover",winsound.SND_ALIAS)

