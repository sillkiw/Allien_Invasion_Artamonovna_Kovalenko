from bullet import Bullet
import pygame as pg
class AllienBullet(Bullet):
    def __init__(self,ai_setting,allien):
        super().__init__(ai_setting)
        self.color = (255, 0, 0)
        
        #начальное положение снарядов
        self.rect = pg.Rect(0,0,self.settings.bullet_width+2,
        self.settings.bullet_height+10)
        self.rect.midtop = allien.rect.midtop
        self.rect.y += 30
        self.y = float(self.rect.y)
    def update(self):
        """Перемещение снаряда вверх"""
        #расчет новой позиции снаряда при полете
        self.y += self.settings.alien_bullet_speed
        #обновление позиции снаряда при полете
        self.rect.y = self.y
    
    def draw_bullet(self):
        """Отрисовка снаряда"""
        pg.draw.circle(self.screen,self.color,(self.rect.x,self.rect.y),8)
        