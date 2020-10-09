import pygame
from util import *


class block:

    def __init__(self, x, y, width, height):
        self.brick = pygame.Rect(x, y, width, height)
        self.blockColor = randColor()

    def draw(self, screen):
        pygame.draw.rect(screen, self.blockColor, self.brick)
