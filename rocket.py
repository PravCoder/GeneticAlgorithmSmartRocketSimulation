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
        self.collided_with_block = False  # for fitness calc
        self.went_out_of_bounds = False

    def draw(self):
        pygame.draw.rect(WIN, self.color, self.rect)


    def move(self):
        if self.step <= len(self.genome)-1 and self.dead == False:  # if its not dead move it
            pos = self.genome[self.step] # (vx, vy)
            self.rect.x += pos[0]  # vx positive move right, negative move left
            self.rect.y += pos[1]  # vy positive move down, negative move up
            self.step += 1


    def is_out_of_bounds(self):
        if self.rect.x <= 0 or self.rect.x+self.rect.width >= WIDTH:
            return True
        if self.rect.y <= 0 or self.rect.y+self.rect.height >= HEIGHT:
            return True
        return False
    
    def eval_fitness(self, target):
        distance_to_target = math.sqrt((self.rect.x - target.rect.x) ** 2 + (self.rect.y - target.rect.y) ** 2)
        self.fitness = 1 / (distance_to_target + 1)  # reward/increase fitness closer rocket is to target
        if self.collided_with_block or self.went_out_of_bounds: self.fitness /= 2 # penalize/decrease fitness if rocket collision or out
        print(f"fitness: {self.fitness}")