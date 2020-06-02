import shelve
from LoginSystem import *

class user():
	user_accounts_path = {}
	default_setup = ['email', 'laptop', 'bankaccount']

	def __init__(self, name):
		self.name = name
		self.account_folder()

	def account_folder(self):
		import os

		for account in self.default_setup:
			path = 'D:\\Python\\Project\\SaveMyPassword\\Database\\{}\\{}\\{}'.format(self.name, account, account)
			if not os.path.exists(path):
				os.makedirs(path)
				sf = shelve.open(path)
				database = {}
				sf['data'] = database
				sf.close()
			self.user_accounts_path.setdefault(account, path)

	def add_account_type(self, account_type):
		if account_type in list(self.user_accounts_path.keys()):
			return

		self.default_setup.append(account_type)
		self.account_folder()
		return

	def add_content(self, account_type, username, password):
		if account_type not in list(self.user_accounts_path.keys()):
			self.add_account_type(account_type)

		sf = shelve.open(self.user_accounts_path.get(account_type))
		sf.setdefault('data')
		database = sf['data']
		if database is None:
			database = {}
		database.setdefault(username, password)
		sf['data'] = database
		sf.close()

		return True

	def show_content(self, account_type):
		if account_type not in list(self.user_accounts_path.keys()):
			return {}

		sf = shelve.open(self.user_accounts_path.get(account_type))
		data = sf.get('data')
		sf.close()

		return data

	def remove_content(self, account_type, username=None):
		if account_type not in list(self.user_accounts_path.keys()):
			return False

		sf = shelve.open(self.user_accounts_path.get(account_type))
		database = {}
		if username is not None:
			for element in list(sf['data'].items()):
				if element[0] != username:
					database.setdefault(element[0], element[1])
		sf['data'] = database
		sf.close()

		return True


def beauty_display(dic, encode=True):
	if len(list(dic.items())) == 0:
		return "You haven't add any account yet!!"

	breakdown_list = list(dic.items())
	result = ''

	for element in breakdown_list:
		element = list(element)
		if encode:
			element[1] = encode_password(element[1])
		formatted_text = "Account: {: <20} ------   Password: {}\n".format(element[0], element[1])
		result += formatted_text

	return result


def main():
	clarify_question = input("Do you have an account yet? ")

	if clarify_question.lower() == 'no':
		print('\n\t\tCREATE AN ACCOUNT')
		username = input("Enter your account name: ")
		pasword = input("\nEnter your password: ")

		while not add_an_account(username, pasword):
			username = input("Enter your account name: ")
			pasword = input("\nEnter your password: ")
		return

	else:
		username = input("Enter your account name: ")
		pasword = input("\nEnter your password: ")

		if not login(username, pasword):
			print("Wrong Password\n")
			return
		else:
			while True:
				us = user(username)
				us.account_folder()

				op = int(input("\nEnter your option: "))
				if op == 0:
					return
				elif op == 1:
					account_type = input('\nEnter your account type: ')
					print(beauty_display(us.show_content(account_type)))
				elif op == 2:
					account_type = input('\nEnter your account type: ')
					username1 = input("Enter your account name: ")
					pasword1 = input("\nEnter your password: ")
					us.add_content(account_type, username1, pasword1)

				elif op == 3:
					account_type = input('\nEnter your account type: ')
					r_username = input("Enter your account name: ")
					us.remove_content(account_type, r_username)