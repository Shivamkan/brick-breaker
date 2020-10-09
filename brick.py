import pygame
from util import *


class block:

    def __init__(self, x, y, width, height):
        self.brick = pygame.Rect(x, y, width, height)
        self.blockColor = randColor()

    def draw(self, screen):
        pygame.draw.rect(screen, self.blockColor, self.brick)

    def collied(self, ball):
        tolerence = 10
        if self.brick.colliderect(ball.ball):
            # print("k")
            if abs(self.brick.top - ball.ball.bottom) < tolerence:
                ball.speed[1] *= -1
            if abs(self.brick.bottom - ball.ball.top) < tolerence:
                ball.speed[1] *= -1
            if abs(self.brick.right - ball.ball.left) < tolerence:
                ball.speed[0] *= -1
            if abs(self.brick.left - ball.ball.right) < tolerence:
                ball.speed[0] *= -1
            return True
        else:
            return False
