import pygame, sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((1100, 700))

pygame.display.set_caption("GIOCO")

space1=pygame.image.load('space1.jpg')


titolo_su_schermo=True
game_name=font.render("Space Wars", True, (240, 80, 255))
name_rect=game_name.name_rect(midbottom=(550,350))
#class player1:
  #  def __init__(self, posx, posy, width = 100, height = 100) -> None:
    #    self.image = pygame.image.load(PLAYER1)


done = False
while not done:
    for ev in pygame.event.get():
        if ev.type == QUIT:
            done = True
    
    screen.blit(space1,(0,0))
    font = pygame.font.SysFont(None, 80)
    
    screen.blit(game_name,name_rect (midbottom))
    
    for ev in pygame.event.get():
        if ev.type == pygame.KEYDOWN:
            titolo_su_schermo=False

    pygame.display.flip()
   
    pygame.display.update()
pygame.quit()



