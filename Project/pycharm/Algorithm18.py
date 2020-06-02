def lineEncoding(s):
    new_str = ''
    list_of_char = []
    index = 0

    while index < len(s) :
        if index == len(s) - 1:
            new_str += s[index]
            list_of_char.append(new_str)
            new_str = ''
            break
        elif s[index] != s[index + 1]:
            new_str += s[index]
            list_of_char.append(new_str)
            new_str = ''
            index += 1
        elif index < len(s) - 1:
            new_str += s[index]
            index += 1

    for element in list_of_char:
        if len(element) == 1:
            new_str += element[0]
        else:
            new_str += str(len(element))
            new_str += element[0]

    return new_str


print(lineEncoding('abcd'))


