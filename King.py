import pygame
from Piece import Piece

class King(Piece):
    def __init__(self, pos, color, board):
        super().__init__(pos, color, board)
        # set path for images and scale for board
        img_path = 'img/' + color[0] + 'king.png'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width - 15, board.tile_height - 15))
        # give letter notation
        self.notation = 'K'

# get all moves for King
    def get_all_moves(self, board):
        output = []
        # front
        move = board.get_square_from_pos(((self.pos[0]), (self.pos[1] - 1)))
        if move is not None:
            if move.occupying_piece is None:
                output.append(move)
            else:
                if move.occupying_piece.color != self.color:
                    output.append(move)
        move = board.get_square_from_pos(((self.pos[0] + 1), (self.pos[1] - 1)))
        if move is not None:
            if move.occupying_piece is None:
                output.append(move)
            else:
                if move.occupying_piece.color != self.color:
                    output.append(move)
        move = board.get_square_from_pos(((self.pos[0] - 1), (self.pos[1] - 1)))
        if move is not None:
            if move.occupying_piece is None:
                output.append(move)
            else:
                if move.occupying_piece.color != self.color:
                    output.append(move)
        # back
        move = board.get_square_from_pos(((self.pos[0]), (self.pos[1] + 1)))
        if move is not None:
            if move.occupying_piece is None:
                output.append(move)
            else:
                if move.occupying_piece.color != self.color:
                    output.append(move)

        move = board.get_square_from_pos(((self.pos[0] + 1), (self.pos[1] + 1)))
        if move is not None:
            if move.occupying_piece is None:
                output.append(move)
            else:
                if move.occupying_piece.color != self.color:
                    output.append(move)
        move = board.get_square_from_pos(((self.pos[0] - 1), (self.pos[1] + 1)))
        if move is not None:
            if move.occupying_piece is None:
                output.append(move)
            else:
                if move.occupying_piece.color != self.color:
                    output.append(move)
        # sides
        move = board.get_square_from_pos(((self.pos[0] + 1), (self.pos[1])))
        if move is not None:
            if move.occupying_piece is None:
                output.append(move)
            else:
                if move.occupying_piece.color != self.color:
                    output.append(move)
        move = board.get_square_from_pos(((self.pos[0] - 1), (self.pos[1])))
        if move is not None:
            if move.occupying_piece is None:
                output.append(move)
            else:
                if move.occupying_piece.color != self.color:
                    output.append(move)
        return output
    # do checks for check/checkmate, color(all pieces block, but if opp color, you can take)
    def get_legal_moves(self):
        output = []

        return output