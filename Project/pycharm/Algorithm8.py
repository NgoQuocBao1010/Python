def isPrime(n):
    if (n < 2):
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    for value in range(3, n, 2):
        if n % value == 0:
            return False
    return True


def primeSum(n):
    result = 0
    if n < 2:
        return 0
    else:
        for number in range(2, n + 1):
            if isPrime(number):
                result += number
        return result % 22082018


print(primeSum(10000))