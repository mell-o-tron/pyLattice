import numpy as np
import math
import pygame
from pygame.locals import *
import time
from lattice_draw import *
import asyncio


norm = lambda v : np.linalg.norm(v,  ord = 2)

that_rounding = lambda a : math.floor(a) if a - math.floor(a) <= .5 else math.ceil(a)

def gaussSVP_one_step (v1, v2):
    
    print(v1, v2)
    
    if norm(v1) > norm(v2):
        vt = v1
        v1 = v2
        v2 = vt

    m_not_rounded = np.dot(v1, v2) / np.dot(v1, v1)
    m = that_rounding(m_not_rounded)
    
    if m == 0:
        return [True, v1, v2, v2 - m_not_rounded * v1]
    else:
        return [False, v1, v2 - m * v1, v2 - m_not_rounded * v1]
    

def active_wait (interval):
    begin_milliseconds = time.time() * 1000
    while time.time() * 1000 < begin_milliseconds + interval:
        pygame.display.flip()
        
    print("done waiting")

def draw_gauss (v1_arg, v2_arg, interval, res, screen, winsize):
    
    v1 = v1_arg
    v2 = v2_arg
    done = 0
    
    
    while(not done):
        screen.fill((10, 10, 10))
        asyncio.run(drawLattice(np.transpose(np.array([v1, v2])), screen, winsize, res, (.4, .4, .4)))
        
        pygame.draw.aaline(screen, [200, 200, 0], [winsize/2, winsize/2], [winsize/2 + res * v1[0], winsize/2 + res * v1[1]], 2)
        pygame.draw.aaline(screen, [0, 200, 200], [winsize/2, winsize/2], [winsize/2 + res * v2[0], winsize/2 + res * v2[1]], 2)
        [done, v1, v2, v_nr] = gaussSVP_one_step (v1, v2)
        
        active_wait(interval/4)
        
        pygame.draw.aaline(screen, [255, 0, 0], [winsize/2, winsize/2], [winsize/2 + res * v_nr[0], winsize/2 + res * v2[1]], 2)
        
        active_wait(interval/4)
        
        pygame.draw.aaline(screen, [200, 0, 200], [winsize/2, winsize/2], [winsize/2 + res * v2[0], winsize/2 + res * v2[1]], 2)
        
        if done:
            print(v1)
        active_wait(interval/2)
