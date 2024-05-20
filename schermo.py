import pygame, sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((900, 700))
screen.fill((255,255,255))
pygame.display.set_caption("GIOCO")

space1=pygame.image.load('space1.jpg')
space=pygame.image.load('space.png')





#class player1:
  #  def __init__(self, posx, posy, width = 100, height = 100) -> None:
    #    self.image = pygame.image.load(PLAYER1)


done = False
while not done:
    for ev in pygame.event.get():
        if ev.type == QUIT:
            done = True
    screen.blit(space,(-100,0))
    screen.blit(space1,(0,0))
   
    pygame.display.update()
pygame.quit()


