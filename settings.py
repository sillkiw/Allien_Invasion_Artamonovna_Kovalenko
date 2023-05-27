import pygame as pg
class Settings():
    """Для хранения параметров игры"""
    def __init__(self,ai_game,width,heigth):
        """Инициализвция статических параметров игры"""
        #Параметры экрана
        self.ai_game = ai_game
        self.screen_width  = width
        self.screen_height  =heigth
        
        #Изображение корабля и заднего фона
        self.bg_image = pg.image.load("images/background.png")
        self.shp_image = pg.image.load("images/ship.png")
        
        #Скорость корабля
        self.ship_speed = 8
        #ограничение кол-ва кораблей на игру
        self.ship_limit = 3
        
        #параметры стрельбы
        self.bullet_speed = 13
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (128, 166, 255)
        self.bullets_allowed = 3

        #параметры пришельцев
        self.allien_bullets_allowed = 1
        #скорость движения в сторону
        self.alien_speed = 5
        self.alien_bullet_speed =6
        #скорость снижения
        self.fleet_drop_speed = 10
        #направление(1 - вправо, -1 - влево)
        self.fleet_direction = 1

        #темп ускорения игры
        self.speedup_scale = 1.1

        #темп роста стоимости пришельцев
        self.score_scale = 1.5

      

        #инициализация параметров для усложнения игры
        self.initialize_dynamic_settings()



    def initialize_dynamic_settings(self):
        """Задание начальных параметров, изменяющихся в ходе игры"""            
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3.0
        self.alien_speed_factor = 1.0
        self.alien_bullet_speed =7
        #fleet_direction = 1 обозначает движение вправо, а -1 - влево            
        self.fleet_direction = 1
        self.allien_bullets_allowed = 1
        #подсчет очков
        self.alien_points = 10

    def increase_speed(self):
        """Увеличение скорости и очков за пришельцев"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale+0.2
        if self.ai_game.stats.level >= 3:
            self.allien_bullets_allowed *= 1.1
            self.alien_bullet_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
