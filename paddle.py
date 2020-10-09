import pygame
from util import *


class paddle:

    def __init__(self, width: int, height: int, ball):
        self.width = width
        self.height = height
        self.paddleSize = 1
        self.paddle = pygame.Rect(width // 2 - 75, height - 40, 150, 20)
        self.lives = 4
        self.died = 1
        self.ball = ball

    def changeSize(self):
        if self.paddleSize < 0:
            self.paddle.width //= 3
            self.paddleSize -= 1

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), self.paddle)

    def handleInput(self, input):
        for event in input:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    self.launchBall()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.paddle.x -= 2
            self.paddle.x = clamp(self.paddle.x, 0, self.width - 150)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.paddle.x += 2
            self.paddle.x = clamp(self.paddle.x, 0, self.width - 150)
        if self.died:
            self.ball.pos = (self.paddle.centerx, self.paddle.y - 10)

    def launchBall(self):
        if self.died:
            self.ball.speed = [0, -4]
            self.died = 0
