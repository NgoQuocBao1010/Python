import tkinter as tk
from tkinter import Button

class my_button(Button):
	active = False
	def __init__(self, master, command):
		super(my_button, self).__init__(master, command)
	def donothing(self):
		return 
	def change_text(self):
		self['text'] = 'bao'
		active = True
	def print_text(self):
		if my_button.active:
			return self['text'] 


def tic_tac_toe():
	root = tk.Tk(className=' Tic Tac Toe')

	canvas = tk.Canvas(root, height=500, width=500)
	canvas.pack()

	bg_image = tk.PhotoImage(file='Chelsea.png')
	bg_label = tk.Label(root, image=bg_image)
	bg_label.place(relwidth=1, relheight=1)

	frame = tk.Frame(root, bg='black', bd = 5)
	frame.place(relx=0.2, rely=0.05, relheight=0.15, relwidth=0.6)

	ttt_label = tk.Label(frame, text='Tic Tac Toe', font=("Comic Sans MS", 25, 'bold'), fg='#D917BE', bg='#17D9C6')
	ttt_label.place(relwidth=1, relheight=1)

	play_frame = tk.Frame(root, bg='white', bd=5)
	play_frame.place(relx=0.05, rely=0.25, relwidth=0.9, relheight=0.7)

	bt1 = my_button(play_frame, command=lambda: self.change_text())
	bt1.place(relx=0.7, rely=0, relheight=0.2, relwidth=0.3)
	print(bt1.print_text())
	root.mainloop()

tic_tac_toe()