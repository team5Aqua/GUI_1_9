# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'auto.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog2(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(986, 481)
        Dialog.setStyleSheet("background-color: rgb(6, 53, 95);")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(520, 20, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(570, 20, 16, 16))
        self.label_4.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 0, 0);\n"
"border-radius:30px;")
        self.label_4.setObjectName("label_4")
        self.Screenshot = QtWidgets.QPushButton(Dialog)
        self.Screenshot.setGeometry(QtCore.QRect(660, 400, 201, 61))
        self.Screenshot.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.Screenshot.setObjectName("Screenshot")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(40, 350, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 221, 321))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.iseewall = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.iseewall.setFont(font)
        self.iseewall.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.iseewall.setAlignment(QtCore.Qt.AlignCenter)
        self.iseewall.setObjectName("iseewall")
        self.verticalLayout.addWidget(self.iseewall)
        self.UltrasonicRead_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.UltrasonicRead_label.setFont(font)
        self.UltrasonicRead_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.UltrasonicRead_label.setText("")
        self.UltrasonicRead_label.setAlignment(QtCore.Qt.AlignCenter)
        self.UltrasonicRead_label.setObjectName("UltrasonicRead_label")
        self.verticalLayout.addWidget(self.UltrasonicRead_label)
        self.currentsensordisp = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.currentsensordisp.setFont(font)
        self.currentsensordisp.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.currentsensordisp.setAlignment(QtCore.Qt.AlignCenter)
        self.currentsensordisp.setObjectName("currentsensordisp")
        self.verticalLayout.addWidget(self.currentsensordisp)
        self.CurrentsensorRead = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.CurrentsensorRead.setFont(font)
        self.CurrentsensorRead.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.CurrentsensorRead.setText("")
        self.CurrentsensorRead.setAlignment(QtCore.Qt.AlignCenter)
        self.CurrentsensorRead.setObjectName("CurrentsensorRead")
        self.verticalLayout.addWidget(self.CurrentsensorRead)
        self.volsensordisp = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.volsensordisp.setFont(font)
        self.volsensordisp.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.volsensordisp.setAlignment(QtCore.Qt.AlignCenter)
        self.volsensordisp.setObjectName("volsensordisp")
        self.verticalLayout.addWidget(self.volsensordisp)
        self.voltagesensorRead = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.voltagesensorRead.setFont(font)
        self.voltagesensorRead.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.voltagesensorRead.setText("")
        self.voltagesensorRead.setAlignment(QtCore.Qt.AlignCenter)
        self.voltagesensorRead.setObjectName("voltagesensorRead")
        self.verticalLayout.addWidget(self.voltagesensorRead)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(240, 10, 271, 241))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.SpeedWin = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.SpeedWin.setFont(font)
        self.SpeedWin.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.SpeedWin.setAlignment(QtCore.Qt.AlignCenter)
        self.SpeedWin.setObjectName("SpeedWin")
        self.verticalLayout_3.addWidget(self.SpeedWin)
        self.lcdauto = QtWidgets.QLCDNumber(self.verticalLayoutWidget_4)
        self.lcdauto.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.lcdauto.setObjectName("lcdauto")
        self.verticalLayout_3.addWidget(self.lcdauto)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.SpeedControlWin = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.SpeedControlWin.setFont(font)
        self.SpeedControlWin.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.SpeedControlWin.setAlignment(QtCore.Qt.AlignCenter)
        self.SpeedControlWin.setObjectName("SpeedControlWin")
        self.verticalLayout_2.addWidget(self.SpeedControlWin)
        self.SpeedSliderAuto = QtWidgets.QSlider(self.verticalLayoutWidget_4)
        self.SpeedSliderAuto.setMaximum(255)
        self.SpeedSliderAuto.setOrientation(QtCore.Qt.Horizontal)
        self.SpeedSliderAuto.setObjectName("SpeedSliderAuto")
        self.verticalLayout_2.addWidget(self.SpeedSliderAuto)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(239, 259, 271, 121))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.MotionStateWin = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.MotionStateWin.setFont(font)
        self.MotionStateWin.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.MotionStateWin.setAlignment(QtCore.Qt.AlignCenter)
        self.MotionStateWin.setObjectName("MotionStateWin")
        self.verticalLayout_5.addWidget(self.MotionStateWin)
        self.MotionStateNow = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.MotionStateNow.setFont(font)
        self.MotionStateNow.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.MotionStateNow.setText("")
        self.MotionStateNow.setAlignment(QtCore.Qt.AlignCenter)
        self.MotionStateNow.setObjectName("MotionStateNow")
        self.verticalLayout_5.addWidget(self.MotionStateNow)
        self.logoAu = QtWidgets.QLabel(Dialog)
        self.logoAu.setGeometry(QtCore.QRect(20, 380, 141, 81))
        self.logoAu.setStyleSheet("image: url(:/logo/img.jpg);")
        self.logoAu.setText("")
        self.logoAu.setObjectName("logoAu")
        self.webcamlabelauto = QtWidgets.QLabel(Dialog)
        self.webcamlabelauto.setGeometry(QtCore.QRect(524, 45, 441, 351))
        self.webcamlabelauto.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.webcamlabelauto.setText("")
        self.webcamlabelauto.setObjectName("webcamlabelauto")

        self.retranslateUi(Dialog)
        self.SpeedSliderAuto.valueChanged['int'].connect(self.lcdauto.display) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "Live"))
        self.label_4.setText(_translate("Dialog", "TextLabel"))
        self.Screenshot.setText(_translate("Dialog", "ScreenShot"))
        self.iseewall.setText(_translate("Dialog", "I See a Wall Far Away"))
        self.currentsensordisp.setText(_translate("Dialog", "Current Sensor Read"))
        self.volsensordisp.setText(_translate("Dialog", "Voltage Sensor Read"))
        self.SpeedWin.setText(_translate("Dialog", "Your Speed "))
        self.SpeedControlWin.setText(_translate("Dialog", "Control Your Speed"))
        self.MotionStateWin.setText(_translate("Dialog", "Motion State"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog2()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
