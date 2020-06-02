def differentSymbolsNaive(s):

    character_list = []

    for character in s:
        if character not in character_list:
            character_list.append(character)

    return character_list

print(differentSymbolsNaive('abcccdsgsfgdf'))