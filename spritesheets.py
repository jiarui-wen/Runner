import pygame
from assets import assets
from settings import *

class Pos_Iterator:
    def __init__(self, count, speed):
        self.pos = 0
        self.count = count
        self.speed = speed

    def update(self):
        self.pos += self.speed
        if self.pos >= self.count:
            self.pos = 0
    
    def get_pos(self):
        return int(self.pos)
    

class Animation:
    def __init__(self, name, speed=0.1, state='default'):
        self.name = name
        self.sprites = assets[name]
        self.speed = speed
        self.state = state
        self.pos = 0

    def set_state(self, state):
        self.state = state
        self.pos = 0

    def animate(self, pos=-1, scale=1):
        if pos < 0: # default
            self.pos += self.speed
            if self.pos >= len(self.sprites[self.state]):
                self.pos = 0
            return pygame.transform.scale_by(self.sprites[self.state][int(self.pos)], scale)
        else: # a pos is passed into the function
            return pygame.transform.scale_by(self.sprites[self.state][pos], scale)


# don't need SpriteSheet class anymore
# class SpriteSheet:
#     def __init__(self, name, count=0, dimension=0, init_scale=1, speed=0.1, state='default'):
#         self.name = name
#         self.count = count
#         self.dimension = dimension
#         self.init_scale = init_scale
#         self.speed = speed
#         self.pos = 0
#         self.state = state
#         self.assets = assets[name]
#         self.sprites = {}

#     def set_state(self, state):
#         self.state = state
#         self.pos = 0

#     def animate(self, pos=-1, scale=1):
#         if pos < 0: # default
#             self.pos += self.speed
#             if self.pos >= self.count:
#                 self.pos = 0
#             return pygame.transform.scale_by(self.sprites[self.state][int(self.pos)], scale)
#         else: # a pos is passed into the function
#             return pygame.transform.scale_by(self.sprites[self.state][pos], scale)

    
# class PlayerSheet(SpriteSheet):
#     def __init__(self):
#         super().__init__('player', count=11, speed=0.2, state='running', init_scale=0.7)
#         self.sprites = assets[self.name]
#         # for state in self.assets:
#         #     self.sprites[state] = []
#         #     for i in range(self.count):
#         #         sprite = pygame.transform.scale_by(self.assets[state][i], self.init_scale)
#         #         self.sprites[state].append(sprite)

# class CoinSheet(SpriteSheet):
#     def __init__(self):
#         super().__init__('coin', count=5, dimension=16, init_scale=2)
#         self.sprites = assets[self.name]
#         # for state in self.assets:
#         #     self.sprites[state] = []
#         #     for i in range(self.count):
#         #         sprite = pygame.transform.scale_by(
#         #             self.assets[state].subsurface(pygame.Rect((self.dimension * i, 0), (self.dimension, self.dimension))), self.init_scale)
#         #         # pygame.Surface.set_colorkey(sprite, )
#         #         self.sprites[state].append(sprite)


# class TorchSheet(SpriteSheet):
#     def __init__(self):
#         super().__init__('torch', count=8, dimension=64)
#         self.sprites = assets[self.name]
#         # for state in self.assets:
#         #     self.sprites[state] = []
#         #     for row in range(2):
#         #         for i in range(4):
#         #             sprite = pygame.transform.scale_by(
#         #                 self.assets[state].subsurface(pygame.Rect((self.dimension * i, self.dimension * row), (self.dimension, self.dimension))), 
#         #                 self.init_scale)
#         #             # pygame.Surface.set_colorkey(sprite, )
#         #             self.sprites[state].append(sprite)

# # def sprite_iterator():
