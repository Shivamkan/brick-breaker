import pygame


class ball:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.pos = [0, 0]
        self.speed = [0, 0]

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 255), self.pos, 10)
