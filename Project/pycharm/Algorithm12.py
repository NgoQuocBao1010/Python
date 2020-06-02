def checkPalindrome(inputString):
    last_index = len(inputString) - 1
    for index in range(last_index//2 + 1):
        if inputString[index] != inputString[last_index - index]:
            return False
    return True


print(checkPalindrome('abba'))