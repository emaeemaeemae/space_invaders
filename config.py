import os

from dotenv import load_dotenv

load_dotenv()

WIDTH = 800
HEIGHT = 800
FPS = 60
LIVES = int(os.getenv('LIVES'))
FONT_SIZE = 30
ENEMY_SHIP_WIDTH = 50
ENEMY_SHIP_HEIGHT = 50
VELOCITY = 5
SHIP_SHOOT_COOLDOWN = 30
PLAYER_LASER_SPEED = 5
