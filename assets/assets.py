import os

from pygame.image import load
from pygame.transform import scale
from config import WIDTH, HEIGHT
# Enemy ships
RED_SPACE_SHIP = load(os.path.join('assets', 'ship_red_small.png'))
BLUE_SPACE_SHIP = load(os.path.join('assets', 'ship_blue_small.png'))
GREEN_SPACE_SHIP = load(os.path.join('assets', 'ship_green_small.png'))

# Player ship
YELLOW_SPACE_SHIP = load(os.path.join('assets', 'ship_yellow.png'))

# Lasers
RED_LASER = load(os.path.join('assets', 'laser_red.png'))
BLUE_LASER = load(os.path.join('assets', 'laser_blue.png'))
GREEN_LASER = load(os.path.join('assets', 'laser_green.png'))
YELLOW_LASER = load(os.path.join('assets', 'laser_yellow.png'))

# Background
BG = scale(load(os.path.join('assets', 'background-black.png')),
           (WIDTH, HEIGHT))

# COLORS
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
