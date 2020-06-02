import tkinter as tk
from tkinter import messagebox
import time as ti
space = 9

lst = ['-' for x in range(9)]

def is_won_comp(bd):
	winner_brackets = [[1, 2, 3], [4, 5, 6], [7, 8, 9],
					  [1, 4, 7], [2, 5, 8], [3, 6, 9],
					  [1, 5, 9], [3, 5, 7]]

	for bk in winner_brackets:
		if bd[bk[0]-1] != '-':
			if bd[bk[0] - 1] == bd[bk[1] - 1] and bd[bk[0] - 1] == bd[bk[2] - 1]:
				return True
	return False


def make_move(num):
	global space
	if num == 0:
		b0['text'] = 'O'
		b0['font'] = ("Comic Sans MS", 25, 'bold')
		b0['fg']   = 'green'
		space -= 1
	elif num == 1:
		b1['text'] = 'O'
		b1['font'] = ("Comic Sans MS", 25, 'bold')
		b1['fg']   = 'green'
		space -= 1
	elif num == 2:
		b2['text'] = 'O'
		b2['font'] = ("Comic Sans MS", 25, 'bold')
		b2['fg']   = 'green'
		space -= 1
	elif num == 3:
		b3['text'] = 'O'
		b3['font'] = ("Comic Sans MS", 25, 'bold')
		b3['fg']   = 'green'
		space -= 1
	elif num == 4:
		b4['text'] = 'O'
		b4['font'] = ("Comic Sans MS", 25, 'bold')
		b4['fg']   = 'green'
		space -= 1
	elif num == 5:
		b5['text'] = 'O'
		b5['font'] = ("Comic Sans MS", 25, 'bold')
		b5['fg']   = 'green'
		space -= 1
	elif num == 6:
		b6['text'] = 'O'
		b6['font'] = ("Comic Sans MS", 25, 'bold')
		b6['fg']   = 'green'
		space -= 1
	elif num == 7:
		b7['text'] = 'O'
		b7['font'] = ("Comic Sans MS", 25, 'bold')
		b7['fg']   = 'green'
		space -= 1
	elif num == 8:
		b8['text'] = 'O'
		b8['font'] = ("Comic Sans MS", 25, 'bold')
		b8['fg']   = 'green'
		space -= 1

def lst_of_moves():
	possible_moves = [pos for pos, letter in enumerate(lst) if letter == '-']
	
	for symbol in ['O', 'X']:
		for pos in possible_moves:
			clone = lst[:]
			clone[pos] = symbol
			if is_won_comp(clone):
				lst[pos] = 'O'
				make_move(pos)
				return

	possible_corner_moves = []
	for pos in [0, 2, 6, 8]:
		if lst[pos] == '-':
			possible_corner_moves.append(pos)
	if len(possible_corner_moves) > 0:
		import random
		pos = random.choice(possible_corner_moves)
		lst[pos] = 'O'
		make_move(pos)
		return

	possible_edge_moves = []
	for pos in [1, 3, 5, 7]:
		if lst[pos] == '-':
			possible_edge_moves.append(pos)
	if len(possible_edge_moves) > 0:
		import random
		pos = random.choice(possible_edge_moves)
		lst[pos] = 'O'
		make_move(pos)
		return


def clicked0():
	global space
	b0['text'] = 'X'
	b0['font'] = ("Comic Sans MS", 25, 'bold')
	b0['fg']   = 'blue'
	space -= 1
	lst[0] = 'X'
	lst_of_moves()
	check()

def clicked1():
	global space
	b1['text'] = 'X'
	b1['font'] = ("Comic Sans MS", 25, 'bold')
	b1['fg']   = 'blue'
	space -= 1
	lst[1] = 'X'
	lst_of_moves()
	check()


def clicked2():
	global space
	b2['text'] = 'X'
	b2['font'] = ("Comic Sans MS", 25, 'bold')
	b2['fg']   = 'blue'
	space -= 1
	lst[2] = 'X'
	lst_of_moves()
	check()


def clicked3():
	global space
	b3['text'] = 'X'
	b3['font'] = ("Comic Sans MS", 25, 'bold')
	b3['fg']   = 'blue'
	space -= 1
	lst[3] = 'X'
	lst_of_moves()
	check()


def clicked4():
	global space
	b4['text'] = 'X'
	b4['font'] = ("Comic Sans MS", 25, 'bold')
	b4['fg']   = 'blue'
	space -= 1
	lst[4] = 'X'
	lst_of_moves()
	check()


def clicked5():
	global space
	b5['text'] = 'X'
	b5['font'] = ("Comic Sans MS", 25, 'bold')
	b5['fg']   = 'blue'
	space -= 1
	lst[5] = 'X'
	lst_of_moves()
	check()


