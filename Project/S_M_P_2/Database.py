import os
import shelve
import shutil

# App login System #
databasePath = ".\\Database\\database"
dataFileNames = ['email', 'phone', 'bank']


def resetDatabase():
	''' 
		Erase all data in database and left only admin as a user
	'''
	sf = shelve.open(databasePath)
	admin = {'admin' : 'test123'}
	sf['data'] = admin
	sf['acct'] = {}
	sf.close()


def openDatabase():
	'''
		Get data from database
	'''
	data = {}

	sf = shelve.open(databasePath)
	data = sf['data']
	sf.close()

	return data


def accountTypesDatabase():
	'''
		Database for all account type that users have saved
	'''

	sf = shelve.open(databasePath)
	acct = sf['acct']
	sf.close()

	return acct


def addNewAccountType(username, newAcct):
	'''
		Add new account type to database for user
	'''
	sf = shelve.open(databasePath)
	acct = sf['acct']
	listAcct = acct[username]
	listAcct.append(newAcct)
	listAcct = list(set(listAcct))
	acct[username] = listAcct
	sf['acct'] = acct
	sf.close()


def viewUsers():
	'''
		Get to see all users that have access to the app
	'''
	data = openDatabase()
	return list(data.keys())


def existedUsername(username):
	''' 
		Check whether the username is being used or not
	'''
	return username in viewUsers()


def makeNewDirectories(username):
	'''
		Create directories and files to store users' data
		** Some default files will be create to store information
	'''
	accountType = accountTypesDatabase().get(username)
	dataUserPath = '.\\Users'
	data = {}

	userpath = f'{dataUserPath}\\{username}'
	os.mkdir(userpath)

	for name in accountType:
		os.mkdir(f"{userpath}\\{name}")
		sf = shelve.open(f"{userpath}\\{name}\\{name}")
		sf['data'] = data
		sf.close()


def addAnUser(username, password):
	'''
		Add an user to database and make directories for his/her data
		Condition: the username must be unique
	'''

	if existedUsername(username):
		return False

	sf = shelve.open(databasePath)
	data = sf['data']
	data.setdefault(username, password)
	sf['data'] = data

	acct = sf['acct']
	acct.setdefault(username, dataFileNames)
	sf['acct'] = acct
	sf.close()

	try:
		makeNewDirectories(username)
	except FileExistsError:
		return False

	return True


def deleteAccountType(username, acct):
	'''
		Delete account type that empty despite the default ones
	'''
	acctsList = list(accountTypesDatabase().get(username))

	if acct in dataFileNames:
		return

	if acct in acctsList:
		acctsList.remove(acct)
		with shelve.open(databasePath) as sf:
			acctL = sf['acct']
			acctL[username] = acctsList
			sf['acct'] = acctL


def deleteUser(username):
	'''
		completely remove an user from Database
	'''
	if not existedUsername(username):
		return

	sf = shelve.open(databasePath)
	data = sf['data']
	data.pop(username)
	sf['data'] = data

	acct = sf['acct']
	acct.pop(username)
	sf['acct'] = acct
	sf.close()

	usernamePath = f'.\\Users\\{username}'
	shutil.rmtree(usernamePath)


def login(username, password):
	'''
		Check for username and password to login and use the app
	'''
	if not existedUsername(username):
		return False

	data = openDatabase()
	return password == data.get(username)


def main():
	#resetDatabase()
	login('bao', '123')
	deleteAccountType('bao', 'test')
	print(accountTypesDatabase())
	return


print(viewUsers())
