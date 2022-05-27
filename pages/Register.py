from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from helpers.HttpHelper import HttpHelper
from pages.Login import Login
from services.UserService import UserService


class Register(QDialog):
    def __init__(self, widget):
        self.widget = widget
        super(Register, self).__init__()
        loadUi("pages/ui/signup.ui", self)
        self.signup_btn.clicked.connect(self.create_account)
        self.redirect_to_login.clicked.connect(self.login)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpass.setEchoMode(QtWidgets.QLineEdit.Password)

    def create_account(self):
        email = self.email.text()
        if self.password.text() == self.confirmpass.text():
            password = self.password.text()
            print(email, password)

            httpHelper = HttpHelper()
            response = httpHelper.doRequest("/api/register", 'POST', {'Content-Type': 'application/json'}, {"email": email, "password": password})

            if response.status_code == 200:
                UserService().set_token(response.json()['token'])
                UserService().set_id(response.json()['id'])
                login = Login(self.widget)
                self.widget.addWidget(login)
                self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def login(self):
        login = Login(self.widget)
        self.widget.addWidget(login)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
