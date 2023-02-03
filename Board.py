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
    # Handle clicks on board
    def handle_click(self, mx, my, button):
        x = mx // self.tile_width
        y = my // self.tile_height
        clicked_square = self.get_square_from_pos((x, y))
        # Right Click
        if button == 1:
            # Testing: Show coord and piece in console
            print(clicked_square.coord + str(clicked_square.occupying_piece))

        # Left Click
        if button == 3:
            # highlight/un-highlight selected square
            if clicked_square.highlight == False:
                clicked_square.highlight = True
            else:
                clicked_square.highlight = False

        # Testing: Moving the pieces off squares
        #if clicked_square.occupying_piece != None:
        #    new_square = self.get_square_from_pos()
        #    new_square.occupying_piece = clicked_square.occupying_piece
        #    clicked_square.occupying_piece = None


    # Draw squares from array
    def draw(self, display):
        for square in self.squares:
            square.draw(display)
