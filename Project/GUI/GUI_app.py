import tkinter as tk

def test_function(entry):
	label['text'] = 'Hello ' + entry


def clicked(event):
	label1['text'] = 'clicked at ' + str(event.x) + ' ' + str(event.y)
	#print('clicked at', event.x, event.y)


def keys(event):
	label1['text'] = 'Pressed ' + repr(event.char)

HEIGHT = 700
WIDTH = 800

root = tk.Tk()

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='image.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg = '#80c1ff', bd=5)
frame.place(relx=0.5, rely = 0.1, relwidth=0.75, relheight=0.1, anchor='n')

button1 = tk.Button(frame, text = 'Get Weather', font=40, command=lambda: test_function(entry.get()))
button1.place(relx=0.7, relheight=1, relwidth=0.3)

entry = tk.Entry(frame, font=40)
entry.place( relwidth=0.65, relheight=1)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.4, anchor='n')

label = tk.Label(lower_frame, text= 'This is a Label', font=40)
label.place(relheight= 1, relwidth=1)

another_frame = tk.Frame(root, bg='black', bd=10)
another_frame.focus_set()	
another_frame.bind('<Return>', keys)
another_frame.bind('<Button-1>', clicked)
another_frame.place(relx=0.5, rely=0.7, relwidth=0.75, relheight=0.1, anchor='n')

label1 = tk.Label(another_frame, text= 'Click into the frame', font=40)
label1.place(relheight= 0.3, relwidth=0.3)

root.mainloop()