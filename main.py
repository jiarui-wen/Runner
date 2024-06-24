import pygame
import sys

import pygame.freetype
from entities import Road, Torch, Player, Coin, Rock, Button
from animation import Pos_Iterator
from settings import *
from random import choice, randint
from assets import assets
from animation import Animation

pygame.init()



ADD_TORCH = pygame.USEREVENT + 1
ADD_COIN = pygame.USEREVENT + 2
ADD_ROCK = pygame.USEREVENT + 3
WAIT = pygame.USEREVENT + 4


class Game:
    def __init__(self, screen):
        # self.screen = pygame.display.set_mode(RES)
        self.screen = screen
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
        self.wait = 2
        pygame.time.set_timer(ADD_TORCH, 500)
        pygame.time.set_timer(ADD_COIN, 300)
        pygame.time.set_timer(ADD_ROCK, 1500)
        pygame.time.set_timer(WAIT, 1000)
        
        for i in range(30):
            num_coins = randint(3, 7)
            self.num_coins.append(num_coins)
            self.lanes.append(choice([-1, 0, 1]))
            self.rock_in_coins.append(randint(1, num_coins))

    def run(self):
        running = True
        while running:
            self.movement = 'default'
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == WAIT:
                    self.wait -= 1
                    if self.wait == 0:
                        pygame.time.set_timer(WAIT, 0)
                elif event.type == pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_ESCAPE:
                            pygame.quit()
                            sys.exit()
                        case pygame.K_a:
                            self.movement = 'left'
                        case pygame.K_d:
                            self.movement = 'right'
                        case pygame.K_w:
                            self.movement = 'up'
                        case pygame.K_p:
                            paused = True
                            while paused:
                                for event in pygame.event.get():
                                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                                        paused = False
                                    elif event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                                        pygame.quit()
                                        sys.exit()
                                self.render()
                                self.pause_screen()
                                pygame.display.update()
                                self.clock.tick(60)



                elif event.type == ADD_TORCH and self.wait == 0:
                    self.torches.add(Torch(True), Torch(False))

                elif event.type == ADD_COIN and self.wait == 0:
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

                    if len(self.num_coins) == 0:
                        for i in range(50):
                            num_coins = randint(3, 7)
                            self.num_coins.append(num_coins)
                            self.lanes.append(choice([-1, 0, 1]))
                            self.rock_in_coins.append(randint(1, num_coins))

                elif event.type == ADD_ROCK and self.wait == 0:
                    choices = [-1, 0, 1]
                    choices.remove(self.lanes[-1])
                    self.rocks.add(Rock(choice(choices)))


                elif event.type == pygame.FINGERMOTION and not self.touch:
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
                if self.player.sprite.rect.bottom < rock.rect.bottom:
                    self.rocks.remove(rock)
                    self.rocks_onscreen.add(rock)
                if self.player.sprite.rect_collision.colliderect(rock):
                    self.player.sprite.dying()
                    while True:
                        died = self.player.sprite.update()
                        if died:
                            return 'score', self.score
                        self.render()
                        pygame.display.update()
                        self.clock.tick(60)

            self.update()
            self.render()
            pygame.display.update()
            self.clock.tick(60)
            # if later decide to have coins rotate on their own instead of uniformly, 
            # just don't pass self.coin_pos to self.coins.update()

    def update(self):
        self.torches.update()
        self.coin_iterator.update()
        self.coin_pos = self.coin_iterator.get_pos()
        self.coins.update(self.coin_pos) 
        self.rocks.update()
        self.player.update(self.movement)
        self.rocks_onscreen.update()

    def render(self):
        self.screen.fill(WALL_GREY)
        self.road.render()
        self.torches.draw(self.screen)
        self.coins.draw(self.screen)
        self.rocks.draw(self.screen)
        self.rocks.draw(self.screen)
        self.player.draw(self.screen)
        self.rocks_onscreen.draw(self.screen) 

    def pause_screen(self):
        self.screen.blit(assets['text']['paused'], (100, 100))
        self.screen.blit(assets['text']['pressentertoresume'], (120, 300))             


