import pygame
from settings import *
from animation import Animation
from random import choice
from assets import assets

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
        self.rect_collision = pygame.Rect((self.rect.centerx, self.rect.centery - Constants.Player.rect_offset_y), (40, 50))
        self.movement = 'default'
        self.x_pos = 1
        self.ignore = False
        self.jumping = False
        self.reset_jump = True
        self.x_dir = 0

    def update(self, movement='default'):
        self.image = self.animation.animate()
        if self.movement == 'dying':
            if self.image == False:
                return True # died
            return False

        if self.ignore:
            if self.movement == 'left':
                if movement == 'default':
                    pass
                elif movement == 'left' and self.x_pos != 0:
                    self.x_pos -= 1
                elif movement == 'right' and self.x_pos != 2:
                    self.movement = 'right'
                    self.x_pos += 1
                    self.x_dir = 1
                elif movement == 'up' and self.jumping == False:
                    self.movement = 'up'
                    self.jumping = True
            elif self.movement == 'right':
                if movement == 'default':
                    pass
                elif movement == 'right' and self.x_pos != 2:
                    self.x_pos += 1
                elif movement == 'left' and self.x_pos != 0:
                    self.movement = 'left'
                    self.x_pos -= 1
                    self.x_dir = -1
                elif movement == 'up' and self.jumping == False:
                    self.movement = 'up'
                    self.jumping = True
            elif self.movement == 'up':
                if movement == 'left' and self.x_pos != 0:
                    self.x_pos -= 1
                    self.x_dir = -1
                elif movement == 'right' and self.x_pos != 2:
                    self.x_pos += 1
                    self.x_dir = 1
            elif self.movement == 'default':
                if movement == 'left' and self.x_pos != 0:
                    self.x_pos -= 1
                    self.x_dir = -1
                elif movement == 'right' and self.x_pos != 2:
                    self.x_pos += 1
                    self.x_dir = 1
                elif movement == 'default':
                    if self.x_dir == 0:
                        self.ignore = False
            
            self.animation.set_state(self.movement, reset=(self.movement == 'up' and self.reset_jump))
            self.image = self.animation.animate()
            if self.movement == 'up' : 
                self.reset_jump = False
                self.animation.set_loop(False)
                if self.image == False:
                    self.jumping = False
                    self.movement = 'default'
                    self.animation.set_state('default')
                    self.animation.set_loop(True)
                    self.reset_jump = True
                    self.image = self.animation.animate()
                    if self.x_dir == 0:
                        self.movement = 'default'
                        self.ignore = False
                    
            if self.x_dir < 0 and self.rect.centerx < Constants.Player.x_pos[self.x_pos]:
                self.rect.centerx = Constants.Player.x_pos[self.x_pos]
                self.x_dir = 0
                if self.movement == 'left':
                    self.movement = 'default'
                    self.animation.set_state('default')
                    self.ignore = False

            elif self.x_dir > 0 and self.rect.centerx > Constants.Player.x_pos[self.x_pos]:
                self.rect.centerx = Constants.Player.x_pos[self.x_pos]
                self.x_dir = 0
                if self.movement == 'right':
                    self.movement = 'default'
                    self.animation.set_state('default')
                    self.ignore = False
        else:
            if movement != 'default':
                if movement == 'left' and self.x_pos != 0:
                    self.ignore = True
                    self.movement = movement
                    self.x_pos -= 1
                    self.x_dir = -1
                elif movement == 'right' and self.x_pos != 2:
                    self.ignore = True
                    self.movement = movement
                    self.x_pos += 1
                    self.x_dir = 1
                elif movement == 'up':
                    self.ignore = True
                    self.movement = movement
                    self.jumping = True

        self.rect.x += (self.x_dir * 10)
        self.rect_collision.centerx = self.rect.centerx
        if self.jumping:
            self.rect_collision.centery = -100
        else:
            self.rect_collision.centery = self.rect.centery - Constants.Player.rect_offset_y

        return False
    
    def dying(self):
        self.animation.set_state('dying', True)
        self.animation.set_loop(False)
        self.movement = 'dying'

class BaseEntity(pygame.sprite.Sprite):
    def get_x(self):
        if self.lane == -1:
            return int((1530 - self.y) / 7)
        elif self.lane == 0:
            return WIDTH // 2
        else:
            return WIDTH - int((1530 - self.y) / 7)
        
    def __init__(self, lane):
        pygame.sprite.Sprite.__init__(self)
        self.lane = lane
        self.scale = 0.5
        self.y = -50
        self.x = self.get_x()
        self.vel = 2
        self.accel = 0.02
    
    def update(self):
        if self.y > HEIGHT + 50:
            self.kill()
        self.x = self.get_x()
        self.y += self.vel
        self.vel += self.accel
        self.scale += 0.01
    


class Coin(BaseEntity):  
    def __init__(self, lane):
        super().__init__(lane)
        self.animation = Animation('coin')
        self.image = self.animation.animate(scale=self.scale)
        self.rect = self.image.get_rect()

    def update(self, p=-1):
        super().update()
        self.image = self.animation.animate(pos=p, scale=self.scale)
        self.rect = self.image.get_rect(center=[self.x, self.y]) # DO NOT DELETE THIS LINE! rect needs to be updated each time the image is scaled.
            

class Rock(BaseEntity):
    def __init__(self, lane):
        super().__init__(lane)
        self.base_img = choice(assets['rock'])
        self.image = self.base_img
        self.rect = self.image.get_rect()

    def update(self):
        super().update()
        self.image = pygame.transform.scale_by(self.base_img, self.scale)
        self.rect = self.image.get_rect(center=[self.x, self.y])

class Button:
  def __init__(self, pos, name):
    self.name = name
    self.pos = pos
    self.image = assets['button'][name][0]
    self.rect = self.image.get_rect(center = pos)

  def update(self, position):
    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
      self.image = assets['button'][self.name][1]
      self.rect.center = [self.pos[0] - 3, self.pos[1] - 3]
    else:
      self.image = assets['button'][self.name][0]
      self.rect.center = self.pos

  def click(self, position):
    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
      return True
    
  def render(self, surf):
    surf.blit(self.image, self.rect)




