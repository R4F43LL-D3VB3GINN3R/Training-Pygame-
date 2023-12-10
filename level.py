#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# [IMPORTS] #

import pygame
from tiles import Tile
from settings import *

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
class Level(pygame.sprite.Sprite):
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# [OBJECTS] #
    
    def __init__(self):
        super().__init__()
        self.tile = Tile(600, 400, 50, 50, (0, 0, 255), 0)
        self.map = stage_001
        self.rect_size = self.tile.height 

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# [METHOD: 001] #

    def printrect(self, surface):

         for row_index, row in enumerate(self.map):
            for col_index, cell in enumerate(row):
                x = col_index * self.rect_size
                y = row_index * self.rect_size

                if cell == 'X':
                    pygame.draw.rect(surface, (0, 0, 255), pygame.Rect(x, y, self.rect_size, self.rect_size))

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# [METHOD: 002] #

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# [METHOD: 004] #

    def run(self, surface):

        self.tile.run(surface)
        self.printrect(surface)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
