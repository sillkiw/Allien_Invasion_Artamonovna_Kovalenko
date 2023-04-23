import sys
import pygame as pg




class AlienInvasion:

    def __init__(self):
        pg.init()

        self.screen = pg.display.set_mode((1200, 800))
        background = pg.image.load("background.jpg")
        background = pg.transform.scale(background, (1200, 800))
        pg.display.set_caption("Alien Invasion")

    def run_game(self):
        background = pg.image.load("background.jpg")
        background = pg.transform.scale(background, (1200, 800))
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
            self.screen.blit(background, (0, 0))

            pg.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()