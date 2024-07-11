import pygame, random
from rocket import Rocket

class Population:
    
    def __init__(self, num_individuals, spawn_pos):
        self.num_individuals = num_individuals
        self.spawn_pos = spawn_pos
        self.chromosomes = []
        self.create_population()
        
    def create_population(self):
        for _ in range(self.num_individuals):
            cur_rocket = Rocket(pos=(self.spawn_pos[0], self.spawn_pos[1]))  
            self.chromosomes.append(cur_rocket)

    def draw_population(self):
        for rocket in self.chromosomes:
            rocket.draw()


    # temp
    def move(self):
        for rocket in self.chromosomes:
            rocket.move(vx=random.randint(-5, 5), vy=random.randint(-5, 0))