import tkinter as tk
from NewDataBase import login
from createaccount import create_account
from tkinter import messagebox


def account_login(username, password):
    if login(username, password) == 1:
        messagebox.showerror('Error', 'Username does not exist')
        return

    elif login(username, password) == 0:
        root.destroy()
        import tttgui2
        return

    else:
        messagebox.showwarning('Warning', 'Wrong Password')



root = tk.Tk(className=' Login System')

canvas = tk.Canvas(root, height=500, width=600)
canvas.pack()

bg_image = tk.PhotoImage(file='tree.png')
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#0AD7EA', bd=5)
frame.place(relx=0.15, rely=0.2, relwidth=0.7, relheight=0.5)

label_usermane = tk.Label(frame, text='Username:', font=("Comic Sans MS", 15))
label_usermane.place(relx=0.075, rely=0.1, relheight=0.1, relwidth=0.3)

label_password = tk.Label(frame, text='Password', font=("Comic Sans MS", 15))
label_password.place(relx=0.075, rely=0.25, relheight=0.1, relwidth=0.3)

user_type_usermane = tk.Entry(frame, font=('gothic', 12))
user_type_usermane.place(relx=0.4, rely=0.1, relheight=0.1, relwidth=0.5)

user_type_password = tk.Entry(frame, font=('Comic Sans MS', 12), show='*')
user_type_password.place(relx=0.4, rely=0.25, relheight=0.1, relwidth=0.5)

summit = tk.Button(frame, bg='yellow', text='Login', font=('gothic', 12),
                   command=lambda: account_login(user_type_usermane.get(), user_type_password.get()))
summit.place(relx=0.4, rely=0.4, relheight=0.1, relwidth=0.3)


create = tk.Button(frame, bg='yellow', text='Create new account',
                   font=('gothic', 12), command=lambda: create_account())
create.place(relx=0.4, rely=0.55, relheight=0.1, relwidth=0.45)
root.mainloop()