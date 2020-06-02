def missingValue(a, b):
    result_list = []

    for element in b:
        if element not in a:
            result_list.append(element)

    result_list.sort()
    return result_list


print(missingValue([11, 4, 11, 7, 13, 4, 12, 11, 10, 14], [1, 4, 11, 7, 3, 7, 10, 13, 4, 8, 12, 11, 10, 14, 12]))
