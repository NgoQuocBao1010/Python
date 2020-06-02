import os
import shelve

database_path = 'D:\\Python\\Project\\SaveMyPassword\\LoginSystem\\Admin'


def reset_database():
	sf = shelve.open(database_path)
	database = {'ngoquocbao1010': "mkcNHQB1010"}
	sf['data'] = database
	sf.close()


def existed_username(username):
	sf = shelve.open(database_path)
	usernames = list(sf['data'].keys())
	sf.close()
	return username in usernames


def correct_password(username, password):
	sf = shelve.open(database_path)
	right_password = sf['data'].get(username)
	sf.close()
	return password == right_password


def legal_password(password):
	if len(password) < 5:
		return False

	if not password.isalnum():
		return False

	return True


def add_an_account(username, password):
	if existed_username(username):
		return False

	if not legal_password(password):
		return False

	sf = shelve.open(database_path)
	database = sf['data']
	database.setdefault(username, password)
	sf['data'] = database
	sf.close()

	return True


# ========================= Encode ============================= #


def ceasar_encode(letter):
	return {'A': 'D',
			'B': 'E',
			'C': 'F',
			'D': 'G',
			'E': 'H',
			'F': 'I', 
			'G': 'J',
			'H': 'K',
			'I': 'L',
			'J': 'M',
			'K': 'N',
			'L': 'O',
			'M': 'P',
			'N': 'Q',
			'O': 'R',
			'P': 'S',
			'Q': 'T',
			'R': 'U',
			'S': 'V',
			'T': 'W',
			'U': 'X',
			'V': 'Y',
			'W': 'Z',
			'X': 'A',
			'Y': 'B',
			'Z': 'C'}.get(letter.upper(), letter)


def encode_password(password):
	new_password = ''
	for letter in password:
		new_password += ceasar_encode(letter)

	return new_password


def login(username, password):
	return existed_username(username) and correct_password(username, password)


#reset_database()
#print(add_an_account('test1010', 'test1010'))
#print(login('test1010', 'test1010'))



