import pygame
from assets import assets
from settings import *

class SpriteSheet:
    def __init__(self, name, count=0, dimension=0, init_scale=1, speed=0.1, state='default'):
        self.name = name
        self.count = count
        self.dimension = dimension
        self.init_scale = init_scale
        self.speed = speed
        self.pos = 0
        self.state = state
        self.assets = assets[name]
        self.sprites = {}

    def set_state(self, state):
        self.state = state
        self.pos = 0

    def animate(self, scale=1):
        self.pos += self.speed
        if self.pos >= self.count:
            self.pos = 0
        return pygame.transform.scale_by(self.sprites[self.state][int(self.pos)], scale)
    
class PlayerSheet(SpriteSheet):
    def __init__(self):
        super().__init__('player', count=11, speed=0.2, state='running')
        self.sprites = self.assets

class CoinSheet(SpriteSheet):
    def __init__(self):
        super().__init__('coin', count=5, dimension=16, init_scale=3)
        for state in self.assets:
            self.sprites[state] = []
            for i in range(self.count):
                sprite = pygame.transform.scale_by(
                    self.assets[state].subsurface(pygame.Rect((self.dimension * i, 0), (self.dimension, self.dimension))), self.init_scale)
                # pygame.Surface.set_colorkey(sprite, )
                self.sprites[state].append(sprite)

class TorchSheet(SpriteSheet):
    def __init__(self):
        super().__init__('torch', count=8, dimension=64)
        for state in self.assets:
            self.sprites[state] = []
            for row in range(2):
                for i in range(4):
                    sprite = pygame.transform.scale_by(
                        self.assets[state].subsurface(pygame.Rect((self.dimension * i, self.dimension * row), (self.dimension, self.dimension))), 
                        self.init_scale)
                    # pygame.Surface.set_colorkey(sprite, )
                    self.sprites[state].append(sprite)