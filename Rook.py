import pygame
from Piece import Piece

class Rook(Piece):
    def __init__(self, pos, color, board):
        super().__init__(pos, color, board)
        # set path for images and scale for board
        img_path = 'img/' + color[0] + 'rook.png'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width - 15, board.tile_height - 15))
        # give letter notation
        self.notation = 'R'

    # get all moves for Rook (THIS IS SUPER LAZY!)
    def get_all_moves(self, board):
        output = []
        # up & down
        for i in range(1, 8):
            move = board.get_square_from_pos((self.pos[0], (self.pos[1] - i)))
            if move is not None:
                if move.occupying_piece is None:
                    output.append(move)
                else:
                    if move.occupying_piece.color != self.color:
                        output.append(move)
                    break
        for i in range(1, 8):
            move = board.get_square_from_pos((self.pos[0], (self.pos[1] + i)))
            if move is not None:
                if move.occupying_piece is None:
                    output.append(move)
                else:
                    if move.occupying_piece.color != self.color:
                        output.append(move)
                    break
        # left & right
        for i in range(1, 8):
            move = board.get_square_from_pos(((self.pos[0] - i), self.pos[1]))
            if move is not None:
                if move.occupying_piece is None:
                    output.append(move)
                else:
                    if move.occupying_piece.color != self.color:
                        output.append(move)
                    break
        for i in range(1, 8):
            move = board.get_square_from_pos(((self.pos[0] + i), self.pos[1]))
            if move is not None:
                if move.occupying_piece is None:
                    output.append(move)
                else:
                    if move.occupying_piece.color != self.color:
                        output.append(move)
                    break
        return output

    # do checks for check/checkmate
    def get_legal_moves(self):
        output = []

        return output