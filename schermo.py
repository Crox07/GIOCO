import pygame, sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((1200, 750))

pygame.display.set_caption("SPACE WARS")

clock=pygame.time.Clock()

Initial_Screen=pygame.image.load('Schermata_inizio.jpg').convert_alpha()
space=pygame.image.load('space.jpg').convert_alpha()
space=pygame.transform.scale(space, (1200,750))

#options_screen=pygame.image.load('stars.jpg').convert_alpha()

font1=pygame.font.Font('Pixeltype.ttf', 150)
font2=pygame.font.Font('Pixeltype.ttf', 120)

#class player1:
  #  def __init__(self, posx, posy, width = 100, height = 100) -> None:
    #    self.image = pygame.image.load(PLAYER1)

player1=pygame.image.load('triangle1.png').convert_alpha()
player1_rec=player1.get_rect(center=(50,375))

player2=pygame.image.load('triangle1.png').convert_alpha()
player2_rec=player2.get_rect(center=(1150,375))

SCHERMATA_INIZIALE=True
SCHERMATA_MENU=False
INIZIO_PARTITA=False
PvP=False
Duo=False

def TITLE_SCREEN():
    global SCHERMATA_INIZIALE
    for ev in pygame.event.get():
        if ev.type==pygame.QUIT:
            pygame.quit()
            sys.exit()



    screen.blit(Initial_Screen, (0, 0))

    game_name = font1.render("Space Wars", True, (0, 0, 102))
    game_name_rect = game_name.get_rect(center=(600, 400))

    riq = pygame.Surface((600, 250))
    riq_rec = riq.get_rect(center=(600, 375))
    riq.fill('WHITE')
    pygame.draw.rect(riq, (102, 204, 204), riq.get_rect(), 10)
    screen.blit(riq, riq_rec)
    screen.blit(game_name, game_name_rect)
    
    pygame.display.flip()

def OPTIONS_MENU():
    global PvP, Duo
    
    for ev in pygame.event.get():
        if ev.type==pygame.QUIT:
            pygame.quit()
            sys.exit()   
    
    
    mouse_pos=pygame.mouse.get_pos()

    screen.blit(space,(0,0)) 
    
    if PvP:
        PvP_color=('red') 

    else:
        PvP_color=(0, 0, 102)
    
    if Duo:
        Duo_color=('red')
    else:
        Duo_color=(0, 0, 102)

    PvP_text=font2.render("PvP", True, (PvP_color))
    PvP_text_rect=PvP_text.get_rect(center=(200,200))
    
    surface1=pygame.Surface((200,100))
    surf_rect=surface1.get_rect(center=(200,200))
    surface1.fill('grey')
    pygame.draw.rect(surface1,'yellow',surface1.get_rect(),3)
    surface1.blit(PvP_text,PvP_text_rect)
    screen.blit(surface1,surf_rect)
    
    Duo_text=font2.render("Duo", True, Duo_color)
    Duo_text_rect=Duo_text.get_rect(center=(1000,200))
    
    surface2=pygame.Surface((200,100))
    surf_rect2=surface2.get_rect(center=(1000,200))
    surface2.fill('grey')
    pygame.draw.rect(surface2,'yellow',surface2.get_rect(),3)     
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
        play_text=font2.render("Press space to play", True, 'white')
        play_text_rect=play_text.get_rect(center=(600,600))
        screen.blit(play_text, play_text_rect)
    
    pygame.display.flip()
    return PvP_text_rect, Duo_text_rect

def GAME_SCREEN():
    global player1_rec, player2_rec, INIZIO_PARTITA,SCHERMATA_MENU
    
    screen.fill('black')
    
    if player1_rec.bottom > 750:
        player1_rec.bottom=750
    if player1_rec.top < 0:
        player1_rec.top=0   
    if player1_rec.left < 0:
        player1_rec.left=0    
    if player1_rec.right > 1200:
        player1_rec.right=1200    

    if player2_rec.bottom > 750:
        player2_rec.bottom=750
    if player2_rec.top < 0:
        player2_rec.top=0   
    if player2_rec.left < 0:
        player2_rec.left=0    
    if player2_rec.right > 1200:
        player2_rec.right=1200     
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player1_rec.y -= 5
    if keys[pygame.K_s]:
        player1_rec.y += 5
    if keys[pygame.K_a]:
        player1_rec.x -= 5
    if keys[pygame.K_d]:
        player1_rec.x += 5


    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player2_rec.y -= 5
    if keys[pygame.K_DOWN]:
        player2_rec.y += 5
    if keys[pygame.K_LEFT]:
        player2_rec.x -= 5
    if keys[pygame.K_RIGHT]:
        player2_rec.x += 5
    
    clock.tick(60)
    screen.blit(player1, player1_rec)
    screen.blit(player2,player2_rec)
    
    if player1_rec.colliderect(player2_rec):
        INIZIO_PARTITA = False
        SCHERMATA_MENU = True
        
        pygame.display.flip()

done = False
PvP_text_rect, Duo_text_rect = None, None

while not done:

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            done=True
        
        if SCHERMATA_INIZIALE and ev.type == pygame.MOUSEBUTTONDOWN:
            SCHERMATA_INIZIALE = False
            SCHERMATA_MENU = True
        
        if SCHERMATA_MENU:
            if ev.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if PvP_text_rect and Duo_text_rect:
                    if PvP_text_rect.collidepoint(mouse_pos):
                        PvP = True
                        Duo = False
                    if Duo_text_rect.collidepoint(mouse_pos):
                        Duo = True
                        PvP = False
            
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_SPACE and (PvP or Duo):
                    
                    player1_rec.center = (50, 375)
                    player2_rec.center = (1150, 375)                    
                    
                    
                    INIZIO_PARTITA = True
                    SCHERMATA_MENU = False


    if SCHERMATA_INIZIALE:
        TITLE_SCREEN()

    elif SCHERMATA_MENU:
        PvP_text_rect, Duo_text_rect =OPTIONS_MENU()

    elif INIZIO_PARTITA:
        GAME_SCREEN()

    
    pygame.display.flip()



pygame.quit()
sys.exit()


