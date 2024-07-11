import pygame, sys, random
from settings import FPS, WIDTH, HEIGHT, WIN,BLACK,GREEN,GREY,GREY2
from rocket import Rocket
from population import Population
pygame.init()

population = Population(5, spawn_pos=(350, 600))

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
        population.draw_population()
        population.move()

        pygame.display.update()

if __name__ == "__main__":
    main()