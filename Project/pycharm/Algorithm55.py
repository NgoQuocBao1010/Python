def beautifulArray(arr):
    if len(arr) == 0 or len(arr) == 1 or len(arr) == 2:
        return False
    elif len(arr) == 3:
        if arr[0] != arr[2]:
            return False
        else:
            return True
    else:
        first_sum = 0
        second_sum = 0
        for index in range(1, len(arr) - 1):
            for index2 in range(index):
                first_sum += arr[index2]
            for index3 in range(index + 1, len(arr)):
                second_sum += arr[index3]

            if first_sum == second_sum:
                return True
            first_sum = 0
            second_sum = 0

        return False


print(beautifulArray([1, 2, 3, 3]))
