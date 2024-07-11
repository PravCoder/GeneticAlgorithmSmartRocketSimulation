import pygame, sys, random
from settings import FPS, WIDTH, HEIGHT, WIN,BLACK,GREEN,GREY,GREY2
from rocket import Rocket
from population import Population
from block import Block
from target import Target
pygame.init()

population = Population(num_individuals=15, spawn_pos=(350, 600))
block1 = Block(pos=(250,400), width=WIDTH-250, height=15)
block2 = Block(pos=(0,150), width=300, height=15)
target = Target(pos=(370, 20), width=50, height=50)


def main():
    run = True
    clock = pygame.time.Clock()
    
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        WIN.fill(GREY2)
        block1.draw()
        block2.draw()
        target.draw()
        population.draw_population()

        population.move()
        population.check_collisions(block1, block2, target)

        if population.is_population_dead() == True:
            population.create_new_generation()

        pygame.display.update()

if __name__ == "__main__":
    main()

"""
If a rocket has not crashed into any obstacles, has not reached the target, has not gone out of bounds, and has reached the end of its genome sequence instructions, you typically consider it in terms of its final position
"""