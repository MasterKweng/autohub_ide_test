import sys
from PySide2.QtWidgets import QApplication, QLabel

if __name__ == "__main__":

    app = QApplication(sys.argv)
    print(sys.argv)

    label = QLabel("hello world")
    label.show()
    # print(app.exec_())
    sys.exit(app.exec_())
    # app.exec()