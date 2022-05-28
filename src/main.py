import pygame
import random
from member import HiveMember
from hive import Hive

pygame.init()
screen_x = 1000
screen_y = 1000
screen = pygame.display.set_mode([screen_x, screen_y])

clock = pygame.time.Clock()
FPS = 30


if __name__ == "__main__":
    # Create hive:
    h1 = Hive(screen=screen)
    for i in range(60):
        h1.members.append(
            HiveMember(
                screen,
                random.randint(0, screen_x),
                random.randint(0, screen_y),
                random.randint(0, 359),
            )
        )

    # Run game:
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))
        h1.tickv2()
        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()
