"""
Description:
This program draws and rotates a cube using Pygame.
The user may change the direction of rotation with their mouse
Friction is also added to slow the cube down over time
"""

# TODO:
# - Add comments to the code
# - Finalize the code and make it look nice

# ----- IMPORTS -----

import math as m
import pygame as py

# ----- CONSTANTS -----

WIDTH        =  600       # Screen width
HEIGHT       =  600       # Screen height
BGCOLOR      =  'black'   # Background color
CUBECOLOR    =  'white'   # Color of the cube lines
THICK        =  3         # Line thickness
DISTANCE     =  500       # Distance from cube to camera
K1           =  500       # Perspective constant
FPS          =  20        # Speed of animation
SENSITIVITY  =  0.0005    # Sensitivity for user input
CUBESIZE     =  100       # Size of the cube on the screen

# ----- GLOBAL VARIABLES -----

running       =  True   # Allows for pausing
mouseDownPos  =  None   # Starting point for rotation by the user

# Define initial rotation angles
A = 0.00 # x-axis
B = 0.00 # y-axis

# List of the cube's vertices in R^3
Vertices = [
  [+1, +1, +1],
  [-1, +1, +1],
  [+1, -1, +1],
  [+1, +1, -1],
  [-1, -1, +1],
  [+1, -1, -1],
  [-1, +1, -1],
  [-1, -1, -1],
]

# List of the connections between vertices, where numbers represent indices of 'Vertices' list
Edges = [
  [0, 1], [3, 6],
  [1, 4], [6, 7],
  [2, 4], [5, 7],
  [0, 2], [3, 5],
  [2, 5], [1, 6],
  [0, 3], [4, 7]
]

# ----- TRANSFORMATION FUNCTIONS -----

# Rotates the given point using angles A, B, and C
def rot(x, y, z):
  # Rotation around x-axis
  xAxis_x = x
  xAxis_y = y * m.cos(A) - z * m.sin(A)
  xAxis_z = y * m.sin(A) + z * m.cos(A)

  # Rotation around y-axis
  yAxis_x = xAxis_x * m.cos(B) + xAxis_z * m.sin(B)
  yAxis_y = xAxis_y
  yAxis_z = xAxis_z * m.cos(B) - xAxis_x * m.sin(B)

  return round(yAxis_x, 6), round(yAxis_y, 6), round(yAxis_z, 6)

# Projects the given point using perspective
def project(x, y, z):
  # Avoid dividing by 0
  if z + DISTANCE == 0:
    z += 0.1

  # Transform (x, y, z) coordinates into (x, y) coordinates with perspective
  factor = K1 / (z + DISTANCE)
  projX = int(WIDTH / 2 - x * factor)
  projY = int(HEIGHT / 2 + y * factor)

  return projX, projY

# Function that rotates (and projects) the cube and draws it
def cube():
  # Reset the Screen
  screen.fill(BGCOLOR)

  # Temporary Points list to replace the points in Vertices
  Points = []
  global Vertices

  # Iteration to acquire rotated point
  for v in range(len(Vertices)):
    vertex = Vertices[v] # Define the point
    x, y, z = rot(vertex[0], vertex[1], vertex[2]) # Rotate the point
    Vertices[v] = [x,y,z] # Change Vertices list with new point
    Points.append(project(x * CUBESIZE, y * CUBESIZE, z * CUBESIZE)) # Add rotated point to our list

  # Iteration to draw projected point
  for edge in Edges:
    py.draw.line(screen, CUBECOLOR, Points[edge[0]], Points[edge[1]], THICK)

  # Update the screen
  py.display.flip()
  clock.tick(FPS)

# Initiate Pygame
py.init()
py.display.set_caption("Rotating Cube")
screen = py.display.set_mode((WIDTH, HEIGHT))
clock = py.time.Clock()

# Animate the movement through continuous calling of the cube() function
while True:
  # Apply friction by reducing the rotation angle values
  A *= 0.95
  B *= 0.95

  # Quit the game if window closed
  for event in py.event.get():
    if event.type == py.QUIT:
      py.quit()

    # Pause the animation
    elif event.type == py.KEYDOWN:
      if event.key == py.K_SPACE:
        running = not running

    # Implementing user input for rotation speed
    elif event.type == py.MOUSEBUTTONDOWN:
      if event.button == 1:
        mouseDownPos = event.pos
        
    elif event.type == py.MOUSEBUTTONUP:
      if event.button == 1 and mouseDownPos is not None:
        # Acquire points
        x1, y1 = mouseDownPos
        x2, y2 = event.pos
        # Calculate the differences
        changeX = x2 - x1
        changeY = y2 - y1
        # Change Rotation speed
        # Order is reversed because a horizontal swipe (change in x) should change the y-axis
        B += changeX * SENSITIVITY
        A += changeY * SENSITIVITY
        # Resent position where mouse is initially pressed
        mouseDownPos = None

  # Update to next frame
  if running:
    cube()
