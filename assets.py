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


assets = {
    # 'torch': load_img('torch', (0, 0, 0)),
    # 'player': load_img('player', (48, 104, 80))
    # 'torch': load_img('torch.png'),
    'player': {
        'running': load_folder('player/running')
    },
    'coin': {
        'default': load_img('coin.png')
    },
    'torch': {
        'default': load_img('torch.png')
    }
}