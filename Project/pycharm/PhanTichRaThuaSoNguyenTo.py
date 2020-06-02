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

def factorSum(n):
    prime_divisor = []
    for divisor in range(2, n+1):
        while n % divisor == 0:
            prime_divisor.append(divisor)
            n /= divisor
    sum = 0
    for value in prime_divisor:
        sum += value
    if sum == 4:
        return 4
    elif isPrime(sum):
        return sum
    else:
        return factorSum(sum)

for i in range(2, 201):
    print(i, factorSum(i))







