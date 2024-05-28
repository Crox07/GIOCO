import pygame, sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((1200, 750))

pygame.display.set_caption("TRON RACER")

clock=pygame.time.Clock()

Initial_Screen=pygame.image.load('Schermata_inizio.jpg').convert_alpha()
space=pygame.image.load('menu.jpg').convert_alpha()
space=pygame.transform.scale(space, (1200,750))

game_name=pygame.image.load('TRON_RACER.jpg')
game_name_rect = game_name.get_rect(center=(600, 400))

#options_screen=pygame.image.load('stars.jpg').convert_alpha()

font1=pygame.font.Font('Pixeltype.ttf', 150)
font2=pygame.font.Font('Pixeltype.ttf', 120)

#class player1:
  #  def __init__(self, posx, posy, width = 100, height = 100) -> None:
    #    self.image = pygame.image.load(PLAYER1)

player1=pygame.image.load('triangle1.png').convert_alpha()
player1_rec=player1.get_rect(center=(50,375))

tron=pygame.image.load('tron2.png').convert_alpha()
tron_rec=tron.get_rect(center=(600,375))

player2=pygame.image.load('triangle1.png').convert_alpha()
player2_rec=player2.get_rect(center=(1150,375))

scia1=pygame.image.load('triangle1.png').convert_alpha()
scia1_rect=scia1.get_rect(center=(50,375))

scia2=pygame.image.load('triangle1.png').convert_alpha()
scia2_rect=scia2.get_rect(center=(50,375))



end_text1=font1.render('PLAYER1 IS THE WINNER',False,'red')
end_text_rec1=end_text1.get_rect(center=(600,300))

end_text2=font1.render('PLAYER2 IS THE WINNER',False,'red')
end_text_rec2=end_text2.get_rect(center=(600,300))

end_text=font2.render('Press space to play again',False,'white')
end_text_rec=end_text2.get_rect(center=(600,475))

trail1_positions=[]
trail2_positions=[]


SCHERMATA_INIZIALE=True
SCHERMATA_MENU=False
INIZIO_PARTITA=False
FINE_PARTITA=False
PvP=False
Duo=False

d={}
d['su']=False
d['giù']=False
d['destra']=False
d['sinistra']=False  
d2={}
d2['su']=False
d2['giù']=False
d2['destra']=False
d2['sinistra']=False 

pygame.mixer.music.load("menu_song.ogg")
pygame.mixer.music.play(-1)

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
    global PvP, Duo
    
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
    pygame.draw.rect(surface1,(76,45,125),surface1.get_rect(),5)
    surface1.blit(PvP_text,PvP_text_rect)
    screen.blit(surface1,surf_rect)
    
    Duo_text=font2.render("Duo", True, Duo_color)
    Duo_text_rect=Duo_text.get_rect(center=(1000,200))
    
    surface2=pygame.Surface((200,100))
    surf_rect2=surface2.get_rect(center=(1000,200))
    surface2.fill('grey')
    pygame.draw.rect(surface2,(76,45,125),surface2.get_rect(),5)     
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

