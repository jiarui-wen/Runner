import pygame
BLUE = (135, 206, 235)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Road:
    def __init__(self, surf):
        self.left_side = 200
        self.width = 25
        self.img = pygame
        self.surf = surf
    
    def render(self):
        pygame.draw.line(self.surf, BLACK, [270, -360], [0, 720])      
        pygame.draw.line(self.surf, BLACK, [270, -360], [540, 720])

class TorchL(pygame.sprite.Sprite):
    def get_y(self):
        return int(-2.6 * self.x + 342)
    
    def __init__(self, surf):
        super().__init__()
        self.surf = surf
        self.scale = 0.5
        self.image = pygame.transform.scale_by(pygame.image.load('torch.png').convert_alpha(), self.scale)
        self.rect = self.image.get_rect()
        self.x = 200
        self.y = self.get_y()
        self.vel = 1
        self.accel = 0.005

    def update(self):
        if self.x < -50:
            self.kill()
            # self.x = 200
            # self.scale = 0.5
        self.scale += 0.006
        self.image = pygame.transform.scale_by(pygame.image.load('torch.png').convert_alpha(), self.scale)
        self.rect = self.image.get_rect()
        self.x -= self.vel
        self.y = self.get_y()
        self.vel += self.accel
        self.rect.center = [self.x, self.y]

    # def render(self):
    #     self.surf.blit(self.img, self.rect)

class TorchR(TorchL):
    def __init__(self, surf):
        super().__init__(surf)

    def update(self):
        super().update()
        self.rect.center = [self.surf.get_width() - self.x, self.y]

    # def render(self):
    #     self.surf.blit(self.img, self.rect)


# class Torch():
#     def get_y(self):
#         return int(-2.6 * self.x + 342)
    
#     def __init__(self, surf):
#         self.surf = surf
#         self.scale = 0.5
#         self.img = pygame.transform.scale_by(pygame.image.load('torch.png').convert_alpha(), self.scale)
#         self.x = 200
#         self.y = self.get_y()
#         self.offset = 150

#     def update(self):
#         if self.x < -100:
#             self.x = 200
#             self.scale = 0.5
#         self.x -= 1
#         self.y = self.get_y()
#         self.scale += 0.006
#         self.img = pygame.transform.scale_by(pygame.image.load('torch.png').convert_alpha(), self.scale)

#     def render(self):
#         self.surf.blit(self.img, [self.x, self.y - self.offset])

# class TorchFlip(Torch):
#     def __init__(self, surf):
#         super().__init__(surf)
#         self.centre_x = 2 * self.surf.get_rect().centerx - self.img.get_rect().centerx

#     def update(self):
#         if self.x > 600:
#             self.x = 

# class TorchRight():
#     def get_y(self):
#         return int(2.6 * self.x - 1062)
    
#     def __init__(self, surf):
#         self.surf = surf
#         self.scale = 0.5
#         self.img = pygame.transform.scale_by(pygame.image.load('torch.png').convert_alpha(), self.scale)
#         self.x = 340
#         self.y = self.get_y()
#         self.offset = -150

#     def update(self):
#         if self.x > 600:
#             self.x = 340
#             self.scale = 0.5
#         self.x += 1
#         self.y = self.get_y()
#         self.scale += 0.006
#         self.img = pygame.transform.scale_by(pygame.image.load('torch.png').convert_alpha(), self.scale)

#     def render(self):
#         self.surf.blit(self.img, [self.x, self.y - self.offset])


    