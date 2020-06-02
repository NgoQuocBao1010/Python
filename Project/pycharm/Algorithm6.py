from PhanTichRaThuaSoNguyenTo import isPrime
def time_all_list_Elements(lst):
    result = 1
    for value in lst:
        result *= value
    return result
def digitsProduct(product):
    x = product
    divisor_list = []
    result_digit_list = []
    if product >= 10 and isPrime(product):
        return -1
    elif 0 < product < 10:
        return product
    elif product == 0:
        return 10
    else:
        for number in range(2, product):
            if product % number == 0 and number < 10 :
                divisor_list.append(number)
        divisor_list.reverse()
        for value in divisor_list:
            while x % value == 0:
                result_digit_list.append(value)
                x /= value
        if time_all_list_Elements(result_digit_list) != product: return -1
        result_digit_list.reverse()
        result = ''
        for value in result_digit_list:
            result += str(value)

        return int(result)


    #return first_digit, second_digit

#print(digitsProduct(450))
for i in range(601):
    print(i,digitsProduct(i))

