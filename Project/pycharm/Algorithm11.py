def amendTheSentence(s):
    new_str = ''
    word = ''
    for index_of_letter in range(len(s)):
        if index_of_letter != 0 and 'A' <= s[index_of_letter] <= 'Z':
            new_str += word.lower() + ' '
            word = ''
        word += s[index_of_letter]
        if index_of_letter == len(s) - 1:
            new_str += word.lower()
    return new_str

print(amendTheSentence('iEiMCyKAdsfGMPa'))
