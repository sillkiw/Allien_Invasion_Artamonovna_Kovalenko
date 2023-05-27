import pygame as pg
from pygame.sprite import Sprite

class Alien(Sprite):
    '''Пришелец'''
    def __init__(self,ai_game):
        """Создание пришельца, задание начального рапсоложения """
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.isblock = False
        #изображение пришельца5
        self.image = pg.transform.scale( pg.image.load('images/aliensh.png').convert_alpha(),(80,80))
        self.rect = self.image.get_rect()

        #создание нового пришельца в левом верхнем углу
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        #фиксация абсциссы пришельца(для отслеживания скорости)
        self.x = float(self.rect.x)
    
    def check_edges(self):
        """Проверка достижения флотом бокового края экрана"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
    def break_block(self):
        self.isblock = False
        self.image = pg.transform.scale( pg.image.load('images/aliensh.png').convert_alpha(),(80,80))
    def update(self):
        """Перемещение пришельца в сторону"""
        self.x += self.settings.alien_speed*self.settings.fleet_direction
        self.rect.x = self.x   

   