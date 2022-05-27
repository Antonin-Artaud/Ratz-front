import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication

from pages.main import Main


def print_hi(name):
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    main = Main(widget)
    widget.setWindowTitle('Ratz')
    widget.setFixedWidth(800)
    widget.setFixedHeight(600)
    widget.addWidget(main)
    widget.show()
    app.exec_()


if __name__ == '__main__':
    print_hi('PyCharm')
