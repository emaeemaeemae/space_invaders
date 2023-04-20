import typing as t

import pygame


def collide(object1, object2):
    offset_x = object2.x - object1.x
    offset_y = object2.y - object1.y
    return object1.mask.overlap(object2.mask, (offset_x, offset_y)) is not None


Timage = t.Optional[pygame.surface.Surface]
Tcolor = t.Literal['red', 'green', 'blue']
