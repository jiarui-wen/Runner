import pygame
from settings import *

pygame.display.set_mode(RES)

def load_img(name):
    img = pygame.image.load('images/'+ name + '.png').convert_alpha()
    # pygame.Surface.set_colorkey(img, colorkey)
    # pygame.Surface.set_colorkey(img, img.get_at((1, 1)))
    return img

assets = {
    # 'torch': load_img('torch', (0, 0, 0)),
    # 'player': load_img('player', (48, 104, 80))
    'torch': load_img('torch'),
    'player': load_img('player')
}