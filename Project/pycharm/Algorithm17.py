def legalcharacter(character):
    numbers = '0123456789'
    legal = True
    allowedcharacter = '? ,'
    if 'z' >= character.lower() >= 'a':
        legal = True
        return legal
    else:
        legal = False
    if character in numbers:
        legal = True
        return legal
    else:
        legal = False
    if character in allowedcharacter:
        legal = True
        return legal
    else:
        legal = False
    return legal

#print(legalcharacter('A'))

def questionCorrection(s):
    new_str = ''
    for character in s:
        if legalcharacter(character) and character != '?':
            new_str += character
        else:
            new_str += ' '
    s = new_str
    new_str = ''

    while s[0] == ' ' or s[0] == ',':
        new_str = s[1:]
        s = new_str
    new_str = ''

    while s[len(s) - 1] == ' ' or s[len(s) - 1] == ',':
        new_str = s[:-1] + '?'
        s = new_str
    new_str = ''

    for index in range(len(s)):
        if s[index] == ' ':
            if s[index + 1] == ' ' or s[index + 1] == ',' or s[index + 1] == '?':
                continue
        if s[index] == ',':
            if s[index + 1] == ',' or s[index + 1] == '?':
                continue
        new_str += s[index]
    s = new_str
    new_str = ''
    #return s

    if s[len(s) - 1] != '?':
        s += '?'
    if s.count(',') >= 1:
        for index in range(len(s)):
            if s[index] == ',':
                if s[index + 1] == ',' or s[index + 1] == '?':
                    continue
                if s[index + 1] != ' ':
                    new_str += s[index] + ' '
                    continue
            new_str += s[index]
        s = new_str


    return s.capitalize()

print(questionCorrection('      are ,you quoc trong,'))