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
        pygame.draw.line(self.surf, WHITE, [WIDTH//2, -360], [0, HEIGHT])      
        pygame.draw.line(self.surf, WHITE, [WIDTH//2, -360], [WIDTH, HEIGHT])

class TorchL(pygame.sprite.Sprite):  
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

        self.y += self.vel
        self.x = self.get_x()
        self.vel += self.accel
        self.scale += 0.01
        self.image = self.sheet.animate(scale=self.scale)
        self.rect = self.image.get_rect() # DO NOT DELETE THIS LINE! rect needs to be updated each time the image is scaled.
        self.rect.center = [self.x, self.y]
        print('left', self.scale, end='')

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
        print('right', self.scale)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sheet = PlayerSheet()
        self.image = self.sheet.animate()
        self.rect = self.image.get_rect(center=PLAYER_CENTER)

    def update(self):
        self.image = self.sheet.animate()

class Coin(pygame.sprite.Sprite):  
    def get_x(self):
        return int((1530 - self.y) / 7)
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.scale = 0.5
        self.sheet = CoinSheet()
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
        self.image = self.sheet.animate(scale=self.scale)
        self.rect = self.image.get_rect() # DO NOT DELETE THIS LINE! rect needs to be updated each time the image is scaled.
        # self.x -= self.vel
        # self.y = self.get_y()
        self.y += self.vel
        self.x = self.get_x()
        self.vel += self.accel
        self.rect.center = [self.x, self.y]

