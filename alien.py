import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    total_number_of_aliens = 0
    
    def __init__(self,game):
        super().__init__() #call sprite class constructor 
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings
        self.image = pygame.image.load('Spaceinvaders/images/ufo.png').convert_alpha() 
        self.rect = self.image.get_rect()
        self.rect.midtop = self.screen_rect.midtop
        # self.rect.x = self.rect.width #60
        # self.rect.y = self.rect.height #58
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.settings = game.settings
        
    def blit_alien(self):
        self.screen.blit(self.image, self.rect)
        
    def update_alien(self):   
        
        if self.rect.right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
            self.rect.x = self.x
        else:
            self.x -= self.settings.ship_speed
            self.rect.x = self.x   #napataan talteen pelkkä kokonaisluku desimaaluluvusta
