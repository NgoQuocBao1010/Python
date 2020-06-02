def truncateString(s):
    new_str = s
    first_index = 0

    while int(s[len(s) - 1]) % 3 == 0 and len(s) > 1 and s[len(s) - 1] != '0':
        new_str = str(int(s) // 10)
        s = new_str

    while int(s[0]) % 3 == 0 and len(s) > 1:
        new_str = s[1:]
        s = new_str

    while (int(s[0]) + int(s[len(s) - 1])) % 3 == 0 and len(s) > 2:
        new_str = s[1:-1]
        s = new_str

    if len(s) == 1 :
        if int(s[0]) % 3 == 0 :
            new_str = ""
            return new_str
        else:
            return s
    elif len(s) == 2 and (int(s[0]) + int(s[1])) % 3 == 0:
        new_str = ''
        return new_str

    if len(new_str) == 0:
        return new_str
    else:
        if int(s[len(s) - 1]) % 3 == 0 and int(s[len(s) - 1]) != 0:
            return truncateString(s)
        elif int(s[0]) % 3 == 0 or (int(s[0]) + int(s[len(s) - 1])) % 3 == 0:
            return truncateString(s)
    return new_str


print(truncateString('90909'))