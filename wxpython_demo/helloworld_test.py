import sys
import random
from PySide2 import QtCore, QtWidgets, QtGui

class MyHelloWorld(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["hello1", "hello2", "hello3"]

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello world")
        # 设置对齐方式
        self.text.setAlignment(QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

        self.button.clicked.connect(self.magic)

    def magic(self):
        self.text.setText(random.choice(self.hello))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyHelloWorld()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec_())