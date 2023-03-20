import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    # This is the base class to manage game assets and behaviour

    def __init__(self):
        pygame.init()
        self.settings= Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")
        self.ship= Ship(self)
    
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
        # Fill screen with background color
        self.screen.fill(self.settings.bg)
        self.ship.blitme()
        # Refresh
        pygame.display.flip()

# Driver Code
ai= AlienInvasion()
ai.run_game()