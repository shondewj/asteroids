import pygame
from constants import *
from player import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    p1 = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    gameloop = True

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    while gameloop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0,0,0))

        p1.draw(screen)
        dt = clock.tick(60)/1000


        p1.update(dt)
        pygame.display.flip()


if __name__ == "__main__":
    main()
