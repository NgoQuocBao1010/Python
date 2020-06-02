def listofcharater(s):
    lst = []

    for character in s:
        if character not in lst:
            lst.append(character)

    return lst


def charactersRearrangement(string1, string2):
    list_of_character1 = []
    list_of_character2 = []

    if len(string1) != len(string2):
        return False
    elif len(string1) == len(string2) == 1:
        if string1 != string2:
            return False
        return True
    else:
        list_of_character1 = listofcharater(string1)
        list_of_character2 = listofcharater(string2)

        for element in list_of_character1:
            if element not in list_of_character2:
                return False
            if string1.count(element) != string2.count(element):
                return False

    return True


print(charactersRearrangement("aaaabbc", "abbbbbc"))