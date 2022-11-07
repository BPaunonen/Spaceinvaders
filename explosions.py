import pygame
from pygame.sprite import Sprite

class Explosion(Sprite):
    def __init__(self,game):
        super().__init__()
        self.anim = {}
        self.anim['alien'] = [] #dictionary, jotta voidaan esim.
        self.anim['ship'] = [] #asettaa eri animaatioita helposti      
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50 #ms (1000ms = 1s)
        self.game = game

        for i in range(9): #0-8
            filename = f"regularExplosion0{i}.png"
            image = pygame.image.load("Spaceinvaders/images/"+filename).convert_alpha()
            scaled_image = pygame.transform.scale(image,(60,58))
            self.anim['alien'].append(scaled_image)
            self.anim['ship'].append(scaled_image)
            
    def set_explosion_center_and_object(self,center,object):
        self.object = object #'alien'                              
        self.image = self.anim[self.object][0] #asetetaan 1.kuva
        self.rect = self.image.get_rect()
        self.rect.center = center
    
    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate: #50ms on kulunut
            self.last_update = now #resetoidaan aika nollaan
            self.frame +=1
            if self.frame == len(self.anim[self.object]):#jos ollaan viimeisessä framessa/kuvassa                
                self.kill() #poistaa spriten kaikista Groupeista
            else:
                center = self.rect.center
                self.image = self.anim[self.object][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center