import pygame
from settings import *
from assets import assets
from spritesheets import PlayerSheet, CoinSheet

class Road:
    def __init__(self, surf):
        self.left_side = 200
        self.width = 25
        self.surf = surf
    
    def render(self):
        pygame.draw.line(self.surf, WHITE, [270, -360], [0, 720])      
        pygame.draw.line(self.surf, WHITE, [270, -360], [540, 720])

class TorchL(pygame.sprite.Sprite):
    def get_y(self):
        return int(-2.6 * self.x + 342)
    
    def __init__(self):
        super().__init__()
        self.scale = 0.5
        self.image = pygame.transform.scale_by(assets['torch'], self.scale)
        self.rect = self.image.get_rect()
        self.x = 200
        self.y = self.get_y()
        self.vel = 1
        self.accel = 0.02

    def update(self):
        if self.x < -50:
            self.kill()

        self.scale += 0.01
        self.image = pygame.transform.scale_by(assets['torch'], self.scale)
        self.rect = self.image.get_rect()
        self.x -= self.vel
        self.y = self.get_y()
        self.vel += self.accel
        self.rect.center = [self.x, self.y]

class TorchR(TorchL):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale_by(
            pygame.transform.flip(assets['torch'], True, False), self.scale)

    def update(self):
        super().update()
        self.image = pygame.transform.scale_by(
            pygame.transform.flip(assets['torch'], True, False), self.scale)
        self.rect.center = [WIDTH - self.x, self.y]

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sheet = PlayerSheet()
        self.image = self.sheet.animate()
        self.rect = self.image.get_rect(center=PLAYER_CENTER)

    def update(self):
        self.image = self.sheet.animate()

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sheet = CoinSheet()
        self.image = self.sheet.animate()
        self.rect = self.image.get_rect(center=(100, 100))

    def update(self):
        self.image = self.sheet.animate()
        

