import pygame
class Text:
    def __init__(self, game, x,y):
        self.screen = game.screen
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        # self.font = pygame.font.Font('font_name.ttf, 48)
        self.x = x
        self.y = y
        
    def blit(self):
        text = self.font.render("ASD", True, self.text_color)
        text_rect = text.get_rect()
        text_rect.topleft = (self.x, self.y)
        self.screen.blit(text, text_rect)