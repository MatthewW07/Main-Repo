
#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
# INCREASE THE NUMBER OF TURTLES
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic","arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold", "red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  col = turtle_colors.pop()
  t.pencolor(col)
  t.fillcolor(col)
  t.lt(90)
  t.speed(0)
  my_turtles.append(t)

# create an initial starting position
startx = 0
starty = 0

# for each turtle we created, we will move it along the diagonal line and down a bit, seperating the turtles
# MAKE SOME FUN VARIABLES FOR THE SPIRAL, LENGTHS, and SIZES-
dir = 0
dis = 0
siz = 1

for t in my_turtles:
  t.penup()
  t.goto(startx, starty)
  t.pendown()
  t.pensize(siz)
  t.right(dir + 45)     
  t.forward(dis + 25)
  startx = t.xcor()
  starty = t.ycor()
  dir += 45
  dis += 5
  siz += 1

#	change the starting position to not overlap the shapes
startx = startx + 50
starty = starty + 50

wn = trtl.Screen()
wn.mainloop()
