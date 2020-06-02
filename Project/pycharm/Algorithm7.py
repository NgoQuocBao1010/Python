def countdigit(n):
    count = 0
    while n >= 1:
        n /= 10
        count = count + 1
    return count


def pagesNumbering(page):
    result = 0
    if 0 < page <= 9:
        result = page
        return result
    else:
        leftovers = (page - (10 ** (countdigit(page) - 1))) * countdigit(page) + countdigit(page)
        result += leftovers
        for number_of_digit in range(0, countdigit(page) - 1):
            result += 9 * (10 ** (number_of_digit) ) * (number_of_digit + 1)
        return result


print(pagesNumbering(1000))



