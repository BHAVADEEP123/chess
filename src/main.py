import pygame
import sys
from const import *
from game import Game

class Main:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption('CHESS')
        self.game = Game()
        
    
    def mainloop(self):
        surface = self.surface
        game = self.game
        dragger = self.game.dagger
        board = self.game.board
        while True:
            game.show_bg(surface)
            game.show_pieces(surface)
            if dragger.dragging:
                dragger.update_blit(surface)
            for event in pygame.event.get():
                #click
                if event.type==pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)
                    clicked_row = dragger.mousey//SQSIZE
                    clicked_col = dragger.mousex//SQSIZE
                    if board.squares[clicked_row][clicked_col].has_piece():
                        piece = board.squares[clicked_row][clicked_col].piece
                        dragger.save_initial(event.pos)
                        dragger.drag_piece(piece)

                #mouse motion
                if event.type==pygame.MOUSEMOTION:
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        # below two lines are important because for every update of blit we need to show the background also
                        # pieces rendering will happen in inner loop and it appeares to be shuttered
                        game.show_bg(surface)
                        game.show_pieces(surface)
                        dragger.update_blit(surface)

                #release
                if event.type==pygame.MOUSEBUTTONUP:
                    dragger.undrag_piece()

                if(event.type==pygame.QUIT):
                    pygame.quit()
                    sys.exit()
            
            pygame.display.update()

#calling main func
main = Main()
main.mainloop()