import pygame
from settings import *
import os

pygame.display.set_mode(RES)

def load_img(name):
    img = pygame.image.load('images/'+ name).convert_alpha()
    # pygame.Surface.set_colorkey(img, colorkey)
    pygame.Surface.set_colorkey(img, img.get_at((1, 1)))
    return img

def load_folder(folder_name):
    images = []
    for img in os.listdir('images/' + folder_name):
        images.append(load_img(folder_name + '/' + img))
    return images

def load_spritesheet(name, dimension, scale=1):
    sprites = []
    img = load_img(name)
    rows = img.get_height() // dimension
    columns = img.get_width() // dimension
    for r in range(rows):
        for c in range(columns):
            sprites.append(pygame.transform.scale_by(
                        img.subsurface(pygame.Rect((dimension * c, dimension * r), (dimension, dimension))), scale))
    return sprites



assets = {
    # 'torch': load_img('torch', (0, 0, 0)),
    # 'player': load_img('player', (48, 104, 80))
    # 'torch': load_img('torch.png'),
    'player': {
        'running': load_folder('player/running')
    },
    'coin': {
        'default': load_spritesheet('coin.png', 16, 1.5)
    },
    'torch': {
        'default': load_spritesheet('torch.png', 64)
    }
}