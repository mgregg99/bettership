# (c) Matthew Gregg 2022 

import os, pygame, sys

from pygame.locals import *

pygame.init()
FPSCLOCK = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((600, 600))
pygame.display.set_caption('BetterShip')

BACKGROUND = (124, 185, 232)



# make background blue
DISPLAYSURF.fill(BACKGROUND)


# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    FPSCLOCK.tick(30)