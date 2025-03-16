import pygame
import numpy as np
import random

BACK_COLOR = (40, 80, 180) #306998
DIE_NEXT_COLOR = (255, 232, 115) #FFE873
ALIVE_NEXT_COLOR = (255, 212, 59) #FFD43B

WIDTH = 600
HEIGHT = 600
CELL = 8

#update the grid according to game rules
def update(window, grid, progress=False):
    new_grid = np.zeros((grid.shape[0], grid.shape[1]))

    for row, col in np.ndindex(grid.shape):
        surrounding = np.sum(grid[row-1:row+2, col-1:col+2]) - grid[row, col]

        color = BACK_COLOR if grid[row][col] == 0 else ALIVE_NEXT_COLOR
        
        if grid[row][col] == 0:
            if surrounding == 3:
               if progress:
                    new_grid[row][col] = 1
                    color = ALIVE_NEXT_COLOR

        if grid[row, col] == 1:
            if surrounding < 2 or surrounding > 3:
                if progress:
                    new_grid[row][col] = 0
                    color = DIE_NEXT_COLOR

            elif 2 <= surrounding <= 3:
                if progress:
                    new_grid[row][col] = 1
                    color = ALIVE_NEXT_COLOR
        
        pygame.draw.rect(window, color, (col * CELL, row * CELL, CELL - 1, CELL - 1))

    return new_grid

def randomize(window, grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid[i,j] = max(random.choice((0,0,0,0,1)), grid[i,j])
            if grid[i,j] == 0:
                pygame.draw.rect(window, BACK_COLOR, (j * CELL, i * CELL, CELL - 1, CELL - 1))
            else:
                pygame.draw.rect(window, ALIVE_NEXT_COLOR, (j * CELL, i * CELL, CELL - 1, CELL - 1))
    pygame.display.flip()
    return grid


def main():
    pygame.init()
    pygame.display.set_caption("Game of Life")

    canvas = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    grid = np.zeros((75,75))
    canvas.fill(BACK_COLOR) 
    update(canvas, grid)

    pygame.display.flip()
    pygame.display.update()

    go = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    go = not go
                    update(canvas, grid)
                    pygame.display.update()
                if event.key == pygame.K_r:
                    randomize(canvas, grid)
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                grid[pos[1] // CELL, pos[0] // CELL] = 1
                update(canvas, grid)
                pygame.display.update()
        
        canvas.fill(BACK_COLOR)

        if go:
            grid = update(canvas, grid, progress=True)
            pygame.display.update()
            FPS = 20
        elif go == False:
            FPS = 20
            
        clock.tick(FPS)


if __name__ == '__main__':
    main()


