import pygame
from util import *

class ball:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.pos = [0, 0]
        self.speed = [0, 0]

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 255), self.pos, 10)

    def move(self):
        self.pos = listadd(self.pos,self.speed)

    def colliedMap(self):
        if self.pos[0]-5 < 0:
            self.speed[0] *= -1
        if self.pos[1]-5 < 0:
            self.speed[1] *= -1
        if self.pos[0]+5 > self.width:
            self.speed[0] *= -1
        if self.pos[1]+5 > self.height:
            self.speed[1] *= -1
