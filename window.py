import sys
import pygame as pg
from settings import Settings 
from ship import Ship
from bullet import Bullet
from allien import Alien


class AlienInvasion:

    def __init__(self):
        pg.init()
        self.settings = Settings()
        self.screen = pg.display.set_mode((0,0),pg.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.background = pg.transform.scale(self.settings.bg_image, (self.settings.screen_width, self.settings.screen_height))

        self.ship = Ship(self)
        self.bullets = pg.sprite.Group()
        self.aliens = pg.sprite.Group()
        self._create_fleet()
        pg.display.set_caption("Alien Invasion")

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

    def _update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _create_fleet(self):
        alien = Alien(self)
        self.aliens.add(alien)
    def _update_screen(self):
        self.screen.blit(self.background, (0, 0))
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        pg.display.flip()

    def _check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN:
              self._check_keydown_events(event)
            elif event.type == pg.KEYUP:
              self._check_keyup_events(event)  
         
    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _check_keydown_events(self,event):
          if event.key == pg.K_RIGHT:
                    self.ship.moving_right = True
          elif event.key == pg.K_LEFT:
                    self.ship.moving_left = True
          elif event.key == pg.K_q:
                    sys.exit()
          elif event.key == pg.K_SPACE:
                    self._fire_bullet()
    def _check_keyup_events(self,event):
          if event.key == pg.K_RIGHT:
                    self.ship.moving_right=False
          elif event.key == pg.K_LEFT:
                    self.ship.moving_left = False
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()