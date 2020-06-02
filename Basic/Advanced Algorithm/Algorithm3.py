def calculate(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n == 3:
        return 2
    return (calculate(n - 1) * calculate(n - 2) + calculate(n - 3)) % (10 ** 9 + 7)


def fibLikeSq(n):
    function = [1, 1, 2]
    index = 3
    while index < n:
        next_element = (function[index - 1] * function[index - 2] + function[index - 3]) % (10 ** 9 + 7)
        function.append(next_element)
        index += 1
    return function[n - 1]



#print(calculate(100))
print(fibLikeSq(4))