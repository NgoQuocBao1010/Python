import tkinter as tk

lst = []

class my_button:
	def __init__(self, place, name, x, y, height, width, stt):
		self.name = name
		self.place = place
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.stt = stt

	def insert(self):
		self.name['text'] = 'X'
		self.name['font'] = ("Comic Sans MS", 25, 'bold')
		self.name['fg'] = 'blue'
		lst.append((self.stt))

	def create(self):
		self.name = tk.Button(self.place, bg='#D9C117', command=lambda : self.insert())
		self.name.place(relx=self.x, rely=self.y, relheight=self.height, relwidth=self.width)

	


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

	button0 = my_button(play_frame, '0', 0, 0, 0.2, 0.3, 0)
	button0.create()

	button1 = my_button(play_frame, '1', 0.35, 0, 0.2, 0.3, 1)
	button1.create()

	button2 = my_button(play_frame, '2', 0.7, 0, 0.2, 0.3, 2)
	button2.create()

	button3 = my_button(play_frame, '3', 0, 0.4, 0.2, 0.3, 3)
	button3.create()

	button4 = my_button(play_frame, '4', 0.35, 0.4, 0.2, 0.3, 4)
	button4.create()

	button5 = my_button(play_frame, '5', 0.7, 0.4, 0.2, 0.3, 5)
	button5.create()

	button6 = my_button(play_frame, '6', 0, 0.8, 0.2, 0.3, 6)
	button6.create()

	button7 = my_button(play_frame, '7', 0.35, 0.8, 0.2, 0.3, 7)
	button7.create()

	button8 = my_button(play_frame, '8', 0.7, 0.8, 0.2, 0.3, 8)
	button8.create()

	root.mainloop()

tic_tac_toe()

def check()
print(lst)
