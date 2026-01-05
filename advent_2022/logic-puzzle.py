from collections import OrderedDict
from common import *


class Drone:
    def __init__(self, initial, velocity):
        """
        Make a drone.
        """
        self.initial = np.array(initial)
        self.velocity = np.array(velocity)

    def adjust_position(self, position):
        """
        Applies the modulus to a position and adjusts
        for the offset.
        """
        position = position % 20
        if position[0] == 0:
            position[0] = 20
        if position[1] == 0:
            position[1] = 20

        return position

    def position(self, day):
        """
        Calculates the position for a day number.
        """
        return self.adjust_position(self.initial + (day - 1)*self.velocity)

    def initial_position(self, day, position):
        """
        Determines the starting position if the position
        is given on a certain day.
        """
        position = np.array(position)
        return self.adjust_position(position - self.velocity*(day - 1))


def highest_common_factor(m, n):
    return max(set(factors(m)).intersection(set(factors(n))))


def drone_positions(which, day):
    """
    Returns a list of the horizontal (which = 0) or
    vertical (which = 1) positions of all drones on
    a particular day.
    """
    return [d.position(day)[which] for d in (red_drone, blue_drone, orange_drone)]


# Solution
red_drone = Drone((18, 13), (7, 1))
blue_drone = Drone((3, 9), (11, 15))
orange_drone = Drone((5, 4), (3, 8))

# Verify clues
# Clues
clues = OrderedDict()
clues[1] = red_drone.velocity[1] == 1
clues[2] = red_drone.velocity[0] in factors(840)
clues[3] = blue_drone.velocity[0] not in {3, 6, 9}
clues[4] = red_drone.position(2)[0] == 5
clues[5] = blue_drone.velocity[1] not in {3, 1, 5}
clues[6] = red_drone.velocity[0] not in factors(128)
clues[7] = blue_drone.velocity[1] not in {4, 7, 6}
clues[8] = blue_drone.velocity[1] in factors(840)
clues[9] = orange_drone.position(5)[1] != 6
clues[10] = len([x for x in drone_positions(1, 8) if x == 20]) == 2
clues[11] = red_drone.velocity[0] in {9, 8, 7}
clues[12] = orange_drone.velocity[0] in {1, 4, 3}
clues[13] = len([x for x in drone_positions(1, 6) if x == 4]) == 2
clues[14] = blue_drone.position(4)[1] == 14
clues[15] = blue_drone.velocity[1] % 2 != 0
clues[16] = orange_drone.velocity[0] in {3, 2, 4}
clues[17] = 4 in drone_positions(0, 14)
clues[18] = 7 in drone_positions(0, 15)
clues[19] = 8 in drone_positions(0, 16)
clues[20] = blue_drone.velocity[0] not in {4, 2, 5}
clues[21] = orange_drone.velocity[0] in {2, 3, 1}
clues[22] = blue_drone.velocity[0] not in factors(323)
clues[23] = blue_drone.velocity[0] % 5 in {1, 4}
clues[24] = highest_common_factor(blue_drone.velocity[0], 28) == 1

# Evaluate the clues
for clue, good in clues.items():
    print("Clue", str(clue) + ":", good)
print("All:", all(clues.values()))


day = 26
print()
print("Drone positions on Dec", str(day) + ":")
print("Red:", red_drone.position(day))
print("Blue:", blue_drone.position(day))
print("Orange:", orange_drone.position(day))
