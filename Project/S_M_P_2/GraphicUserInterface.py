import tkinter as tk
from tkinter import StringVar
import Database
from Users import *
import subGUI
from tkinter import messagebox

global appHeight, appWidth
appHeight = 500
appWidth  = 800


def loginGUI():
	'''
		Login Screen
		What appears on the screen when the user open the app and login
	'''


	def submitFuction():
		'''
			Fuction of the submit button
			Login into the app
			Then change to the in app screen
		'''
		usn = usernameEntry.get()
		pwd = passEntry.get()

		check = Database.login(usn, pwd)

		if check:
			global user
			user = User(usn)
			root.destroy()
			inAppGUI()

		else:
			messagebox.showerror('Error', 'Incorrect username or password!\nPlease try again!')


	def signUpFuction():
		'''
			Fuction of the create account button
			Create new account for new users
		'''
		subGUI.signUpGUI()


	root = tk.Tk()

	canvas = tk.Canvas(root, height=appHeight, width=appWidth, bg='#19CC7A')
	canvas.pack()

	welcomeLabel = tk.Label(canvas, text='Welcome to SaveMyPass', font=("Comic Sans MS", 18, "bold"),
							fg="#6BCC19", bg="white")
	welcomeLabel.place(relx=0.3, rely=0.05, relwidth=0.4, relheight=0.1)

	usernameLabel = tk.Label(canvas, text='Username', font=("mincho", 15, 'bold'),
							fg="#196BCC", bg="white")
	usernameLabel.place(relx=0.2, rely=0.25, relwidth=0.12, relheight=0.075)

	passwLabel = tk.Label(canvas, text='Password', font=("mincho", 15, 'bold'),
							fg="#196BCC", bg="white")
	passwLabel.place(relx=0.2, rely=0.35, relwidth=0.12, relheight=0.075)

	usernameEntry = tk.Entry(canvas, font=("Gothic", 13), fg="#2019CC")
	usernameEntry.place(relx=0.35, rely=0.25, relwidth=0.45, relheight=0.075)

	passEntry = tk.Entry(canvas, font=("mincho", 13), fg="#2019CC", show='*')
	passEntry.place(relx=0.35, rely=0.35, relwidth=0.45, relheight=0.075)

	submitButton = tk.Button(canvas, text='Submit', bg='white', fg='#196BCC',
							font=('mincho', 15), command= submitFuction)
	submitButton.place(relx=0.44, rely=0.6, relwidth=0.12, relheight=0.1)

	createAccountButton = tk.Button(canvas, text='Sign Up', bg='white', fg='#196BCC',
							font=('mincho', 15), command= signUpFuction)
	createAccountButton.place(relx=0.44, rely=0.75, relwidth=0.12, relheight=0.1)

	root.mainloop()


