# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_window(object):
    def setupUi(self, window):
        window.setObjectName(_fromUtf8("window"))
        window.resize(384, 247)
        self.gridLayout = QtGui.QGridLayout(window)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(window)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.checkOpengl = QtGui.QCheckBox(window)
        self.checkOpengl.setObjectName(_fromUtf8("checkOpengl"))
        self.gridLayout.addWidget(self.checkOpengl, 0, 0, 1, 1)
        self.checkUsbcurrent = QtGui.QCheckBox(window)
        self.checkUsbcurrent.setObjectName(_fromUtf8("checkUsbcurrent"))
        self.gridLayout.addWidget(self.checkUsbcurrent, 1, 0, 1, 1)
        self.rebootButton = QtGui.QPushButton(window)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rebootButton.sizePolicy().hasHeightForWidth())
        self.rebootButton.setSizePolicy(sizePolicy)
        self.rebootButton.setMinimumSize(QtCore.QSize(0, 24))
        self.rebootButton.setObjectName(_fromUtf8("rebootButton"))
        self.gridLayout.addWidget(self.rebootButton, 4, 0, 1, 1)
        self.comboGpuram = QtGui.QComboBox(window)
        self.comboGpuram.setObjectName(_fromUtf8("comboGpuram"))
        self.comboGpuram.addItem(_fromUtf8(""))
        self.comboGpuram.addItem(_fromUtf8(""))
        self.comboGpuram.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboGpuram, 2, 1, 1, 2)
        self.buttonBox = QtGui.QDialogButtonBox(window)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 4, 1, 1, 2)
        self.comboAudio = QtGui.QComboBox(window)
        self.comboAudio.setObjectName(_fromUtf8("comboAudio"))
        self.comboAudio.addItem(_fromUtf8(""))
        self.comboAudio.addItem(_fromUtf8(""))
        self.comboAudio.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboAudio, 3, 1, 1, 2)
        self.label_2 = QtGui.QLabel(window)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)

        self.retranslateUi(window)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), window.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), window.reject)
        QtCore.QMetaObject.connectSlotsByName(window)

    def retranslateUi(self, window):
        window.setWindowTitle(_translate("window", "RaspberryPi Configuration", None))
        self.label.setText(_translate("window", "GPU RAM size :", None))
        self.checkOpengl.setText(_translate("window", "Enable OpenGL driver", None))
        self.checkUsbcurrent.setText(_translate("window", "Maximize USB Current (1200mA)", None))
        self.rebootButton.setText(_translate("window", "Reboot", None))
        self.comboGpuram.setItemText(0, _translate("window", "64 MB", None))
        self.comboGpuram.setItemText(1, _translate("window", "128 MB", None))
        self.comboGpuram.setItemText(2, _translate("window", "192 MB", None))
        self.comboAudio.setItemText(0, _translate("window", "Auto", None))
        self.comboAudio.setItemText(1, _translate("window", "HDMI", None))
        self.comboAudio.setItemText(2, _translate("window", "3.5mm Jack", None))
        self.label_2.setText(_translate("window", "Audio Output :", None))

