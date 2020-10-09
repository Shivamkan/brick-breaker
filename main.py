import sys
from random import randint
import pygame
import paddle
import ball


class Main:

    def __init__(self, width, height):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((width, height))
        self.width = width
        self.height = height
        self.blocks = []
        self.ball = ball.ball(self.width,self.height)
        self.paddle = paddle.paddle(self.width, self.height, self.ball)


    def draw(self):
        self.screen.fill((20, 20, 20))
        self.paddle.draw(self.screen)
        self.ball.draw(self.screen)
        pygame.display.flip()

    def handleinput(self):
        input = pygame.event.get()
        for event in input:
            if event.type == pygame.QUIT:
                sys.exit()
        self.paddle.handleInput(input)

    def run(self):
        while True:
            self.clock.tick(60)
            self.handleinput()
            self.draw()


run = Main(500, 500)
run.run()
