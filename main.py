import pygame
import sys
from entities import Road, TorchL, TorchR, Player, Coin
from settings import *
from spritesheets import CoinSheet

pygame.init()



TORCH_EVENT = pygame.USEREVENT + 1
COIN_EVENT = pygame.USEREVENT + 2
pygame.time.set_timer(TORCH_EVENT, 500)
pygame.time.set_timer(COIN_EVENT, 300)


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(RES)
        self.clock = pygame.time.Clock()
        self.road = Road(self.screen)
        self.torches = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.player.add(Player())
        self.coins = pygame.sprite.Group()
        self.coin_sheet = CoinSheet()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == TORCH_EVENT:
                    self.torches.add(TorchL(), TorchR())
                elif event.type == COIN_EVENT:
                    self.coins.add(Coin())

            self.screen.fill(BLACK)
            self.road.render()
            self.torches.update()
            self.torches.draw(self.screen)
            # print(len(self.torches.sprites()))
            self.player.update()
            self.player.draw(self.screen)
            self.coins.update()
            self.coins.draw(self.screen)
            print(len(self.torches.sprites()))

            pygame.display.update()
            self.clock.tick(60)

    
Game().run()