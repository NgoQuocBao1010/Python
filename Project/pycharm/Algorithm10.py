def checkStrongPassword(password):
    numbers = '1234567890'
    specialsymbols = '!@#$%^&*()-+'
    if len(password) < 6:
        return False
    else:
        for number in numbers:
            if number in password:
                break
            if number == '0':
                return False

        for letter in password:
            if 'a' <= letter <= 'z':
               break
            if letter == 'z':
                return False

        for letter in password:
            countime = 0
            countime += 1
            if 'A' <= letter <= 'Z':
               break
            if letter == 'Z':
                return False

        for symbol in specialsymbols:
            if symbol in password:
                return True
            if symbol == '+':
                return False

print(checkStrongPassword('AAAAaaaa'))







