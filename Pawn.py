import pygame
from Piece import Piece

class Pawn(Piece):
    def __init__(self, pos, color, board):
        super().__init__(pos, color, board)
        # set path for images and scale for board
        img_path = 'img/' + color[0] + 'pawn.png'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width - 15, board.tile_height - 15))
        # give letter notation
        self.notation = ' '
    # get all moves for Pawn, then check for legality
    def get_all_moves(self):
        output =[]
        if self.has_moved:
            pass
        return output

    # do checks for check/checkmate, color(all pieces block, but if opp color, you can take)
    def get_legal_moves(self):
        output =[]

        # Castling - King cannot move through check
        # Promotion of Pawn
        return output
