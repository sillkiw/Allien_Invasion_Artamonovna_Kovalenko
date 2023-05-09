import pygame as pg
class Ship():
    def __init__(self,ai_game):
        self.screen = ai_game
        self.screen_rect = ai_game.get_rect()
        self.image = pg.transform.scale(pg.image.load("images/ship.png").convert_alpha(),(100,100))
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom 
    
    def blitme(self):
        self.screen.blit(self.image,self.rect)