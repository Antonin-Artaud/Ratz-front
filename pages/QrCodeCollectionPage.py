from PIL.ImageQt import ImageQt
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QLabel, QHBoxLayout, QScrollArea, QWidget, QVBoxLayout
from PyQt5.uic import loadUi
from PyQt5.uic.uiparser import QtWidgets

import qrcode
from helpers.HttpHelper import HttpHelper
from services.UserService import UserService


class QrCodeCollection(QDialog):
    def __init__(self, widget):
        self.widget = widget
        super(QrCodeCollection, self).__init__()
        loadUi("pages/ui/qrcodeList.ui", self)
        self.actionVoir_les_QRcode_enregistrer.triggered.connect(self.show_qrcode)
        self.actionGenerate_QRcode.triggered.connect(self.generate_qrcode)
        self.draw()

    def show_qrcode(self):
        pass

    def generate_qrcode(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() - 1)

    def draw(self):
        httpHelper = HttpHelper()
        response = httpHelper.doRequest("/api/user/" + str(UserService().get_id()) + "/qrcodes", 'GET',
                                        {'Content-Type': 'application/json',
                                         'Authorization': 'Bearer ' + str(UserService().get_token())})

        # [{"qrCodeId":1,"url":"hehehehe","encodedUrl":"1011100111011010100100100000011100001010010010110001110000011001100110011000101100100101110101000100111110001111100110011101100110101011110011100111110011000000010010001100001101000110010011101101100101010010","informationFormat":"001011010001001","userId":3,"user":null}]

        if response.status_code == 200:
            response = response.json()

            for i in range(len(response)):
                encoded_url = response[i]['encodedUrl']
                information_format = response[i]['informationFormat']
                url = response[i]['url']

                im = qrcode.draw(information_format, encoded_url)
                # convert pil image to qt image
                qim = ImageQt(im)
                # convert qt image to qt pixmap
                qt_pixmap = QtGui.QPixmap.fromImage(qim)

                image = QLabel()
                image.setPixmap(qt_pixmap)

                if i % 2 == 0:
                    self.url_left.setText(url)
                    self.qrcode_left.setPixmap(qt_pixmap)
                else:
                    self.url_right.setText(url)
                    self.qrcode_right.setPixmap(qt_pixmap)


        else:
            print(response.status_code)
