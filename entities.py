import pygame
from settings import *
from assets import assets
from spritesheets import PlayerSheet, CoinSheet, TorchSheet

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
    
    def get_x(self):
        return int((342 - self.y) / 2.6)
    
    def __init__(self):
        super().__init__()
        self.scale = 0.5
        # self.image = pygame.transform.scale_by(assets['torch'], self.scale)
        self.sheet = TorchSheet()
        self.image = self.sheet.animate(scale=self.scale)
        self.rect = self.image.get_rect()
        # self.x = 200
        # self.y = self.get_y()
        self.y = -50
        self.x = self.get_x()
        self.vel = 2
        self.accel = 0.02

    def update(self):
        if self.x < -50:
            self.kill()

        self.scale += 0.01
        # self.image = pygame.transform.scale_by(assets['torch'], self.scale)
        self.image = self.sheet.animate(scale=self.scale)
        # self.x -= self.vel
        # self.y = self.get_y()
        self.y += self.vel
        self.x = self.get_x()
        self.vel += self.accel
        self.rect.center = [self.x, self.y]

class TorchR(TorchL):
    def __init__(self):
        super().__init__()
        # self.image = pygame.transform.scale_by(
        #     pygame.transform.flip(assets['torch'], True, False), self.scale)
        self.image = pygame.transform.flip(self.sheet.animate(scale=self.scale), True, False)

    def update(self):
        super().update()
        # self.image = pygame.transform.scale_by(
        #     pygame.transform.flip(assets['torch'], True, False), self.scale)
        self.image = pygame.transform.flip(self.sheet.animate(scale=self.scale), True, False)
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
    def get_y(self):
        return int(-7 * self.x + 1530)
    
    def get_x(self):
        return int((1530 - self.y) / 7)
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.scale = 0.5
        # self.sheet = CoinSheet()
        self.image = self.sheet.animate()
        self.rect = self.image.get_rect()
        # self.x = 270
        # self.y = self.get_y()
        self.y = -50
        self.x = self.get_x()
        self.vel = 2
        self.accel = 0.02

    def update(self):
        if self.x < -50:
            self.kill()

        self.scale += 0.01
        self.image = self.sheet.animate(pos=p, scale=self.scale)
        # self.x -= self.vel
        # self.y = self.get_y()
        self.y += self.vel
        self.x = self.get_x()
        self.vel += self.accel
        self.rect.center = [self.x, self.y]

