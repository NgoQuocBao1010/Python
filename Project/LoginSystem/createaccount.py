import tkinter as tk
from tkinter import messagebox
import NewDataBase as nb


def add_account(username, password):
    if nb.create_new_account(username, password) == 2:
        messagebox.showerror('Error', 'Username is existed')
        return
    elif nb.create_new_account(username, password) == 3:
        messagebox.showerror('Error', 'Invalid Username')
        return
    elif nb.create_new_account(username, password) == 1:
        messagebox.showerror('Error', 'Invalid Password')
        return
    else:
        messagebox.showinfo('Information', 'Create Successfully')
        return


def create_account():
    root = tk.Tk(className='Create An Account')

    canvas = tk.Canvas(root, height=400, width=400, bg='#0AD7EA')
    canvas.pack()

    name_frame = tk.Frame(canvas, bg='#0AD7EA', bd=5)
    name_frame.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.15)

    label = tk.Label(name_frame, bg='white', fg='black',
                     text='Create An Account', font=("Comic Sans MS", "15"))
    label.place(relheight=1, relwidth=1)

    create_frame = tk.Frame(canvas, bg='#0AD7EA', bd=5)
    create_frame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.25)

    username_label = tk.Label(create_frame, bg='white', fg='black',
                                text='Username', font=("gothic", "10"))
    username_label.place(relx=0.05, rely=0.1, relwidth=0.3, relheight=0.25)

    pass_label = tk.Label(create_frame, bg='white', fg='black',
                                text='Password', font=("gothic", "10"))
    pass_label.place(relx=0.05, rely=1-0.1-0.25, relwidth=0.3, relheight=0.25)

    entry_username = tk.Entry(create_frame, bg='black', fg='#17D925',
                              font=("gothic", "12", 'bold'))
    entry_username.place(relx=0.4, rely=0.1, relwidth=0.5, relheight=0.25)

    entry_password = tk.Entry(create_frame, bg='black', fg='#17D925',
                              font=("gothic", "12", 'bold'), show='*')
    entry_password.place(relx=0.4, rely=1-0.1-0.25, relwidth=0.5, relheight=0.25)

    create = tk.Button(canvas, bg='#0AD7EA', fg='#D91755', text='Create',
                       font=("gothic", "9", 'bold'),
                       command=lambda: add_account(entry_username.get(), entry_password.get()))
    create.place(relx=0.72, rely=0.56, relwidth=0.18, relheight=0.055)


    root.mainloop()


#create_account()