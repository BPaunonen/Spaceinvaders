import pygame



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
        
        
    def blit(self):
        self.screen.blit(self.image, self.rect)
        
    def update(self):
        if self.moving_right:
            self.x += self.settings.ship_speed
        elif self.moving_right and self.rect.midbottom > self.screen_rect.right:
            self.rect.midbottom = self.screen_rect.left 
            self.x += self.settings.ship_speed 
            
        # if self.moving_right and self.rect.right < self.screen_rect.right:
        #     self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        #napataan talteen pelkkä kokonaisluku desimaaluluvusta    
        self.rect.x = self.x