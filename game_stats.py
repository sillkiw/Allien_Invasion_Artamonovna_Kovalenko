class GameStats():
    """Отслеживание статистики игры"""

    def __init__(self, ai_game):
        """Инициализация статистики"""
        self.settings = ai_game.settings
        self.reset_stats()

        #запуск игры в неактивном состоянии
        self.game_active = False
        
        #флаг для завершения игры после потери последнего корабля
        self.game_active = True

        

    def reset_stats(self):
        """Инициализация статистики, изменяющейся в ходе игры"""
        self.ships_left = self.settings.ship_limit