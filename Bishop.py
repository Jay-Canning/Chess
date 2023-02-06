import pygame
from Piece import Piece

class Bishop(Piece):
    def __init__(self, pos, color, board):
        super().__init__(pos, color, board)
        # set path for images and scale for board
        img_path = 'img/' + color[0] + 'bishop.png'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width - 15, board.tile_height - 15))
        # give letter notation
        self.notation = 'B'

    # get all moves for Bishop (THIS IS SUPER LAZY!)
    def get_all_moves(self, board):
        output = []
        # NW & SE
        for i in range(1,8):
            move = board.get_square_from_pos((self.pos[0] - i, (self.pos[1] - i)))
            if move is not None:
                if move.occupying_piece is None:
                    output.append(move)
                else:
                    if move.occupying_piece.color != self.color:
                        output.append(move)
                    break
        for i in range(1, 8):
            move = board.get_square_from_pos((self.pos[0] + i, (self.pos[1] + i)))
            if move is not None:
                if move.occupying_piece is None:
                    output.append(move)
                else:
                    if move.occupying_piece.color != self.color:
                        output.append(move)
                    break
        # NE & SW
        for i in range(1, 8):
            move = board.get_square_from_pos(((self.pos[0] - i), self.pos[1] + i))
            if move is not None:
                if move.occupying_piece is None:
                    output.append(move)
                else:
                    if move.occupying_piece.color != self.color:
                        output.append(move)
                    break
        for i in range(1, 8):
            move = board.get_square_from_pos(((self.pos[0] + i), self.pos[1] - i))
            if move is not None:
                if move.occupying_piece is None:
                    output.append(move)
                else:
                    if move.occupying_piece.color != self.color:
                        output.append(move)
                    break
        return output
    # do checks for check/checkmate, color(all pieces block, but if opp color, you can take)
    def get_legal_moves(self):
        output = []

        return output