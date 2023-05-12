import pygame as pg
class Settings():

    def __init__(self):
        #Параметры экрана
        self.screen_width = 1000
        self.screen_height = 600
        
        #Изображение корабля и заднего фона
        self.bg_image = pg.image.load("images/background.png")
        self.shp_image = pg.image.load("images/ship.png")
        
        #Скорость корабля
        self.ship_speed = 4.5

        self.bullet_speed = 3.5
        self.bullet_width = 3
        self.bullet_heigh = 15
        self.bullet_color = (60,60,60)
