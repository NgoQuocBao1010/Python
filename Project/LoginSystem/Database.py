def addpassword(username, pass1):
    fle = open('passwordfile.txt', mode = 'a+')
    fle.write(username)
    fle.write(' ')
    fle.write(pass1)
    fle.write('\n')
    fle.close()


def check_password(pass1):
    if len(pass1) < 6:
        return False

    nums = '0123456789'
    special_symbols = '!@#$%^&*'

    index = 0

    while index < len(pass1):
        if pass1[index] in nums:
            break
        if index == len(pass1) - 1:
            return False
        index += 1

    index = 0
    while index < len(pass1):
        if 'a' <= pass1[index] <= 'z':
            break
        if index == len(pass1) - 1:
            return False
        index += 1

    index = 0
    while index < len(pass1):
        if 'A' <= pass1[index] <= 'Z':
            break
        if index == len(pass1) - 1:
            return False
        index += 1

    index = 0
    while index < len(pass1):
        if pass1[index] in special_symbols:
            break
        if index == len(pass1) - 1:
            return False
        index += 1

    return True


def check_username(username):
    if len(username) < 4:
        return False

    index = 0
    while index < len(username):
        if 'a' <= username[index] <= 'z':
            break
        if index == len(username) - 1:
            return False
        index += 1

    return True


def convert_to_list(file):
    fle = open(file)
    data = fle.read()
    fle.close()

    list_from_data = data.split('\n')
    list_of_users = []
    for user in list_from_data:
        if user != '':
            dt = user.split(' ')
            list_of_users.append(dt)

    return dict(list_of_users)


def check_username_exist(username):
    list_of_user = convert_to_list('passwordfile.txt')
    value = list_of_user.get(username)

    if value == None:
        return False
    else:
        return True


def check_pass_exist(username, password):
    list_of_user = convert_to_list('passwordfile.txt')

    if not check_username_exist(username):
        return False
    else:
        value = list_of_user.get(username)
        if value == password:
            return True
        else:
            return False


def login():
    username = input('\nEnter your username: ')
    trying_time = 1
    list_of_user = convert_to_list('passwordfile.txt')

    if check_username_exist(username):
        password = input('Enter your password (You have 3 times to enter): ')

        if list_of_user[username] == password:
            print('\nLogin Succesfully')

        while list_of_user[username] != password and trying_time < 3:
            trying_time += 1
            password = input('\nIncorrect Password!!\nPlease enter again: ')
            if list_of_user[username] == password:
                print('\nLogin Succesfully')

    else:
        print('**Username does not exist**')


def create_new_account():
    print('\n====\t\tCreate New Account\t\t====\n')
    print('Instruction:')
    print('\t1. Your username and password should be at least 6 letters long.')
    print('\t2. Your password has to contain number, uppercase letters, lowercase letters and special symbols.')
    username = input('\nEnter new username: ')

    while check_username_exist(username):
        print('\nUsername is existed')
        username = input('\nEnter username again: ')

    while not check_username(username):
        print('Invalid username')
        username = input('\nEnter new username: ')

    password = input('\nEnter new password: ')

    while not check_password(password):
        print('Invalid password')
        password = input('\nEnter new password: ')

    addpassword(username, password)
    print('\nCreate Account Successfull')



#print(check_password('quocBao101$'))