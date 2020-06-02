phone_number = input('Enter your phone number: ')

# first solution(This is stupid)
text_number = ''
for number in phone_number:
    if number == '1':
        text_number += 'One '
    elif number == '2':
        text_number += 'Two '
    elif number == '3':
        text_number += 'Three '
    elif number == '4':
        text_number += 'Four '
    elif number == '5':
        text_number += 'Five '
    elif number == '6':
        text_number += 'Six '
    elif number == '7':
        text_number += 'Seven '
    elif number == '8':
        text_number += 'Eight '
    elif number == '9':
        text_number += 'Nine '
    elif number == '0':
        text_number += 'Zero '
    else:
        print(' Invalid Input ')

print(text_number)
print('\n\n')

#Second Solution
dictionary_num_to_text ={
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four',
    '5': 'Five',
    '6': 'Six',
    '7': 'Seven',
    '8': 'Eight',
    '9': 'Nine',
    '0': 'Zero'
}
text_number = ''
for num in phone_number:
    text_number += dictionary_num_to_text.get(num, 'INVALID INPUT!!!!') + ' '

print(text_number)
