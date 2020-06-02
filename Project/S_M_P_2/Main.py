import Database
import Users

def main():
    op = input("Do you have an account yet?:(Yes/No) ").lower()
    if op == 'no':
        usern = input('Enter your username: ')
        pswd = input('Enter your password: ')
        add = Database.addAnUser(usern, pswd)

        while not add:
            print("Your username have already been used. Please try another username: ")
            usern = input('Enter your username: ')
            add = Database.addAnUser(usern, pswd)

        print("Congratulation! Your account is created!")
    else:
        usern = input('Enter your username: ')
        pswd = input('Enter your password: ')
        login = Database.login(usern, pswd)

        while not login:
            print("Incorrect Username or Password! PLease try again")
            usern = input('Enter your username: ')
            pswd = input('Enter your password: ')
            login = Database.login(usern, pswd)
        print('Congratulation!! Login successfully!!')


main()