def transform(a):
    if 0< a < 10:
        return a
    else:
        result = 0

        while a > 0:
            result += (a % 10)
            a //= 10
        return result

def digitalSumSort(a):

    for index in range(len(a) - 1):
        for index2 in range(index + 1, len(a)):
            if transform(a[index]) > transform(a[index2]):
                temp = a[index]
                a[index] = a[index2]
                a[index2] = temp
            elif transform(a[index]) == transform(a[index2]):
                if a[index] > a[index2]:
                    temp = a[index]
                    a[index] = a[index2]
                    a[index2] = temp

    return a


#print(transform(1020))
print(digitalSumSort([22, 13, 400, 404, 8, 701]))