from typing import Tuple
import pygame
import math


class HiveMember:
    def __init__(self, screen, x, y, color: Tuple, rot=0) -> None:
        self._screen = screen
        self.posX = x
        self.posY = y
        # Rotation: 0 Degrees means "down"
        self.rot = rot
        self.speed = 2.5
        self.path = []
        self.visibilityRange = 50
        self.color = color

    @property
    def position(self):
        return (self.posX, self.posY)

    def move(self):
        self.path.append((self.posX, self.posY))

        deltaX = math.sin(math.radians(self.rot)) * self.speed
        deltaY = math.cos(math.radians(self.rot)) * self.speed

        new_x = self.posX + deltaX
        new_y = self.posY + deltaY

        # BLOCK AT WALLS
        # if new_x > self._screen.get_width():
        #     new_x -= abs(new_x - self._screen.get_width())
        # elif new_x < 0:
        #     new_x += abs(new_x)
        # if new_y > self._screen.get_height():
        #     new_y -= abs(new_y - self._screen.get_height())
        # elif new_y < 0:
        #     new_y += abs(new_y)

        # SNAKE STYLE
        if new_x > self._screen.get_width():
            new_x -= self._screen.get_width()
        elif new_x < 0:
            new_x += self._screen.get_width()

        if new_y > self._screen.get_height():
            new_y -= self._screen.get_height()
        elif new_y < 0:
            new_y += self._screen.get_height()

        self.posX = new_x
        self.posY = new_y

    def draw(self, draw_tail=False):
        bodyRadius = 10
        pygame.draw.circle(self._screen, self.color, (self.posX, self.posY), bodyRadius)

        # head
        deltaX = math.sin(math.radians(self.rot)) * bodyRadius
        deltaY = math.cos(math.radians(self.rot)) * bodyRadius
        headPos = (self.posX + deltaX, self.posY + deltaY)
        pygame.draw.circle(self._screen, (255, 0, 0), headPos, bodyRadius / 2)

        # tail
        if draw_tail:
            for index, point in enumerate(self.path[::-1]):
                if index <= 100:
                    pygame.draw.circle(self._screen, (240, 240, 240), point, 1)
                    # pygame.draw.line(surface, color, start_pos, end_pos, width)

        # visibility range
        pygame.draw.circle(
            self._screen, (216, 255, 20), self.position, self.visibilityRange, width=1
        )
