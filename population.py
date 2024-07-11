import pygame, random
from settings import *
from rocket import Rocket

class Population:
    
    def __init__(self, num_individuals, spawn_pos):
        self.num_individuals = num_individuals
        self.spawn_pos = spawn_pos
        self.chromosomes = []
        self.create_population()

    def create_population(self):
        for _ in range(self.num_individuals):
            cur_rocket = Rocket(pos=(self.spawn_pos[0], self.spawn_pos[1]), genome=self.random_genome())  
            self.chromosomes.append(cur_rocket)

    def draw_population(self):
        for rocket in self.chromosomes:
            rocket.draw()

    def move(self):
        for rocket in self.chromosomes:
            rocket.move()

    def random_genome(self): # for inital pop
        genome = []
        for _ in range(250):
            # (vx, vy) vx positive move right, negative move left vy positive move down, negative move up
            genome.append((random.randint(-max_rocket_vel, max_rocket_vel), random.randint(-max_rocket_vel, max_rocket_vel)))
        return genome
    
    def eval_fitness(self):
        pass