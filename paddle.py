import pygame


class paddle:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.paddlesize = 1
        self.paddle = pygame.Rect(width // 2 - 75, height - 40, 150, 20)
        self.lives = 3

    def changeSize(self):
        if self.paddlesize < 0:
            self.paddle.width //= 3
            self.paddlesize -= 1

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), self.paddle)
