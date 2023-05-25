import sys
import pygame as pg
import random
from time import sleep
from settings import Settings 
from ship import Ship
from bullet import Bullet
from allien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from animated_sprite import ExplosionFX
import cv2 

class AlienInvasion:
    '''Управление поведением игры'''
    def __init__(self):
        """Инициализация игры, создание окна"""    
        pg.init()
        pg.display.set_caption("Alien Invasion")

        #полноэкранный режим
        self.screen = pg.display.set_mode((0,0),pg.FULLSCREEN)
        self.settings = Settings(self.screen.get_rect().width,self.screen.get_rect().height)
        self.background = pg.transform.scale(self.settings.bg_image, (self.settings.screen_width, self.settings.screen_height))
        self.stats = GameStats(self)
        self.ship = Ship(self)
        self.bullets = pg.sprite.Group()
        self.aliens = pg.sprite.Group()
        
        self._create_fleet()
        self.images_explosion = []
        
        self.exps = pg.sprite.Group()
        for i in range(0,13):
            text = 'images/explosion/{0}.png'.format(i)
            self.images_explosion.append(pg.transform.scale(pg.image.load(text),(self.ship.rect.width,self.ship.rect.height)) )  
        self.clock = pg.time.Clock()
        #создание для хранения статистики и панели результатов
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        #создание кнопки Play
        self.play_button = Button(self, "Play")

    def run_game(self):
        """Основной цикл"""
        while True:
            self.clock.tick(80)
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
                self.update_lifetimes()
                self.delete_exps()
                self.update_count_frames()
                self.update_indences()
                self.update_frames_exps()
            self._update_screen()
            pg.time.delay(0)

    def _ship_hit(self):
        """Обработка столкновения корабля с пришельцем"""
        #уменьшение ships_left - число оставшихся кораблей
        if self.stats.ships_left > 0:
            #уменьшение ships_left и обновление панели счета
            self.stats.ships_left -= 1
            self.sb.prep_lives()

            #очистка списков пришельцев и снарядов
            self.aliens.empty()
            self.bullets.empty()

            #создание нового флота и размещение корабля в центре
            self._create_fleet()
            self.ship.center_ship()

            #пауза
            sleep(0.3)
        else:
            self._reset_game()
            self.stats.game_active = False
            #вернуть видимость курсору мыши после завершения игры
            pg.mouse.set_visible(True)

    def _create_fleet(self):
        """Создание флота пришельцев"""
        #создание одного пришельца
        alien = Alien(self)
        #размеры пришельца
        alien_width, alien_height = alien.rect.size
        #расчет свободного пространства для пришельцев
        available_space_x = self.settings.screen_width-(2*alien_width)
        #расчет количества пришельцев на экране
        number_aliens_x = available_space_x // (2*alien_width)

        #кол-во рядов пришельцев
        ship_height = self.ship.rect.height
        available_space_y = self.settings.screen_height - (alien_height)-ship_height
        number_rows = available_space_y // (2*alien_height)
        #создание флота пришельцев
        for row_number in range(number_rows):
            #создание ряда пришельцев
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _check_fleet_edges(self):
        """Проверка на достижения бокового края экрана"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _check_aliens_bottom(self):
        """Проверка на достижения нижнего края экрана пришельцами"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                #происходит то же, что при столкновении с кораблем
                self._ship_hit()
                break
    
    def _change_fleet_direction(self):
        """Снижение флота и смена направления"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _create_alien(self,alien_number, row_number):
        """Создание пришельца с учетом его места"""
        alien = Alien(self)
        alien_width,alien_height = alien.rect.size
        alien.x = alien_width+2*alien_width*alien_number 
        alien.rect.x = alien.x
        alien.rect.y = alien_height +  1.5*alien_height * row_number
        self.aliens.add(alien)

    def _update_screen(self):
        """Обновление изображения экрана"""
        self.screen.blit(self.background, (0, 0))
        self.ship.blitme()
      
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        #отрисовка пришельца
        self.aliens.draw(self.screen)
    
        #вывод счета
        self.sb.show_score()

        for exp in self.exps.sprites():
            exp.blitme()

        #отображение кнопки Play поверх других поверхностей в том случае, если игра неактивна
        if not self.stats.game_active:
            self._set_game_menu()
        
        pg.display.flip()
    
    def _set_game_menu(self):
          blmask = pg.Surface((self.settings.screen_width,self.settings.screen_height))
          blmask.fill((0,0,0))
          blmask.set_alpha(150)
          self.screen.blit(blmask,(0,0))
          self.play_button.draw_button()


    def _update_bullets(self):
        """Обновление позиций снарядов, удаление старых"""
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)  
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """проверка попадания в пришельца и последующее уничтожение снаряда и пришельца"""
        #(True, True - нужно ли удалять снаряд пришельца и  соответственно)      
        collisions = pg.sprite.groupcollide(self.bullets,self.aliens,True,True)
        #обновление счета
        if collisions:
            self.stats.score += self.settings.alien_points
         
            #1 пришелец += очки за него
            for aliens in collisions.values():
                for alien in aliens:
                    explsound =  firesound = pg.mixer.Sound("sounds/expl.mp3")
                    explsound.set_volume(0.6)
                    explsound.play()
                    x = alien.rect.centerx + 20
                    y = alien.rect.centery
                    self.exps.add(ExplosionFX(self.screen, self.images_explosion, 1, x, y))
                self.stats.score += self.settings.alien_points * len(aliens)
            #новая картинка счета
            self.sb.prep_score()
            self.sb.check_high_score()
        self.start_new_level()
       
       
       
       
       
    def start_new_level(self):
        #есть ли еще пришельцы
        if not self.aliens:
        # Уничтожение существующих снарядов и создание нового флота.
            self.bullets.empty()
            self._create_fleet()
            #увеличение скорости
            self.settings.increase_speed()
            #увеличение уровня
            self.stats.level += 1
            self.sb.prep_level()



    def _update_aliens(self):
        """Обновление позиций пришельцев"""
        self._check_fleet_edges()
        self.aliens.update()
        #проверка столкновений пришельцев с кораблем
        if pg.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        #gроверка на достижения нижнего края экрана пришельцами
        self._check_aliens_bottom()


    def _check_events(self):
        """Управление событиями(клавиш и мыши)"""
        for event in pg.event.get():
            #выход
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN:
              self._check_keydown_events(event)
            elif event.type == pg.KEYUP:
              self._check_keyup_events(event)  
            #отслеживание нажатия мыши для запуска игры
            elif event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = pg.mouse.get_pos()
                self._check_play_button(mouse_pos)
    
    def _check_play_button(self, mouse_pos):
        """Запуск новой игры только при нажатии кнопки Play."""
        #отслеживание области нажатия мыши
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self._reset_game()
    
    def _reset_game(self):
        #сброс игровых настроек(скорости)
        self.settings.initialize_dynamic_settings()

        #сброс игровой статистики
        self.stats.reset_stats()
        self.stats.game_active = True
        self.sb.prep_images()
            
            #очистка списков пришельцев и снарядов
        self.aliens.empty()
        self.bullets.empty()
            
            #создание нового флота и размещение корабля в центре
        self._create_fleet()
        self.ship.center_ship()

        #скрытие курсора мыши
        pg.mouse.set_visible(False)

    def _check_keydown_events(self,event):
          """Отслеживание нажатия клавиш"""
          if event.key == pg.K_RIGHT:
                    self.ship.moving_right = True
          elif event.key == pg.K_LEFT:
                    self.ship.moving_left = True
          #нажатие клавиши q для выхода из игры  
          elif event.key == pg.K_q:
                    sys.exit()
          elif event.key == pg.K_SPACE and self.stats.game_active:
                    self._fire_bullet()
    
    def _check_keyup_events(self,event):
          """Отслеживание прекращения удержания клавиш"""
          if event.key == pg.K_RIGHT:
                    self.ship.moving_right=False
          elif event.key == pg.K_LEFT:
                    self.ship.moving_left = False
    def update_lifetimes(self):
        for exp in self.exps:
            exp.update_lifetime()
    def delete_exps(self):
        for exp in self.exps:
            if exp.lifetime == 0:
                self.exps.remove(exp)
    def update_frames_exps(self):
        for exp in self.exps:    
            exp.update_frame()
    def update_count_frames(self):
        for exp in self.exps:
            exp.update_count_frame()
    def update_indences(self):
        for exp in self.exps:
            exp.update_i()
  
    def _fire_bullet(self):
          if len(self.bullets) < self.settings.bullets_allowed:
                    firesound = pg.mixer.Sound("sounds/fire.mp3")
                    firesound.set_volume(0.5)
                    firesound.play(0)
                    new_bullet = Bullet(self)
                    self.bullets.add(new_bullet)
   


if __name__ == '__main__':
    """Запуск игры"""
    ai = AlienInvasion()
    ai.run_game()