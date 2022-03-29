import pygame

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

WHITE =  (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GRAY = (128, 128, 128)

CROWN = pygame.transform.scale(pygame.image.load('assets/graycrown.png'), (45, 25))

