import pygame, sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((1200, 750))

pygame.display.set_caption("GIOCO")



Initial_Screen=pygame.image.load('Schermata_inizio.jpg').convert_alpha()
space=pygame.image.load('space.jpg').convert_alpha()
space=pygame.transform.scale(space, (1200,750))

options_screen=pygame.image.load('stars.jpg').convert_alpha()

font1=pygame.font.Font('Pixeltype.ttf', 150)
font2=pygame.font.Font('Pixeltype.ttf', 120)

#class player1:
  #  def __init__(self, posx, posy, width = 100, height = 100) -> None:
    #    self.image = pygame.image.load(PLAYER1)

SCHERMATA_INIZIALE=True
SCHERMATA_MENU=False

PvP=False
Duo=False

def TITLE_SCREEN():
    global SCHERMATA_INIZIALE
    for ev in pygame.event.get():
        if ev.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(Initial_Screen,(0,0))
    game_name= font1.render("Space Wars", True, (0, 0, 102)).convert_alpha()
    game_name_rect=game_name.get_rect(center=(600,400))
    pygame.draw.rect(screen,(102,204,204),game_name_rect)
    pygame.draw.rect(screen,'black',game_name_rect,3)
    screen.blit(game_name, game_name_rect)
    pygame.display.flip()

def OPTIONS_MENU():
    global PvP, Duo
    
    mouse_pos=pygame.mouse.get_pos()

    screen.blit(options_screen,(0,0)) 
    
    if PvP:
        PvP_color=(255,20,20)
    else:
        PvP_color=(20,20,255)
    
    if Duo:
        Duo_color=(255,20,20)
    else:
        Duo_color=(20,20,255)

    PvP_text=font2.render("PvP", True, (PvP_color))
    PvP_text_rect=PvP_text.get_rect(center=(200,200))
    
    surface1=pygame.Surface((200,100))
    surf_rect=surface1.get_rect(center=(200,200))
    surface1.fill('grey')
    pygame.draw.rect(surface1,'yellow',surface1.get_rect(),10)
    surface1.blit(PvP_text,PvP_text_rect)
    
    screen.blit(surface1,surf_rect)
    
    Duo_text=font2.render("Duo", True, Duo_color)
    Duo_text_rect=Duo_text.get_rect(center=(1000,200))
    
    surface2=pygame.Surface((200,100))
    surf_rect2=surface2.get_rect(center=(1000,200))
    surface2.fill('grey')
    pygame.draw.rect(surface2,'yellow',surface2.get_rect(),10)     
    surface2.blit(Duo_text,Duo_text_rect)

    screen.blit(surface2,surf_rect2)
    
    for ev in pygame.event.get():
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if PvP_text_rect.collidepoint(mouse_pos):
                PvP=True
                Duo=False

            if  Duo_text_rect.collidepoint(mouse_pos):
                Duo=True
                PvP=False


    screen.blit(PvP_text, PvP_text_rect)
    screen.blit(Duo_text, Duo_text_rect)

    if PvP or Duo:
        play_text=font2.render("Press space to play", True, (20, 20, 255))
        play_text_rect=play_text.get_rect(center=(600,600))
        screen.blit(play_text, play_text_rect)

    pygame.display.flip()



done = False
while not done:

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            done = True
        if ev.type == pygame.MOUSEBUTTONDOWN and SCHERMATA_INIZIALE==True:
                SCHERMATA_INIZIALE = False
                SCHERMATA_MENU = True

    if SCHERMATA_INIZIALE:
        TITLE_SCREEN()

    elif SCHERMATA_MENU:
        OPTIONS_MENU()

    pygame.display.flip()



pygame.quit()
sys.exit()


