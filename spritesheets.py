import pygame
from assets import assets
from settings import *

class SpriteSheet:
    def __init__(self, name, width, height, count, scale=1, speed=0.1, state='none'):
        self.sheet = assets[name]
        self.width = width
        self.height = height
        self.count = count
        self.scale = scale
        self.speed = speed
        self.pos = 0
        self.state = state
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
        super().__init__('player', 16, 16, 4, scale=8, state='forward')

        self.sprites = {"forward": [],
                        "left": [],
                        "right": []}
        
        for i in range(self.count): 
            self.sprites['forward'].append(pygame.transform.scale_by(
                self.sheet.subsurface(pygame.Rect((self.width * i, self.height * 4), (self.width, self.height))), self.scale))
            self.sprites['left'].append(pygame.transform.scale_by(
                self.sheet.subsurface(pygame.Rect((self.width * i, self.height * 3), (self.width, self.height))), self.scale))
            self.sprites['right'].append(pygame.transform.scale_by(
                self.sheet.subsurface(pygame.Rect((self.width * i, self.height * 5), (self.width, self.height))), self.scale))
            
        for state in self.sprites:
            for img in self.sprites[state]:
                pygame.Surface.set_colorkey(img, PLAYER_COLORKEY)



