import pygame
from bullet import Bullet


class Ship:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.image = pygame.image.load('Spaceinvaders/images/ship.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.settings = game.settings
        self.moving_right = False
        self.moving_left = False
        self.x = float(self.rect.x)
        self.settings = game.settings
        self.game = game
        self.bullets = pygame.sprite.Group()
        
    def blit(self):
        self.screen.blit(self.image, self.rect)
        
    def fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self, self.game)
            self.bullets.add(new_bullet) # lisätään new_bullet sprite-grouppiin
        
    def update_bullets(self):
        self.bullets.update()# kutsuu kaikkien bullet instanssien update  metodia
        for b in self.bullets.copy():
            if b.rect.bottom < 0:
                self.bullets.remove(b)
    
    
    def update(self):   
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        #napataan talteen pelkkä kokonaisluku desimaaluluvusta    
        self.rect.x = self.x