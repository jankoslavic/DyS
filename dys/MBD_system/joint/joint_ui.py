# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'joint.ui'
#
# Created: Tue Aug 04 18:20:19 2015
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(300, 385)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(300, 0))
        Form.setMaximumSize(QtCore.QSize(300, 1000))
        self.formLayout_2 = QtGui.QFormLayout(Form)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.groupBox_basicInfo = QtGui.QGroupBox(Form)
        self.groupBox_basicInfo.setObjectName(_fromUtf8("groupBox_basicInfo"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_basicInfo)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.name_label = QtGui.QLabel(self.groupBox_basicInfo)
        self.name_label.setObjectName(_fromUtf8("name_label"))
        self.gridLayout.addWidget(self.name_label, 0, 0, 1, 1)
        self.jointTypecomboBox = QtGui.QComboBox(self.groupBox_basicInfo)
        self.jointTypecomboBox.setObjectName(_fromUtf8("jointTypecomboBox"))
        self.jointTypecomboBox.addItem(_fromUtf8(""))
        self.jointTypecomboBox.addItem(_fromUtf8(""))
        self.jointTypecomboBox.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.jointTypecomboBox, 2, 2, 1, 1)
        self.jointID_lineEdit = QtGui.QLineEdit(self.groupBox_basicInfo)
        self.jointID_lineEdit.setEnabled(False)
        self.jointID_lineEdit.setObjectName(_fromUtf8("jointID_lineEdit"))
        self.gridLayout.addWidget(self.jointID_lineEdit, 1, 2, 1, 1)
        self.name_lineEdit = QtGui.QLineEdit(self.groupBox_basicInfo)
        self.name_lineEdit.setObjectName(_fromUtf8("name_lineEdit"))
        self.gridLayout.addWidget(self.name_lineEdit, 0, 2, 1, 1)
        self.jointType_label = QtGui.QLabel(self.groupBox_basicInfo)
        self.jointType_label.setObjectName(_fromUtf8("jointType_label"))
        self.gridLayout.addWidget(self.jointType_label, 2, 0, 1, 1)
        self.jointID_label = QtGui.QLabel(self.groupBox_basicInfo)
        self.jointID_label.setObjectName(_fromUtf8("jointID_label"))
        self.gridLayout.addWidget(self.jointID_label, 1, 0, 1, 1)
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.SpanningRole, self.groupBox_basicInfo)
        self.groupBox_simulationParameters = QtGui.QGroupBox(Form)
        self.groupBox_simulationParameters.setObjectName(_fromUtf8("groupBox_simulationParameters"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_simulationParameters)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.bodyIDj_label = QtGui.QLabel(self.groupBox_simulationParameters)
        self.bodyIDj_label.setObjectName(_fromUtf8("bodyIDj_label"))
        self.gridLayout_2.addWidget(self.bodyIDj_label, 1, 0, 1, 1)
        self.uPi_lineEdit = QtGui.QLineEdit(self.groupBox_simulationParameters)
        self.uPi_lineEdit.setObjectName(_fromUtf8("uPi_lineEdit"))
        self.gridLayout_2.addWidget(self.uPi_lineEdit, 4, 1, 1, 1)
        self.bodyIDi_lineEdit = QtGui.QLineEdit(self.groupBox_simulationParameters)
        self.bodyIDi_lineEdit.setObjectName(_fromUtf8("bodyIDi_lineEdit"))
        self.gridLayout_2.addWidget(self.bodyIDi_lineEdit, 0, 1, 1, 1)
        self.bodyIDi_label = QtGui.QLabel(self.groupBox_simulationParameters)
        self.bodyIDi_label.setObjectName(_fromUtf8("bodyIDi_label"))
        self.gridLayout_2.addWidget(self.bodyIDi_label, 0, 0, 1, 1)
        self.uPi_label = QtGui.QLabel(self.groupBox_simulationParameters)
        self.uPi_label.setObjectName(_fromUtf8("uPi_label"))
        self.gridLayout_2.addWidget(self.uPi_label, 4, 0, 1, 1)
        self.uPj_lineEdit = QtGui.QLineEdit(self.groupBox_simulationParameters)
        self.uPj_lineEdit.setObjectName(_fromUtf8("uPj_lineEdit"))
        self.gridLayout_2.addWidget(self.uPj_lineEdit, 5, 1, 1, 1)
        self.uPj_label = QtGui.QLabel(self.groupBox_simulationParameters)
        self.uPj_label.setObjectName(_fromUtf8("uPj_label"))
        self.gridLayout_2.addWidget(self.uPj_label, 5, 0, 1, 1)
        self.bodyIDj_lineEdit = QtGui.QLineEdit(self.groupBox_simulationParameters)
        self.bodyIDj_lineEdit.setObjectName(_fromUtf8("bodyIDj_lineEdit"))
        self.gridLayout_2.addWidget(self.bodyIDj_lineEdit, 1, 1, 1, 1)
        self.line = QtGui.QFrame(self.groupBox_simulationParameters)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_2.addWidget(self.line, 2, 0, 1, 2)
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.SpanningRole, self.groupBox_simulationParameters)
        self.bottom_horizontalLayout = QtGui.QHBoxLayout()
        self.bottom_horizontalLayout.setObjectName(_fromUtf8("bottom_horizontalLayout"))
        self.info_lineEdit = QtGui.QLineEdit(Form)
        self.info_lineEdit.setEnabled(False)
        self.info_lineEdit.setObjectName(_fromUtf8("info_lineEdit"))
        self.bottom_horizontalLayout.addWidget(self.info_lineEdit)
        self.save_pushButton = QtGui.QPushButton(Form)
        self.save_pushButton.setObjectName(_fromUtf8("save_pushButton"))
        self.bottom_horizontalLayout.addWidget(self.save_pushButton)
        self.cancel_pushButton = QtGui.QPushButton(Form)
        self.cancel_pushButton.setObjectName(_fromUtf8("cancel_pushButton"))
        self.bottom_horizontalLayout.addWidget(self.cancel_pushButton)
        self.formLayout_2.setLayout(3, QtGui.QFormLayout.SpanningRole, self.bottom_horizontalLayout)
        self.groupBox_comment = QtGui.QGroupBox(Form)
        self.groupBox_comment.setObjectName(_fromUtf8("groupBox_comment"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_comment)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.textEdit = QtGui.QTextEdit(self.groupBox_comment)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMinimumSize(QtCore.QSize(260, 40))
        self.textEdit.setMaximumSize(QtCore.QSize(260, 40))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.gridLayout_3.addWidget(self.textEdit, 0, 0, 1, 1)
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.SpanningRole, self.groupBox_comment)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.name_lineEdit, self.jointID_lineEdit)
        Form.setTabOrder(self.jointID_lineEdit, self.jointTypecomboBox)
        Form.setTabOrder(self.jointTypecomboBox, self.bodyIDi_lineEdit)
        Form.setTabOrder(self.bodyIDi_lineEdit, self.bodyIDj_lineEdit)
        Form.setTabOrder(self.bodyIDj_lineEdit, self.uPi_lineEdit)
        Form.setTabOrder(self.uPi_lineEdit, self.uPj_lineEdit)
        Form.setTabOrder(self.uPj_lineEdit, self.info_lineEdit)
        Form.setTabOrder(self.info_lineEdit, self.save_pushButton)
        Form.setTabOrder(self.save_pushButton, self.cancel_pushButton)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Joint", None))
        self.groupBox_basicInfo.setTitle(_translate("Form", "Basic Info", None))
        self.name_label.setText(_translate("Form", "Name", None))
        self.jointTypecomboBox.setItemText(0, _translate("Form", "Revolute", None))
        self.jointTypecomboBox.setItemText(1, _translate("Form", "Fixed", None))
        self.jointTypecomboBox.setItemText(2, _translate("Form", "Translational", None))
        self.jointType_label.setText(_translate("Form", "Type", None))
        self.jointID_label.setText(_translate("Form", "Joint id", None))
        self.groupBox_simulationParameters.setTitle(_translate("Form", "Simulation Parameters", None))
        self.bodyIDj_label.setText(_translate("Form", "Body ID j", None))
        self.bodyIDi_label.setText(_translate("Form", "Body ID i", None))
        self.uPi_label.setText(_translate("Form", "u_P i, [x, y]", None))
        self.uPj_label.setText(_translate("Form", "u_P j, [x, y]", None))
        self.save_pushButton.setText(_translate("Form", "Save", None))
        self.cancel_pushButton.setText(_translate("Form", "Cancel", None))
        self.groupBox_comment.setTitle(_translate("Form", "Comment", None))
