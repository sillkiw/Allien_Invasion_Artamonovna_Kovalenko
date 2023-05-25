import pygame as pg
from pygame.sprite import Sprite
from random import choice
class Bullet(Sprite):
    """Стрельба"""
    def __init__(self,ai_game):
        """Создание снарядов относительно расположения корабля"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings 
        self.color = self.settings.bullet_color
        
        #начальное положение снарядов
        self.rect = pg.Rect(0,0,self.settings.bullet_width,
        self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        self.rect.y += 10
        #позиция снаряда
        self.y = float(self.rect.y)
    
    def update(self):
        """Перемещение снаряда вверх"""
        #расчет новой позиции снаряда при полете
        self.y -= self.settings.bullet_speed
        #обновление позиции снаряда при полете
        self.rect.y = self.y
    
    def draw_bullet(self):
        """Отрисовка снаряда"""
        pg.draw.rect(self.screen,self.color,self.rect)