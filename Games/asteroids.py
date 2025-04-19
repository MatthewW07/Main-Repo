"""
Asteroid Game:
The user is located in space, where asteroids appear every 4 seconds
The user must shoot these asteroids by pressing 's'
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

STARS = 60
ASTEROID_SPEED = 1
ASTEROID_RATE = 3000
FPS = 20
GAME_OVER = False

level = 0
point = 0

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
    
# Tutorial
def tutorial():
  tut = t.Turtle()
  tut.color("blue")
  tut.pu()
  tut.hideturtle()
  tut.goto(0, 90)
  tut.write("W -> Forward", True, "center", ("Georgia", 20, 'normal'))
  tut.setpos(0, 30)
  tut.write("A -> Left", True, "center", ("Georgia", 20, 'normal'))
  tut.setpos(0, -30)
  tut.write("D -> Right", True, "center", ("Georgia", 20, 'normal'))
  tut.setpos(0, -90)
  tut.write("G -> Shoot", True, "center", ("Georgia", 20, 'normal'))
  wn.update()
  wn.ontimer(tut.clear(), 3000)

# Asteroids
def asteroid():
  global level, ASTEROID_RATE, ASTEROID_SPEED
  if level % 5 == 0:
    ASTEROID_RATE = max(2000, ASTEROID_RATE-100)
  if level % 8 == 0:
    ASTEROID_SPEED = min(6, ASTEROID_SPEED+1)
  # ChatGPT gave the following 2 lines
  if GAME_OVER: 
    return
  # Inesh styled the Asteroids
  newAsteroid = t.Turtle()
  newAsteroid.shape("circle")
  newAsteroid.shapesize(3)
  asteroids.append([newAsteroid, True])
  # Google AI Overview gave the 'choice' method
  x = random.choice(list(range(100, 480)) + list(range(-480, -100)))
  y = random.choice(list(range(100, 330)) + list(range(-330, -100)))
  newAsteroid.pu()
  newAsteroid.pencolor("orange")
  newAsteroid.goto(x, y)
  if x < 0:
    newAsteroid.setheading(math.degrees(math.atan((y-user.ycor())/(x-user.xcor()))))
  else:
    newAsteroid.setheading(math.degrees(math.atan((y-user.ycor())/(x-user.xcor())))+180)
  wn.update()
  level += 1
  wn.ontimer(asteroid, ASTEROID_RATE)

# Move asteroids forward
def moveAsteroids():
  # ChatGPT gave the following 2 lines
  if GAME_OVER:
    return
  i = 0
  while i < len(asteroids):
    obj = asteroids[i][0]
    alive = asteroids[i][1]
    if alive:
      obj.fd(ASTEROID_SPEED)
      i += 1
    else:
      asteroids.pop(i)
  wn.update()
  wn.ontimer(moveAsteroids, 10)
  collide()

# Lasers
def lasers():
  global point, asteroids, shots
  if GAME_OVER:
    return
  i = 0
  while i < len(shots):
    pew = shots[i]
    pew.fd(8)
    x = pew.xcor()
    y = pew.ycor()
    tempA = []
    for j in range(len(asteroids)):
      if pew.distance(asteroids[j][0]) < 40 and asteroids[j][1] == True:
        asteroids[j][1] = False
        asteroids[j][0].hideturtle()
        point += 1
      else:
        tempA.append(asteroids[j])
    asteroids = tempA
    if (x < -520) or (x > 520) or (y < -370) or (y > 370):
      shots.pop(i)
    else:
      i += 1
  wn.update()
  if len(shots) > 0:
    wn.ontimer(lasers, 10)

# check for collision
def collide():
  for i in range(len(asteroids)):
    if user.distance(asteroids[i][0]) < 40 and asteroids[i][1]:
      global ASTEROID_SPEED, GAME_OVER
      ASTEROID_SPEED = 0
      GAME_OVER = True
      disable()
      stop = t.Turtle()
      stop.pu()
      stop.goto(0,250)
      stop.color("red")
      stop.write("GAME OVER!", True, "center", ("Georgia", 20, 'normal'))
      stop.setpos(0, stop.ycor()-50)
      stop.write("You shot " + str(point) + " asteroids!", True, "center", ("Georgia", 20, 'normal'))
      
# Event functions

movement = {
  'fd' : False,
  'rt' : False,
  'lt' : False
}

def disable():
  wn.onkeypress(None, "w")
  wn.onkeypress(None, "a")
  wn.onkeypress(None, "s")
  wn.onkeypress(None, "d")

def right():
  movement['rt'] = True
def left():
  movement['lt'] = True
def forward():
  movement['fd'] = True
def rightStop():
  movement['rt'] = False
def leftStop():
  movement['lt'] = False
def forwardStop():
  movement['fd'] = False

def shoot():
  shot = t.Turtle()
  shot.pu()
  shot.pencolor("blue")
  shot.color("blue")
  shot.setheading(user.heading())
  shot.setpos(user.pos())
  shots.append(shot)
  lasers()

def move():
  if movement['fd']:
    user.fd(3)
  if movement['rt']:
    user.rt(6)
  if movement['lt']:
    user.lt(6)
  wn.ontimer(move, 30)

# Main Events ----------

stars()
tutorial()

asteroid()
wn.ontimer(asteroid, ASTEROID_RATE)
moveAsteroids()

move()

wn.listen()

wn.onkeypress(right, 'd')
wn.onkeypress(left, 'a')
wn.onkeypress(forward, 'w')

wn.onkeyrelease(rightStop, 'd')
wn.onkeyrelease(leftStop, 'a')
wn.onkeyrelease(forwardStop, 'w')

wn.onkey(shoot, "g")

wn.exitonclick()