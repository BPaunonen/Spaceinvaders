import pygame
from ship import Ship
from settings import Settings
from events import Events
from alien import Alien
from UI import Text

class SpaceInvaders:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption(self.settings.caption)
        self.bg_image = pygame.image.load("Spaceinvaders/images/starfield.png").convert_alpha()
        self.ship = Ship(self)
        self.events = Events()
        self.aliens = pygame.sprite.Group()
        self.create_alien()
        self.alien_text = Text(self, 200, 150)

    def create_alien(self):
        self.alien = Alien(self)
        self.aliens.add(self.alien)
        
    def run(self):
        
        while True:
            self.events.check_keys(self.ship)
            self.alien_text.blit()
            self.screen.blit(self.bg_image, self.screen.get_rect())
            self.aliens.draw(self.screen)
            self.ship.blit()
            self.ship.update()
            self.ship.update_bullets() # kutsuu jokaisen bulletin update()
            self.alien.update_alien()
            for b in self.ship.bullets:
                b.draw_bullet()
            
            pygame.display.flip()
        
if __name__ == '__main__':
    game = SpaceInvaders()
    game.run()