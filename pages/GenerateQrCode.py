from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

import qrcode
from helpers.HttpHelper import HttpHelper
from pages.QrCodeCollectionPage import QrCodeCollection
from services.UserService import UserService


class GenerateQrCode(QDialog):
    def __init__(self, widget):
        self.widget = widget
        super(GenerateQrCode, self).__init__()
        loadUi("pages/ui/generateQRCode.ui", self)
        self.actionVoir_QRcode.triggered.connect(self.show_qrcode)
        self.actionGenerate_QRcod.triggered.connect(self.generate_qrcode)
        self.submit_button.clicked.connect(self.submit)

    def show_qrcode(self):
        qrCodeCollection = QrCodeCollection(self.widget)
        self.widget.addWidget(qrCodeCollection)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def generate_qrcode(self):
        pass

    def submit(self):
        data = self.data.text()

        endpoint = '/api/user/' + str(UserService().get_id()) + '/qrcodes'

        httpHelper = HttpHelper()
        header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + str(UserService().get_token())}
        response = httpHelper.doRequest(endpoint, 'POST', header, data)

        if response.status_code == 200:
            qrCodeCollection = QrCodeCollection(self.widget)
            self.widget.addWidget(qrCodeCollection)
            self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
        else:
            print(response.status_code)

