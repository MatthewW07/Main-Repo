"""
Asteroid Game:
The user is located in space, where asteroids appear every 4 seconds
The user must shoot these asterods by pressing 's'
The user can move: right with 'd', left with 'a', and forward with 'w'
"""

"""
Credits:
Date: 3/22/2025
Author: Matthew
ChatGPT helped with stopping the game
AI credits given in code
"""

import turtle as t
import random
import math

# Variables -----------

STARS = 40
ASTEROID_SPEED = 1
ASTEROID_RATE = 3000
FPS = 20
GAME_OVER = False

# Objects ------------

asteroids = []
shots = []

# Background screen
wn = t.Screen()
wn.setup(1000, 700)
wn.bgcolor("black")
wn.tracer(False)

# Turtle to draw the stars
star = t.Turtle()
star.color("white")
star.hideturtle()
star.pu()
star.pensize(1)

# User turtle
user = t.Turtle()
user.color("white")
user.pencolor("white")
user.shape("arrow")
user.pensize(3)
user.pu()

# Functions ------------

# Stars
def stars():
  for i in range(STARS):
    x = random.randint(-480,480)
    y = random.randint(-330,330)
    star.goto(x, y)
    star.pd()
    star.circle(1)
    star.pu()

# Asteroids
def asteroid():
  # ChatGPT gave the following 2 lines
  if GAME_OVER: 
    return
  newAsteroid = t.Turtle()
  newAsteroid.shapesize(5)
  asteroids.append([newAsteroid, True])
  # Google AI Overview gave the 'choice' method
  x = random.choice(list(range(100, 480)) + list(range(-480, -100)))
  y = random.choice(list(range(100, 330)) + list(range(-330, -100)))
  newAsteroid.pu()
  newAsteroid.pencolor("white")
  newAsteroid.goto(x, y)
  if x < 0:
    newAsteroid.setheading(math.degrees(math.atan(y/x)))
  else:
    newAsteroid.setheading(math.degrees(math.atan(y/x))+180)
  wn.update()
  wn.ontimer(asteroid, ASTEROID_RATE)

# Move asteroids forward
def moveAsteroids():
  # ChatGPT gave the following 2 lines
  if GAME_OVER:
    return
  for i in range(len(asteroids)):
    obj = asteroids[i][0]
    alive = asteroids[i][1]
    if alive:
      obj.fd(ASTEROID_SPEED)
    wn.update()
  wn.ontimer(moveAsteroids, 10)
  collide()

# Lasers
def lasers():
  if GAME_OVER:
    return
  for i in range(len(shots)):
    pew = shots[i]
    pew.fd(5)
    x = pew.xcor()
    y = pew.ycor()
    for j in range(len(asteroids)):
      if pew.distance(asteroids[j][0]) < 30:
        asteroids[j][1] = False
        asteroids[j][0].hideturtle()
        
    if (x < -520) or (x > 520) or (y < -370) or (y > 370):
      shots.pop(i)
  wn.update()
  if len(shots) > 0:
    wn.ontimer(lasers, 10)

# check for collision
def collide():
  for i in range(len(asteroids)):
    if user.distance(asteroids[i][0]) < 20 and asteroids[i][1]:
      global ASTEROID_SPEED, GAME_OVER
      ASTEROID_SPEED = 0
      GAME_OVER = True
      disable()
      stop = t.Turtle()
      stop.pu()
      stop.goto(0,250)
      stop.color("red")
      stop.write("GAME OVER!", True, "center", ("Georgia", 20, 'normal'))
      
# Event functions
def disable():
  wn.onkeypress(None, "w")
  wn.onkeypress(None, "a")
  wn.onkeypress(None, "s")
  wn.onkeypress(None, "d")

def right():
  user.rt(15)
  wn.update()

def left():
  user.lt(15)
  wn.update()

def move():
  user.fd(5)
  wn.update()

def shoot():
  shot = t.Turtle()
  shot.pu()
  shot.pencolor("white")
  shot.color("white")
  shot.setheading(user.heading())
  shot.setpos(user.pos())
  shots.append(shot)
  lasers()

# Main Events ----------

stars()

asteroid()
wn.ontimer(asteroid, ASTEROID_RATE)
moveAsteroids()

wn.listen()
wn.onkeypress(right, "d")
wn.onkeypress(left, "a")
wn.onkeypress(move, "w")
wn.onkey(shoot, "s")

wn.exitonclick()