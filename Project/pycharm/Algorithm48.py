def sortByHeight(a):

    for index in range(len(a)):
        if a[index] == -1:
            continue
        else:
            for index2 in range(index, len(a)):
                if a[index2] == -1:
                    continue
                else:
                    if a[index] > a[index2]:
                        temp = a[index]
                        a[index] = a[index2]
                        a[index2] = temp
    return a


print(sortByHeight([1, 5, -1, 9, 2]))