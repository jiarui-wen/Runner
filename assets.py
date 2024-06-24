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
        'default': load_folder('player/running', Constants.Player.init_scale),
        'left': load_folder('player/left', Constants.Player.init_scale),
        'right': load_folder('player/right', Constants.Player.init_scale),
        'up': load_folder('player/up', Constants.Player.init_scale),
        'dying': load_folder('player/dying', Constants.Player.init_scale),
        'idle': load_folder('player/idle', Constants.Player.init_scale),
        'lookaround': load_folder('player/lookaround', Constants.Player.init_scale),
        'turn': load_folder('player/turn', Constants.Player.init_scale)
        # 'drawsword': load_folder('player/drawsword', Constants.Player.init_scale)

    },
    'coin': {
        'default': load_spritesheet('coin.png', Constants.Coin.dimension, Constants.Coin.init_scale)
    },
    'torch': {
        'default': load_spritesheet('torch.png', Constants.Torch.dimension)
    },
    'rock': load_folder('rock', 0.5),
    'button': {
        'play': load_folder('button/play'),
        'info': load_folder('button/info'),
        'ok': load_folder('button/ok'),
        'home': load_folder('button/home'),
        'clearstats': load_folder('button/clearstats', 0.4),
        'clear': load_folder('button/clear', 0.7),
        'cancel': load_folder('button/cancel', 0.7)
    },
    'text': {
        'dungeonrun': load_img('dungeonrun.png'),
        'paused': load_img('paused.png', 1.5),
        'pressentertoresume': load_img('pressentertoresume.png', 0.4),
        'stats': load_img('stats.png', 0.4)
    },
    'infopage': load_img('infopage.png'),
    'clearpage': load_img('clearpage.png')
}