import pygame
from const import *

class Dragger:
    def __init__(self) -> None:
        self.piece = None
        self.dragging = False
        self.mousex = 0
        self.mousey = 0
        self.initial_row = 0
        self.initial_col = 0
    
    def update_blit(self, surface):
        texture = self.piece.texture
        img = pygame.image.load(texture)
        img_center = (self.mousex, self.mousey)
        self.piece.texture_rect = img.get_rect(center=img_center)
        #update blit
        surface.blit(img, self.piece.texture_rect)

    def update_mouse(self, pos):
        self.mousex, self.mousey = pos
    
    def save_initial(self,pos):
        self.initial_row = pos[1]//SQSIZE
        self.initial_col = pos[0]//SQSIZE

    def drag_piece(self, piece):
        self.piece = piece
        self.dragging = True
    
    def undrag_piece(self):
        self.piece = None
        self.dragging = False