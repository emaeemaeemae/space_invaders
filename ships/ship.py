from __future__ import annotations

import pygame

import config
import utils

from laser import Laser
from assets.assets import GREEN, RED


class Ship:
    def __init__(self, x: int, y: int, health: int = 100):
        self.x = x
        self.y = y
        self.health = health
        self.max_health = health
        self.image = None
        self.laser_image = None
        self.mask = None
        self.lasers = []
        self.cool_down_counter = 0

    def set_mask(self):
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self, window):
        for laser in self.lasers:
            laser.draw(window)
        window.blit(self.image, (self.x, self.y))

        green_width = (self.health / self.max_health) * self.get_width()
        red_width = self.get_width() - green_width
        hp_line_y = self.y + self.get_height() + 10

        pygame.draw.rect(window, GREEN,
                         (self.x, hp_line_y,
                          green_width, 7))
        pygame.draw.rect(window, RED,
                         (self.x + green_width, hp_line_y,
                          red_width, 7))

    def cooldown(self):
        if self.cool_down_counter >= config.SHIP_SHOOT_COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x, self.y, self.laser_image)
            self.lasers.append(laser)
            self.cool_down_counter = 1

    def get_width(self):
        return self.image.get_width()

    def get_height(self):
        return self.image.get_height()

    def move_lasers(self, enemies: list[Ship]):
        is_player = 1 if self.__class__.__name__ == 'PlayerShip' else -1
        self.cooldown()
        for laser in self.lasers[:]:
            laser.move(-config.PLAYER_LASER_SPEED * is_player)
            if laser.off_screen():
                self.lasers.remove(laser)
            else:
                for enemy in enemies[:]:
                    if utils.collide(laser, enemy):
                        enemy.health -= 50
                        if enemy.health <= 0:
                            if is_player == 1:
                                enemies.remove(enemy)
                            else:
                                enemies[0].health = 0
                        self.lasers.remove(laser)
