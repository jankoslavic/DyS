# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'force.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(306, 582)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(306, 582))
        Form.setMaximumSize(QtCore.QSize(306, 582))
        self.formLayout_2 = QtGui.QFormLayout(Form)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.groupBox_basicInfo = QtGui.QGroupBox(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_basicInfo.sizePolicy().hasHeightForWidth())
        self.groupBox_basicInfo.setSizePolicy(sizePolicy)
        self.groupBox_basicInfo.setObjectName(_fromUtf8("groupBox_basicInfo"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_basicInfo)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.forceID_lineEdit = QtGui.QLineEdit(self.groupBox_basicInfo)
        self.forceID_lineEdit.setEnabled(False)
        self.forceID_lineEdit.setObjectName(_fromUtf8("forceID_lineEdit"))
        self.gridLayout.addWidget(self.forceID_lineEdit, 1, 2, 1, 1)
        self.forceID_label = QtGui.QLabel(self.groupBox_basicInfo)
        self.forceID_label.setObjectName(_fromUtf8("forceID_label"))
        self.gridLayout.addWidget(self.forceID_label, 1, 0, 1, 1)
        self.name_label = QtGui.QLabel(self.groupBox_basicInfo)
        self.name_label.setObjectName(_fromUtf8("name_label"))
        self.gridLayout.addWidget(self.name_label, 0, 0, 1, 1)
        self.name_lineEdit = QtGui.QLineEdit(self.groupBox_basicInfo)
        self.name_lineEdit.setObjectName(_fromUtf8("name_lineEdit"))
        self.gridLayout.addWidget(self.name_lineEdit, 0, 2, 1, 1)
        self.line_2 = QtGui.QFrame(self.groupBox_basicInfo)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout.addWidget(self.line_2, 2, 0, 1, 3)
        self.load_data_pushButton = QtGui.QPushButton(self.groupBox_basicInfo)
        self.load_data_pushButton.setObjectName(_fromUtf8("load_data_pushButton"))
        self.gridLayout.addWidget(self.load_data_pushButton, 4, 0, 1, 1)
        self.data_file_lineEdit = QtGui.QLineEdit(self.groupBox_basicInfo)
        self.data_file_lineEdit.setObjectName(_fromUtf8("data_file_lineEdit"))
        self.gridLayout.addWidget(self.data_file_lineEdit, 4, 2, 1, 1)
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.SpanningRole, self.groupBox_basicInfo)
        self.groupBox_simulationParameters = QtGui.QGroupBox(Form)
        self.groupBox_simulationParameters.setObjectName(_fromUtf8("groupBox_simulationParameters"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_simulationParameters)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.uPi_label = QtGui.QLabel(self.groupBox_simulationParameters)
        self.uPi_label.setObjectName(_fromUtf8("uPi_label"))
        self.gridLayout_2.addWidget(self.uPi_label, 1, 0, 1, 1)
        self.Mz_label = QtGui.QLabel(self.groupBox_simulationParameters)
        self.Mz_label.setObjectName(_fromUtf8("Mz_label"))
        self.gridLayout_2.addWidget(self.Mz_label, 5, 0, 1, 1)
        self.uPi_lineEdit = QtGui.QLineEdit(self.groupBox_simulationParameters)
        self.uPi_lineEdit.setObjectName(_fromUtf8("uPi_lineEdit"))
        self.gridLayout_2.addWidget(self.uPi_lineEdit, 1, 1, 1, 1)
        self.Fy_lineEdit = QtGui.QLineEdit(self.groupBox_simulationParameters)
        self.Fy_lineEdit.setInputMask(_fromUtf8(""))
        self.Fy_lineEdit.setObjectName(_fromUtf8("Fy_lineEdit"))
        self.gridLayout_2.addWidget(self.Fy_lineEdit, 4, 1, 1, 1)
        self.bodyID_lineEdit = QtGui.QLineEdit(self.groupBox_simulationParameters)
        self.bodyID_lineEdit.setObjectName(_fromUtf8("bodyID_lineEdit"))
        self.gridLayout_2.addWidget(self.bodyID_lineEdit, 0, 1, 1, 1)
        self.Fy_label = QtGui.QLabel(self.groupBox_simulationParameters)
        self.Fy_label.setObjectName(_fromUtf8("Fy_label"))
        self.gridLayout_2.addWidget(self.Fy_label, 4, 0, 1, 1)
        self.bodyID_label = QtGui.QLabel(self.groupBox_simulationParameters)
        self.bodyID_label.setObjectName(_fromUtf8("bodyID_label"))
        self.gridLayout_2.addWidget(self.bodyID_label, 0, 0, 1, 1)
        self.Mz_lineEdit = QtGui.QLineEdit(self.groupBox_simulationParameters)
        self.Mz_lineEdit.setObjectName(_fromUtf8("Mz_lineEdit"))
        self.gridLayout_2.addWidget(self.Mz_lineEdit, 5, 1, 1, 1)
        self.Fx_label = QtGui.QLabel(self.groupBox_simulationParameters)
        self.Fx_label.setObjectName(_fromUtf8("Fx_label"))
        self.gridLayout_2.addWidget(self.Fx_label, 3, 0, 1, 1)
        self.Fx_lineEdit = QtGui.QLineEdit(self.groupBox_simulationParameters)
        self.Fx_lineEdit.setObjectName(_fromUtf8("Fx_lineEdit"))
        self.gridLayout_2.addWidget(self.Fx_lineEdit, 3, 1, 1, 1)
        self.line = QtGui.QFrame(self.groupBox_simulationParameters)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_2.addWidget(self.line, 2, 0, 1, 2)
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.SpanningRole, self.groupBox_simulationParameters)
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
        self.formLayout_2.setLayout(5, QtGui.QFormLayout.SpanningRole, self.bottom_horizontalLayout)
        self.groupBox_comment = QtGui.QGroupBox(Form)
        self.groupBox_comment.setMinimumSize(QtCore.QSize(0, 40))
        self.groupBox_comment.setObjectName(_fromUtf8("groupBox_comment"))
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox_comment)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.comment_textEdit = QtGui.QTextEdit(self.groupBox_comment)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comment_textEdit.sizePolicy().hasHeightForWidth())
        self.comment_textEdit.setSizePolicy(sizePolicy)
        self.comment_textEdit.setMinimumSize(QtCore.QSize(260, 40))
        self.comment_textEdit.setMaximumSize(QtCore.QSize(260, 40))
        self.comment_textEdit.setObjectName(_fromUtf8("comment_textEdit"))
        self.gridLayout_4.addWidget(self.comment_textEdit, 0, 0, 1, 1)
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.SpanningRole, self.groupBox_comment)
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 40))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.scale_lineEdit = QtGui.QLineEdit(self.groupBox)
        self.scale_lineEdit.setObjectName(_fromUtf8("scale_lineEdit"))
        self.gridLayout_3.addWidget(self.scale_lineEdit, 0, 1, 1, 1)
        self.scale_label = QtGui.QLabel(self.groupBox)
        self.scale_label.setObjectName(_fromUtf8("scale_label"))
        self.gridLayout_3.addWidget(self.scale_label, 0, 0, 1, 1)
        self.color_lineEdit = QtGui.QLineEdit(self.groupBox)
        self.color_lineEdit.setObjectName(_fromUtf8("color_lineEdit"))
        self.gridLayout_3.addWidget(self.color_lineEdit, 1, 1, 1, 1)
        self.color_label = QtGui.QLabel(self.groupBox)
        self.color_label.setObjectName(_fromUtf8("color_label"))
        self.gridLayout_3.addWidget(self.color_label, 1, 0, 1, 1)
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.SpanningRole, self.groupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.name_lineEdit, self.forceID_lineEdit)
        Form.setTabOrder(self.forceID_lineEdit, self.bodyID_lineEdit)
        Form.setTabOrder(self.bodyID_lineEdit, self.uPi_lineEdit)
        Form.setTabOrder(self.uPi_lineEdit, self.Fx_lineEdit)
        Form.setTabOrder(self.Fx_lineEdit, self.Fy_lineEdit)
        Form.setTabOrder(self.Fy_lineEdit, self.Mz_lineEdit)
        Form.setTabOrder(self.Mz_lineEdit, self.info_lineEdit)
        Form.setTabOrder(self.info_lineEdit, self.save_pushButton)
        Form.setTabOrder(self.save_pushButton, self.cancel_pushButton)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Force", None))
        self.groupBox_basicInfo.setTitle(_translate("Form", "Basic Info", None))
        self.forceID_label.setText(_translate("Form", "Force id", None))
        self.name_label.setText(_translate("Form", "Name", None))
        self.load_data_pushButton.setText(_translate("Form", "Load", None))
        self.groupBox_simulationParameters.setTitle(_translate("Form", "Simulation Parameters", None))
        self.uPi_label.setText(_translate("Form", "u_P, [x, y]", None))
        self.Mz_label.setText(_translate("Form", "Mz, Nm", None))
        self.Fy_label.setText(_translate("Form", "Fy, N", None))
        self.bodyID_label.setText(_translate("Form", "Body ID i", None))
        self.Fx_label.setText(_translate("Form", "Fx, N", None))
        self.save_pushButton.setText(_translate("Form", "Save", None))
        self.cancel_pushButton.setText(_translate("Form", "Cancel", None))
        self.groupBox_comment.setTitle(_translate("Form", "Comment", None))
        self.groupBox.setTitle(_translate("Form", "Visualization", None))
        self.scale_label.setText(_translate("Form", "Scale", None))
        self.color_label.setText(_translate("Form", "Color, RGB", None))

