import pygame
from assets import assets
from settings import *

class SpriteSheet:
    def __init__(self, name, count=0, dimension=0, scale=1, speed=0.1, state='default'):
        self.name = name
        self.count = count
        self.dimension = dimension
        self.scale = scale
        self.speed = speed
        self.pos = 0
        self.state = state
        self.assets = assets[name]
        self.sprites = {}

    def set_state(self, state):
        self.state = state
        self.pos = 0

    def animate(self):
        self.pos += self.speed
        if self.pos >= self.count:
            self.pos = 0
        return self.sprites[self.state][int(self.pos)]
    
class PlayerSheet(SpriteSheet):
    def __init__(self):
        super().__init__('player', count=11, speed=0.2, state='running')
        self.sprites = self.assets

class CoinSheet(SpriteSheet):
    def __init__(self):
        super().__init__('coin', count=5, dimension=16, scale=3)
        # self.sheet = assets[self.name][self.state]
        # self.count = self.sheet.get_width() // self.dimension
        # self.sprites = {}
        # for i in range(self.sheet.get_width()//self.dimension):
        #     self.sprites['default'].append(pygame.transform.scale_by(
        #         self.sheet.subsurface(pygame.Rect((self.dimension * i, 0), (self.dimension, self.dimension))), self.scale))
        self.sprites = {'default': []}
        for state in self.assets:
            for i in range(self.count):
                sprite = pygame.transform.scale_by(
                    self.assets[state].subsurface(pygame.Rect((self.dimension * i, 0), (self.dimension, self.dimension))), self.scale)
                pygame.Surface.set_colorkey(sprite, PLAYER_COLORKEY)
                self.sprites[state].append(sprite)

        
    
# class PlayerSheet(SpriteSheet):
#     def __init__(self):
#         super().__init__('player', 16, 16, 4, scale=8, state='forward')

#         self.sprites = {"forward": [],
#                         "left": [],
#                         "right": []}
        
#         for i in range(self.count): 
#             self.sprites['forward'].append(pygame.transform.scale_by(
#                 self.sheet.subsurface(pygame.Rect((self.width * i, self.height * 4), (self.width, self.height))), self.scale))
#             self.sprites['left'].append(pygame.transform.scale_by(
#                 self.sheet.subsurface(pygame.Rect((self.width * i, self.height * 3), (self.width, self.height))), self.scale))
#             self.sprites['right'].append(pygame.transform.scale_by(
#                 self.sheet.subsurface(pygame.Rect((self.width * i, self.height * 5), (self.width, self.height))), self.scale))
            
#         for state in self.sprites:
#             for img in self.sprites[state]:
#                 pygame.Surface.set_colorkey(img, PLAYER_COLORKEY)



