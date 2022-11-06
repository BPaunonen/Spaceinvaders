import pygame
import sys
import stats
# sound = pygame.mixer.Sound('Spaceinvaders/images/blaster.wav')
class Events:
    # pygame.init()
    # pygame.mixer.init(44100, -16,2,2512)
    # pygame.time.sleep(5)
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
                    # sound.play()
                    game_ship.fire_bullet()
                    
        
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    game_ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    game_ship.moving_left = False