import pygame
from const import *
from board import Board
from dragger import Dragger

class Game:

    def __init__(self):
        self.board = Board()
        self.dragger = Dragger()

    def show_bg(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if (row +col) % 2 == 0:
                    color = (240,240,240)
                else:
                    color = (30,30,30)

                rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)
                
                pygame.draw.rect(surface, color, rect)


    def show_pieces(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                #check if theres a piece on a certain square
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece

                    img = pygame.image.load(piece.texture)
                    img_center = col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2
                    piece.texture_rect = img.get_rect(center=img_center)
                    surface.blit(img, piece.texture_rect)

                    # texture
                    self.piece.set_texture(size=120)
                    texture = self.piece.texture
                    # img
                    img = pygame.image.load(texture)
                    # rect
                    img_center = (self.mouseX, self.mouseY)
                    self.piece.texture_rect = img.get_rect(img_center)