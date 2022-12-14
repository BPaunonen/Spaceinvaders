import pygame
from ship import Ship

class Settings():
    def __init__(self):
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.caption = ("Space Invaders")
        
        #bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0, 204, 255)
        self.bullet_speed = 0.8
        self.bullets_allowed = 3 
        
        #ship settings
        self.ship_speed = 0.5
        
        self.alien_speed = 0.3
        
    