def GAME_SCREEN(d,d2):
    global player1_rec, player2_rec, INIZIO_PARTITA,SCHERMATA_MENU, scia1_rect, trail1_positions, scia2_rect, trail2_positions
    screen.fill('black')
    
    if player1_rec.bottom > 750:
        player1_rec.bottom=750
        for key in d.keys():
            d[key] = False
        d['su']=True

    if player1_rec.top < 0:
        player1_rec.top=0  
        for key in d.keys():
            d[key] = False
        d['giù']=True

    if player1_rec.left < 0:
        player1_rec.left=0 
        for key in d.keys():
            d[key] = False
        d['destra']=True

    if player1_rec.right > 1200:
        player1_rec.right=1200    
        for key in d.keys():
            d[key] = False
        d['sinistra']=True

    if player2_rec.bottom > 750:
        player2_rec.bottom=750
        for key in d2.keys():
            d2[key] = False
        d2['su']=True

    if player2_rec.top < 0:
        player2_rec.top=0
        for key in d2.keys():
            d2[key] = False
        d2['giù']=True

    if player2_rec.left < 0:
        player2_rec.left=0
        for key in d2.keys():
            d2[key] = False
        d2['destra']=True

    if player2_rec.right > 1200:
        player2_rec.right=1200     
        for key in d2.keys():
            d2[key] = False
        d2['sinistra']=True


    
    keys = pygame.key.get_pressed()

    
    if keys[pygame.K_UP] or d2['su']:
        player2_rec.y -= 5
        for key in d2:
            d2[key]=False
        d2['su']=True
        
    if keys[pygame.K_DOWN] or d2['giù']:
        player2_rec.y += 5
        for key in d2:
            d2[key]=False
        d2['giù']=True   
    if keys[pygame.K_LEFT] or d2['sinistra']:
        player2_rec.x -= 5
        for key in d2:
            d2[key]=False
        d2['sinistra']=True    
    if keys[pygame.K_RIGHT]or d2['destra']:
        player2_rec.x += 5
        for key in d2:
            d2[key]=False
        d2['destra']=True
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] or d['su']:
        player1_rec.y -= 5
        for key in d:
            d[key]=False
        d['su']=True
    if keys[pygame.K_s] or d['giù']:
        player1_rec.y += 5
        for key in d:
            d[key]=False
        d['giù']=True
    if keys[pygame.K_a] or d['sinistra']:
        player1_rec.x -= 5
        for key in d:
            d[key]=False
        d['sinistra']=True
    if keys[pygame.K_d] or d['destra']:
        player1_rec.x += 5
        for key in d:
            d[key]=False
        d['destra']=True

    screen.blit(player1, player1_rec)
    screen.blit(player2,player2_rec)

    trail1_positions.append((player1_rec.x, player1_rec.y))
    trail2_positions.append((player2_rec.x, player2_rec.y))

    if len(trail1_positions) > 80:
        trail1_positions.pop(0) 

    if len(trail2_positions) > 80:
        trail2_positions.pop(0)
    
    for posizione in trail1_positions:
        scia1_rect.topleft = posizione
        screen.blit(scia1,scia1_rect)
        if player2_rec.colliderect(scia1_rect):
            INIZIO_PARTITA = False
            display_end_screen(winner=1)
    
    for posizione in trail2_positions:
        scia2_rect.topleft = posizione
        screen.blit(scia2,scia2_rect)
        if player1_rec.colliderect(scia2_rect):
            INIZIO_PARTITA = False
            display_end_screen(winner=2)
          
    
    pygame.display.flip()

def display_end_screen(winner):
    global SCHERMATA_MENU, INIZIO_PARTITA, FINE_PARTITA, trail1_positions, trail2_positions
    trail1_positions.clear()
    trail2_positions.clear() 
    screen.fill('black')
    if winner == 1:
        screen.blit(end_text1, end_text_rec1)
    else:
        screen.blit(end_text2, end_text_rec2)
    screen.blit(end_text, end_text_rec)

    FINE_PARTITA=True

    for key in d.keys():
        d[key] = False

    for key in d2.keys():
        d2[key] = False
    
    pygame.display.flip() 


done = False
PvP_text_rect, Duo_text_rect = None, None

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
                if PvP_text_rect and Duo_text_rect:
                    if PvP_text_rect.collidepoint(mouse_pos):
                        PvP = True
                        Duo = False
                    if Duo_text_rect.collidepoint(mouse_pos):
                        Duo = True
                        PvP = False
                
            elif ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_SPACE and (PvP or Duo):
                                     
                    pygame.mixer.music.load("game_song.ogg")
                    pygame.mixer.music.play(-1)
                
                    player1_rec.center = (50, 375)
                    player2_rec.center = (1150, 375)                    
                                     
                    INIZIO_PARTITA = True
                    SCHERMATA_MENU = False

        elif FINE_PARTITA and ev.type == pygame.KEYDOWN and ev.key == pygame.K_SPACE:
            FINE_PARTITA = False
            SCHERMATA_MENU=True
            pygame.mixer.music.load("menu_song.ogg")
            pygame.mixer.music.play(-1)


    if SCHERMATA_INIZIALE:
        TITLE_SCREEN()

    elif SCHERMATA_MENU:
        PvP_text_rect, Duo_text_rect =OPTIONS_MENU()

    elif INIZIO_PARTITA:
        GAME_SCREEN(d,d2)

    clock.tick(60)
        
    pygame.display.flip()



pygame.quit()
sys.exit()



