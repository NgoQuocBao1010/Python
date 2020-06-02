def differentValuesInMultiplicationTable2(n, m):
    list_of_value = []

    for row in range(1, n + 1):
        for column in range(1, m + 1):
            value = row * column
            if value not in list_of_value:
                list_of_value.append(value)

    return len(list_of_value)

print(differentValuesInMultiplicationTable2(4, 4))