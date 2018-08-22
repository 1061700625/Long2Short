#coding:utf-8

import requests
import pyperclip
import sys
from PyQt5.QtWidgets import QApplication , QMainWindow
from short import *
from PyQt5 import sip

class MYWINOW(Ui_MainWindow):
    # def __init__(self):
    #    pass
    def fetch(self, long_url):
        url = "http://dwz.cn/admin/create"
        data = '{"url":"%s"}' % long_url
        html = requests.post(url, data=data)
        short_url = html.json()["ShortUrl"]
        return short_url

    def change(self):
        long_url = self.lineEdit.text()
        short_url = self.fetch(long_url)
        pyperclip.copy(short_url)
        result = short_url + "\n已复制到剪切板!"
        self.textBrowser.setText(result)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Mainwindow = QMainWindow()
    ui = MYWINOW()
    ui.setupUi(Mainwindow)
    Mainwindow.show()
    sys.exit(app.exec_())














