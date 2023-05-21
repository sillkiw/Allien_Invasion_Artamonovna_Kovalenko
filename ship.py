import pygame as pg
from pygame.sprite import Sprite

class Ship(Sprite):
    """Управление коряблем"""
    def __init__(self,ai_game):
        
        #создание корабля(корабль рассматривается как прямоугольник)
        super().__init__()
        
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = self.screen.get_rect()
        
        #загрузка изображения корабля
        self.image = pg.transform.scale(ai_game.settings.shp_image.convert_alpha(),(90,90))
        self.rect = self.image.get_rect()

        #задание стартовой позитиции корабля(середина нижнего края экрана)
        self.rect.midbottom = self.screen_rect.midbottom
      
        self.x = float(self.rect.x)

        #Флаги перемещения
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """Ограничение движение корабля в рамках экрана"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x +=self.settings.ship_speed
        if self.moving_left and self.rect.left>0:
            self.x -=self.settings.ship_speed
        self.rect.x = self.x

    def blitme(self):
        """Отрисовка корабля на экране в настоящий момент времени"""
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        """Размещение корабля в середине нижней части экрана"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)