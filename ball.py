import pygame
from util import *


class ball:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.ball = pygame.Rect(0, 0, 20, 20)
        self.pos = [0, 0]
        self.speed = [0, 0]

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 255), self.ball.center, 10)

    def move(self):
        self.ball.center = listadd(self.ball.center, self.speed)

    def colliedMap(self):
        if self.ball.centerx - 15 < 0:
            self.speed[0] *= -1
        if self.ball.centery - 15 < 0:
            self.speed[1] *= -1
        if self.ball.centerx + 15 > self.width:
            self.speed[0] *= -1
        if self.ball.centery + 15 > self.height:
            self.speed[1] *= -1
