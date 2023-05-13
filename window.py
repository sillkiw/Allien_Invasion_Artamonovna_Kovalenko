import sys
import pygame as pg
from settings import Settings 
from ship import Ship
from bullet import Bullet
from allien import Alien
import random


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
        alien_width,alien_height = alien.rect.size
        available_space_x = self.settings.screen_width-(2*alien_width)
        number_aliens_x = available_space_x // (2*alien_width)

        ship_height = self.ship.rect.height
        available_space_y = self.settings.screen_height - (alien_height)-ship_height
        number_rows = available_space_y // (2*alien_height)
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number,row_number)

    def _create_alien(self,alien_number,row_number):
        alien = Alien(self)
        alien_width,alien_height = alien.rect.size
        alien.x = alien_width+2*alien_width*alien_number 
        alien.rect.x = alien.x+random.choice([-35,25,0])
        alien.rect.y = alien.rect.height +  1.5*alien.rect.height * row_number
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
            pg.mixer.Sound("sounds/fire.mp3").play()
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