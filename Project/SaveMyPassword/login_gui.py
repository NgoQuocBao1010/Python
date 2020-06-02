import tkinter as tk
from tkinter import messagebox
import LoginSystem


def add_an_account():
	global submit_button, Username_entry, Password_entry

	usn = Username_entry.get()
	paw = Password_entry.get()

	if LoginSystem.add_an_account(usn, paw):
		messagebox.showinfo('Congratulation!', 'Adding Sucessfully!!')
		root.destroy()
	else:
		messagebox.showerror('Error' ,'Invalid account name or Password')
		Username_entry.delete(0, tk.END)
		Password_entry.delete(0, tk.END)


h = 250
w = 400
root = tk.Tk(className=' Create an Account'.upper())

canvas = tk.Canvas(root, height=h, width=w, bg='white')
canvas.pack()

Username_l = tk.Label(canvas, text='Username', font=("Comic Sans MS", 10, 'bold'), fg='#D917BE', bg='#17D9C6')
Username_l.place(relx=0.05, rely=0.15, relwidth=0.15, relheight=0.1)

Password_l = tk.Label(canvas, text='Password', font=("Comic Sans MS", 10, 'bold'), fg='#D917BE', bg='#17D9C6')
Password_l.place(relx=0.05, rely=0.45, relwidth=0.15, relheight=0.1)

Username_entry = tk.Entry(canvas, font=("Courier", 13, 'bold'), fg='black', bg='white')
Username_entry.place(relx=0.25, rely=0.15, relwidth=0.7, relheight=0.1)

Password_entry = tk.Entry(canvas, font=("Courier", 13, 'bold'), fg='black', bg='white', show='*')
Password_entry.place(relx=0.25, rely=0.45, relwidth=0.7, relheight=0.1)

submit_button = tk.Button(canvas, text='Submit', font=("Comic Sans MS", 13, 'bold'), fg='gray', bg='yellow'
							, command= add_an_account)
submit_button.place(relx=0.4, rely=0.7, relwidth=0.25, relheight=0.1)
root.mainloop()