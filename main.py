import pygame
import sys
from entities import Road, Torch, Player, Coin
from animation import Pos_Iterator
from settings import *

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
        self.coin_iterator = Pos_Iterator(5, 0.1)
        # pygame.event.set_grab(1)
        self.touch = False

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_q:
                            pygame.quit()
                            sys.exit()
                elif event.type == TORCH_EVENT:
                    self.torches.add(Torch(True), Torch(False))
                elif event.type == COIN_EVENT:
                    self.coins.add(Coin())
                elif event.type == pygame.FINGERMOTION and (self.touch == False):
                    self.touch = True
                    if abs(event.dx) > abs(event.dy):
                        if event.dx < -0.001:
                            print('left')
                        elif event.dx > 0.001:
                            print('right')
                    else:
                        if event.dy < -0.001:
                            print('up')
                        elif event.dy > 0.001:
                            print('down')

                elif event.type == pygame.FINGERUP:
                    self.touch = False
                
                # elif event.type == pygame.MOUSEMOTION:
                #     movement = pygame.mouse.get_rel()
                #     left = bool(movement[0] < -3)
                #     up = bool(movement[1] < -3)
                #     if left:
                #         print('left!')
                #     # print('left', left, 'up', up)


            self.screen.fill(BLACK)
            self.road.render()
            self.torches.update()
            self.torches.draw(self.screen)
            self.player.update()
            self.player.draw(self.screen)

            self.coin_iterator.update()
            self.coin_pos = self.coin_iterator.get_pos()
            self.coins.update(self.coin_pos) 
            # if later decide to have coins rotate on their own instead of uniformly, 
            # just don't pass self.coin_pos to self.coins.update()
            self.coins.draw(self.screen)

            pygame.display.update()
            self.clock.tick(60)
            # print(self.clock.get_fps())

    
Game().run()