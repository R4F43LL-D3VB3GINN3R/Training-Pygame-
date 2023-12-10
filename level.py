#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# [IMPORTS] #

import pygame
from tiles import Tile

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
class Level(pygame.sprite.Sprite):
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# [OBJECTS] #
    
    def __init__(self):
        super().__init__()

        self.tile = Tile(600, 400, 50, 50, (0, 0, 255), 0)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# [METHOD: 001] #



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# [METHOD: 002] #



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# [METHOD: 003] #



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# [METHOD: 004] #

    def run(self, surface):

        self.tile.run(surface)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#