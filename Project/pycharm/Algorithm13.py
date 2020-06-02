def formatString(input_string):
    new_str = ''
    word = ''
    for index in range(len(input_string)):
        if index != 0 and input_string[index - 1] == ' ' and input_string[index] != ' ':
            new_str += word + ' '
            word = ''
        if input_string[index] != ' ':
            word += input_string[index]
        if index == len(input_string) - 1:
            new_str += word
    new_str2 = new_str
    if new_str[0] == ' ':
        new_str2 = new_str[1:None]
    return new_str2


print(formatString('abc   a aa  a a'))



