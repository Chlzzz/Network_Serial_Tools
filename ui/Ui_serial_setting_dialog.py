# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Codes\python\PyQt5实用工具\ui\serial_setting_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SerialSettingDialog(object):
    def setupUi(self, SerialSettingDialog):
        SerialSettingDialog.setObjectName("SerialSettingDialog")
        SerialSettingDialog.resize(174, 200)
        self.verticalLayout = QtWidgets.QVBoxLayout(SerialSettingDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(SerialSettingDialog)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.botelvLabel = QtWidgets.QLabel(self.groupBox)
        self.botelvLabel.setObjectName("botelvLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.botelvLabel)
        self.cb_baud_rate = QtWidgets.QComboBox(self.groupBox)
        self.cb_baud_rate.setObjectName("cb_baud_rate")
        self.cb_baud_rate.addItem("")
        self.cb_baud_rate.addItem("")
        self.cb_baud_rate.addItem("")
        self.cb_baud_rate.addItem("")
        self.cb_baud_rate.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cb_baud_rate)
        self.Label = QtWidgets.QLabel(self.groupBox)
        self.Label.setObjectName("Label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Label)
        self.cb_data = QtWidgets.QComboBox(self.groupBox)
        self.cb_data.setObjectName("cb_data")
        self.cb_data.addItem("")
        self.cb_data.addItem("")
        self.cb_data.addItem("")
        self.cb_data.addItem("")
        self.cb_data.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cb_data)
        self.Label_2 = QtWidgets.QLabel(self.groupBox)
        self.Label_2.setObjectName("Label_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.Label_2)
        self.cb_parity = QtWidgets.QComboBox(self.groupBox)
        self.cb_parity.setObjectName("cb_parity")
        self.cb_parity.addItem("")
        self.cb_parity.addItem("")
        self.cb_parity.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.cb_parity)
        self.Label_3 = QtWidgets.QLabel(self.groupBox)
        self.Label_3.setObjectName("Label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.Label_3)
        self.cb_flow_control = QtWidgets.QComboBox(self.groupBox)
        self.cb_flow_control.setObjectName("cb_flow_control")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.cb_flow_control)
        self.Label_4 = QtWidgets.QLabel(self.groupBox)
        self.Label_4.setObjectName("Label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.Label_4)
        self.cb_stop = QtWidgets.QComboBox(self.groupBox)
        self.cb_stop.setObjectName("cb_stop")
        self.cb_stop.addItem("")
        self.cb_stop.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.cb_stop)
        self.horizontalLayout.addLayout(self.formLayout)
        self.verticalLayout.addWidget(self.groupBox)
        self.dialogButtonBox = QtWidgets.QDialogButtonBox(SerialSettingDialog)
        self.dialogButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.dialogButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.dialogButtonBox.setObjectName("dialogButtonBox")
        self.verticalLayout.addWidget(self.dialogButtonBox)

        self.retranslateUi(SerialSettingDialog)
        self.dialogButtonBox.accepted.connect(SerialSettingDialog.accept) # type: ignore
        self.dialogButtonBox.rejected.connect(SerialSettingDialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(SerialSettingDialog)

    def retranslateUi(self, SerialSettingDialog):
        _translate = QtCore.QCoreApplication.translate
        SerialSettingDialog.setWindowTitle(_translate("SerialSettingDialog", "Dialog"))
        self.groupBox.setTitle(_translate("SerialSettingDialog", "串口设置"))
        self.botelvLabel.setText(_translate("SerialSettingDialog", "波特率："))
        self.cb_baud_rate.setItemText(0, _translate("SerialSettingDialog", "9600"))
        self.cb_baud_rate.setItemText(1, _translate("SerialSettingDialog", "19200"))
        self.cb_baud_rate.setItemText(2, _translate("SerialSettingDialog", "57600"))
        self.cb_baud_rate.setItemText(3, _translate("SerialSettingDialog", "115200"))
        self.cb_baud_rate.setItemText(4, _translate("SerialSettingDialog", "27600"))
        self.Label.setText(_translate("SerialSettingDialog", "数据位："))
        self.cb_data.setItemText(0, _translate("SerialSettingDialog", "5"))
        self.cb_data.setItemText(1, _translate("SerialSettingDialog", "6"))
        self.cb_data.setItemText(2, _translate("SerialSettingDialog", "7"))
        self.cb_data.setItemText(3, _translate("SerialSettingDialog", "8"))
        self.cb_data.setItemText(4, _translate("SerialSettingDialog", "9"))
        self.Label_2.setText(_translate("SerialSettingDialog", "校验位："))
        self.cb_parity.setItemText(0, _translate("SerialSettingDialog", "none"))
        self.cb_parity.setItemText(1, _translate("SerialSettingDialog", "odd"))
        self.cb_parity.setItemText(2, _translate("SerialSettingDialog", "even"))
        self.Label_3.setText(_translate("SerialSettingDialog", "流控制："))
        self.Label_4.setText(_translate("SerialSettingDialog", "停止位："))
        self.cb_stop.setItemText(0, _translate("SerialSettingDialog", "1"))
        self.cb_stop.setItemText(1, _translate("SerialSettingDialog", "0"))
