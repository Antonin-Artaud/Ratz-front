from PyQt5 import QtWidgets
from PyQt5.uic import loadUi

from pages.Login import Login
from pages.Register import Register


class Main(QtWidgets.QMainWindow):
    def __init__(self, widget):
        self.widget = widget
        super(Main, self).__init__()
        loadUi("pages/ui/main.ui", self)
        self.login_button.clicked.connect(self.authentication)
        self.signup_button.clicked.connect(self.signup)

    def authentication(self):
        login = Login(self.widget)
        self.widget.addWidget(login)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def signup(self):
        register = Register(self.widget)
        self.widget.addWidget(register)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
