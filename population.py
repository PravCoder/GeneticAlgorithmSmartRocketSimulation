import pygame, random
from settings import *
from rocket import Rocket

class Population:
    
    def __init__(self, num_individuals, spawn_pos):
        self.num_individuals = num_individuals
        self.spawn_pos = spawn_pos
        self.chromosomes = []  # individauls of current generation, list of rocket-objs
        self.genome_length = 250
        self.create_population()
        self.parent_rockets = [] # selected rockets to create offspring of this generation
        self.tournament_size = 50
        self.genetion_num = 1
        self.mutation_rate = 0.05 
        # generation stats
        self.max_reached_target = 0
        self.max_fitness = -1
        self.max_fitness = -1
        self.average_fitness = -1

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

    def random_genome(self): # for inital pop constructs list of random thrust vectors which is a genome 
        genome = []
        for _ in range(self.genome_length): # for every element in genome add a random vector (vx, vy)
            # (vx, vy) vx positive move right, negative move left vy positive move down, negative move up
            
            # left-up, right-up, left-down, right-down
            # genome.append((random.randint(-max_rocket_vel, max_rocket_vel), random.randint(-max_rocket_vel, max_rocket_vel)))
            # left-up, right-up only
            genome.append((random.randint(-max_rocket_vel, max_rocket_vel), random.randint(-max_rocket_vel, 0)))
        return genome
    

    def check_collisions(self, block1, block2, target):
        for rocket in self.chromosomes:
            if rocket.rect.colliderect(block1.rect) or rocket.rect.colliderect(block2.rect):
                rocket.dead = True
                rocket.collided_with_block = True # for fitness calculation
                #print("Block collision!")
            if rocket.rect.colliderect(target.rect):
                rocket.reached_target = True
                #print("Target reached!")
            if rocket.is_out_of_bounds() == True:
                rocket.dead = True
                rocket.went_out_of_bounds = True
                #print("Rocket out of bounds!")
            if rocket.dead == True: rocket.eval_fitness(target)
            

    def is_population_dead(self):
        for rocket in self.chromosomes:
            if rocket.dead == False:
                return False
        
        return True
    
    def create_new_generation(self): 
        self.genetion_num += 1
        self.select_best_rockets_tournament_selection()  # use tournament selection to select best rockets based on fitness
        self.chromosomes = []  # clear the current population
        
        for _ in range(self.num_individuals // 2):
            parent1 = random.choice(self.parent_rockets)
            parent2 = random.choice(self.parent_rockets)
            
            offspring1, offspring2 = self.single_point_crossover(parent1, parent2)
            
            # Apply mutation for genetic diversity (if needed)
            offspring1.mutate(self.mutation_rate)
            offspring2.mutate(self.mutation_rate)
            
            self.chromosomes.append(offspring1)
            self.chromosomes.append(offspring2)


    def select_best_rockets_elite(self):
        sorted_rockets = sorted(self.chromosomes, key=lambda rocket: rocket.fitness, reverse=True)
        self.parent_rockets = sorted_rockets[:2]

    def select_best_rockets_tournament_selection(self):
        self.parent_rockets = [] # make sure parent rockets is clear
        for _ in range(self.num_individuals):  # iterate size of population which will also be the number of parent rockest
            self.parent_rockets.append(self.tournament_selection())

    def single_point_crossover(self, parent1, parent2):
        # choose parent with smaller genome?
        crossover_point = random.randint(1, len(parent1.genome)-1) # choose random cross-point frmo indx-1 to last index in the parent1s genome
        genome1 = parent1.genome[:crossover_point] + parent2.genome[crossover_point:] # take genomes of p1 before crossover-point, and combine it with genomes of p2 after crossover-point
        genome2 = parent1.genome[crossover_point:] + parent2.genome[:crossover_point] #  take genomes of p1 after crossover-point, and combine it with genomes of p2 before crossover-point 
        offspring1 = Rocket(pos=self.spawn_pos, genome=genome1)
        offspring2 = Rocket(pos=self.spawn_pos, genome=genome2)
        return offspring1, offspring2
    
    def tournament_selection(self):
        tournament = random.sample(self.chromosomes, self.tournament_size) # from the population of rockets select a subet of rockets (tournament-size)
        tournament.sort(key=lambda rocket: rocket.fitness, reverse=True) # from teh randomly selected rocket sort them based on fitness and return the highest fitness rocket
        return tournament[0]                                            # return the highest fitness of the selected sample

    def show_info(self, prin=True):
        
        all_fitness = [r.fitness for r in self.chromosomes]
        num_reached_target = sum([1  for r in self.chromosomes if r.reached_target])
        self.max_fitness = max(all_fitness)
        self.min_fitness = min(all_fitness)
        self.average_fitness = sum(all_fitness) / len(all_fitness)
        self.max_reached_target = max(self.max_reached_target, num_reached_target)
        if prin:
            print(f"\nGenetion #{self.genetion_num}")
            print(f"Max fitness: {self.max_fitness}")
            print(f"Min fitness: {self.min_fitness}")
            print(f"Average fitness: {self.average_fitness}")
            print(f"Num reached target: {num_reached_target}")

        a = FONT.render(f"Previous Gen #{self.genetion_num}", 1, WHITE)
        b = FONT.render(f"Max fitness: {self.max_fitness}", 1, WHITE)
        c = FONT.render(f"Min fitness: {self.min_fitness}", 1, WHITE)
        d = FONT.render(f"Average fitness: {self.average_fitness}", 1, WHITE)
        e = FONT.render(f"Num reached target: {num_reached_target}", 1, WHITE)

        texts = [a, b, c, d, e]
        x, y, increment = 30, 600, 30
        for t in texts:
            WIN.blit(t, (x, y))
            y += increment
        