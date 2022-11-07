import pygame
from bullet import Bullet
from explosions import Explosion
import time

class Ship:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.image = pygame.image.load('Spaceinvaders/images/xwing.png').convert_alpha()
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
    
    def play(self):
        pygame.mixer.init()
        pygame.mixer.music.load("Spaceinvaders/images/blaster.wav") 
        pygame.mixer.music.play()
        time.sleep(0)
    
    def fire_bullet(self):
        
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self, self.game)
            self.bullets.add(new_bullet) # lisätään new_bullet sprite-grouppiin
            self.play()
            self.game.stats.bullets_fired += 1 
    def update_bullets(self):
        self.bullets.update()# kutsuu kaikkien bullet instanssien update  metodia
        for b in self.bullets.copy():
            if b.rect.bottom < 0:
                self.bullets.remove(b)
        
        collision = pygame.sprite.groupcollide(self.bullets,self.game.aliens,True,True)
        if collision: # ==True
            for aliens in collision.values(): #kaikki alienit mihin osuttiin
                for alien in aliens:                    
                    explosion = Explosion(self.game)
                    explosion.set_explosion_center_and_object(alien.rect.center,'alien')
                    self.game.explosions.add(explosion)
                    self.game.stats.score += 1
            #self.game.create_alien_fleet()
    
    
    def update(self):   
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        if pygame.sprite.spritecollideany(self,  self.game.aliens):
            print("Crash")
        
        #napataan talteen pelkkä kokonaisluku desimaaluluvusta    
        self.rect.x = self.x