import pygame
from Piece import Piece

class Knight(Piece):
    def __init__(self, pos, color, board):
        super().__init__(pos, color, board)
        # set path for images and scale for board
        img_path = 'img/' + color[0] + 'knight.png'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width - 15, board.tile_height - 15))
        # give letter notation
        self.notation = 'N'

# get all moves for Knight (SUPER DUPER LAZY)
    def get_all_moves(self, board):
        output = []
        # top left
        move = board.get_square_from_pos(((self.pos[0] - 1), (self.pos[1] - 2)))
        if move is not None:
            output.append(move)
        # top left
        move = board.get_square_from_pos(((self.pos[0] - 2), (self.pos[1] - 1)))
        if move is not None:
            output.append(move)
        # bottom left
        move = board.get_square_from_pos(((self.pos[0] - 1), (self.pos[1] + 2)))
        if move is not None:
            output.append(move)
        # bottom left
        move = board.get_square_from_pos(((self.pos[0] - 2), (self.pos[1] + 1)))
        if move is not None:
            output.append(move)
        # top right
        move = board.get_square_from_pos(((self.pos[0] + 1), (self.pos[1] - 2)))
        if move is not None:
            output.append(move)
        # top right
        move = board.get_square_from_pos(((self.pos[0] + 2), (self.pos[1] - 1)))
        if move is not None:
            output.append(move)
        # bottom right
        move = board.get_square_from_pos(((self.pos[0] + 1), (self.pos[1] + 2)))
        if move is not None:
            output.append(move)
        # bottom right
        move = board.get_square_from_pos(((self.pos[0] + 2), (self.pos[1] + 1)))
        if move is not None:
            output.append(move)

        return output