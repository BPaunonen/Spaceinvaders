import pygame
import sys

class Events:
    def check_keys(self, game_ship):       
    # vastaanotetaan näppäin- ja hiirikomentoja
        for event in pygame.event.get(): 
            
            # mikäli ikkuna suljetaan
            if event.type == pygame.QUIT:
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    game_ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    game_ship.moving_left = True
                elif event.key == pygame.K_SPACE:
                    game_ship.fire_bullet()
        
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    game_ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    game_ship.moving_left = False