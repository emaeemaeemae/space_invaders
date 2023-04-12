import config
import utils

from .ship import Ship
from assets.assets import *


class PlayerShip(Ship):
    def __init__(self, x=0, y=0, health=100):
        super().__init__(x, y, health)
        self.image = YELLOW_SPACE_SHIP
        self.laser_image = YELLOW_LASER
        self.set_mask()

        self.x = (config.WIDTH - self.get_width()) // 2
        self.y = config.HEIGHT - self.get_height() - 50

    def move_left(self):
        self.x -= config.VELOCITY
        if self.x < 0 - self.get_width():
            self.x = config.WIDTH

    def move_right(self):
        self.x += config.VELOCITY
        if self.x > config.WIDTH:
            self.x = 0 - self.get_width()

    def move_up(self):
        self.y = max(self.y - config.VELOCITY,
                     config.HEIGHT // 2)

    def move_down(self):
        self.y = min(self.y + config.VELOCITY,
                     config.HEIGHT - self.get_height() - 25)

