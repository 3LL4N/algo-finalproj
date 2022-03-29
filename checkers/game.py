import pygame
from .constants import WHITE, BLACK
from .board import Board

class Game:
    def __init__(self, win): 
        self.selected = None
        self.board = Board()
        self.turn = BLACK
        self.valid_moves = {}
        self.win = win

    def update(self):
        self.board.draw()
        pygame.display.update()
