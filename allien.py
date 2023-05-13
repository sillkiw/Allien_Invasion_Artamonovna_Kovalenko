import pygame as pg
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen

        self.image = pg.transform.scale(pg.image.load('images/aliensh.png').convert_alpha(),(84,84))
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x) 
