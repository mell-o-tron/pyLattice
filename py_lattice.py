import pygame
from   pygame.locals import *
import math
import numpy as np
import asyncio
from   lattice_draw import *


########################################### PYGAME WINDOW ###########################################

clock = pygame.time.Clock()

# Set up the drawing window
window_size = 800

screen = pygame.display.set_mode([window_size, window_size])

res = 30

screen.fill((10, 10, 10))

M = np.array([[1, 0], [0, 1]])

i = -5
di = 1
while True:
    
    if i > 5 or i < -5:
        di = -di
    
    i += di * 1

    screen.fill((10, 10, 10))
    
    T = np.array([[i, 1], [0, 2*i]])
    M1 = np.matmul(M, T)

    asyncio.run(drawLattice (M, screen, window_size, res, (1,1,0)))
    asyncio.run(drawLattice (M1, screen, window_size, res, (0,1,1)))

    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit(0)
            
        elif event.type == MOUSEWHEEL:
            if res > 5:
                res += event.y * 1
            
            print(f"Zoomed {event.y}" )
            # can access properties with
            # proper notation(ex: event.y)
            
    clock.tick(60)

pygame.quit()
