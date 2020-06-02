def makeArrayConsecutive(sequence):
    min_of_sequence = min(sequence)
    max_of_sequence = max(sequence)

    result = []
    for number in range(min_of_sequence + 1, max_of_sequence):
        if number not in sequence:
            result.append(number)

    return result


print(makeArrayConsecutive([5, 4, 6]))