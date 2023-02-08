import pygame
from Square import Square
from Pawn import Pawn
from Knight import Knight
from Bishop import Bishop
from Rook import Rook
from Queen import Queen
from King import King

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        # work out tile size - chess is 8x8
        self.tile_width = width // 8
        self.tile_height = height // 8
        # Track selected piece and turn
        self.selected_piece = None
        self.turn = 'white'
        # Array of board's squares
        self.squares = self.generate_squares()
        # starting position config
        self.config = [
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'],
        ]
        self.setup_board()
    # Generate squares for 8x8
    def generate_squares(self):
        output = []
        for y in range(8):
            for x in range(8):
                output.append(
                    Square(x, y, self.tile_width, self.tile_height)
                )
        return output
    # Return a square from given coords
    def get_square_from_pos(self, pos):
        for square in self.squares:
            if (square.x, square.y) == (pos[0], pos[1]):
                return square
    # Return a piece from a given position if it occupies the square
    def get_piece_from_pos(self, pos):
        if self.get_square_from_pos(pos) is not None:
            if self.get_square_from_pos(pos).occupying_piece is not None:
                return self.get_square_from_pos(pos).occupying_piece
    # setup board starting position
    def setup_board(self):
        # iterating 2d list
        for y, row in enumerate(self.config):
            for x, piece in enumerate(row):
                if piece != '':
                    square = self.get_square_from_pos((x, y))
                    # Checking from config and setting the squares' pieces
                    if piece[1] == 'R':
                        square.occupying_piece = Rook(
                            (x, y), 'white' if piece[0] == 'w' else 'black', self
                        )
                    elif piece[1] == 'N':
                        square.occupying_piece = Knight(
                            (x, y), 'white' if piece[0] == 'w' else 'black', self
                        )
                    elif piece[1] == 'B':
                        square.occupying_piece = Bishop(
                            (x, y), 'white' if piece[0] == 'w' else 'black', self
                        )
                    elif piece[1] == 'Q':
                        square.occupying_piece = Queen(
                            (x, y), 'white' if piece[0] == 'w' else 'black', self
                        )
                    elif piece[1] == 'K':
                        square.occupying_piece = King(
                            (x, y), 'white' if piece[0] == 'w' else 'black', self
                        )
                    elif piece[1] == 'P':
                        square.occupying_piece = Pawn(
                            (x, y), 'white' if piece[0] == 'w' else 'black', self
                        )
    # change piece location
    def move(self, x , y):
        prev_sq = self.get_square_from_pos(self.selected_piece.pos)
        next_sq = self.get_square_from_pos((x, y))
        # if pawn takes en passent, capture the pawn below the target square
        if self.selected_piece.notation == ' ':
            if self.selected_piece.color == 'white':
                sq = self.get_square_from_pos((next_sq.x, (next_sq.y + 1)))
                pawn = self.get_square_from_pos((next_sq.x, (next_sq.y + 1))).occupying_piece
                if pawn is not None:
                    if pawn.en_passent_available:
                        # set square to no occupying piece
                        sq.occupying_piece = None
            if self.selected_piece.color == 'black':
                sq = self.get_square_from_pos((next_sq.x, (next_sq.y - 1)))
                pawn = self.get_square_from_pos((next_sq.x, (next_sq.y - 1))).occupying_piece
                if pawn is not None:
                    if pawn.en_passent_available:
                        # set square to no occupying piece
                        sq.occupying_piece = None
        # en passent is no longer available
        for s in self.squares:
            if s.occupying_piece is not None:
                if s.occupying_piece.notation == ' ':
                    s.occupying_piece.en_passent_available = False
        # update has moved
        self.selected_piece.has_moved = True
        # if is a pawn move that moves 2 squares, en passent is true
        if self.selected_piece.notation == ' ':
            if self.selected_piece.color == 'white':
                diff = (prev_sq.y) - (next_sq.y)
            else:
                diff = (next_sq.y) - (prev_sq.y)
            if diff == 2:
                self.selected_piece.en_passent_available = True

        # change position
        self.selected_piece.pos = next_sq.pos
        next_sq.occupying_piece = self.selected_piece
        # clear previous
        prev_sq.occupying_piece = None
        self.selected_piece = None
        # Un-highlight all squares
        for square in self.squares:
            square.highlight = False

        # Toggle Turn
        if self.turn == 'white':
            self.turn = 'black'
        elif self.turn == 'black':
            self.turn = 'white'

    # Handle clicks on board
    def handle_click(self, mx, my, button):
        x = mx // self.tile_width
        y = my // self.tile_height
        clicked_square = self.get_square_from_pos((x, y))
        # Right Click
        if button == 1:
            # select piece
            if self.selected_piece is None:
                if clicked_square.occupying_piece is not None:
                    if clicked_square.occupying_piece.color == self.turn:
                        self.selected_piece = clicked_square.occupying_piece
            # if there is a selected piece,
            else:
                # occupied landing-square:
                # if it is your own piece, deselect
                if clicked_square.occupying_piece is not None:
                    if clicked_square.occupying_piece.color == self.selected_piece.color:
                        for square in self.squares:
                            square.highlight = False
                        self.selected_piece = None

                    # NEED TO IMPLEMENT CHECKS/MATE
                    # PAWN PROMO (push/cap, select promo, new piece, check if king in check etc)
                    # EN PASSENT, CASTLING (move Rook with King)
                    # MAKE SURE PIECES CAN ONLY MAKE LEGAL MOVES

                    # if it is an opponents piece, check if you can take it, then move or reset
                    else:
                        if clicked_square in self.selected_piece.get_all_moves(self):
                            self.move(x, y)
                        # or deselect
                        else:
                            for square in self.squares:
                                square.highlight = False
                            self.selected_piece = None
                # unoccupied landing-square:
                # if it is a move from get_all_moves, move or reset
                if clicked_square.occupying_piece is None:
                    if clicked_square in self.selected_piece.get_all_moves(self):
                        self.move(x, y)
                    # or deselect
                    else:
                        for square in self.squares:
                            square.highlight = False
                        self.selected_piece = None
        # Left Click
        if button == 3:
            # highlight/un-highlight selected square
            if not clicked_square.highlight:
                clicked_square.highlight = True
            else:
                clicked_square.highlight = False

    # Draw
    def draw(self, display):
        # when clicked, highlight current square and legal moves
        if self.selected_piece is not None:
            self.get_square_from_pos(self.selected_piece.pos).highlight = True
            for square in self.selected_piece.get_all_moves(self):
                square.highlight = True
        # draw squares from array
        for square in self.squares:
            square.draw(display)
