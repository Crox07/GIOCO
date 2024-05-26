import pygame
import sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((1200, 750))
pygame.display.set_caption("SPACE WARS")

Initial_Screen = pygame.image.load('Schermata_inizio.jpg').convert_alpha()
space = pygame.image.load('space.jpg').convert_alpha()
space = pygame.transform.scale(space, (1200, 750))

font1 = pygame.font.Font('Pixeltype.ttf', 150)
font2 = pygame.font.Font('Pixeltype.ttf', 120)

SCHERMATA_INIZIALE = True
SCHERMATA_MENU = False
INIZIO_PARTITA = False
PvP = False
Duo = False

def TITLE_SCREEN():
    screen.blit(Initial_Screen, (0, 0))
    game_name = font1.render("Space Wars", True, (0, 0, 102))
    game_name_rect = game_name.get_rect(center=(600, 400))
    pygame.draw.rect(screen, (102, 204, 204), game_name_rect)
    pygame.draw.rect(screen, 'black', game_name_rect, 3)
    screen.blit(game_name, game_name_rect)
    pygame.display.flip()

def OPTIONS_MENU():
    global PvP, Duo

    mouse_pos = pygame.mouse.get_pos()
    screen.blit(space, (0, 0))

    PvP_color = 'red' if PvP else (0, 0, 102)
    Duo_color = 'red' if Duo else (0, 0, 102)

    PvP_text = font2.render("PvP", True, PvP_color)
    PvP_text_rect = PvP_text.get_rect(center=(200, 200))
    surface1 = pygame.Surface((200, 100))
    surf_rect1 = surface1.get_rect(center=(200, 200))
    surface1.fill('grey')
    pygame.draw.rect(surface1, 'yellow', surface1.get_rect(), 3)
    surface1.blit(PvP_text, PvP_text_rect)
    screen.blit(surface1, surf_rect1)

    Duo_text = font2.render("Duo", True, Duo_color)
    Duo_text_rect = Duo_text.get_rect(center=(1000, 200))
    surface2 = pygame.Surface((200, 100))
    surf_rect2 = surface2.get_rect(center=(1000, 200))
    surface2.fill('grey')
    pygame.draw.rect(surface2, 'yellow', surface2.get_rect(), 3)
    surface2.blit(Duo_text, Duo_text_rect)
    screen.blit(surface2, surf_rect2)

    if PvP or Duo:
        play_text = font2.render("Press space to play", True, 'white')
        play_text_rect = play_text.get_rect(center=(600, 600))
        screen.blit(play_text, play_text_rect)

    pygame.display.flip()

def GAME_SCREEN():
    screen.fill('black')
    # Add game logic and rendering here
    pygame.display.flip()

done = False
while not done:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            done = True
        if SCHERMATA_INIZIALE and ev.type == pygame.MOUSEBUTTONDOWN:
            SCHERMATA_INIZIALE = False
            SCHERMATA_MENU = True
        if SCHERMATA_MENU:
            if ev.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if PvP_text_rect.collidepoint(mouse_pos):
                    PvP = True
                    Duo = False
                if Duo_text_rect.collidepoint(mouse_pos):
                    Duo = True
                    PvP = False
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_SPACE and (PvP or Duo):
                    SCHERMATA_MENU = False
                    INIZIO_PARTITA = True

    if SCHERMATA_INIZIALE:
        TITLE_SCREEN()
    elif SCHERMATA_MENU:
        OPTIONS_MENU()
    elif INIZIO_PARTITA:
        GAME_SCREEN()

pygame.quit()
sys.exit()

