import pygame 
from settings import Settings
from ship import Ship
from events import Events
from alien import Alien
from UI import Text
from stats import Stats

class SpaceInvaders:
    def __init__(self):
        # pygamen initialisointi pitää tehdä aina ensimmäisenä
        pygame.init()         
        # luodaan olio Settings-luokasta
        self.settings = Settings()
        # asetetaan resoluutio
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        # asetetaan yläpalkkiin pelin nimi
        pygame.display.set_caption(self.settings.caption)
        # asetetaan taustakuva muuttujaan
        self.bg_image = pygame.image.load("Spaceinvaders/images/bg.jpg").convert_alpha()
        self.ship = Ship(self) 
        self.events = Events()
        self.aliens = pygame.sprite.Group()
        self.explosions = pygame.sprite.Group()
        self.create_alien_fleet()

        self.txt_bullets_fired = Text(self.screen,0,0)
        self.txt_score = Text(self.screen,700,0)  #parempi olisi käyttää rect:in topright
                #(tekstin rect:in topright = screen_rect.topright )

        self.stats = Stats()

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
            self.aliens.add(alien) #lisätään ko. alien aliens-spritegroup:iin
    def change_fleet_direction(self):
        for alien in self.aliens:
            alien.rect.y += alien.width
            alien.direction = -alien.direction
            
    def run(self): 
        while True: # main loop
            self.events.check_keys(self.ship)       #täytetään ruutu sinisellä värillä        
            self.screen.blit(self.bg_image, self.screen.get_rect())
            self.aliens.draw(self.screen)
    
            #tekstit
            self.txt_bullets_fired.blit("BULLETS FIRED",self.stats.bullets_fired)
            self.txt_score.blit("SCORE",self.stats.score)
            self.aliens.update()
            self.explosions.update()
            self.explosions.draw(self.screen)
            self.ship.blit()                        #piirretään alus ruudulle        
            self.ship.update() 
            self.ship.update_bullets() #kutsuu jokaisen 
                                        #bulletin update()-metodia                    
            for b in self.ship.bullets:  #.sprites()
                b.draw_bullet() #piirretään kukin bullet

            pygame.display.flip()                 # päivitetään päivittyneet kohdat

# ainoastaan, mikäli tätä tiedostoa yritetään ajaa:
if __name__ == '__main__':
    # luodaan olio eli instanssi luokasta:
    game = SpaceInvaders()
    # kutsutaan luokan metodia (metodi = luokan funktio)
    game.run()