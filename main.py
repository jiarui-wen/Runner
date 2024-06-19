import pygame
import sys
from entities import Road, Torch, Player, Coin, Rock
from animation import Pos_Iterator
from settings import *
from random import choice, randint

pygame.init()



ADD_TORCH = pygame.USEREVENT + 1
ADD_COIN = pygame.USEREVENT + 2
ADD_ROCK = pygame.USEREVENT + 3

pygame.time.set_timer(ADD_TORCH, 500)
pygame.time.set_timer(ADD_COIN, 300)
pygame.time.set_timer(ADD_ROCK, 1500)


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
        self.rocks = pygame.sprite.Group()
        self.rocks_onscreen = pygame.sprite.Group()
        self.touch = False
        self.movement = 'default'
        self.score = 0
        self.health = 50
        self.num_coins = []
        self.lanes = []
        self.rock_in_coins = []
        
        for i in range(50):
            num_coins = randint(3, 7)
            self.num_coins.append(num_coins)
            self.lanes.append(choice([-1, 0, 1]))
            self.rock_in_coins.append(randint(1, num_coins-1))


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
                        case pygame.K_a:
                            self.movement = 'left'
                        case pygame.K_d:
                            self.movement = 'right'
                        case pygame.K_w:
                            self.movement = 'up'

                elif event.type == ADD_TORCH:
                    self.torches.add(Torch(True), Torch(False))

                elif event.type == ADD_COIN:
                    if len(self.num_coins) == 0:
                        for i in range(50):
                            num_coins = randint(3, 7)
                            self.num_coins.append(num_coins)
                            self.lanes.append(choice([-1, 0, 1]))
                            self.rock_in_coins.append(randint(0, num_coins))

                    if self.num_coins[-1] == 0:
                        self.num_coins.pop(-1)
                        self.lanes.pop(-1)
                        self.rock_in_coins.pop(-1)
                    else:
                        if self.num_coins[-1] == self.rock_in_coins[-1]:
                            self.rocks.add(Rock(self.lanes[-1]))
                        else:
                            self.coins.add(Coin(self.lanes[-1]))
                        self.num_coins[-1] -= 1

                elif event.type == ADD_ROCK:
                    choices = [-1, 0, 1]
                    choices.remove(self.lanes[-1])
                    self.rocks.add(Rock(choice(choices)))

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

            for rock in self.rocks.sprites():
                if self.player.sprite.rect_collision.colliderect(rock):
                    # pygame.sprite.Sprite.kill(rock)
                    self.rocks.remove(rock)
                    self.rocks_onscreen.add(rock)
                    self.health -= 1

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
            self.rocks.update()
            self.rocks.draw(self.screen)
            self.rocks_onscreen.update()
            self.rocks_onscreen.draw(self.screen)
            self.rocks.draw(self.screen)
            self.player.update(self.movement)
            self.player.draw(self.screen)

            # pygame.draw.rect(self.screen, "Red", self.player.sprite.rect_collision)

            pygame.display.update()
            self.clock.tick(60)
            # print(self.clock.get_fps())
            # print(self.health)
            # print(self.score)
            

    
Game().run()