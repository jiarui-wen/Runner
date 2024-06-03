import pygame
import sys
from entities import Road, TorchL, TorchR

pygame.init()

BLUE = (135, 206, 235)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

TORCH_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(TORCH_EVENT, 500)


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((540, 720))
        self.clock = pygame.time.Clock()
        self.road = Road(self.screen)
        self.torches = pygame.sprite.Group()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == TORCH_EVENT:
                    self.torches.add(TorchL(self.screen), TorchR(self.screen))

            self.screen.fill(BLACK)
            self.road.render()
            self.torches.update()
            self.torches.draw(self.screen)
            # print(len(self.torches.sprites()))

            pygame.display.update()
            self.clock.tick(60)

    
Game().run()