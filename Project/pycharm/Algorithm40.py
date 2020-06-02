def prefixsum(a):
    lenghthB = len(a)
    result = []
    for index in range(lenghthB):
        value = 0
        for num in range(index + 1):
            value += a[num]
        result.append(value)
    return result


print(prefixsum([1, 2, 3]))