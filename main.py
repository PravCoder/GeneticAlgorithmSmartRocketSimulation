import pygame, sys, random
from settings import FPS, WIDTH, HEIGHT, WIN,BLACK,GREEN,GREY,GREY2
from rocket import Rocket
from population import Population
from block import Block
pygame.init()

population = Population(10, spawn_pos=(350, 600))
block1 = Block(pos=(250,400), width=WIDTH-250, height=15)
block2 = Block(pos=(0,150), width=300, height=15)


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
        population.draw_population()
        population.move()

        pygame.display.update()

if __name__ == "__main__":
    main()

"""
If a rocket has not crashed into any obstacles, has not reached the target, has not gone out of bounds, and has reached the end of its genome sequence instructions, you typically consider it in terms of its final position
"""