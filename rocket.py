import pygame, math, random
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
        self.collision_penalty = 10
        self.genome_completion_penalty = 5
        self.genome_completed = False

    def draw(self):
        pygame.draw.rect(WIN, self.color, self.rect)


    def move(self):
        if self.step <= len(self.genome)-1 and self.dead == False:  # if its not dead move it
            pos = self.genome[self.step] # (vx, vy)
            self.rect.x += pos[0]  # vx positive move right, negative move left
            self.rect.y += pos[1]  # vy positive move down, negative move up
            self.step += 1
            if self.step >= len(self.genome)-1:
                self.genome_completed = True
        else:  # if the cur-step is more than genome length it is done
            self.dead = True


    def is_out_of_bounds(self):
        if self.rect.x <= 0 or self.rect.x+self.rect.width >= WIDTH:
            return True
        if self.rect.y <= 0 or self.rect.y+self.rect.height >= HEIGHT:
            return True
        return False
    
    def is_done_steps(self):
        if self.steps >= len(self.genome)-1:
            return True
        return False
    
    def eval_fitness(self, target):
        distance_to_target = math.sqrt((self.pos[0] - target.pos[0])**2 + (self.pos[1] - target.pos[1])**2)
        
        if self.collided_with_block or self.went_out_of_bounds:
            self.fitness = 1 / (distance_to_target + 1) - self.collision_penalty
        elif self.genome_completed:
            self.fitness = 1 / (distance_to_target + 1) - self.genome_completion_penalty
        else:
            self.fitness = 1 / (distance_to_target + 1)

        
        if self.collided_with_block or self.went_out_of_bounds or self.genome_completed:
            print(f"fitness: {self.fitness} - penalized")
        else:
            print(f"fitness: {self.fitness}")

    def mutate(self, mutation_rate):
        mutated_genome = []
        for gene in self.genome:
            if random.random() < mutation_rate:
                mutated_gene = (gene[0] + random.uniform(-1, 1), gene[1] + random.uniform(-1, 1))
            else:
                mutated_gene = gene
            mutated_genome.append(mutated_gene)
        self.genome = mutated_genome