class Menu:
    def __init__(self, screen):
        # self.screen = pygame.display.set_mode(RES)
        self.screen = screen
        self.play_button = Button((200, 330), 'play')
        self.info_button = Button((350, 330), 'info')
        self.clock = pygame.time.Clock()
        self.road = Road(self.screen)
        self.text = assets['text']['dungeonrun']
        self.player_animation = Animation('player', speed=0.2, state='idle', loop=False)
        self.player_img = self.player_animation.animate()
        self.player_rect = self.player_img.get_rect(center=PLAYER_CENTER)
    
    def run(self):
        running = True
        while running:
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_ESCAPE:
                            pygame.quit()
                            sys.exit()
                        # case pygame.K_RETURN:
                        #     return 
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    play = self.play_button.click(mouse)
                    if play:
                        self.player_animation.set_state('turn', True)
                        self.player_animation.set_loop(False)
                        while True:
                            self.player_img = self.player_animation.animate()
                            if self.player_img == False:
                                return 'game'
                            self.screen.fill(WALL_GREY)
                            self.road.render()
                            self.screen.blit(self.player_img, self.player_rect)
                            pygame.display.update()
                            self.clock.tick(60)    
                            

                    info = self.info_button.click(mouse)
                    if info:
                        ok_button = Button((WIDTH//2, 600), 'ok')
                        in_info = True
                        while in_info: 
                            mouse = pygame.mouse.get_pos()
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    if ok_button.click(mouse):
                                        in_info = False
                                elif event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                                    pygame.quit()
                                    sys.exit()
                            ok_button.update(mouse)
                            self.render()
                            self.screen.blit(assets['infopage'], (20, 50))
                            ok_button.render(self.screen)
                            pygame.display.update()
                            self.clock.tick(60)    

            self.player_img = self.player_animation.animate()
            if self.player_img == False:
                self.player_animation.set_state(choice(['idle', 'lookaround']), reset=True)
                self.player_img = self.player_animation.animate()
            self.play_button.update(mouse)
            self.info_button.update(mouse)

            self.render()
            pygame.display.update()
            self.clock.tick(60)

    def render(self):
        self.screen.fill(WALL_GREY)
        self.road.render()
        self.screen.blit(self.text, (50, 50))
        self.screen.blit(self.player_img, self.player_rect)
        self.play_button.render(self.screen)
        self.info_button.render(self.screen)

class Score:
    def __init__(self, screen, scores):
        self.scores = scores
        self.new_score = scores[-1]
        print(self.new_score)
        self.scores.sort(reverse=True)
        print(self.scores)

        self.screen = screen
        self.road = Road(screen)
        self.clock = pygame.time.Clock()
        self.home_button = Button((360, 420), 'home')
        self.play_button = Button((200, 420), 'play')
        self.player_animation = Animation('player', speed=0.2, state='idle', loop=False)
        self.player_img = self.player_animation.animate()
        self.player_rect = self.player_img.get_rect(center=PLAYER_CENTER)
        self.font_rank = pygame.freetype.SysFont('Aerial', 25)
        self.font_score = pygame.freetype.SysFont('Aerial', 25, True)
        self.text = assets['text']['stats']

        
    def run(self):
        while True:
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_ESCAPE:
                            pygame.quit()
                            sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    play = self.play_button.click(mouse)
                    if play:
                        self.player_animation.set_state('turn', True)
                        self.player_animation.set_loop(False)
                        while True:
                            self.player_img = self.player_animation.animate()
                            if self.player_img == False:
                                return 'game'
                            self.screen.fill(WALL_GREY)
                            self.road.render()
                            self.screen.blit(self.player_img, self.player_rect)
                            pygame.display.update()
                            self.clock.tick(60)    
                    home = self.home_button.click(mouse)
                    if home:
                        return 'menu'
                    
            self.player_img = self.player_animation.animate()
            if self.player_img == False:
                self.player_animation.set_state(choice(['idle', 'lookaround']), reset=True)
                self.player_img = self.player_animation.animate()
                    
            self.play_button.update(mouse)
            self.home_button.update(mouse)

            self.render()
            pygame.display.update()
            self.clock.tick(60)

    def render(self):
        self.screen.fill(WALL_GREY)
        self.road.render()
        # self.screen.blit(self.text, (50, 50))
        self.screen.blit(self.player_img, self.player_rect)
        self.play_button.render(self.screen)
        self.home_button.render(self.screen)
        self.screen.blit(self.text, (150, 30))

        for i in range(5):
        #     rank = self.font_rank.render(str(i + 1), True, 'Black')
        #     rank_rect = rank.get_rect(center=(100, 100 + 50 * i))
            try:
                self.font_score.render_to(self.screen, (300, 140 + 35 * i), str(self.scores[i]), COIN_YELLOW)
                self.font_rank.render_to(self.screen, (180, 140 + 35 * i), str(i + 1), RED)
                self.screen.blit(pygame.transform.scale(assets['coin']['default'][0], (25, 25)), (270, 137 + 35 * i))
            except IndexError:
                pass
                
                

        

# screen = pygame.display.set_mode(RES)
# while True:
#     Menu(screen).run()
    # Game(screen).run()


def main():
    screen = pygame.display.set_mode(RES)
    state = 'menu'
    scores = []
    while True:
        match state:
            case 'menu':
                state = Menu(screen).run()
            case 'game':
                state, score = Game(screen).run()
                scores.append(score)
            case 'score':
                state = Score(screen, scores).run()

main()