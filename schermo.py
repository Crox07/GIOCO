import pygame, sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((1200, 750))

pygame.display.set_caption("GIOCO")

Initial_Screen=pygame.image.load('Schermata_inizio.jpg')
space1=pygame.image.load('space1.jpg')
space1=pygame.transform.scale(space1, (1200,750))


font1=pygame.font.Font(None, 80)
font2=pygame.font.Font(None, 80)

#class player1:
  #  def __init__(self, posx, posy, width = 100, height = 100) -> None:
    #    self.image = pygame.image.load(PLAYER1)

SCHERMATA_INIZIALE=True

def TITLE_SCREEN():
    global SCHERMATA_INIZIALE
    for ev in pygame.event.get():
        if ev.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(Initial_Screen,(0,0))
    game_name= font1.render("Space Wars", True, (20, 20, 255))
    game_name_rect=game_name.get_rect(center=(600,400))
    screen.blit(game_name, game_name_rect)
    pygame.display.flip()



done = False
while not done:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            done = True
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if SCHERMATA_INIZIALE:
                SCHERMATA_INIZIALE = False

    if SCHERMATA_INIZIALE:
        TITLE_SCREEN()
    else:
        screen.blit(space1,(0,0))
        pygame.display.flip()



pygame.quit()
sys.exit()


