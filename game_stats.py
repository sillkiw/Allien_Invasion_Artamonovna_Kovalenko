class GameStats():
    """Отслеживание статистики игры"""

    def __init__(self, ai_game):
        """Инициализация статистики"""
        self.settings = ai_game.settings
        self.reset_stats()

        #запуск игры в неактивном состоянии
        self.game_active = False
      

        #хранение рекорда
        self.high_score = 0

        

    def reset_stats(self):
        """Инициализация статистики, изменяющейся в ходе игры"""
        self.ships_left = self.settings.ship_limit

        #начальное число очков(сбрасывается при начале игры)
        self.score = 0

        #текущий уровень
        self.level = 1