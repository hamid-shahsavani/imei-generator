# -*- coding: utf-8 

from PyQt5 import QtCore, QtGui, QtWidgets 
from os.path import isdir , isfile , realpath
from random import randint
from os import mkdir , system
from platform import system as os_type
from sys import exit , argv
try:
    from os import startfile
except:
    pass

class Ui_base_style(object):
    def setupUi(self, base_style):
        def handle_click(*args, **kwargs):
            if len(str(self.default_range_line_edit.text())) > 15:
                msg=QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setText('maximum number entered at \'default range\' input is 15 number ...')  
                msg.setStyleSheet("background-color:rgb(32,32,32);color:white")         
                msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                msg.setDefaultButton(QtWidgets.QMessageBox.Ignore)
                reply=msg.exec_()
            elif len(str(self.how_many_line_edit.text())) > 3:
                msg=QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setText('maximum size for \'how many\' input is 999 number ...')  
                msg.setStyleSheet("background-color:rgb(32,32,32);color:white")         
                msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                msg.setDefaultButton(QtWidgets.QMessageBox.Ignore)
                reply=msg.exec_()
            elif (str(self.how_many_line_edit.text()) == '0') or (str(self.how_many_line_edit.text()) == ''):
                msg=QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setText('specify at least one number for the  \'how many\' input ...')  
                msg.setStyleSheet("background-color:rgb(32,32,32);color:white")         
                msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                msg.setDefaultButton(QtWidgets.QMessageBox.Ignore)
                reply=msg.exec_()
            elif str(self.default_range_line_edit.text()) == '':
                msg=QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setText('specify at least one number for the  \'default range\' input ...')  
                msg.setStyleSheet("background-color:rgb(32,32,32);color:white")         
                msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                msg.setDefaultButton(QtWidgets.QMessageBox.Ignore)
                reply=msg.exec_()
            elif str(self.how_many_line_edit.text()).isdigit() == False:
                msg=QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setText('type \'how many\' input is not number ...')  
                msg.setStyleSheet("background-color:rgb(32,32,32);color:white")         
                msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                msg.setDefaultButton(QtWidgets.QMessageBox.Ignore)
                reply=msg.exec_()
            elif str(self.default_range_line_edit.text()).isdigit() == False:
                msg=QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setText('type \'default range\' input is not number ...')  
                msg.setStyleSheet("background-color:rgb(32,32,32);color:white")         
                msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                msg.setDefaultButton(QtWidgets.QMessageBox.Ignore)
                reply=msg.exec_()
            else:
                generate_list(str(self.default_range_line_edit.text()), str(self.how_many_line_edit.text()))

        base_style.setObjectName("base_style")
        base_style.resize(139, 138)
        font = QtGui.QFont()
        font.setItalic(True)
        base_style.setFont(font)
        base_style.setStyleSheet("background-color: rgb(32, 32, 32);")
        self.generate_button = QtWidgets.QPushButton(base_style)
        self.generate_button.setGeometry(QtCore.QRect(10, 90, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(9)
        font.setItalic(False)
        self.generate_button.setFont(font)
        self.generate_button.setStyleSheet("background-color: rgb(0, 0, 124);")
        self.generate_button.setObjectName("generate_button")
        self.generate_button.clicked.connect(handle_click)
        self.default_range_lable = QtWidgets.QLabel(base_style)
        self.default_range_lable.setGeometry(QtCore.QRect(30, 0, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setItalic(False)
        self.default_range_lable.setFont(font)
        self.default_range_lable.setStyleSheet("color: rgb(0, 128, 255);")
        self.default_range_lable.setObjectName("default_range_lable")
        self.how_many_lable = QtWidgets.QLabel(base_style)
        self.how_many_lable.setGeometry(QtCore.QRect(40, 40, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setItalic(False)
        self.how_many_lable.setFont(font)
        self.how_many_lable.setStyleSheet("color: rgb(0, 128, 255);")
        self.how_many_lable.setObjectName("how_many_lable")
        self.imei_generator_by_SYS113_lable = QtWidgets.QLabel(base_style)
        self.imei_generator_by_SYS113_lable.setGeometry(QtCore.QRect(10, 120, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setItalic(True)
        self.imei_generator_by_SYS113_lable.setFont(font)
        self.imei_generator_by_SYS113_lable.setStyleSheet("color: rgb(0, 255, 0);")
        self.imei_generator_by_SYS113_lable.setObjectName("imei_generator_by_SYS113_lable")
        self.default_range_line_edit = QtWidgets.QLineEdit(base_style)
        self.default_range_line_edit.setGeometry(QtCore.QRect(10, 20, 121, 23))
        self.default_range_line_edit.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.default_range_line_edit.setObjectName("default_range_line_edit")
        self.how_many_line_edit = QtWidgets.QLineEdit(base_style)
        self.how_many_line_edit.setGeometry(QtCore.QRect(10, 60, 121, 23))
        self.how_many_line_edit.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.how_many_line_edit.setObjectName("how_many_line_edit")
        self.retranslateUi(base_style)
        QtCore.QMetaObject.connectSlotsByName(base_style)

    def retranslateUi(self, base_style):
        _translate = QtCore.QCoreApplication.translate
        base_style.setWindowTitle(_translate("base_style", "Form"))
        self.generate_button.setText(_translate("base_style", "generate"))
        self.default_range_lable.setText(_translate("base_style", "default range"))
        self.how_many_lable.setText(_translate("base_style", "how many"))
        self.imei_generator_by_SYS113_lable.setText(_translate("base_style", "imei generator by SYS113"))
        self.default_range_line_edit.setText(_translate("base_style", "1234567"))
        self.how_many_line_edit.setText(_translate("base_style", "20"))

def checksum(string):
    digits = list(map(int, string))
    odd_sum = sum(digits[-1::-2])
    even_sum = sum([sum(divmod(2 * d, 10)) for d in digits[-2::-2]])
    return (odd_sum + even_sum) % 10

def generate(string):
    cksum = checksum(string + '0')
    return (10 - cksum) % 10

def append_luhn(string):
    return string + str(generate(string))

def generate_imei(subject_imei):
    imei_digits = []
    for i in range(0, 14):
        try:
            digit = subject_imei[i]
        except IndexError:
            digit = randint(0, 9)
        imei_digits.append(str(digit))
    return append_luhn("".join(imei_digits))

def generate_list(Imei, quantity):
    _generate = open('imei.txt', 'w')
    _generate.write('.__________________________.\n' +'| imei generator by SYS113 |'+'\n.__________________________.\n')
    for x in range(1, int(quantity)+1):
        _generate = open('imei.txt', 'a')
        if len(str(x)) == 1:
            _generate.write('| '+str(x)+'    |  '+generate_imei(Imei)+'  |'+'\n')
        if len(str(x)) == 2:
            _generate.write('| '+str(x)+'   |  '+generate_imei(Imei)+'  |'+'\n')
        if len(str(x)) == 3:
            _generate.write('| '+str(x)+'  |  '+generate_imei(Imei)+'  |'+'\n')
    _generate.write('.__________________________.\n' +'| imei generator by SYS113 |'+'\n.__________________________.\n')
    _generate.close()

    if os_type() == 'Linux':
        system('xdg-open imei.txt')
    elif os_type() == 'Windows':
        startfile('imei.txt')

if __name__ == "__main__":
    app = QtWidgets.QApplication(argv)
    base_style = QtWidgets.QWidget()
    ui = Ui_base_style()
    ui.setupUi(base_style)
    base_style.show()
    exit(app.exec())
