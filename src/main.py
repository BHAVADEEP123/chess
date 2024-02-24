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
        while True:
            game.show_bg(surface)
            for event in pygame.event.get():
                if(event.type==pygame.QUIT):
                    pygame.quit()
                    sys.exit()
            
            pygame.display.update()

#calling main func
main = Main()
main.mainloop()