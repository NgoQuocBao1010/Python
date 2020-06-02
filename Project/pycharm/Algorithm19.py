def commonCharacterCount(s1, s2):
    count_ele = 0
    result = 0
    character_list_s1 = []

    for character in s1:
        if character not in character_list_s1:
            character_list_s1.append(character)

    for element in character_list_s1:
        if s1.count(element) != 0 and s2.count(element) != 0:
            if s1.count(element) <= s2.count(element):
                count_ele += s1.count(element)
            else:
                count_ele += s2.count(element)

    return count_ele


print(commonCharacterCount("abca", "xyzbac"))
