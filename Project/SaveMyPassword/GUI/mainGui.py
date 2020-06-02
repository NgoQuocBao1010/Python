import tkinter as tk
import sys
sys.path.append('..')
import LoginSystem, main
from main import user
from tkinter import messagebox


def submit():
	global submit_button, Username_entry, Password_entry, already_login, Instruction_label, content_label

	usn = Username_entry.get()
	paw = Password_entry.get()

	if not already_login:
		if LoginSystem.login(usn, paw):
			already_login = True
			Instruction_label['text'] = Instruction.get('login confirm')
			global subject
			subject = user(usn)
			add_account_button.destroy()	
		else:
			Instruction_label['text'] = Instruction.get('error')
			messagebox.showerror('Error', 'Wrong password or account name')

	else:
		type_of_actions = filter(lambda x: x == 'add content' or 
										   x == 'show content' or 
										   x == "remove content", list(Instruction.keys()))
		action = 'None'

		for element in type_of_actions:
			if Instruction.get(element) == Instruction_label['text']:
				action = element

		if action == "add content":
			acct = account_type.get().lower()

			if subject.add_content(acct, usn, paw):
				Instruction_label['text'] = Instruction.get('success')
			else:
				Instruction_label['text'] = Instruction.get('fail')

		elif action == "show content":
			acct = account_type.get().lower()	

			result = subject.show_content(acct)

			content_label['text'] = '  ' + main.beauty_display(result)

		elif action == "remove content":
			acct = account_type.get().lower()

			if subject.remove_content(acct, usn):
				Instruction_label['text'] = Instruction.get('success')
			else:
				Instruction_label['text'] = Instruction.get('fail')


	Username_entry.delete(0, tk.END)
	Password_entry.delete(0, tk.END)
	account_type.delete(0, tk.END)


def add_account():
	import login_gui


def add_content():
	if already_login:
		Instruction_label['text'] = Instruction.get('add content')


def show_content():
	if already_login:
		Instruction_label['text'] = Instruction.get('show content')


def remove_content():
	if already_login:
		Instruction_label['text'] = Instruction.get('remove content')



Instruction = {
		'login': 			"Enter your account name and Password",
		'error': 			"Error!! Please try again or create an account",
		'login confirm': 	"Login Sucessfully",
		'guide':			"Choose an action",
		'success':			"Sucessfully",
		'fail':				"Failed",
		'add content': 		"Enter your account_type, Username, and Password",
		'show content':		"Enter the kind of account you want to see",
		'remove content':	"Enter your all the info of that account"
	}


h = 500
w = 800

root = tk.Tk(className=' Save The Pass')

already_login = False

canvas = tk.Canvas(root, height=h, width=w, bg='white')
canvas.pack()

Instruction_label = tk.Label(canvas, bg='gray', text=Instruction.get('login'), 
							font=("Gothic", 13), fg='blue')
Instruction_label.place(relx=0.1, rely=0.0, relwidth=0.8, relheight=0.1)

Username_l = tk.Label(canvas, text='Username', font=("Comic Sans MS", 13, 'bold'), fg='#D917BE', bg='#17D9C6')
Username_l.place(relx=0.05, rely=0.15, relwidth=0.15, relheight=0.075)

Password_l = tk.Label(canvas, text='Password', font=("Comic Sans MS", 13, 'bold'), fg='#D917BE', bg='#17D9C6')
Password_l.place(relx=0.05, rely=0.25, relwidth=0.15, relheight=0.075)

Username_entry = tk.Entry(canvas, font=("Courier", 13, 'bold'), fg='black', bg='white')
Username_entry.place(relx=0.25, rely=0.15, relwidth=0.5, relheight=0.075)

Password_entry = tk.Entry(canvas, font=("Courier", 13, 'bold'), fg='black', bg='white', show='*')
Password_entry.place(relx=0.25, rely=0.25, relwidth=0.5, relheight=0.075)

submit_button = tk.Button(canvas, text='Submit', font=("Comic Sans MS", 13, 'bold'), fg='gray', bg='yellow',
							command= submit)
submit_button.place(relx=0.8, rely=0.15, relwidth=0.15, relheight=0.075)

add_account_button = tk.Button(canvas, text='Add Account', font=("Comic Sans MS", 13, 'bold'), fg='gray', bg='yellow',
							command= add_account)
add_account_button.place(relx=0.8, rely=0.25, relwidth=0.2, relheight=0.075)


frame = tk.Frame(canvas, bg='green', bd=20)
frame.place(relx=0.05, rely=0.4, relheight=0.55, relwidth=0.9)

content_label = tk.Label(canvas, bg='gray', font=("Comic Sans MS", 10, 'bold'))
content_label.place(relx=0.07, rely=0.5, relheight=0.41, relwidth=0.7)

account_type_l = tk.Label(frame, text='Account Type', font=("Courier", 10), bg='#33FFC6', fg='red')
account_type_l.place(relx=0.00, rely=0.00, relwidth=0.25, relheight=0.1)

account_type = tk.Entry(frame, font=("Courier", 13, 'bold'))
account_type.place(relx=0.3, rely=0.00, relwidth=0.5208, relheight=0.1)

add_password = tk.Button(frame, text='Add', font=("Courier", 15, 'bold'), fg='black', bg='red',
							command= add_content)
add_password.place(relx=0.85, rely=0.00, relwidth=0.15, relheight=0.15)

show_password = tk.Button(frame, text='Show', font=("Courier", 15, 'bold'), fg='black', bg='red',
							command= show_content)
show_password.place(relx=0.85, rely=0.2, relwidth=0.15, relheight=0.15)

remove_password = tk.Button(frame, text='Remove', font=("Courier", 15, 'bold'), fg='black', bg='red',
							command= remove_content)
remove_password.place(relx=0.85, rely=0.4, relwidth=0.15, relheight=0.15)



root.mainloop()

