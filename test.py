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
        # �E�B�W�F�b�g���쐬���܂��B
        self.edit = QLineEdit("")
        self.button = QPushButton("Post")
        # ���C�A�E�g���쐬���E�B�W�F�b�g��ǉ����܂�
        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        # �_�C�A���O�̃��C�A�E�g��ݒ肵�܂�
        self.setLayout(layout)
        # �{�^���̃V�O�i����greetings�Ɛڑ����܂�
        self.button.clicked.connect(self.greetings)
 
# ���[�U�ֈ��A���܂�
    def greetings(self):
        client.publish(topic, self.edit.text(), _qos, retain)
 
if __name__ == '__main__':
    # Qt Application�����܂�
    app = QApplication(sys.argv)
    # form���쐬���ĕ\�����܂�
    form = Form()
    form.show()
    # Qt�̃��C�����[�v���J�n���܂�
    sys.exit(app.exec_())