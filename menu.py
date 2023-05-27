import pygame as pg
class Menu:
    def __init__(self):
        self._callbacks = []
        self.current_option_index = 0
        self._current_option_index = 0
        self.font = pg.font.SysFont(None, 48)
    def append_option(self,option,callback):
        self._option_surfaces.append(self.font.render(option,True,(255,255,255)))