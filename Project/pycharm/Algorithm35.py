from math import sqrt
from Algorithm34 import calculatelength


def insideCircle(point, center, radius):
    distance_bet_point_center = calculatelength(point, center)

    if distance_bet_point_center > radius:
        return False
    else:
        return True


print(insideCircle([0, 0], [0, 0], 1))