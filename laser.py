import pygame
import config
import utils


class Laser:

    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))

    def move(self, v):
        self.y += v

    def off_screen(self):
        return not (0 <= self.y <= config.HEIGHT)

    def collision(self, other):
        return utils.collide(self, other)