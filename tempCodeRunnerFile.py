import pygame, sys
from pygame.locals import *
from classe_player import Player

pygame.init()

screen = pygame.display.set_mode((1200, 750))
pygame.display.set_caption("TRON RACER")
clock=pygame.time.Clock()

Initial_Screen=pygame.image.load('Schermata_inizio.jpg').convert_alpha()
space=pygame.image.load('menu.jpg').convert_alpha()
space=pygame.transform.scale(space, (1200,750))

game_name=pygame.image.load('TRON_RACER.jpg')
game_name_rect = game_name.get_rect(center=(600, 400))

font1=pygame.font.Font('Pixeltype.ttf', 150)
font2=pygame.font.Font('Pixeltype.ttf', 120)

tron=pygame.image.load('tron2.png').convert_alpha()
tron_rec=tron.get_rect(center=(600,375))

scia1=pygame.image.load('bluecircle.png').convert_alpha()
scia2=pygame.image.load('orangecircle.png').convert_alpha()


end_text1=font1.render('PLAYER1 IS THE WINNER',False,'red')
end_text_rec1=end_text1.get_rect(center=(600,300))

end_text2=font1.render('PLAYER2 IS THE WINNER',False,'red')
end_text_rec2=end_text2.get_rect(center=(600,300))

end_text=font2.render('Press space to play again',False,'white')
end_text_rec=end_text2.get_rect(center=(600,475))

controls1 = {'su': pygame.K_w, 'giù': pygame.K_s, 'sinistra': pygame.K_a, 'destra': pygame.K_d}
controls2 = {'su': pygame.K_UP, 'giù': pygame.K_DOWN, 'sinistra': pygame.K_LEFT, 'destra': pygame.K_RIGHT}

pygame.mixer.music.load("menu_song.ogg")
pygame.mixer.music.play(-1)

player1=Player('triangle1.png', (50,375), scia1)
player2=Player('tronmotorbike.png', (1150,375), scia2)

SCHERMATA_INIZIALE=True
SCHERMATA_MENU=False
INIZIO_PARTITA=False
FINE_PARTITA=False
PvP=False
exit1=False
done = False

def TITLE_SCREEN():
    global SCHERMATA_INIZIALE
    
    for ev in pygame.event.get():
        if ev.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(Initial_Screen, (0, 0))

    screen.blit(game_name, game_name_rect)
    
    pygame.display.flip()

def OPTIONS_MENU():
    global PvP, exit1
    
    for ev in pygame.event.get():
        if ev.type==pygame.QUIT:
            pygame.quit()
            sys.exit()   
    
    
    mouse_pos=pygame.mouse.get_pos()
    screen.blit(space,(0,0)) 
    
    sfon_mot=pygame.Surface((350,750))
    sfon_mot_rec=sfon_mot.get_rect(midbottom=(600,750))
    sfon_mot.fill('black')
    screen.blit(sfon_mot,sfon_mot_rec)
    pygame.draw.line(screen,'white',(420,0), (420, 750),10)
    pygame.draw.line(screen,'white',(780,0), (780, 750),10)
    screen.blit(tron,tron_rec)
    if PvP:
        PvP_color=('red')
        play_text=font2.render("Press space to play", True, 'white')
        play_text_rect=play_text.get_rect(center=(600,600))
        screen.blit(play_text, play_text_rect)

    else:
        PvP_color=(0, 0, 102)
    
    if exit1:
        exit1_color=('red')
        exit_text=font2.render("Press space to exit", True, 'white')
        exit_text_rect=exit_text.get_rect(center=(600,600))
        screen.blit(exit_text, exit_text_rect)
    else:
        exit1_color=(0, 0, 102)

    PvP_text=font2.render("PvP", True, (PvP_color))
    PvP_text_rect=PvP_text.get_rect(center=(200,200))
    
    surface1=pygame.Surface((200,100))
    surf_rect=surface1.get_rect(center=(200,200))
    surface1.fill('grey')
    pygame.draw.rect(surface1,(76,45,125),surface1.get_rect(),5)
    surface1.blit(PvP_text,PvP_text_rect)
    screen.blit(surface1,surf_rect)
    
    exit1_text=font2.render("Exit", True, exit1_color)
    exit1_text_rect=exit1_text.get_rect(center=(1000,200))
    
    surface2=pygame.Surface((200,100))
    surf_rect2=surface2.get_rect(center=(1000,200))
    surface2.fill('grey')
    pygame.draw.rect(surface2,(76,45,125),surface2.get_rect(),5)     
    surface2.blit(exit1_text,exit1_text_rect)
    screen.blit(surface2,surf_rect2)
    


    for ev in pygame.event.get():
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if PvP_text_rect.collidepoint(mouse_pos):
                PvP=True
                exit1=False

            if  exit1_text_rect.collidepoint(mouse_pos):
                exit1=True
                PvP=False


    screen.blit(PvP_text, PvP_text_rect)
    screen.blit(exit1_text, exit1_text_rect)

    
    pygame.display.flip()
    return PvP_text_rect, exit1_text_rect

