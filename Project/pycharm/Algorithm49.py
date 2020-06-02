def sortByLength(inputArray):
    result = []
    len_array = len(inputArray)
    max_len_of_ele = -1

    for element in inputArray:
        if len(element) > max_len_of_ele:
            max_len_of_ele = len(element)

    for length in range(max_len_of_ele + 1):
        for element in inputArray:
            if len(element) == length:
                result.append(element)

    return result


print(sortByLength(["abc", "", "aaa", "a", "zz"]))
