def numberZeroDigits(n):
    result = 0
    if n < 5:
        return 0
    else:
        i = 1
        while 5 ** i <= n:
            result += n//(5 ** i)
            i += 1
        return result


print(numberZeroDigits(100))