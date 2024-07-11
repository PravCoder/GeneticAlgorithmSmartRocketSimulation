import pygame, math
from settings import *

class Block(pygame.sprite.Sprite):

    def __init__(self, pos, width, height):
        self.pos = pos
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.width, self.height ) # 350, 650


    def draw(self):
        pygame.draw.rect(WIN, RED, self.rect)

    