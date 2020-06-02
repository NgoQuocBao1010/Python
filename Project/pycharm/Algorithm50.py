def areSimilar(a, b):
    if len(a) != len(b):
        return False

    for element in a:
        if element not in b:
            return False

    length = len(a)
    different_spots = 0

    for index in range(length):
        if a[index] != b[index]:
            different_spots += 1

        if different_spots > 2:
            return False

    return True


print(areSimilar([1, 1, 4], [1,2,3]))

