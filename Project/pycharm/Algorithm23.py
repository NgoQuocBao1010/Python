def differentSubstringsTrie(s):
    substring = ''
    list_of_substring = []

    for index in range(len(s)):
        substring = ''
        for index2 in range(len(s)):
            for get in range(index, index2 + 1):
                substring += s[get]
            if substring not in list_of_substring and substring != '':
                list_of_substring.append(substring)
            substring = ''

    return list_of_substring

print(differentSubstringsTrie('abac'))

