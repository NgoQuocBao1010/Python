import tkinter as tk
from tkinter import messagebox
import Database
from Users import *


def signUpGUI():
	'''
		Create a GUI for user to make new account
	'''

	def submitSUFunction():
		'''
			Fuction of the submit button in sign up GUI
		'''
		usn = Username_entry.get()
		pwd = Password_entry.get()

		import Database
		check = Database.addAnUser(usn, pwd)

		if check:
			messagebox.showinfo('Information', 'Sucessfully!')
			root.destroy()
		else:
			root.destroy()
			messagebox.showinfo('Error', 'Please try to use other username or password')
	


	h = 250
	w = 400
	root = tk.Tk(className=' Create an Account'.upper())

	canvas = tk.Canvas(root, height=h, width=w, bg='#19CC7A')
	canvas.pack()

	Username_l = tk.Label(canvas, text='Username', font=("Comic Sans MS", 10, 'bold'), fg='#196BCC', bg='white')
	Username_l.place(relx=0.05, rely=0.15, relwidth=0.15, relheight=0.1)

	Password_l = tk.Label(canvas, text='Password', font=("Comic Sans MS", 10, 'bold'), fg='#196BCC', bg='white')
	Password_l.place(relx=0.05, rely=0.45, relwidth=0.15, relheight=0.1)

	Username_entry = tk.Entry(canvas, font=("Courier", 13, 'bold'), fg='black', bg='white')
	Username_entry.place(relx=0.25, rely=0.15, relwidth=0.7, relheight=0.1)

	Password_entry = tk.Entry(canvas, font=("Courier", 13, 'bold'), fg='black', bg='white', show='*')
	Password_entry.place(relx=0.25, rely=0.45, relwidth=0.7, relheight=0.1)

	submit_button = tk.Button(canvas, text='Submit', font=("Comic Sans MS", 13, 'bold'), bg='white', fg='#196BCC'
								, command= submitSUFunction)
	submit_button.place(relx=0.4, rely=0.7, relwidth=0.25, relheight=0.1)
	root.mainloop()


def saveGUI(user):
	'''
		Create another window to save passeord
	'''
	h = 400
	w = 500
	root1 = tk.Tk(className='Save Password')

	def submitSUFunction():
		'''
			Save password to binary file
		'''
		usn = Username_entry.get()
		pwd = Password_entry.get()
		acct = acctype_entry.get()

		user.addPassword(usn, pwd, acct)
		messagebox.showinfo('Information', 'Sucessfully Saved!')
		root1.destroy()

	canvas = tk.Canvas(root1, height=h, width=w, bg='#19CC7A')
	canvas.pack()

	instruction = "Please enter your username, password and the type of your account"

	instructionLabel = tk.Label(canvas, text=instruction, font=("mincho", 12, 'bold'), 
								fg="#19CC21", bg='white')
	instructionLabel.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.1)

	Username_l = tk.Label(canvas, text='Username', font=("Comic Sans MS", 10, 'bold'), fg='#196BCC', bg='white')
	Username_l.place(relx=0.05, rely=0.25, relwidth=0.15, relheight=0.1)

	Password_l = tk.Label(canvas, text='Password', font=("Comic Sans MS", 10, 'bold'), fg='#196BCC', bg='white')
	Password_l.place(relx=0.05, rely=0.45, relwidth=0.15, relheight=0.1)

	acctype_l = tk.Label(canvas, text='Type', font=("Comic Sans MS", 10, 'bold'), fg='#196BCC', bg='white')
	acctype_l.place(relx=0.05, rely=0.65, relwidth=0.15, relheight=0.1)

	Username_entry = tk.Entry(canvas, font=("Courier", 13, 'bold'), fg='black', bg='white')
	Username_entry.place(relx=0.25, rely=0.25, relwidth=0.7, relheight=0.1)

	Password_entry = tk.Entry(canvas, font=("Courier", 13, 'bold'), fg='black', bg='white', show='*')
	Password_entry.place(relx=0.25, rely=0.45, relwidth=0.7, relheight=0.1)

	acctype_entry = tk.Entry(canvas, font=("Courier", 13, 'bold'), fg='black', bg='white')
	acctype_entry.place(relx=0.25, rely=0.65, relwidth=0.7, relheight=0.1)

	submit_button = tk.Button(canvas, text='Submit', font=("Comic Sans MS", 13, 'bold'), bg='white', fg='#196BCC',
								command=submitSUFunction)
	submit_button.place(relx=0.4, rely=0.88, relwidth=0.25, relheight=0.1)
	root1.mainloop()


def deleteGUI(user):
	'''
		Create another window to delete saved password
	'''
	h = 400
	w = 500
	root1 = tk.Tk(className=' Delete Password')

	def submitSUFunction():
		'''
			Delete password from binary files
		'''
		usn = Username_entry.get()
		acct = acctype_entry.get()

		user.removeAccount(usn, acct)
		root1.destroy()

	canvas = tk.Canvas(root1, height=h, width=w, bg='#19CC7A')
	canvas.pack()

	instruction = "Please enter your username and the type of your account"

	instructionLabel = tk.Label(canvas, text=instruction, font=("mincho", 12, 'bold'), 
								fg="#19CC21", bg='white')
	instructionLabel.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.1)

	Username_l = tk.Label(canvas, text='Username', font=("Comic Sans MS", 10, 'bold'), fg='#196BCC', bg='white')
	Username_l.place(relx=0.05, rely=0.25, relwidth=0.15, relheight=0.1)

	acctype_l = tk.Label(canvas, text='Type', font=("Comic Sans MS", 10, 'bold'), fg='#196BCC', bg='white')
	acctype_l.place(relx=0.05, rely=0.4, relwidth=0.15, relheight=0.1)

	Username_entry = tk.Entry(canvas, font=("Courier", 13, 'bold'), fg='black', bg='white')
	Username_entry.place(relx=0.25, rely=0.25, relwidth=0.7, relheight=0.1)

	acctype_entry = tk.Entry(canvas, font=("Courier", 13, 'bold'), fg='black', bg='white')
	acctype_entry.place(relx=0.25, rely=0.4, relwidth=0.7, relheight=0.1)

	submit_button = tk.Button(canvas, text='Submit', font=("Comic Sans MS", 13, 'bold'), bg='white', fg='#196BCC',
								command=submitSUFunction)
	submit_button.place(relx=0.4, rely=0.65, relwidth=0.25, relheight=0.1)
	root1.mainloop()


