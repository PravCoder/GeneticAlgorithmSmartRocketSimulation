import pygame, sys, random
from settings import FPS, WIDTH, HEIGHT, WIN,BLACK,GREEN,GREY,GREY2
from rocket import Rocket
pygame.init()

r1 = Rocket(pos=(350, 600))  

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
        r1.draw()
        r1.move(vx=random.randint(0, 5), vy=random.randint(-5, 5))

        pygame.display.update()

if __name__ == "__main__":
    main()