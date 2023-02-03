import pygame

class Square:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.pos = (x, y)
        self.highlight = False
        # attribute to track current piece on square
        self.occupying_piece = None
        # chess coord for square
        self.coord = self.get_coord()
        # abs value for draw
        self.abs_x = x * width
        self.abs_y = y * height
        self.abs_pos = (self.abs_x, self. abs_y)
        # decide color - set color
        self.color = 'light' if (x + y) % 2 == 0 else 'dark'
        self.draw_color = (220, 208, 194) if self.color == 'light' else (53, 53, 53)
        self.highlight_color = (100, 249, 83) if self.color == 'light' else (0, 228, 10)
        # Rect for draw
        self.rect = pygame.Rect(
            self.abs_x,
            self.abs_y,
            width,
            height
        )

    # return the chess board coord eg. a1, c4, e4
    def get_coord(self):
        columns = 'abcdefgh'
        return columns[self.x] + str(8 - self.y)

    # draw the square
    def draw(self, display):
        if self.highlight:
            pygame.draw.rect(display, self.highlight_color, self.rect)
        else:
            pygame.draw.rect(display, self.draw_color, self.rect)
        # if square has a piece, draw piece
        if self.occupying_piece != None:
            centering_rect = self.occupying_piece.img.get_rect()
            centering_rect.center = self.rect.center
            display.blit(self.occupying_piece.img, centering_rect.topleft)