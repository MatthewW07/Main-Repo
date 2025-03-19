# This a school project y'all
# Gotta make a maze without using DFS
# Taking random to a new level

# 1.2.4 - Maze
# Author : Matthew Wang

# Imports:

import turtle as t
import random

# Variables:

WALLS = 33
WALL_LENGTH = 16
PATH_WIDTH = 2 * WALL_LENGTH

wn = t.Screen()
wn.tracer(False)

maze = t.Turtle()
maze.hideturtle()
maze.pensize(4)
maze.color("darkorchid")

run = t.Turtle()
run.pensize(4)
run.color("red")
run.speed(5)

# Functions

def spiral(len=WALL_LENGTH):
    maze.lt(90)
    for i in range(1, WALLS + 1):
        Wall(WALL_LENGTH, i)
        maze.lt(90)

def Door(DOOR, i):
    maze.fd(DOOR)
    maze.penup()
    maze.fd(PATH_WIDTH)
    maze.pendown()


def Barrier(BARRIER, i):
    maze.fd(BARRIER)
    maze.lt(90)
    maze.fd(PATH_WIDTH)
    maze.bk(PATH_WIDTH)
    maze.rt(90)

def Wall(WALL_LENGTH, i):
    length = WALL_LENGTH * i
    if i > 7:
        DOOR = random.randint(PATH_WIDTH, (length - PATH_WIDTH))
        BARRIER = random.randint(PATH_WIDTH, (length - PATH_WIDTH))
        REST = length - max(DOOR, BARRIER)
        if DOOR < BARRIER:
            Door(DOOR, i)
            Barrier(BARRIER-DOOR, i)
            maze.fd(REST)
        else:
            Barrier(BARRIER, i)
            Door(DOOR-BARRIER, i)
            maze.fd(REST)
    elif i > 2:
        maze.fd(length)
    else:
        maze.pu()
        maze.fd(length)
        maze.pd()

# Movement Functions
def right():
    run.setheading(0)

def up():
    run.setheading(90)

def left():
    run.setheading(180)

def down():
    run.setheading(270)

def move():
    run.fd(WALL_LENGTH)

# Main Function

spiral()
wn.tracer((True))
wn.onkeypress(right, "d")
wn.onkeypress(up, "w")
wn.onkeypress(left, "a")
wn.onkeypress(down, "s")
wn.onkeypress(move, "g")
wn.listen()
wn.exitonclick()