def clicked6():
	global space
	b6['text'] = 'X'
	b6['font'] = ("Comic Sans MS", 25, 'bold')
	b6['fg']   = 'blue'
	space -= 1
	lst[6] = 'X'
	lst_of_moves()
	check()


def clicked7():
	global space
	b7['text'] = 'X'
	b7['font'] = ("Comic Sans MS", 25, 'bold')
	b7['fg']   = 'blue'
	space -= 1
	lst[7] = 'X'
	lst_of_moves()
	check()


def clicked8():
	global space
	b8['text'] = 'X'
	b8['font'] = ("Comic Sans MS", 25, 'bold')
	b8['fg']   = 'blue'
	space -= 1
	lst[8] = 'X'
	lst_of_moves()
	check()


def is_win():
	if b0['text'] == b1['text'] and b0['text'] == b2['text'] and b0['text'] == 'X':
		return 1
	if b3['text'] == b4['text'] and b3['text'] == b5['text'] and b3['text'] == 'X':
		return 1
	if b6['text'] == b7['text'] and b6['text'] == b8['text'] and b6['text'] == 'X':
		return 1
	if b0['text'] == b3['text'] and b6['text'] == b3['text'] and b0['text'] == 'X':
		return 1
	if b4['text'] == b1['text'] and b7['text'] == b1['text'] and b1['text'] == 'X':
		return 1
	if b2['text'] == b5['text'] and b8['text'] == b2['text'] and b2['text'] == 'X':
		return 1
	if b0['text'] == b4['text'] and b0['text'] == b8['text'] and b0['text'] == 'X':
		return 1
	if b2['text'] == b4['text'] and b6['text'] == b2['text'] and b2['text'] == 'X':
		return 1

	if b0['text'] == b1['text'] and b0['text'] == b2['text'] and b0['text'] == 'O':
		return 0
	if b3['text'] == b4['text'] and b3['text'] == b5['text'] and b3['text'] == 'O':
		return 0
	if b6['text'] == b7['text'] and b6['text'] == b8['text'] and b6['text'] == 'O':
		return 0
	if b0['text'] == b3['text'] and b6['text'] == b3['text'] and b0['text'] == 'O':
		return 0
	if b4['text'] == b1['text'] and b7['text'] == b1['text'] and b1['text'] == 'O':
		return 0
	if b2['text'] == b5['text'] and b8['text'] == b2['text'] and b2['text'] == 'O':
		return 0
	if b0['text'] == b4['text'] and b0['text'] == b8['text'] and b0['text'] == 'O':
		return 0
	if b2['text'] == b4['text'] and b6['text'] == b2['text'] and b2['text'] == 'O':
		return 0



def check():
	global space
	if is_win() == 1:
		messagebox.showinfo('Congratulation', 'Winner winner Chicken Dinnner!!')
		root.destroy()
		return
	elif is_win() == 0:
		messagebox.showinfo('Sorry', 'You fucking suck!')
		root.destroy()
		return

	if space == 0:
		messagebox.showinfo('Information', 'Tie Game!!')
		root.destroy()
	


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

b0 = tk.Button(play_frame, bg='#D9C117', command=lambda: clicked0())
b0.place(relx=0, rely=0, relheight=0.2, relwidth=0.3)

b1 = tk.Button(play_frame, bg='#D9C117', command=lambda: clicked1())
b1.place(relx=0.35, rely=0, relheight=0.2, relwidth=0.3)

b2 = tk.Button(play_frame, bg='#D9C117', command=lambda: clicked2())
b2.place(relx=0.7, rely=0, relheight=0.2, relwidth=0.3)

b3 = tk.Button(play_frame, bg='#D9C117', command=lambda: clicked3())
b3.place(relx=0, rely=0.4, relheight=0.2, relwidth=0.3)

b4 = tk.Button(play_frame, bg='#D9C117', command=lambda: clicked4())
b4.place(relx=0.35, rely=0.4, relheight=0.2, relwidth=0.3)

b5 = tk.Button(play_frame, bg='#D9C117', command=lambda: clicked5())
b5.place(relx=0.7, rely=0.4, relheight=0.2, relwidth=0.3)

b6 = tk.Button(play_frame, bg='#D9C117', command=lambda: clicked6())
b6.place(relx=0, rely=0.8, relheight=0.2, relwidth=0.3)

b7 = tk.Button(play_frame, bg='#D9C117', command=lambda: clicked7())
b7.place(relx=0.35, rely=0.8, relheight=0.2, relwidth=0.3)

b8 = tk.Button(play_frame, bg='#D9C117', command=lambda: clicked8())
b8.place(relx=0.7, rely=0.8, relheight=0.2, relwidth=0.3)

if space == 0:
	win
root.mainloop()
