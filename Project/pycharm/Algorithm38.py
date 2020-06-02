def isMonotonous(sequence):
    length = len(sequence)

    if length == 1:
        return True
    else:
        if sequence[0] < sequence[1]:
            for index in range(length - 1):
                if sequence[index] >= sequence[index + 1]:
                    return False
        elif sequence[0] > sequence[1]:
            for index in range(length - 1):
                if sequence[index] <= sequence[index + 1]:
                    return False
        else:
            return False

        return True


print(isMonotonous([5, 3, -2]))