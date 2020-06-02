from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class MyGUI(QMainWindow):
	def __init__(self):
		super(MyGUI, self).__init__()
		self.setGeometry(200, 200, 800, 800)
		self.setWindowTitle('FirstTime')
		self.InitUI()

	def InitUI(self):
		self.label = QtWidgets.QLabel(self)
		self.label.setText('Hello World')
		self.label.move(50, 50)

		self.button = QtWidgets.QPushButton(self)
		self.button.setText('Click here')
		self.button.clicked.connect(self.clicked)

	def clicked(self):
		self.label.setText('You \'ve press the button')
		self.update()

	def update(self):
		self.label.adjustSize()



def window():
	app = QApplication(sys.argv)
	win = MyGUI()

	win.show()
	sys.exit(app.exec_())


window()
