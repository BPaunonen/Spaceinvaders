
# 4) Luo Settings-luokkaan myös check_keys()-niminen metodi, 
# ja siirrä nykyisen run()-metodin sisältö sinne. Kutsu metodia run()-metodissa.
# -> main.py -tiedoston luettavuus pysyy näin siistimpänä, 
# ja koodin "refaktorointi" on muutenkin hyvää harjoitusta!
import pygame
import sys
from ship import Ship

class Settings():
    def __init__(self):
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.caption = ("Space Invaders")
        self.bg_color = (230, 230, 230)
        
        #ship settings
        self.ship_speed = 0.5
        
    def check_keys(self, game_ship):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    game_ship.moving_right = True
                if event.key == pygame.K_LEFT:
                    game_ship.moving_left = True
            
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    game_ship.moving_right = False
                if event.key == pygame.K_LEFT:
                    game_ship.moving_left = False