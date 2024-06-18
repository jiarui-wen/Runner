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
        self.touch = False
        self.movement = 'default'
        self.score = 0

    def run(self):
        running = True
        while running:
            self.movement = 'default'
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
                            self.movement = 'left'
                        elif event.dx > 0.001:
                            self.movement = 'right'
                    else:
                        if event.dy < -0.001:
                            self.movement = 'up'
                        elif event.dy > 0.001:
                            print('down')

                elif event.type == pygame.FINGERUP:
                    self.touch = False
                    
            for coin in self.coins.sprites():
                if self.player.sprite.rect_collision.colliderect(coin):
                    pygame.sprite.Sprite.kill(coin)
                    self.score += 1

            self.screen.fill(WALL_GREY)
            self.road.render()
            self.torches.update()
            self.torches.draw(self.screen)

            self.coin_iterator.update()
            self.coin_pos = self.coin_iterator.get_pos()
            self.coins.update(self.coin_pos) 
            # if later decide to have coins rotate on their own instead of uniformly, 
            # just don't pass self.coin_pos to self.coins.update()
            self.coins.draw(self.screen)
            self.player.update(self.movement)
            self.player.draw(self.screen)

            pygame.display.update()
            self.clock.tick(60)
            # print(self.clock.get_fps())
            print(self.score)
            

    
Game().run()