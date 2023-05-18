import pygame as pg
class Settings():
    """Для хранения параметров игры"""
    def __init__(self):
        #Параметры экрана
        self.screen_width = 1000
        self.screen_height = 600
        
        #Изображение корабля и заднего фона
        self.bg_image = pg.image.load("images/background.png")
        self.shp_image = pg.image.load("images/ship.png")
        
        #Скорость корабля
        self.ship_speed = 6.5
        #ограничение кол-ва кораблей на игру
        self.ship_limit = 3
        
        #параметры стрельбы
        self.bullet_speed = 7.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0,0,255)
        self.bullets_allowed = 3

        #параметры пришельцев

        #скорость движения в сторону
        self.alien_speed = 40
        #скорость снижения
        self.fleet_drop_speed = 30
        #направление(1 - вправо, -1 - влево)
        self.fleet_direction = 1
