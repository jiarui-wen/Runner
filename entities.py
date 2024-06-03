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
        pygame.draw.line(self.surf, WHITE, [270, -360], [0, 720])      
        pygame.draw.line(self.surf, WHITE, [270, -360], [540, 720])

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
        self.accel = 0.02

    def update(self):
        if self.x < -50:
            self.kill()

        self.scale += 0.01
        self.image = pygame.transform.scale_by(pygame.image.load('torch.png').convert_alpha(), self.scale)
        self.rect = self.image.get_rect()
        self.x -= self.vel
        self.y = self.get_y()
        self.vel += self.accel
        self.rect.center = [self.x, self.y]

class TorchR(TorchL):
    def __init__(self, surf):
        super().__init__(surf)
        self.image = pygame.transform.scale_by(
            pygame.transform.flip(pygame.image.load('torch.png').convert_alpha(), True, False), self.scale)

    def update(self):
        super().update()
        self.image = pygame.transform.scale_by(
            pygame.transform.flip(pygame.image.load('torch.png').convert_alpha(), True, False), self.scale)
        self.rect.center = [self.surf.get_width() - self.x, self.y]
