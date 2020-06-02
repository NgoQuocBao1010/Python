def isArithmeticProgression(sequence):
    length = len(sequence)
    d = sequence[1] - sequence[0]

    for index in range(length - 1):
        d1 = sequence[index + 1] - sequence[index]
        if d1 != d:
            return False

    return True

print(isArithmeticProgression([1, 2, 100]))