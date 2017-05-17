# -*- coding: utf-8 -*-

# Fom implementation generated from reading ui file 'simulation_control_widget.ui'
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
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.resize(304, 989)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(304, 0))
        Form.setMaximumSize(QtCore.QSize(304, 1000))
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.simulationStartButton = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.simulationStartButton.sizePolicy().hasHeightForWidth())
        self.simulationStartButton.setSizePolicy(sizePolicy)
        self.simulationStartButton.setObjectName(_fromUtf8("simulationStartButton"))
        self.horizontalLayout.addWidget(self.simulationStartButton)
        self.simulationStopButton = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.simulationStopButton.sizePolicy().hasHeightForWidth())
        self.simulationStopButton.setSizePolicy(sizePolicy)
        self.simulationStopButton.setObjectName(_fromUtf8("simulationStopButton"))
        self.horizontalLayout.addWidget(self.simulationStopButton)
        self.simulationResetButton = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.simulationResetButton.sizePolicy().hasHeightForWidth())
        self.simulationResetButton.setSizePolicy(sizePolicy)
        self.simulationResetButton.setObjectName(_fromUtf8("simulationResetButton"))
        self.horizontalLayout.addWidget(self.simulationResetButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.mainSettings_groupBox = QtGui.QGroupBox(Form)
        self.mainSettings_groupBox.setObjectName(_fromUtf8("mainSettings_groupBox"))
        self.gridLayout_7 = QtGui.QGridLayout(self.mainSettings_groupBox)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.integrationMethodComboBox = QtGui.QComboBox(self.mainSettings_groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.integrationMethodComboBox.sizePolicy().hasHeightForWidth())
        self.integrationMethodComboBox.setSizePolicy(sizePolicy)
        self.integrationMethodComboBox.setMinimumSize(QtCore.QSize(0, 0))
        self.integrationMethodComboBox.setObjectName(_fromUtf8("integrationMethodComboBox"))
        self.gridLayout_7.addWidget(self.integrationMethodComboBox, 1, 2, 1, 1)
        self.label = QtGui.QLabel(self.mainSettings_groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_7.addWidget(self.label, 0, 0, 1, 1)
        self.analysisTypeComboBox = QtGui.QComboBox(self.mainSettings_groupBox)
        self.analysisTypeComboBox.setObjectName(_fromUtf8("analysisTypeComboBox"))
        self.analysisTypeComboBox.addItem(_fromUtf8(""))
        self.analysisTypeComboBox.addItem(_fromUtf8(""))
        self.gridLayout_7.addWidget(self.analysisTypeComboBox, 0, 2, 1, 1)
        self.integrationMethod_Label = QtGui.QLabel(self.mainSettings_groupBox)
        self.integrationMethod_Label.setObjectName(_fromUtf8("integrationMethod_Label"))
        self.gridLayout_7.addWidget(self.integrationMethod_Label, 1, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(0, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem, 0, 1, 1, 1)
        self.endTime = QtGui.QLineEdit(self.mainSettings_groupBox)
        self.endTime.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhPreferNumbers)
        self.endTime.setObjectName(_fromUtf8("endTime"))
        self.gridLayout_7.addWidget(self.endTime, 2, 2, 1, 1)
        self.useBSM_checkBox = QtGui.QCheckBox(self.mainSettings_groupBox)
        self.useBSM_checkBox.setObjectName(_fromUtf8("useBSM_checkBox"))
        self.gridLayout_7.addWidget(self.useBSM_checkBox, 4, 2, 1, 1)
        self.endTime_label = QtGui.QLabel(self.mainSettings_groupBox)
        self.endTime_label.setObjectName(_fromUtf8("endTime_label"))
        self.gridLayout_7.addWidget(self.endTime_label, 2, 0, 1, 1)
        self.stepsNumber_label = QtGui.QLabel(self.mainSettings_groupBox)
        self.stepsNumber_label.setObjectName(_fromUtf8("stepsNumber_label"))
        self.gridLayout_7.addWidget(self.stepsNumber_label, 3, 0, 1, 1)
        self.stepsNumber = QtGui.QLineEdit(self.mainSettings_groupBox)
        self.stepsNumber.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhPreferNumbers)
        self.stepsNumber.setObjectName(_fromUtf8("stepsNumber"))
        self.gridLayout_7.addWidget(self.stepsNumber, 3, 2, 1, 1)
        self.verticalLayout.addWidget(self.mainSettings_groupBox)
        self.tabWidget = QtGui.QTabWidget(Form)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.simulation = QtGui.QWidget()
        self.simulation.setObjectName(_fromUtf8("simulation"))
        self.gridLayout = QtGui.QGridLayout(self.simulation)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.relTol = QtGui.QLineEdit(self.simulation)
        self.relTol.setEnabled(True)
        self.relTol.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhPreferNumbers)
        self.relTol.setObjectName(_fromUtf8("relTol"))
        self.gridLayout.addWidget(self.relTol, 4, 2, 1, 1)
        self.Hmin = QtGui.QLineEdit(self.simulation)
        self.Hmin.setEnabled(True)
        self.Hmin.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhPreferNumbers)
        self.Hmin.setObjectName(_fromUtf8("Hmin"))
        self.gridLayout.addWidget(self.Hmin, 1, 2, 1, 1)
        self.Hmax = QtGui.QLineEdit(self.simulation)
        self.Hmax.setEnabled(True)
        self.Hmax.setMinimumSize(QtCore.QSize(0, 0))
        self.Hmax.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Hmax.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Hmax.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhPreferNumbers)
        self.Hmax.setObjectName(_fromUtf8("Hmax"))
        self.gridLayout.addWidget(self.Hmax, 0, 2, 1, 1)
        self.Hcontact = QtGui.QLineEdit(self.simulation)
        self.Hcontact.setEnabled(True)
        self.Hcontact.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhPreferNumbers)
        self.Hcontact.setObjectName(_fromUtf8("Hcontact"))
        self.gridLayout.addWidget(self.Hcontact, 2, 2, 1, 1)
        self.Hmin_label_2 = QtGui.QLabel(self.simulation)
        self.Hmin_label_2.setObjectName(_fromUtf8("Hmin_label_2"))
        self.gridLayout.addWidget(self.Hmin_label_2, 2, 0, 1, 1)
        self.Hmax_label = QtGui.QLabel(self.simulation)
        self.Hmax_label.setObjectName(_fromUtf8("Hmax_label"))
        self.gridLayout.addWidget(self.Hmax_label, 0, 0, 1, 1)
        self.TOL_C_label = QtGui.QLabel(self.simulation)
        self.TOL_C_label.setObjectName(_fromUtf8("TOL_C_label"))
        self.gridLayout.addWidget(self.TOL_C_label, 6, 0, 1, 1)
        self.absTol_label = QtGui.QLabel(self.simulation)
        self.absTol_label.setObjectName(_fromUtf8("absTol_label"))
        self.gridLayout.addWidget(self.absTol_label, 3, 0, 1, 1)
        self.absTol = QtGui.QLineEdit(self.simulation)
        self.absTol.setEnabled(True)
        self.absTol.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhPreferNumbers)
        self.absTol.setObjectName(_fromUtf8("absTol"))
        self.gridLayout.addWidget(self.absTol, 3, 2, 1, 1)
        self.Hmin_label = QtGui.QLabel(self.simulation)
        self.Hmin_label.setObjectName(_fromUtf8("Hmin_label"))
        self.gridLayout.addWidget(self.Hmin_label, 1, 0, 1, 1)
        self.relTolLabel = QtGui.QLabel(self.simulation)
        self.relTolLabel.setObjectName(_fromUtf8("relTolLabel"))
        self.gridLayout.addWidget(self.relTolLabel, 4, 0, 1, 1)
        self.TOL_dq_i = QtGui.QLineEdit(self.simulation)
        self.TOL_dq_i.setEnabled(True)
        self.TOL_dq_i.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhPreferNumbers)
        self.TOL_dq_i.setObjectName(_fromUtf8("TOL_dq_i"))
        self.gridLayout.addWidget(self.TOL_dq_i, 5, 2, 1, 1)
        self.TOL_dq_i_label = QtGui.QLabel(self.simulation)
        self.TOL_dq_i_label.setObjectName(_fromUtf8("TOL_dq_i_label"))
        self.gridLayout.addWidget(self.TOL_dq_i_label, 5, 0, 1, 1)
        self.TOL_C = QtGui.QLineEdit(self.simulation)
        self.TOL_C.setEnabled(True)
        self.TOL_C.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhPreferNumbers)
        self.TOL_C.setObjectName(_fromUtf8("TOL_C"))
        self.gridLayout.addWidget(self.TOL_C, 6, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(0, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 1, 1, 1)
        self.tabWidget.addTab(self.simulation, _fromUtf8(""))
        self.animation = QtGui.QWidget()
        self.animation.setObjectName(_fromUtf8("animation"))
        self.gridLayout_2 = QtGui.QGridLayout(self.animation)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.updateDt_label = QtGui.QLabel(self.animation)
        self.updateDt_label.setObjectName(_fromUtf8("updateDt_label"))
        self.gridLayout_2.addWidget(self.updateDt_label, 1, 0, 1, 1)
        self.updateStep_lineEdit = QtGui.QLineEdit(self.animation)
        self.updateStep_lineEdit.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhPreferNumbers)
        self.updateStep_lineEdit.setObjectName(_fromUtf8("updateStep_lineEdit"))
        self.gridLayout_2.addWidget(self.updateStep_lineEdit, 2, 2, 1, 1)
        self.currentStep_label = QtGui.QLabel(self.animation)
        self.currentStep_label.setObjectName(_fromUtf8("currentStep_label"))
        self.gridLayout_2.addWidget(self.currentStep_label, 3, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(0, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 1, 1, 1, 1)
        self.playbackSpeed_doubleSpinBox = QtGui.QDoubleSpinBox(self.animation)
        self.playbackSpeed_doubleSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.playbackSpeed_doubleSpinBox.setKeyboardTracking(True)
        self.playbackSpeed_doubleSpinBox.setProperty("value", 1.0)
        self.playbackSpeed_doubleSpinBox.setObjectName(_fromUtf8("playbackSpeed_doubleSpinBox"))
        self.gridLayout_2.addWidget(self.playbackSpeed_doubleSpinBox, 5, 2, 1, 1)
        self.numberOfSteps_label = QtGui.QLabel(self.animation)
        self.numberOfSteps_label.setObjectName(_fromUtf8("numberOfSteps_label"))
        self.gridLayout_2.addWidget(self.numberOfSteps_label, 4, 0, 1, 1)
        self.updateDt_lineEdit = QtGui.QLineEdit(self.animation)
        self.updateDt_lineEdit.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhPreferNumbers)
        self.updateDt_lineEdit.setObjectName(_fromUtf8("updateDt_lineEdit"))
        self.gridLayout_2.addWidget(self.updateDt_lineEdit, 1, 2, 1, 1)
        self.updateDisplay_comboBox = QtGui.QComboBox(self.animation)
        self.updateDisplay_comboBox.setObjectName(_fromUtf8("updateDisplay_comboBox"))
        self.updateDisplay_comboBox.addItem(_fromUtf8(""))
        self.updateDisplay_comboBox.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.updateDisplay_comboBox, 0, 2, 1, 1)
        self.updateDisplay_label = QtGui.QLabel(self.animation)
        self.updateDisplay_label.setObjectName(_fromUtf8("updateDisplay_label"))
        self.gridLayout_2.addWidget(self.updateDisplay_label, 0, 0, 1, 1)
        self.currentStep_lineEdit = QtGui.QLineEdit(self.animation)
        self.currentStep_lineEdit.setEnabled(True)
        self.currentStep_lineEdit.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhPreferNumbers)
        self.currentStep_lineEdit.setObjectName(_fromUtf8("currentStep_lineEdit"))
        self.gridLayout_2.addWidget(self.currentStep_lineEdit, 3, 2, 1, 1)
        self.numberOfSteps_lineEdit = QtGui.QLineEdit(self.animation)
        self.numberOfSteps_lineEdit.setEnabled(False)
        self.numberOfSteps_lineEdit.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhPreferNumbers)
        self.numberOfSteps_lineEdit.setObjectName(_fromUtf8("numberOfSteps_lineEdit"))
        self.gridLayout_2.addWidget(self.numberOfSteps_lineEdit, 4, 2, 1, 1)
        self.playbackSpeed_label = QtGui.QLabel(self.animation)
        self.playbackSpeed_label.setObjectName(_fromUtf8("playbackSpeed_label"))
        self.gridLayout_2.addWidget(self.playbackSpeed_label, 5, 0, 1, 1)
        self.updateStep_label = QtGui.QLabel(self.animation)
        self.updateStep_label.setObjectName(_fromUtf8("updateStep_label"))
        self.gridLayout_2.addWidget(self.updateStep_label, 2, 0, 1, 1)
        self.tabWidget.addTab(self.animation, _fromUtf8(""))
        self.solution = QtGui.QWidget()
        self.solution.setObjectName(_fromUtf8("solution"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.solution)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.loadSolutionFileStatus = QtGui.QCheckBox(self.solution)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loadSolutionFileStatus.sizePolicy().hasHeightForWidth())
        self.loadSolutionFileStatus.setSizePolicy(sizePolicy)
        self.loadSolutionFileStatus.setMinimumSize(QtCore.QSize(200, 0))
        self.loadSolutionFileStatus.setObjectName(_fromUtf8("loadSolutionFileStatus"))
        self.verticalLayout_2.addWidget(self.loadSolutionFileStatus)
        self.restoreInitialConditionsStatus = QtGui.QCheckBox(self.solution)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.restoreInitialConditionsStatus.sizePolicy().hasHeightForWidth())
        self.restoreInitialConditionsStatus.setSizePolicy(sizePolicy)
        self.restoreInitialConditionsStatus.setMinimumSize(QtCore.QSize(200, 0))
        self.restoreInitialConditionsStatus.setObjectName(_fromUtf8("restoreInitialConditionsStatus"))
        self.verticalLayout_2.addWidget(self.restoreInitialConditionsStatus)
        spacerItem3 = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.tabWidget.addTab(self.solution, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        spacerItem4 = QtGui.QSpacerItem(10, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.info = QtGui.QGroupBox(Form)
        self.info.setObjectName(_fromUtf8("info"))
        self.gridLayout_4 = QtGui.QGridLayout(self.info)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.simulationStartTime_dateTimeEdit = QtGui.QDateTimeEdit(self.info)
        self.simulationStartTime_dateTimeEdit.setEnabled(False)
        self.simulationStartTime_dateTimeEdit.setAutoFillBackground(True)
        self.simulationStartTime_dateTimeEdit.setFrame(True)
        self.simulationStartTime_dateTimeEdit.setReadOnly(True)
        self.simulationStartTime_dateTimeEdit.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.simulationStartTime_dateTimeEdit.setObjectName(_fromUtf8("simulationStartTime_dateTimeEdit"))
        self.gridLayout_4.addWidget(self.simulationStartTime_dateTimeEdit, 0, 1, 1, 1)
        self.simulationTimeToFinish_timeEdit = QtGui.QTimeEdit(self.info)
        self.simulationTimeToFinish_timeEdit.setEnabled(False)
        self.simulationTimeToFinish_timeEdit.setAutoFillBackground(True)
        self.simulationTimeToFinish_timeEdit.setFrame(True)
        self.simulationTimeToFinish_timeEdit.setReadOnly(True)
        self.simulationTimeToFinish_timeEdit.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.simulationTimeToFinish_timeEdit.setObjectName(_fromUtf8("simulationTimeToFinish_timeEdit"))
        self.gridLayout_4.addWidget(self.simulationTimeToFinish_timeEdit, 4, 1, 1, 1)
        self.simulationElapsedTime_timeEdit = QtGui.QTimeEdit(self.info)
        self.simulationElapsedTime_timeEdit.setEnabled(False)
        self.simulationElapsedTime_timeEdit.setAutoFillBackground(True)
        self.simulationElapsedTime_timeEdit.setFrame(True)
        self.simulationElapsedTime_timeEdit.setReadOnly(True)
        self.simulationElapsedTime_timeEdit.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.simulationElapsedTime_timeEdit.setObjectName(_fromUtf8("simulationElapsedTime_timeEdit"))
        self.gridLayout_4.addWidget(self.simulationElapsedTime_timeEdit, 1, 1, 1, 1)
        self.ram_label = QtGui.QLabel(self.info)
        self.ram_label.setObjectName(_fromUtf8("ram_label"))
        self.gridLayout_4.addWidget(self.ram_label, 7, 0, 1, 1)
        self.cpu_label = QtGui.QLabel(self.info)
        self.cpu_label.setObjectName(_fromUtf8("cpu_label"))
        self.gridLayout_4.addWidget(self.cpu_label, 6, 0, 1, 1)
        self.loadedSolution_label = QtGui.QLabel(self.info)
        self.loadedSolution_label.setObjectName(_fromUtf8("loadedSolution_label"))
        self.gridLayout_4.addWidget(self.loadedSolution_label, 9, 0, 1, 1)
        self.solutionFileLoaded_display = QtGui.QLineEdit(self.info)
        self.solutionFileLoaded_display.setEnabled(False)
        self.solutionFileLoaded_display.setFrame(True)
        self.solutionFileLoaded_display.setObjectName(_fromUtf8("solutionFileLoaded_display"))
        self.gridLayout_4.addWidget(self.solutionFileLoaded_display, 11, 0, 1, 2)
        self.memory_doubleSpinBox = QtGui.QDoubleSpinBox(self.info)
        self.memory_doubleSpinBox.setEnabled(False)
        self.memory_doubleSpinBox.setAutoFillBackground(True)
        self.memory_doubleSpinBox.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.memory_doubleSpinBox.setWrapping(False)
        self.memory_doubleSpinBox.setFrame(True)
        self.memory_doubleSpinBox.setReadOnly(True)
        self.memory_doubleSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.memory_doubleSpinBox.setObjectName(_fromUtf8("memory_doubleSpinBox"))
        self.gridLayout_4.addWidget(self.memory_doubleSpinBox, 7, 1, 1, 1)
        self.cpu_doubleSpinBox = QtGui.QDoubleSpinBox(self.info)
        self.cpu_doubleSpinBox.setEnabled(False)
        self.cpu_doubleSpinBox.setAutoFillBackground(True)
        self.cpu_doubleSpinBox.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.cpu_doubleSpinBox.setFrame(True)
        self.cpu_doubleSpinBox.setReadOnly(True)
        self.cpu_doubleSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.cpu_doubleSpinBox.setObjectName(_fromUtf8("cpu_doubleSpinBox"))
        self.gridLayout_4.addWidget(self.cpu_doubleSpinBox, 6, 1, 1, 1)
        self.simulationStartTime_label = QtGui.QLabel(self.info)
        self.simulationStartTime_label.setObjectName(_fromUtf8("simulationStartTime_label"))
        self.gridLayout_4.addWidget(self.simulationStartTime_label, 0, 0, 1, 1)
        self.simulationElapsedTime_label = QtGui.QLabel(self.info)
        self.simulationElapsedTime_label.setObjectName(_fromUtf8("simulationElapsedTime_label"))
        self.gridLayout_4.addWidget(self.simulationElapsedTime_label, 1, 0, 1, 1)
        self.simulationTimeToFinish_label = QtGui.QLabel(self.info)
        self.simulationTimeToFinish_label.setObjectName(_fromUtf8("simulationTimeToFinish_label"))
        self.gridLayout_4.addWidget(self.simulationTimeToFinish_label, 4, 0, 1, 1)
        self.simulation_progressBar = QtGui.QProgressBar(self.info)
        self.simulation_progressBar.setEnabled(True)
        self.simulation_progressBar.setMaximum(100)
        self.simulation_progressBar.setProperty("value", 0)
        self.simulation_progressBar.setTextVisible(True)
        self.simulation_progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.simulation_progressBar.setInvertedAppearance(False)
        self.simulation_progressBar.setObjectName(_fromUtf8("simulation_progressBar"))
        self.gridLayout_4.addWidget(self.simulation_progressBar, 5, 0, 1, 2)
        self.verticalLayout.addWidget(self.info)
        self.animationControl = QtGui.QHBoxLayout()
        self.animationControl.setObjectName(_fromUtf8("animationControl"))
        self.backwardButton = QtGui.QToolButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backwardButton.sizePolicy().hasHeightForWidth())
        self.backwardButton.setSizePolicy(sizePolicy)
        self.backwardButton.setAccessibleName(_fromUtf8(""))
        self.backwardButton.setText(_fromUtf8(""))
        self.backwardButton.setArrowType(QtCore.Qt.LeftArrow)
        self.backwardButton.setObjectName(_fromUtf8("backwardButton"))
        self.animationControl.addWidget(self.backwardButton)
        self.playButton = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playButton.sizePolicy().hasHeightForWidth())
        self.playButton.setSizePolicy(sizePolicy)
        self.playButton.setObjectName(_fromUtf8("playButton"))
        self.animationControl.addWidget(self.playButton)
        self.forwardButton = QtGui.QToolButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.forwardButton.sizePolicy().hasHeightForWidth())
        self.forwardButton.setSizePolicy(sizePolicy)
        self.forwardButton.setText(_fromUtf8(""))
        self.forwardButton.setArrowType(QtCore.Qt.RightArrow)
        self.forwardButton.setObjectName(_fromUtf8("forwardButton"))
        self.animationControl.addWidget(self.forwardButton)
        self.verticalLayout.addLayout(self.animationControl)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Simulation Control", None))
        self.simulationStartButton.setText(_translate("Form", "Start", None))
        self.simulationStopButton.setText(_translate("Form", "Stop", None))
        self.simulationResetButton.setText(_translate("Form", "Reset", None))
        self.mainSettings_groupBox.setTitle(_translate("Form", "Main settings", None))
        self.label.setText(_translate("Form", "Analysis type", None))
        self.analysisTypeComboBox.setItemText(0, _translate("Form", "Kinematic", None))
        self.analysisTypeComboBox.setItemText(1, _translate("Form", "Dynamic", None))
        self.integrationMethod_Label.setText(_translate("Form", "Integration method", None))
        self.useBSM_checkBox.setText(_translate("Form", "Use BSM", None))
        self.endTime_label.setText(_translate("Form", "End time, s", None))
        self.stepsNumber_label.setText(_translate("Form", "Number of steps", None))
        self.Hmin_label_2.setText(_translate("Form", "Hcontact", None))
        self.Hmax_label.setText(_translate("Form", "Hmax", None))
        self.TOL_C_label.setText(_translate("Form", "TOL C(q, t)", None))
        self.absTol_label.setText(_translate("Form", "AbsTol", None))
        self.Hmin_label.setText(_translate("Form", "Hmin", None))
        self.relTolLabel.setText(_translate("Form", "RelTol", None))
        self.TOL_dq_i_label.setText(_translate("Form", "TOL dq_i", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.simulation), _translate("Form", "Simulation", None))
        self.updateDt_label.setText(_translate("Form", "dt", None))
        self.currentStep_label.setText(_translate("Form", "Current step ", None))
        self.numberOfSteps_label.setText(_translate("Form", "Number of steps", None))
        self.updateDisplay_comboBox.setItemText(0, _translate("Form", "dt", None))
        self.updateDisplay_comboBox.setItemText(1, _translate("Form", "step", None))
        self.updateDisplay_label.setText(_translate("Form", "Update display on every", None))
        self.playbackSpeed_label.setText(_translate("Form", "Playback speed", None))
        self.updateStep_label.setText(_translate("Form", "step", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.animation), _translate("Form", "Animation", None))
        self.loadSolutionFileStatus.setText(_translate("Form", "Load solution", None))
        self.restoreInitialConditionsStatus.setText(_translate("Form", "Restore initial conditions", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.solution), _translate("Form", "Solution", None))
        self.info.setTitle(_translate("Form", "Info", None))
        self.ram_label.setText(_translate("Form", "Memory, %", None))
        self.cpu_label.setText(_translate("Form", "CPU, %", None))
        self.loadedSolution_label.setText(_translate("Form", "Loaded solution", None))
        self.simulationStartTime_label.setText(_translate("Form", "Simulation started", None))
        self.simulationElapsedTime_label.setText(_translate("Form", "Elapsed time", None))
        self.simulationTimeToFinish_label.setText(_translate("Form", "Est. time to finish", None))
        self.playButton.setText(_translate("Form", "Play", None))
