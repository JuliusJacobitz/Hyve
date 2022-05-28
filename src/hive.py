import random
from types import MemberDescriptorType
from member import HiveMember
from typing import List
import numpy as np


class Hive:
    def __init__(self, screen, members: List[HiveMember] = []) -> None:
        self._screen = screen
        self.members = members

    def findNeighbours(self, member: HiveMember):
        res = []
        for neighbour in self.members:
            if neighbour == member:
                continue

            # Check if in visibility range
            distance = np.linalg.norm(
                np.array(neighbour.position) - np.array(member.position)
            )
            if distance <= member.visibilityRange:
                res.append(neighbour)

        return res

    def tick(self):
        for member in self.members:
            # randomly change direction
            delta_rot = random.randint(-90, 90)
            member.rot += delta_rot

            # move
            member.move()
            # draw
            member.draw()

    def tickv2(self):
        """
        1. Each member is assigned a random rotation
        2. Then for each member it is checked, if neighbours are in range
        3. If so, set the rotation to the mean of the n rotations and override the neighbours too.
        4. Move and draw
        """
        # 1.
        for member in self.members:
            member.rot += random.randint(-10, 10)

        # 2.
        for member in self.members:
            neighbours = self.findNeighbours(member)

            # 3.
            if neighbours:
                mean_rot = np.mean(np.array([member.rot] + [i.rot for i in neighbours]))
                mean_rot = mean_rot % 359

                # set rotation
                member.rot = mean_rot
                for neighbour in neighbours:
                    neighbour.rot = mean_rot

        # 4.
        for member in self.members:
            # move
            member.move()
            # draw
            member.draw()

    # def _draw(self):
    #     for member in self.members:
    #         member.draw()0

    # def _move(self):
    #     for member in self.members:
    #         member.move()
