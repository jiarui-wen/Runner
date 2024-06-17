import pygame
from settings import *
import os

pygame.display.set_mode(RES)

def load_img(name, scale=1):
    img = pygame.transform.scale_by(pygame.image.load('images/'+ name).convert_alpha(), scale)
    pygame.Surface.set_colorkey(img, img.get_at((1, 1)))
    return img

def load_folder(folder_name, scale=1):
    images = []
    for file in os.listdir('images/' + folder_name):
        img = load_img(folder_name + '/' + file, scale)
        images.append(img)
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
    'player': {
        'default': load_folder('player/running', 0.7)
    },
    'coin': {
        'default': load_spritesheet('coin.png', 16, 1.5)
    },
    'torch': {
        'default': load_spritesheet('torch.png', 64)
    }
}