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
    def get_all_moves(self, board):
        output = []
        if self.color == 'white':
            if not self.has_moved:
                move = board.get_square_from_pos(((self.pos[0]), (self.pos[1] - 1)))
                if move is not None:
                    output.append(move)
                move = board.get_square_from_pos(((self.pos[0]), (self.pos[1] - 2)))
                if move is not None:
                    output.append(move)
            else:
                move = board.get_square_from_pos(((self.pos[0]), (self.pos[1] - 1)))
                if move is not None:
                    output.append(move)
        else:
            if not self.has_moved:
                move = board.get_square_from_pos(((self.pos[0]), (self.pos[1] + 1)))
                if move is not None:
                    output.append(move)
                move = board.get_square_from_pos(((self.pos[0]), (self.pos[1] + 2)))
                if move is not None:
                    output.append(move)
            else:
                move = board.get_square_from_pos(((self.pos[0]), (self.pos[1] + 1)))
                if move is not None:
                    output.append(move)
        return output


    # do checks for check/checkmate, color(all pieces block, but if opp color, you can take)
    def get_legal_moves(self):
        output = []

        # Castling - King cannot move through check
        # Promotion of Pawn
        return output
