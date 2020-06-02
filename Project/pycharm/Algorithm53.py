from Algorithm52 import searchElement

def searchElement02(a, k):
    rows = len(a)
    columns = len(a[0])
    list_of_elements = []

    for row in range(rows):
        for column in range(columns):
            if a[row][column] not in list_of_elements:
                list_of_elements.append(a[row][column])

    return searchElement(list_of_elements, k)


print(searchElement02([[ 17,  53, 126, 208, 235],        [280, 324, 352, 413, 426],        [461, 549, 569, 632, 683],        [706, 731, 742, 807, 862],        [872, 890, 915, 918, 983]], 18))