def inAppGUI():
	'''
		What appear on the screen after the user sucessfully login
		save password, change password ...
	'''
	def createDropdownMenu():
		'''
			Create a dropdown menu base on account type that had been saved by users
		'''
		global clicked
		clicked = StringVar()
		clicked.set('email')

		dropDownAccType = tk.OptionMenu(root, clicked, *user.listOfAccountTypes())
		dropDownAccType.config(font=("mincho", 15, "bold"), bg='white', fg='#19C5CC')
		dropDownAccType.place(relx=0.3, rely=0.3, relwidth=0.15, relheight=0.075)


	def saveButtonFuction():
		'''
			Fuction to the save button
			Save password from user and reset dropdown menu
		'''
		root.destroy()
		subGUI.saveGUI(user)
		inAppGUI()
		

	def showButtonFuction(encrypt=False):
		'''
			Fuction to the show button
			Show both username and password for the user
			However the password will be show as a buch of "*" if encrypt is False
		'''
		def emptyAccount(strtext):
			'''
				Check whether there is any account in that account type
			'''
			num = '0123456789'

			for letter in strtext:
				if letter in num:
					return False
				if 'a' <= letter.lower() <= 'z':
					return False

			return True

		check = var.get()
		if check == 'on':
			encrypt = True

		text = user.nicelyDisplay(clicked.get())
		text2 = user.nicelyDisplay(clicked.get(), False)
		usnDisplay['text'] = text
		encodePass = ''

		if not emptyAccount(text):
			if not encrypt:
				for letter in text2:
					encodePass += '*'
				text2 = encodePass
		else:
			text = text2 = 'NO ACCOUNT ADDED'

		usnDisplay['text'] = text
		pwdDisplay['text'] = text2


	def deleteButtonFuction():
		'''
			Fuction to the delete button
			Delete unwanted account from user
		'''
		root.destroy()
		subGUI.deleteGUI(user)
		inAppGUI()


	def changeButtonFuction():
		'''
			Fuction to the change button
			Change the password of saved account
		'''
		root.destroy()
		subGUI.changeGUI(user)
		inAppGUI()


	###     =====Main GUI======     ###
	root = tk.Tk()
	canvas = tk.Canvas(root, height=appHeight, width=appWidth, bg='#19CC7A')
	canvas.pack()

	welcomeLabel = tk.Label(canvas, text='SaveMyPass', font=("Comic Sans MS", 18, "bold"),
							fg="#19CC21", bg="#196BCC")
	welcomeLabel.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.1)

	usnLabel = tk.Label(canvas, fg='white', text='Username', font=("mincho", 15),
						bg="#196BCC")	
	usnLabel.place(relx=0.05, rely=0.3, relwidth=0.12, relheight=0.075)

	pwdLabel = tk.Label(canvas, fg='white', text='Password', font=("mincho", 15),
						bg="#196BCC")	
	pwdLabel.place(relx=0.55, rely=0.3, relwidth=0.12, relheight=0.075)

	usnDisplay = tk.Label(canvas, bg='white', anchor='nw', justify='left', font=("Comic Sans MS", 15),
							fg='#2019CC')
	usnDisplay.place(relx=0.05, rely=0.4, relwidth=0.4, relheight=0.575)

	pwdDisplay = tk.Label(canvas, bg='white', anchor='nw', justify='left', font=("Comic Sans MS", 15),
							fg='#2019CC')
	pwdDisplay.place(relx=0.55, rely=0.4, relwidth=0.4, relheight=0.575)

	buttonTextColor = "white"
	buttonBGColor   = '#19C5CC'

	createDropdownMenu()

	savePassB1 = tk.Button(canvas, bg=buttonBGColor, text='Save', font=("mincho", 15),
						fg=buttonTextColor, command=saveButtonFuction)
	savePassB1.place(relx=0.05, rely=0.2, relwidth=0.14, relheight=0.075)

	showPassB2 = tk.Button(canvas, bg=buttonBGColor, text='Show', font=("mincho", 15),
						fg=buttonTextColor, command=showButtonFuction)
	showPassB2.place(relx=0.24, rely=0.2, relwidth=0.14, relheight=0.075)

	removeB3 = tk.Button(canvas, bg=buttonBGColor, text='Delete', font=("mincho", 15),
						fg=buttonTextColor, command=deleteButtonFuction)
	removeB3.place(relx=0.43, rely=0.2, relwidth=0.14, relheight=0.075)

	changeB4 = tk.Button(canvas, bg=buttonBGColor, text='Change', font=("mincho", 15),
						fg=buttonTextColor, command=changeButtonFuction)
	changeB4.place(relx=0.62, rely=0.2, relwidth=0.14, relheight=0.075)

	var = StringVar()
	encryptB5 = tk.Checkbutton(canvas, text='Encrypt', font=("mincho", 15, "bold"),
					 			bg='white', fg='#19C5CC', variable=var
					 			, onvalue='on', offvalue='off')
	encryptB5.deselect()
	encryptB5.place(relx=0.81, rely=0.3, relwidth=0.14, relheight=0.075)
	root.mainloop()


loginGUI()
