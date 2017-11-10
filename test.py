#!/usr/bin/python
#-'''- coding: utf-8 -'''-
 
import sys
import paho.mqtt.client as mqtt
from PySide.QtCore import *
from PySide.QtGui import *
from time import sleep

host = '127.0.0.1'
port = 1883
topic = 'shara/test/aaa'
_qos = 1
retain = 0

client = mqtt.Client(protocol=mqtt.MQTTv311)

client.connect(host, port=port, keepalive=60)

class Form(QDialog):
 
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        # ウィジェットを作成します。
        self.edit = QLineEdit("")
        self.button = QPushButton("Post")
        # レイアウトを作成しウィジェットを追加します
        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        # ダイアログのレイアウトを設定します
        self.setLayout(layout)
        # ボタンのシグナルをgreetingsと接続します
        self.button.clicked.connect(self.greetings)
 
# ユーザへ挨拶します
    def greetings(self):
        client.publish(topic, self.edit.text(), _qos, retain)
 
if __name__ == '__main__':
    # Qt Applicationを作ります
    app = QApplication(sys.argv)
    # formを作成して表示します
    form = Form()
    form.show()
    # Qtのメインループを開始します
    sys.exit(app.exec_())