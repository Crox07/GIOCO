import pygame

class Player:
    def __init__(self, immagine_player, pos_iniziale, trail_image):
        self.image=pygame.image.load(immagine_player).convert_alpha()
        self.rect=self.image.get_rect(center=pos_iniziale)
        self.start_pos = pos_iniziale
        self.trail_pos=[]
        self.direction = {'su': False, 'giù': False, 'destra': False, 'sinistra':False}
        self.trail_image= trail_image
        self.punti=0

    def add_point(self):
        self.punti+=1
    
    def vittoria(self):
        return self.punti >=3
    
    def reset(self):

        self.rect.center = self.start_pos
        self.trail_pos.clear()
        self.reset_direzioni()
        
    def controllo_bordi(self):

        if self.rect.bottom > 750:
            self.rect.bottom = 750
            self.reset_direzioni()
            self.direction['su'] = True

        if self.rect.top < 0:
            self.rect.top = 0
            self.reset_direzioni()
            self.direction['giù'] = True

        if self.rect.left < 0:
            self.rect.left = 0
            self.reset_direzioni()
            self.direction['destra'] = True

        if self.rect.right > 1200:
            self.rect.right = 1200
            self.reset_direzioni()
            self.direction['sinistra'] = True 

    def movimenti(self, keys, tasto):

        self.controllo_bordi()

        if keys[tasto['su']] or self.direction['su']:
            self.rect.y -= 5
            self.reset_direzioni()
            self.direction['su']=True

        if keys[tasto['giù']] or self.direction['giù']:
            self.rect.y += 5
            self.reset_direzioni()
            self.direction['giù']=True

        if keys[tasto['sinistra']] or self.direction['sinistra']:
            self.rect.x -= 5
            self.reset_direzioni()
            self.direction['sinistra']=True

        if keys[tasto['destra']] or self.direction['destra']:
            self.rect.x += 5
            self.reset_direzioni()
            self.direction['destra']=True

        self.trail_pos.append((self.rect.x, self.rect.y))
            
        if len(self.trail_pos) > 80:
            self.trail_pos.pop(0) 

    def reset_direzioni(self):
        for key in self.direction.keys():
            self.direction[key]=False

    def disegno_player_e_scia(self, schermo):
        for posizione in self.trail_pos:
            trail_rect= self.trail_image.get_rect(topleft=posizione)
            schermo.blit(self.trail_image, trail_rect)
        schermo.blit(self.image, self.rect)

    def controllo_collisioni(self, scia_avversaria_pos):
        for posizione in scia_avversaria_pos:
            trail_rect= self.trail_image.get_rect(topleft=posizione)
            if self.rect.colliderect(trail_rect):
                return True
        return False 
