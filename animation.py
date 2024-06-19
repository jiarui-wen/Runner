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
        self.loop = True

    def set_state(self, state, reset=False):
        self.state = state
        if reset:
            self.pos = 0

    def set_loop(self, loop):
        self.loop = loop
        
    def animate(self, pos=-1, scale=1):
        if pos < 0: # default
            self.pos += self.speed
            if self.pos >= len(self.sprites[self.state]):
                if self.loop:   
                    self.pos = 0
                else:
                    return False
            return pygame.transform.scale_by(self.sprites[self.state][int(self.pos)], scale)
        else: # a pos is passed into the function
            return pygame.transform.scale_by(self.sprites[self.state][pos], scale)
