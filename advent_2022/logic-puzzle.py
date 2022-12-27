from dataclasses import dataclass
import numpy as np
from common import *


class Drone:
    def __init__(self, initial, velocity):
        """
        Make a drone.
        """
        self.initial = np.array(initial)
        self.velocity = np.array(velocity)

    def position(self, day):
        """
        Calculates the position for a day number.
        """
        p = self.initial + (day - 1)*self.velocity
        p = p % 20

        if p[0] == 0:
            p[0] = 20
        if p[1] == 0:
            p[1] = 20

        return p


d = Drone((1, 12), (5, 7))

for day in range(1, 6+1):
    print(d.position(day))
