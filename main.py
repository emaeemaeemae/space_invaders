import pygame

from game import Game


def main():
    game = Game()
    clock = pygame.time.Clock()
    while game.run:
        clock.tick(game.FPS)

        game.check_lost()
        game.check_next_level()

        game.tick()
        game.redraw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            game.run = False

        if game.lost:
            continue

        if keys[pygame.K_LEFT]:
            game.player_ship.move_left()
        if keys[pygame.K_RIGHT]:
            game.player_ship.move_right()
        if keys[pygame.K_UP]:
            game.player_ship.move_up()
        if keys[pygame.K_DOWN]:
            game.player_ship.move_down()
        if keys[pygame.K_SPACE]:
            game.player_ship.shoot()


if __name__ == '__main__':
    main()
