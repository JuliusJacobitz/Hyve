import pygame
import math


class HiveMember:
    def __init__(self, screen, x, y, rot=0) -> None:
        self._screen = screen
        self.posX = x
        self.posY = y
        # Rotation: 0 Degrees means "down"
        self.rot = rot
        self.speed = 1.5
        self.path = []
        self.visibilityRange = 50

    @property
    def position(self):
        return (self.posX, self.posY)

    def move(self):
        self.path.append((self.posX, self.posY))

        deltaX = math.sin(math.radians(self.rot)) * self.speed
        deltaY = math.cos(math.radians(self.rot)) * self.speed
        self.posX += deltaX
        self.posY += deltaY

    def draw(self):
        bodyRadius = 10
        pygame.draw.circle(
            self._screen, (0, 0, 255), (self.posX, self.posY), bodyRadius
        )

        # head
        deltaX = math.sin(math.radians(self.rot)) * bodyRadius
        deltaY = math.cos(math.radians(self.rot)) * bodyRadius
        headPos = (self.posX + deltaX, self.posY + deltaY)
        pygame.draw.circle(self._screen, (255, 0, 0), headPos, bodyRadius / 2)

        # tail
        for index, point in enumerate(self.path[::-1]):
            if index <= 500:
                pygame.draw.circle(self._screen, (100, 100, 100), point, 1)
                # pygame.draw.line(surface, color, start_pos, end_pos, width)

        # visibility range
        pygame.draw.circle(
            self._screen, (216, 255, 20), self.position, self.visibilityRange, width=1
        )
