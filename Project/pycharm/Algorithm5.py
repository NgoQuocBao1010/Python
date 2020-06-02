def countdigit(n):
    count = 0
    while n >= 1:
        n /= 10
        count = count + 1
    return count
def lastDigitDiffZero(n):
    fact = 1
    while countdigit(n) > 3:
        n =  n - 10 ** (countdigit(n) - 1)

    for number in range(1,n+1):
        fact *= number
        while fact % 10 == 0 :
            fact //= 10
    result = fact % 10
    return result

print(lastDigitDiffZero(1032))