import random

import config
from assets.assets import *
from .ship import Ship


class EnemyShip(Ship):
    COLOR_MAP = {
        'red': (RED_SPACE_SHIP, RED_LASER),
        'blue': (BLUE_SPACE_SHIP, BLUE_LASER),
        'green': (GREEN_SPACE_SHIP, GREEN_LASER)
    }

    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.image, self.laser_image = self.COLOR_MAP[color]
        self.set_mask()

    @classmethod
    def generate_enemy(cls):
        x = random.randint(0, config.WIDTH - config.ENEMY_SHIP_WIDTH)
        y = random.randint(-4, -1) * config.ENEMY_SHIP_HEIGHT
        color = random.choice(['red', 'blue', 'green'])
        return cls(x, y, color)

    def move(self, v):
        self.y += v