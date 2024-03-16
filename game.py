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
                    color = (252,168,0)
                else:
                    color = (247,217,177)

                rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)
                
                pygame.draw.rect(surface, color, rect)


    def show_pieces(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                #check if theres a piece on a certain square
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece

                    # all pieces except dragger piece
                    if piece is not self.dragger.piece:
                        piece.set_texture(size =80)
                        img = pygame.image.load(piece.texture)
                        img_center = col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2
                        piece.texture_rect = img.get_rect(center=img_center)
                        surface.blit(img, piece.texture_rect)

                    # texture
#                    self.piece.set_texture(size=128)
#                    texture = self.piece.texture
                    # img
#                    img = pygame.image.load(texture)
                    # rect
#                    img_center = (self.mouseX, self.mouseY)
#                    self.piece.texture_rect = img.get_rect(img_center)