def GAME_SCREEN():
    global INIZIO_PARTITA,SCHERMATA_MENU 
    screen.fill('black')

    keys = pygame.key.get_pressed()
    
    player1.movimenti(keys, controls1)
    player2.movimenti(keys, controls2)

    player1.disegno_player_e_scia(screen)
    player1.disegno_player_e_scia(screen)


    if player1.controllo_collisioni(player2.trail_pos):
            INIZIO_PARTITA = False
            display_end_screen(winner=1)

    if player2.controllo_collisioni(player1.trail_pos):
            INIZIO_PARTITA = False
            display_end_screen(winner=2)

    pygame.display.flip()


def display_end_screen(winner):
    global SCHERMATA_MENU, INIZIO_PARTITA, FINE_PARTITA
    player1.trail_pos.clear()
    player2.trail_pos.clear()
    screen.fill('black')

    if winner == 1:
        screen.blit(end_text1, end_text_rec1)
    else:
        screen.blit(end_text2, end_text_rec2)
    screen.blit(end_text, end_text_rec)

    FINE_PARTITA=True

    pygame.display.flip() 

PvP_text_rect, exit1_text_rect = None, None

while not done:

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            done=True
            
        elif SCHERMATA_INIZIALE and ev.type == pygame.MOUSEBUTTONDOWN:
            SCHERMATA_INIZIALE = False
            SCHERMATA_MENU = True
            
        elif SCHERMATA_MENU:
            if ev.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if PvP_text_rect and exit1_text_rect:
                    if PvP_text_rect.collidepoint(mouse_pos):
                        PvP = True
                        exit1 = False
                    if exit1_text_rect.collidepoint(mouse_pos):
                        exit1 = True
                        PvP = False
                
            elif ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_SPACE:
                    if PvP:             
                        pygame.mixer.music.load("game_song.ogg")
                        pygame.mixer.music.play(-1)
                        player1.rect.center = (50, 375)
                        player2.rect.center = (1150, 375)                            
                        INIZIO_PARTITA = True
                        SCHERMATA_MENU = False
                    if exit1:
                        pygame.QUIT
                        sys.exit()

        elif FINE_PARTITA and ev.type == pygame.KEYDOWN and ev.key == pygame.K_SPACE:
            FINE_PARTITA = False
            SCHERMATA_MENU=True
            pygame.mixer.music.load("menu_song.ogg")
            pygame.mixer.music.play(-1)


    if SCHERMATA_INIZIALE:
        TITLE_SCREEN()

    elif SCHERMATA_MENU:
        PvP_text_rect, exit1_text_rect = OPTIONS_MENU()

    elif INIZIO_PARTITA:
        GAME_SCREEN()

    clock.tick(60)
        
    pygame.display.flip()



pygame.quit()
sys.exit()

