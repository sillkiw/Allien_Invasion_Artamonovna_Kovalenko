import pygame as pg
class Settings():

    def __init__(self):
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_image = pg.image.load("images/background.png")
        self.shp_image = pg.image.load("images/ship.png")
        self.ship_speed = 1.5