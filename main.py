import pygame
from ship import Ship
from settings import Settings

class SpaceInvaders:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption(self.settings.caption)
        self.ship = Ship(self)
               
    def run(self):
        while True:
            self.settings.check_keys(self.ship)
            self.screen.fill(self.settings.bg_color)
            self.ship.blit()
            self.ship.update()
            pygame.display.flip()
        
if __name__ == '__main__':
    game = SpaceInvaders()
    game.run()