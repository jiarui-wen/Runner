import pygame
from settings import *
from animation import Animation

class Road:
    def __init__(self, surf):
        self.left_side = 200
        self.width = 25
        self.surf = surf

    def render(self):
        pygame.draw.polygon(self.surf, FLOOR_GREY, [(WIDTH//2, -360), (0, HEIGHT), (WIDTH, HEIGHT)])

class Torch(pygame.sprite.Sprite):  
    def get_x(self):
        return int((342 - self.y) / 2.6)
    
    def __init__(self, is_left):
        super().__init__()
        self.scale = 0.5
        self.animation = Animation('torch')
        self.image = self.animation.animate(scale=self.scale)
        self.rect = self.image.get_rect()
        self.is_left = is_left
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
        self.image = self.animation.animate(scale=self.scale)
        self.rect = self.image.get_rect() # DO NOT DELETE THIS LINE! rect needs to be updated each time the image is scaled.
        if self.is_left:
            self.rect.center = [self.x, self.y]
        else:
            self.rect.center = [WIDTH - self.x, self.y]

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.animation = Animation('player', speed=0.2)
        self.image = self.animation.animate()
        self.rect = self.image.get_rect(center=PLAYER_CENTER)
        self.movement = 'default'
        self.x_pos = 1
        self.ignore = False

    def update(self, movement='default'):
        self.image = self.animation.animate()

        if self.ignore:
            if self.movement == 'left':
                self.rect.x -= 10
                if self.rect.centerx < Constants.Player.x_pos[self.x_pos - 1]:
                    self.rect.centerx = Constants.Player.x_pos[self.x_pos - 1]
                    self.x_pos -= 1
                    self.ignore = False
                    # self.movement = 'default'
                    self.animation.set_state('default')
            elif self.movement == 'right':
                self.rect.x += 10
                if self.rect.centerx > Constants.Player.x_pos[self.x_pos + 1]:
                    self.rect.centerx = Constants.Player.x_pos[self.x_pos + 1]
                    self.x_pos += 1
                    self.ignore = False
                    self.animation.set_state('default')

        else:
            if movement == 'default':
                pass
            elif (movement == 'left' and self.x_pos != 0) or (movement == 'right' and self.x_pos != 2):
                self.ignore = True
                self.movement = movement
                self.animation.set_state(movement)

class Coin(pygame.sprite.Sprite):  
    def get_x(self):
        return int((1530 - self.y) / 7)
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.scale = 0.5
        self.animation = Animation('coin')
        self.image = self.animation.animate(scale=self.scale)
        self.rect = self.image.get_rect()
        self.y = -50
        self.x = self.get_x()
        self.vel = 2
        self.accel = 0.02

    def update(self, p=-1):
        if self.y < -50:
            self.kill()

        self.scale += 0.01
        self.image = self.animation.animate(pos=p, scale=self.scale)
        self.rect = self.image.get_rect() # DO NOT DELETE THIS LINE! rect needs to be updated each time the image is scaled.
        self.y += self.vel
        self.x = self.get_x()
        self.vel += self.accel
        self.rect.center = [self.x, self.y]

