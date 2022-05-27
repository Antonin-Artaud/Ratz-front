from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from helpers.HttpHelper import HttpHelper
from pages.GenerateQrCode import GenerateQrCode
from services.UserService import UserService


class Login(QDialog):
    def __init__(self, widget):
        self.widget = widget
        super(Login, self).__init__()
        loadUi('pages/ui/loginPage.ui', self)
        self.login_btn.clicked.connect(self.loginAction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.signup_btn.clicked.connect(self.create_account)

    def loginAction(self):
        email = self.email.text()
        password = self.password.text()

        httpHelper = HttpHelper()
        response = httpHelper.doRequest('/api/login', 'POST', {'Content-Type': 'application/json'}, {"email": email, "password": password},)

        if response.status_code == 200:
            UserService().set_token(response.json()['token'])
            UserService().set_id(response.json()['id'])
            generateQrCode = GenerateQrCode(self.widget)
            self.widget.addWidget(generateQrCode)
            self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
        else:
            print(response.status_code)

    def create_account(self):
        from pages.Register import Register
        register = Register(self.widget)
        self.widget.addWidget(register)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

