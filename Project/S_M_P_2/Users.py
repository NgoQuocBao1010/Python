import os
import shelve
import Database
import shutil

usersDataPath = '.\\Users'

class User:
	userpath = ''
	accountTypes = []

	def __init__(self, username):
		'''
			Create a path for the user depend on username from Database
		'''
		self.username = username
		self.userpath = f"{usersDataPath}\\{username}"


	def listOfAccountTypes(self):
		'''
			Get a list of account types that have been saved
		'''
		return list(Database.accountTypesDatabase().get(self.username))


	def makeDirectory(self, acctype):
		'''
			Make new directory for new account type
		'''
		if acctype in self.listOfAccountTypes():
			return

		Database.addNewAccountType(self.username, acctype)

		os.mkdir(f"{self.userpath}\\{acctype}")

		sf = shelve.open(f"{self.userpath}\\{acctype}\\{acctype}")
		data = {}
		sf['data'] = data
		sf.close()
		return


	def viewAccountData(self, acctype):
		''' 
			View Data that had been saved to users
			If there is nothing return {}
			This fuction should be private
		'''

		if acctype not in self.listOfAccountTypes():
			return {}

		sf = shelve.open(f"{self.userpath}\\{acctype}\\{acctype}")
		data = sf['data']
		sf.close()
		return data


	def addPassword(self, username, password, acctype):
		'''
			Add Password that user want to save
		'''
		self.makeDirectory(acctype)

		dataPath = f"{self.userpath}\\{acctype}\\{acctype}"

		sf = shelve.open(dataPath)
		data = sf['data']
		data.setdefault(username, password)
		sf['data'] = data
		sf.close()


	def changePassword(self, username, password, acctype):
		'''
			Change password from saved account
		'''
		if acctype not in self.listOfAccountTypes():
			return False

		if username not in self.viewAccounts(acctype):
			return False

		dataPath = f"{self.userpath}\\{acctype}\\{acctype}"

		with shelve.open(dataPath) as sf:
			data = sf['data']
			data[username] = password
			sf['data'] = data

		return True
		

	def removeAccount(self, username, acctype):
		'''
			Remove account and account's password from database
		'''
		if acctype not in self.listOfAccountTypes():
			return

		dataPath = f"{self.userpath}\\{acctype}\\{acctype}"
		sf = shelve.open(dataPath)
		data = sf['data']
		if username in list(data.keys()):
			data.pop(username)
			sf['data'] = data

		sf.close()

		defaultAcc = ['email', 'phone', 'bank']

		if acctype not in defaultAcc and len(self.viewAccountData(acctype)) == 0:
			Database.deleteAccountType(self.username, acctype)
			shutil.rmtree(f"{self.userpath}\\{acctype}")


	def viewAccounts(self, acctype):
		'''
			View all account that has been added of that type
		'''
		return list(self.viewAccountData(acctype).keys())


	def nicelyDisplay(self, acctype, username=True):
		result = ''
		i = 1
		if username:
			for account in self.viewAccounts(acctype):
				result += str(i) + '. ' + account + '\n'
				i += 1

		else:
			for password in list(self.viewAccountData(acctype).values()):
				result += str(i) + '. ' + password + '\n'
				i += 1
		return result


def main():
	a = User('bao')
	#a.removeAccount('12345', '123')
	#print(a.viewAccountData('email'))
	#a.changePassword('tesfsadfat', '1234', 'emdsfsadfail')
	#print(a.viewAccountData('email'))
	#print(a.viewAccounts('email'))
	#print(a.listOfAccountTypes())
	#print(a.nicelyDisplay('email'))
	

#main()

