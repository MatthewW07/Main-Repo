# Rotating Cube

import math as m
import pygame as py

WIDTH = 600
HEIGHT = 600
BackColor = (0,0,0)
Color = (255, 255, 255)
Speed = 1
distance = 500
K1 = 500
FPS = 20

A = 0.02
B = 0.08
C = 0.04
cubeWidth = 100

Vertices = [
    [1, 1, 1],
    [-1, 1, 1],
    [1, -1, 1],
    [1, 1, -1],
    [-1, -1, 1],
    [1, -1, -1],
    [-1, 1, -1],
    [-1, -1, -1]
]

Edges = [
    [0,1], [3,6],
    [1,4], [6,7],
    [2,4], [5,7],
    [0,2], [3,5],
    [2,5], [1,6],
    [0,3], [4,7]
]


def rot(x, y, z):
    # x axis
    Rx, Ry, Rz = x, y * m.cos(A) - z * m.sin(A), y * m.sin(A) + z * m.cos(A)
    # y axis
    Sx, Sy, Sz = Rx * m.cos(B) + Rz * m.sin(B), Ry, Rz * m.cos(B) - Rx * m.sin(B)
    # z axis
    Fx, Fy, Fz = Sx * m.cos(C) - Sy * m.sin(C), Sx * m.sin(C) + Sy * m.cos(C), Sz
    return round(Fx,6), round(Fy,6), round(Fz,6)

def project(x, y, z):
    if z + distance == 0:
        z += 0.1
    factor = K1 / (z + distance)
    #factor = 1
    projX = int(WIDTH / 2 - x * factor)
    projY = int(HEIGHT / 2 + y * factor)
    return projX, projY

def cube():
    Points = []
    global Vertices
    for v in range(len(Vertices)):
        vertex = Vertices[v]
        x, y, z = rot(vertex[0], vertex[1], vertex[2])
        Vertices[v] = [x,y,z]
        Points.append(project(x * cubeWidth, y * cubeWidth, z * cubeWidth))
    for edge in Edges:
        py.draw.line(screen, Color, Points[edge[0]], Points[edge[1]])


py.init()
py.display.set_caption("Rotating Cube")
screen = py.display.set_mode((WIDTH, HEIGHT))
clock = py.time.Clock()

running = True
while True:
    screen.fill(BackColor)

    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
        if event.type == py.K_SPACE:
            running = not running

    cube()
    py.display.flip()
    clock.tick(FPS)

py.quit()
