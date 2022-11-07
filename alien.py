import pygame
from pygame.sprite import Sprite
from settings import Settings

class Alien(Sprite):
    def __init__(self,game):
        super().__init__()
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.image = pygame.image.load("Spaceinvaders/images/tie.png").convert_alpha()
        self.rect = self.image.get_rect()
        
        self.rect.midtop = self.screen_rect.midtop 
        # self.rect.x = self.rect.width #60 pikseliä vasemmasta reunasta oikealle
        # self.rect.y = self.rect.height #58 pikseliä yläreunasta alas
        # (eli kuvan leveyden ja korkeuden verran (60x58) )
        self.x = float(self.rect.x)
        self.direction = 1   
        self.settings = Settings()     
        self.game=game
        

    def blit(self):
        self.screen.blit(self.image,self.rect)
    
    def create_alien_fleet(self):
        alien = Alien(self) # tämä alien ei tule alien fleetiin(tätä ei lisätä aliens-sprite group:iin). tässä olio luodaan vain, jotta saadaan selville tarvittava leveys. 
        alien_width = alien.rect.width
        # lasketaan, montako alienia ruutuun mahtuu niin, että molempiin reunoihin jää alienin verran tilaa:
        available_space_x = self.settings.screen_width - (2*alien_width) # jos ruutu on 800 ja alienin leveys 60, available_space_x = 680
        number_of_aliens_x = available_space_x // (2*alien_width) # // on floor division, eli esim. 15//2 tarkoittaa, montako kertaa luku 2 menee lukuun 15 (eli vastaus on 7)
        for alien_number in range(number_of_aliens_x): # käydään läpi kaikki (tässä 5) alienit
            alien = Alien(self) 
            alien.x = alien_width + 2 * alien_width * alien_number # sijoitetaan ko. alienin x-arvo niin, että väliin jää aina alienin verran tilaa 
                                                                  #(huom.x-arvo viittaa alienin vasempaan reunaan, siksi lasketaan 2 alienin verran (alien+alienin verran tyhjää tilaa))
            alien.rect.x = alien.x
            self.game.aliens.add(alien) #lisätään ko. alien aliens-spritegroup:iin
            
    def change_fleet_direction(self):
        for alien in self.game.aliens:
            alien.rect.y += alien.rect.width
            alien.direction = -alien.direction
    
    def check_fleet_edges(self):
        for alien in self.game.aliens:
            if alien.check_edges():
                self.change_fleet_direction()
                break
            
    
    def check_edges(self):
        if self.rect.right >= self.screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):        
        if self.direction==1 and self.rect.right <= self.screen_rect.right:        
            self.x += self.settings.alien_speed 
        elif self.direction==-1 and self.rect.left >=self.screen_rect.left:            
            self.x -= self.settings.alien_speed     
        # else:
        #     self.direction= -self.direction #suunta muutetaan
        #     self.rect.y += self.rect.height

        self.rect.x = self.x
