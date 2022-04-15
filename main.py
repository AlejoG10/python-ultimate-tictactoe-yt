import pygame
import sys

from const import *
from game import Game

class Main:

    def __init__(self):
        self.screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
        pygame.display.set_caption('ULTIMATE TIC TAC TOE')
        self.game = Game(ultimate=True, max=True)

    def mainloop(self):

        screen = self.screen
        game = self.game

        self.screen.fill( BG_COLOR )
        game.render_board(screen)

        while True:

            for event in pygame.event.get():

                # click
                if event.type == pygame.MOUSEBUTTONDOWN and game.playing:
                    xclick, yclick = event.pos

                    if game.board.valid_sqr(xclick, yclick):
                        game.board.mark_sqr(xclick, yclick, game.player)
                        game.board.draw_fig(screen, xclick, yclick)

                        # ultimate winner ?
                        winner = game.board.check_draw_win(screen)
                        if winner:
                            game.board.manage_win(screen, winner, onmain=True)
                            game.ultimate_winner(screen, winner)

                        game.next_turn()

                # keypress
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        game.restart()
                        self.screen.fill( BG_COLOR )
                        game.render_board(screen)

                # quit
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()


if __name__ == '__main__':
    main = Main()
    main.mainloop()