def goodword(s):
    checklist = []

    for letter in s:
        if 'a' <= letter <= 'z':
            if letter not in checklist:
                checklist.append(letter)
            else:
                return False
        else:
            return False

    return True


def differentWords(s):
    s = s.lower()
    split_word = []
    word = ''
    
    for index in range(len(s)):
        if 'a' <= s[index] <= 'z':
            word += s[index]
        else:
            if word in split_word:
                word = ''
            if word != '' and word not in split_word:
                split_word.append(word)
                word = ''

        if index == len(s) - 1:
            if word in split_word:
                word = ''
            if word != '' and word not in split_word:
                split_word.append(word)
                word = ''

    print(split_word)
    result = 0
    for word in split_word:
        if goodword(word):
            result += 1

    return result


print(differentWords("ABC aBC abc abc"))
