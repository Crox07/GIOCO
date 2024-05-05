import pygame, sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((900, 700))
screen.fill((255,255,255))
pygame.display.set_caption("GIOCO")

done = False
while not done:
    for ev in pygame.event.get():
        if ev.type == QUIT:
            done = True
pygame.quit()