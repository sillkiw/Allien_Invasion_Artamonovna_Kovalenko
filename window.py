import sys
import pygame as pg
from settings import Settings 




class AlienInvasion:

    def __init__(self):
        pg.init()
        self.settings = Settings()
        self.screen = pg.display.set_mode((self.settings.width, self.settings.height))
        self.background = pg.transform.scale(self.settings.load_image, (self.settings.width, self.settings.height))
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