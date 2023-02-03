# Declare Libraries
import pygame
from Board import Board

# Initialise Pygame
pygame.init()
# Setup screen
WINDOW_SIZE = (600, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)
# Setup Title Bar and Icon
pygame.display.set_caption('Chess Master: Deluxe Edition')
icon = pygame.image.load('img/bpawn.png')
pygame.display.set_icon(icon)
# Setup Board
board = Board(WINDOW_SIZE[0], WINDOW_SIZE[1])
# Draw Function
def draw(display):
    board.draw(display)
    pygame.display.update()

# main Loop
if __name__ == '__main__':
    running = True
    while running:
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    board.handle_click(mx, my, 1)
                elif event.button == 3:
                    board.handle_click(mx, my, 3)

        draw(screen)
