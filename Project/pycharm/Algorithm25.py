def isPangram(sentence):
    string = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
    list_of_letters = string.split(' ')

    for letter in list_of_letters:
        if letter not in sentence.lower():
            return False
    return True


print(isPangram('The quick brown fox jumps over the lazy dog.'))