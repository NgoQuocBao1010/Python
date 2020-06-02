import Database
answer = input('Welcome to my website!\nDo you have an account yet?: ')

if answer.lower() == 'yes':
    Database.login()
elif answer.lower() == 'no':
    Database.create_new_account()
    answer = input('\nDo you want to login? ')

    if answer.lower() == 'yes':
        Database.login()


