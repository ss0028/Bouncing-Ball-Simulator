#Bouncing ball program
#created by Shikha Singh

import turtle
import random

wn=turtle.Screen()                                                       #sets the screen for bouncing balls
wn.bgcolor("black")                                                      #sets background-color of the screen
wn.title("BOUNCING BALL SIMULATOR")                                      #sets title of the screen
wn.tracer(0)

balls=[]
colors=["pink","white","yellow","red","purple","blue","gray","green"]
for x in range(15):
    balls.append(turtle.Turtle())

for ball in balls:
    ball.shape("circle")
    ball.color(random.choice(colors))
    ball.penup()                                                           #turtle starts by default-at the center of screen,so not to show its movement to another position by drawing line use penup()
    ball.speed(8)    #sets the animation speed
    x=random.randint(-200,200)
    y=random.randint(200,400)
    ball.goto(x,y)                                                      #sets position of ball on screen
    ball.dy=0
    ball.dx=random.randint(-6,6)
gravity=0.1

while True:
    wn.update()
    for ball in balls:
        ball.dy-=gravity                                               #to bring ball down to show effect of gravity
        ball.sety(ball.ycor()+ball.dy)
        ball.setx(ball.xcor()+ball.dx)
        
        #checks for a wall collision
        if ball.xcor()>300:
            ball.dx*=-1
        if ball.xcor()<-300:
            ball.dx*=-1
            
        #Check for a bounce from lower surface
        if ball.ycor()<-300:
            ball.dy*=-1
        


wn.mainloop()