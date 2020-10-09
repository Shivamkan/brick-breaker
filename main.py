import sys
import pygame
import paddle
import ball
import brick


class Main:

    def __init__(self, width, height):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((width, height))
        self.width = width
        self.height = height
        self.blocks = self.spawnbrick(15,10)
        self.ball = ball.ball(self.width, self.height)
        self.paddle = paddle.paddle(self.width, self.height, self.ball)

    def spawnbrick(self, i, j):
        blocks = []
        blockwidth = (self.width//i)
        blockheight = ((self.height / 2)//j)
        for x in range(i):
            for y in range(j):
                blocks.append(brick.block(x * blockwidth + 5, (y * blockheight)+10, blockwidth - 10, blockheight - 10))
        return blocks

    def draw(self):
        self.screen.fill((20, 20, 20))
        self.paddle.draw(self.screen)
        self.ball.draw(self.screen)
        self.drawBricks()
        pygame.display.flip()

    def brickCollied(self):
        toBePoped = []
        for x in self.blocks:
            if x.collied(self.ball):
                toBePoped.append(x)
        for x in toBePoped:
            self.blocks.pop(self.blocks.index(x))

    def drawBricks(self):
        for x in range(len(self.blocks)):
            self.blocks[x].draw(self.screen)

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
            self.ball.move()
            self.ball.colliedMap()
            self.paddle.collied()
            self.brickCollied()
            self.draw()


run = Main(500, 500)
run.run()
