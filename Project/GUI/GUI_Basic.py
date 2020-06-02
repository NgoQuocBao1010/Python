from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


def window():
	app = QApplication(sys.argv) # tạo 1 môi trường để thao tác
	win = QMainWindow() # tạo 1 cửa sổ window
	win.setGeometry(200, 200, 800, 800) # 2 vị trí đầu để chỉ tọa độ xuất hiện của màn hình, 2 vị trí sau là bề ngang và bề dọc
	win.setWindowTitle('FirstTime') # đặt tên

	label = QtWidgets.QLabel(win)
	label.setText('Hello World')
	label.move(50, 50) # vị trí đặt Label

	win.show() # hiện cửa sổ
	sys.exit(app.exec_()) # đóng cửa sổ


window()