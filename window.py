import sys
import pygame as pg




class AlienInvasion:

    def __init__(self):
        pg.init()

        self.screen = pg.display.set_mode((900, 600))
        self.background = pg.transform.scale(pg.image.load("background.jpg"), (1200, 800))
        pg.display.set_caption("Alien Invasion")

    def run_game(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
            self.screen.blit(self.background, (0, 0))
            pg.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()