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
        self.en_passent_available = False

    # get all moves for Pawn, then check for legality
    def get_all_moves(self, board):
        output = []
        # pawn movement for white
        if self.color == 'white':
            # two possible moves if haven't moved yet
            if not self.has_moved:
                move = board.get_square_from_pos(((self.pos[0]), (self.pos[1] - 1)))
                if move is not None:
                    if move.occupying_piece is None:
                        output.append(move)
                move = board.get_square_from_pos(((self.pos[0]), (self.pos[1] - 2)))
                if move is not None:
                    if move.occupying_piece is None:
                        output.append(move)
            else:
                move = board.get_square_from_pos(((self.pos[0]), (self.pos[1] - 1)))
                if move is not None:
                    if move.occupying_piece is None:
                        output.append(move)
            # check for enemies on diagonals
            move = board.get_square_from_pos(((self.pos[0] - 1), (self.pos[1] - 1)))
            if move is not None:
                if move.occupying_piece is not None and move.occupying_piece.color == 'black':
                    output.append(move)
            move = board.get_square_from_pos(((self.pos[0] + 1), (self.pos[1] - 1)))
            if move is not None:
                if move.occupying_piece is not None and move.occupying_piece.color == 'black':
                    output.append(move)
            # check for en passent
            # left
            piece = board.get_piece_from_pos(((self.pos[0] - 1), (self.pos[1])))
            move = board.get_square_from_pos(((self.pos[0] - 1), (self.pos[1] - 1)))
            if piece is not None:
                if piece.notation == ' ' and piece.en_passent_available:
                    if move is not None:
                        output.append(move)
            # right
            piece = board.get_piece_from_pos(((self.pos[0] + 1), (self.pos[1])))
            move = board.get_square_from_pos(((self.pos[0] + 1), (self.pos[1] - 1)))
            if piece is not None:
                if piece.notation == ' ' and piece.en_passent_available:
                    if move is not None:
                        output.append(move)
        # pawn movement for black
        else:
            if not self.has_moved:
                move = board.get_square_from_pos(((self.pos[0]), (self.pos[1] + 1)))
                if move is not None:
                    if move.occupying_piece is None:
                        output.append(move)
                move = board.get_square_from_pos(((self.pos[0]), (self.pos[1] + 2)))
                if move is not None:
                    if move.occupying_piece is None:
                        output.append(move)
            else:
                move = board.get_square_from_pos(((self.pos[0]), (self.pos[1] + 1)))
                if move is not None:
                    if move.occupying_piece is None:
                        output.append(move)
            # check for enemies on diagonals
            move = board.get_square_from_pos(((self.pos[0] - 1), (self.pos[1] + 1)))
            if move is not None:
                if move.occupying_piece is not None and move.occupying_piece.color == 'white':
                    output.append(move)
            move = board.get_square_from_pos(((self.pos[0] + 1), (self.pos[1] + 1)))
            if move is not None:
                if move.occupying_piece is not None and move.occupying_piece.color == 'white':
                    output.append(move)
            # check for en passent
            piece = board.get_piece_from_pos(((self.pos[0] + 1), (self.pos[1])))
            move = board.get_square_from_pos(((self.pos[0] + 1), (self.pos[1] + 1)))
            if piece is not None:
                if piece.notation == ' ' and piece.en_passent_available:
                    if move is not None:
                        output.append(move)
            piece = board.get_piece_from_pos(((self.pos[0] - 1), (self.pos[1])))
            move = board.get_square_from_pos(((self.pos[0] - 1), (self.pos[1] + 1)))
            if piece is not None:
                if piece.notation == ' ' and piece.en_passent_available:
                    if move is not None:
                        output.append(move)

        return output


    # do checks for check/checkmate, color(all pieces block, but if opp color, you can take)
    def get_legal_moves(self):
        output = []

        # Castling - King cannot move through check
        # Promotion of Pawn
        return output
