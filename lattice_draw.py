import pygame
from pygame.locals import *
import math
import numpy as np
import asyncio

async def draw_point(M, screen, winsize, res, i, j, col = (1,1,1)):
    curr_transformed =  np.matmul(M, np.array([i,j]))
    nexti_transformed = np.matmul(M, np.array([i+res,j]))
    nextj_transformed = np.matmul(M, np.array([i,j+res]))
                
    current_position = (curr_transformed[0] + math.floor(winsize/2), curr_transformed[1] + math.floor(winsize/2))
                
    nexti_position = (nexti_transformed[0] + math.floor(winsize/2), nexti_transformed[1] + math.floor(winsize/2))
                
    nextj_position = (nextj_transformed[0] + math.floor(winsize/2), nextj_transformed[1] + math.floor(winsize/2))
                
                
                
    curr_dist_origin    = np.linalg.norm(curr_transformed,  ord = 8)
    nexti_dist_origin   = np.linalg.norm(nexti_transformed, ord = 8)
    nextj_dist_origin   = np.linalg.norm(nextj_transformed, ord = 8)
                
    curr_lum_point = max((200 - curr_dist_origin/2), 10)
    nexti_lum_point = max((200 - nexti_dist_origin/2), 10)
    nextj_lum_point = max((200 - nextj_dist_origin/2), 10)
                
    curr_color = (curr_lum_point * col[0], 
                  curr_lum_point * col[1], 
                  curr_lum_point * col[2])
    
    nexti_color = ((curr_lum_point + nexti_lum_point) * .5 * col[0], 
                  (curr_lum_point + nexti_lum_point) * .5 * col[1], 
                  (curr_lum_point + nexti_lum_point) * .5 * col[2])
    
    nextj_color = ((curr_lum_point + nextj_lum_point) * .5 * col[0], 
                  (curr_lum_point + nextj_lum_point) * .5 * col[1], 
                  (curr_lum_point + nextj_lum_point) * .5 * col[2])
    
    pygame.draw.circle(screen, curr_color, current_position, 3)
                
    pygame.draw.aaline(screen, nexti_color, current_position, nexti_position, 2)
                
    pygame.draw.aaline(screen, nextj_color, current_position, nextj_position, 2)



async def drawLattice (M, screen, winsize, res, col):
    for i in range(math.floor(-winsize) + 1, math.floor(winsize)):
        for j in range(math.floor(-winsize/2) + 1, math.floor(winsize/2)):
            if i % res == 0 and j % res == 0:
                await(draw_point(M, screen, winsize, res, i, j, col)) 
