import pygame
from copy import deepcopy

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def minimax(position, depth, max_player, game):
    
    if depth == 0 or position.winner() != None:
        return position.evaluate(), position
    
    if max_player:
        maxEval = float('-inf')
        best_move = None

        for move in get_all_moves(position, WHITE, game):

            eval = minimax(move, depth - 1, False, game)
            maxEval = max(maxEval, eval)

            if maxEval == eval:
                best_move = move

        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None

        for move in get_all_moves(position, BLACK, game):

            eval = minimax(move, depth - 1, True, game)
            minEval = min(minEval, eval)

            if minEval == eval:
                best_move = move

        return minEval, best_move
        

def simulate_move(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])

    if skip:
        board.remove(skip)

    return board

def get_all_moves(board, color, game):
    moves = []

    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)

        for move, skip in valid_moves.items():
            
            temp_board = deepcopy(board) # Uses tempray board when testing and not the actual board
            new_board = simulate_move(piece, move, temp_board, game, skip)
            
            moves.append(new_board)
    
    return moves
