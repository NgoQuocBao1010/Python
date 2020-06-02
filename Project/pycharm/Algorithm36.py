def isQuare(x, y):
    return x[0]*y[0] + x[1]*y[1] == 0


def createVector(x, y):
    vector = []
    vector.append(x[0] - y[0])
    vector.append(x[1] - y[1])
    return vector


def isRectangle(points):
    a = createVector(points[0], points[1])
    b = createVector(points[1], points[2])
    c = createVector(points[2], points[3])
    d = createVector(points[3], points[0])

    if not isQuare(a, b):
        return False

    if not isQuare(b, c):
        return False

    if not isQuare(c, d):
        return False

    if not isQuare(d, a):
        return False

    return True
#print(createVector((1, 2), (2, 3)))
print(isRectangle([[0,0],   [1,1],   [0,2],   [-1,1]]))


