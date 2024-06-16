import pygame
import sys
from entities import Road, TorchL, TorchR, Player, Coin
from settings import *

pygame.init()



TORCH_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(TORCH_EVENT, 500)


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(RES)
        self.clock = pygame.time.Clock()
        self.road = Road(self.screen)
        self.torches = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.player.add(Player())
        self.coins = pygame.sprite.Group()
        self.coins.add(Coin())

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == TORCH_EVENT:
                    self.torches.add(TorchL(), TorchR())

            self.screen.fill(BLACK)
            self.road.render()
            self.torches.update()
            self.torches.draw(self.screen)
            # print(len(self.torches.sprites()))
            self.player.update()
            self.player.draw(self.screen)
            self.coins.update()
            self.coins.draw(self.screen)

            pygame.display.update()
            self.clock.tick(60)

    
Game().run()