import pygame
pygame.font.init()

BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (255,69,0)
GREY = (65, 64, 90)
BLUE = (30,144,255)
GREEN = (0,255,0)
GOLD = (255,185,15)
BROWN = (184,134,11)
GREY2 = (100,100,100)

WIDTH = 700
HEIGHT = 750 
FONT = pygame.font.SysFont("Arial", 20) 
FPS = 60       
ROCKET_WIDTH = 10
ROCKET_HEIGHT = 20
max_rocket_vel = 5

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
WIN.fill(GREY2)