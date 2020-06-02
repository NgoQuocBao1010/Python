def searchElement(a, n):
    a.sort()
    rank_list = []
    rank = 1

    for index in range(len(a)):
        if index == 0 or a[index] == a[index - 1]:
            rank_list.append(rank)
        else:
            rank += 1
            rank_list.append(rank)

    for index in range(len(rank_list)):
        if rank_list[index] == n:
            return a[index]

    return -1


#print(searchElement([1, 3, 8, 2, 4, 10, 5, 12], 4))
#print(searchElement([ 395, -472,  666, -927, -449], 3))
#print(searchElement([100, 100, 99, 98, 102, 103], 4))
#print(searchElement([1878619,  623915, 1088266, 1598839, 1867929,  690510, 1032037, 1923980, 1897839], 6))
#print(searchElement([]))