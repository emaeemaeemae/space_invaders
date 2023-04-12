import random

import pygame
import config

from typing import Optional
from display import WINDOW
from assets.assets import *
from ships import Ship, EnemyShip, PlayerShip


class Game:
    def __init__(self):
        self.run = True
        self.FPS = config.FPS
        self.window = WINDOW
        self.player_ship: Optional[PlayerShip] = None
        self.enemy_ships = []
        self.level = 1
        self.lives = config.LIVES
        self.font = pygame.font.SysFont('comicsans', config.FONT_SIZE)
        self.lost_font = pygame.font.SysFont('comicsans', config.FONT_SIZE * 3)
        self.lost = False

        self.init()

    def init(self):
        self.set_player_ship(PlayerShip())
        self.generate_enemies()

    def redraw_window(self):
        self.window.blit(BG, (0, 0))

        # draw labels
        lives_label = self.font.render(f'Lives: {self.lives}', True, WHITE)
        level_label = self.font.render(f'Level: {self.level}', True, WHITE)

        self.window.blit(lives_label, (10, 10))
        self.window.blit(level_label, (10, 10 + config.FONT_SIZE + 10))

        # draw ships
        self.draw_ships()

        if self.lost:
            lost_label = self.lost_font.render(f'You Lost!!!', True, WHITE)
            x = (config.WIDTH - lost_label.get_width()) // 2
            y = (config.HEIGHT - lost_label.get_height()) // 2
            self.window.blit(lost_label, (x, y))

        pygame.display.update()

    def draw_ships(self):
        self.player_ship.draw(self.window)

        for ship in self.enemy_ships:
            ship.draw(self.window)

    def add_enemy_ship(self, ship):
        self.enemy_ships.append(ship)

    def set_player_ship(self, ship):
        self.player_ship = ship

    def generate_enemies(self):
        # for _ in range(self.level + 5):
        #     self.add_enemy_ship(EnemyShip.generate_enemy())
        while len(self.enemy_ships) < self.level:
            self.add_enemy_ship(EnemyShip.generate_enemy())

    def next_level(self):
        self.level += 1
        self.generate_enemies()

    def check_next_level(self):
        if len(self.enemy_ships) == 0:
            self.next_level()

    def check_lives(self, enemy):
        if enemy.y + enemy.get_height() > config.HEIGHT:
            self.lives -= 1
            self.enemy_ships.remove(enemy)

    def tick(self):
        if self.lost:
            return
        for enemy in self.enemy_ships[:]:
            enemy.move(self.level)
            if not random.randint(0, 5 * config.FPS):
                enemy.shoot()
            enemy.move_lasers([self.player_ship])
            self.check_lives(enemy)

        self.player_ship.move_lasers(self.enemy_ships)

    def check_lost(self):
        if self.lives <= 0:
            self.lost = True
