import pygame

# A class to manage the ship
class Ship:
    def __init__(self, ai_game):
        self.screen= ai_game.screen
        self.screen_rect= ai_game.screen.get_rect()

        #Load the ship image
        self.image = pygame.image.load("Alien_Invasion/images/ship.bmp")
        self.rect= self.image.get_rect()

        # Initial position
        self.rect.midbottom = self.screen_rect.midbottom
    
    def blitme(self):
        # Put the ship at current location
        self.screen.blit(self.image, self.rect)