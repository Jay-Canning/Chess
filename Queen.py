import pygame
from Piece import Piece

class Queen(Piece):
    def __init__(self, pos, color, board):
        super().__init__(pos, color, board)
        # set path for images and scale for board
        img_path = 'img/' + color[0] + 'queen.png'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width - 15, board.tile_height - 15))
        # give letter notation
        self.notation = 'Q'

# get all moves for Queen (THIS IS SUPER LAZY!)
    def get_all_moves(self, board):
        output = []
        # NW & SE
        for i in range(9):
            move = board.get_square_from_pos((self.pos[0] - i, (self.pos[1] - i)))
            if move is not None:
                output.append(move)
        for i in range(9):
            move = board.get_square_from_pos((self.pos[0] + i, (self.pos[1] + i)))
            if move is not None:
                output.append(move)
        # NE & SW
        for i in range(9):
            move = board.get_square_from_pos(((self.pos[0] - i), self.pos[1] + i))
            if move is not None:
                output.append(move)
        for i in range(9):
            move = board.get_square_from_pos(((self.pos[0] + i), self.pos[1] - i))
            if move is not None:
                output.append(move)
        # up & down
        for i in range(9):
            move = board.get_square_from_pos((self.pos[0], (self.pos[1] - i)))
            if move is not None:
                output.append(move)
        for i in range(9):
            move = board.get_square_from_pos((self.pos[0], (self.pos[1] + i)))
            if move is not None:
                output.append(move)
        # left & right
        for i in range(9):
            move = board.get_square_from_pos(((self.pos[0] - i), self.pos[1]))
            if move is not None:
                output.append(move)
        for i in range(9):
            move = board.get_square_from_pos(((self.pos[0] + i), self.pos[1]))
            if move is not None:
                output.append(move)
        return output