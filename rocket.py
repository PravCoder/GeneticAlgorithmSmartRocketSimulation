import pygame, math
from settings import *

class Rocket(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        self.pos = pos
        self.color = BLACK
        self.vel = 10
        self.rect = pygame.Rect(self.pos[0], self.pos[1], ROCKET_WIDTH, ROCKET_HEIGHT) # 350, 650

    def draw(self):
        pygame.draw.rect(WIN, self.color, self.rect)


    def move(self, vx, vy):
        self.rect.x += vx
        self.rect.y += vy