import pygame, math
from settings import *

class Rocket(pygame.sprite.Sprite):

    def __init__(self, pos, genome):
        super().__init__()
        self.pos = pos
        self.color = BLACK
        self.vel = 10
        self.rect = pygame.Rect(self.pos[0], self.pos[1], ROCKET_WIDTH, ROCKET_HEIGHT) # 350, 650

        self.genome = genome
        self.fitness = 0
        self.step = 0
        self.dead = False # true when colision with block
        self.reached_target = False # true when collision with target

    def draw(self):
        pygame.draw.rect(WIN, self.color, self.rect)


    def move(self):
        if self.step <= len(self.genome)-1 and self.dead == False:  # if its not dead move it
            pos = self.genome[self.step] # (vx, vy)
            self.rect.x += pos[0]  # vx positive move right, negative move left
            self.rect.y += pos[1]  # vy positive move down, negative move up
            self.step += 1