def deleteGUI(user):
	'''
		Create another window to delete saved password
	'''
	h = 400
	w = 500
	root1 = tk.Tk(className=' Delete Password')

	def submitSUFunction():
		'''
			Delete password from binary files
		'''
		usn = Username_entry.get()
		acct = acctype_entry.get()

		user.removeAccount(usn, acct)
		root1.destroy()

	canvas = tk.Canvas(root1, height=h, width=w, bg='#19CC7A')
	canvas.pack()

	instruction = "Please enter your username and the type of your account"

	instructionLabel = tk.Label(canvas, text=instruction, font=("mincho", 12, 'bold'), 
								fg="#19CC21", bg='white')
	instructionLabel.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.1)

	Username_l = tk.Label(canvas, text='Username', font=("Comic Sans MS", 10, 'bold'), fg='#196BCC', bg='white')
	Username_l.place(relx=0.05, rely=0.25, relwidth=0.15, relheight=0.1)

	acctype_l = tk.Label(canvas, text='Type', font=("Comic Sans MS", 10, 'bold'), fg='#196BCC', bg='white')
	acctype_l.place(relx=0.05, rely=0.4, relwidth=0.15, relheight=0.1)

	Username_entry = tk.Entry(canvas, font=("Courier", 13, 'bold'), fg='black', bg='white')
	Username_entry.place(relx=0.25, rely=0.25, relwidth=0.7, relheight=0.1)

	acctype_entry = tk.Entry(canvas, font=("Courier", 13, 'bold'), fg='black', bg='white')
	acctype_entry.place(relx=0.25, rely=0.4, relwidth=0.7, relheight=0.1)

	submit_button = tk.Button(canvas, text='Submit', font=("Comic Sans MS", 13, 'bold'), bg='white', fg='#196BCC',
								command=submitSUFunction)
	submit_button.place(relx=0.4, rely=0.65, relwidth=0.25, relheight=0.1)
	root1.mainloop()


def changeGUI(user):
	'''
		Create another window to save passeord
	'''
	h = 400
	w = 500
	root1 = tk.Tk(className='Change Password')

	def submitSUFunction():
		'''
			Save password to binary file
		'''
		usn = Username_entry.get()
		pwd = Password_entry.get()
		acct = acctype_entry.get()

		check = user.changePassword(usn, pwd, acct)

		if check:
			messagebox.showinfo('Information', 'Sucessfully Changed!')
		else:
			messagebox.showerror('Error', 'Changed Failed')
		root1.destroy()

	canvas = tk.Canvas(root1, height=h, width=w, bg='#19CC7A')
	canvas.pack()

	instruction = "Please enter your username, password and the type of your account"

	instructionLabel = tk.Label(canvas, text=instruction, font=("mincho", 12, 'bold'), 
								fg="#19CC21", bg='white')
	instructionLabel.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.1)

	Username_l = tk.Label(canvas, text='Username', font=("Comic Sans MS", 10, 'bold'), fg='#196BCC', bg='white')
	Username_l.place(relx=0.05, rely=0.25, relwidth=0.15, relheight=0.1)

	Password_l = tk.Label(canvas, text='Password', font=("Comic Sans MS", 10, 'bold'), fg='#196BCC', bg='white')
	Password_l.place(relx=0.05, rely=0.45, relwidth=0.15, relheight=0.1)

	acctype_l = tk.Label(canvas, text='Type', font=("Comic Sans MS", 10, 'bold'), fg='#196BCC', bg='white')
	acctype_l.place(relx=0.05, rely=0.65, relwidth=0.15, relheight=0.1)

	Username_entry = tk.Entry(canvas, font=("Courier", 13, 'bold'), fg='black', bg='white')
	Username_entry.place(relx=0.25, rely=0.25, relwidth=0.7, relheight=0.1)

	Password_entry = tk.Entry(canvas, font=("Courier", 13, 'bold'), fg='black', bg='white', show='*')
	Password_entry.place(relx=0.25, rely=0.45, relwidth=0.7, relheight=0.1)

	acctype_entry = tk.Entry(canvas, font=("Courier", 13, 'bold'), fg='black', bg='white')
	acctype_entry.place(relx=0.25, rely=0.65, relwidth=0.7, relheight=0.1)

	submit_button = tk.Button(canvas, text='Submit', font=("Comic Sans MS", 13, 'bold'), bg='white', fg='#196BCC',
								command=submitSUFunction)
	submit_button.place(relx=0.4, rely=0.88, relwidth=0.25, relheight=0.1)
	root1.mainloop()


#signUpGUI()
us = User('bao')
#deleteGUI(us)
#saveGUI(us)
#print(us.viewAccounts('email'))
