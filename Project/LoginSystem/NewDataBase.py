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


def login(username, password):
    list_of_users = convert_to_list('passwordfile.txt')

    if check_username_exist(username):
        if list_of_users[username] == password:
            return 0

        else:
            return 2
    else:
        return 1


def create_new_account(username, password):

    if check_username_exist(username):
        return 2

    elif not check_username(username):
        return 3

    elif not check_password(password):
        return 1
    else:
        addpassword(username, password)
        return 0



#print(check_password('quocBao101$'))