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
    new_members = []
    for i in range(20):
        new_members.append(
            HiveMember(
                screen,
                random.randint(0, screen_x),
                random.randint(0, screen_y),
                (0, 149, 255),
                random.randint(0, 359),
            )
        )
    h1.members = new_members

    h2 = Hive(screen=screen)
    new_members = []
    for i in range(20):
        new_members.append(
            HiveMember(
                screen,
                random.randint(0, screen_x),
                random.randint(0, screen_y),
                (255, 149, 0),
                random.randint(0, 359),
            )
        )
    h2.members = new_members

    # Run game:
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((41, 41, 41))

        h1.tickv2()
        h2.tickv2()

        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()
