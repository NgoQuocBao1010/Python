def isTandemRepeat(inputString):
    if len(inputString) % 2 != 0:
        return False
    else:
        first_str = ''
        second_str = ''
        for index in range(len(inputString)//2):
            first_str += inputString[index]
        for index in range(len(inputString)//2, len(inputString)):
            second_str += inputString[index]

        if first_str == second_str:
            return True
        else:
            return False


print(isTandemRepeat('1111'))