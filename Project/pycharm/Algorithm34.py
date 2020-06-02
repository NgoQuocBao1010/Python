from math import sqrt


def calculatelength(x, y):
    return sqrt((x[0] - y[0]) * (x[0] - y[0]) + (x[1] - y[1]) * (x[1] - y[1]))


def findSquareSide(x, y):
    list_of_point = list(zip(x, y))

    x = calculatelength(list_of_point[0], list_of_point[1])
    y = calculatelength(list_of_point[0], list_of_point[2])

    if x > y:
        length_of_border = y
    else:
        length_of_border = x

    return int(length_of_border * length_of_border)


#print(calculatelength((1, 0), (0, 1)))
