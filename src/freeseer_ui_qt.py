# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/freeseer_ui_qt.ui'
#
# Created: Fri Apr  2 00:13:04 2010
#      by: PyQt4 UI code generator 4.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_FreeseerMainWindow(object):
    def setupUi(self, FreeseerMainWindow):
        FreeseerMainWindow.setObjectName("FreeseerMainWindow")
        FreeseerMainWindow.resize(585, 509)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/freeseer/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FreeseerMainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(FreeseerMainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.main = QtGui.QWidget()
        self.main.setObjectName("main")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.main)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.recordButton = QtGui.QPushButton(self.main)
        self.recordButton.setMinimumSize(QtCore.QSize(0, 40))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/recordButton/record_red_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(":/recordButton/stop_red_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.recordButton.setIcon(icon1)
        self.recordButton.setCheckable(True)
        self.recordButton.setObjectName("recordButton")
        self.verticalLayout_2.addWidget(self.recordButton)
        self.talkListLayout = QtGui.QHBoxLayout()
        self.talkListLayout.setObjectName("talkListLayout")
        self.talkLabel = QtGui.QLabel(self.main)
        self.talkLabel.setMaximumSize(QtCore.QSize(40, 24))
        self.talkLabel.setObjectName("talkLabel")
        self.talkListLayout.addWidget(self.talkLabel)
        self.talkList = QtGui.QComboBox(self.main)
        self.talkList.setObjectName("talkList")
        self.talkListLayout.addWidget(self.talkList)
        self.verticalLayout_2.addLayout(self.talkListLayout)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.previewWidget = QtGui.QWidget(self.main)
        self.previewWidget.setObjectName("previewWidget")
        self.gridLayout.addWidget(self.previewWidget, 0, 0, 2, 1)
        self.audioFeedbackSlider = QtGui.QSlider(self.main)
        self.audioFeedbackSlider.setEnabled(False)
        self.audioFeedbackSlider.setOrientation(QtCore.Qt.Vertical)
        self.audioFeedbackSlider.setObjectName("audioFeedbackSlider")
        self.gridLayout.addWidget(self.audioFeedbackSlider, 0, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.audioFeedbackCheckbox = QtGui.QCheckBox(self.main)
        self.audioFeedbackCheckbox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.audioFeedbackCheckbox.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/headphones/headphones.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.audioFeedbackCheckbox.setIcon(icon2)
        self.audioFeedbackCheckbox.setObjectName("audioFeedbackCheckbox")
        self.verticalLayout_2.addWidget(self.audioFeedbackCheckbox)
        self.tabWidget.addTab(self.main, "")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.videoConfigBox = QtGui.QGroupBox(self.tab)
        self.videoConfigBox.setObjectName("videoConfigBox")
        self.horizontalLayout = QtGui.QHBoxLayout(self.videoConfigBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtGui.QWidget(self.videoConfigBox)
        self.widget.setObjectName("widget")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.localDesktopButton = QtGui.QRadioButton(self.widget)
        self.localDesktopButton.setChecked(True)
        self.localDesktopButton.setObjectName("localDesktopButton")
        self.verticalLayout_5.addWidget(self.localDesktopButton)
        self.hardwareButton = QtGui.QRadioButton(self.widget)
        self.hardwareButton.setObjectName("hardwareButton")
        self.verticalLayout_5.addWidget(self.hardwareButton)
        self.horizontalLayout.addWidget(self.widget)
        self.localDesktopBox = QtGui.QGroupBox(self.videoConfigBox)
        self.localDesktopBox.setMinimumSize(QtCore.QSize(0, 138))
        self.localDesktopBox.setObjectName("localDesktopBox")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.localDesktopBox)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.recordLocalDesktopButton = QtGui.QRadioButton(self.localDesktopBox)
        self.recordLocalDesktopButton.setChecked(True)
        self.recordLocalDesktopButton.setObjectName("recordLocalDesktopButton")
        self.verticalLayout_6.addWidget(self.recordLocalDesktopButton)
        self.recordLocalWindowButton = QtGui.QRadioButton(self.localDesktopBox)
        self.recordLocalWindowButton.setEnabled(False)
        self.recordLocalWindowButton.setObjectName("recordLocalWindowButton")
        self.verticalLayout_6.addWidget(self.recordLocalWindowButton)
        self.recordLocalAreaButton = QtGui.QRadioButton(self.localDesktopBox)
        self.recordLocalAreaButton.setEnabled(False)
        self.recordLocalAreaButton.setObjectName("recordLocalAreaButton")
        self.verticalLayout_6.addWidget(self.recordLocalAreaButton)
        self.horizontalLayout.addWidget(self.localDesktopBox)
        self.hardwareBox = QtGui.QGroupBox(self.videoConfigBox)
        self.hardwareBox.setMinimumSize(QtCore.QSize(0, 138))
        self.hardwareBox.setFlat(False)
        self.hardwareBox.setCheckable(False)
        self.hardwareBox.setChecked(False)
        self.hardwareBox.setObjectName("hardwareBox")
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.hardwareBox)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.usbsrcButton = QtGui.QRadioButton(self.hardwareBox)
        self.usbsrcButton.setChecked(True)
        self.usbsrcButton.setObjectName("usbsrcButton")
        self.verticalLayout_7.addWidget(self.usbsrcButton)
        self.firewiresrcButton = QtGui.QRadioButton(self.hardwareBox)
        self.firewiresrcButton.setObjectName("firewiresrcButton")
        self.verticalLayout_7.addWidget(self.firewiresrcButton)
        self.videoDeviceList = QtGui.QComboBox(self.hardwareBox)
        self.videoDeviceList.setObjectName("videoDeviceList")
        self.verticalLayout_7.addWidget(self.videoDeviceList)
        self.horizontalLayout.addWidget(self.hardwareBox)
        self.verticalLayout_8.addWidget(self.videoConfigBox)
        self.soundConfigBox = QtGui.QGroupBox(self.tab)
        self.soundConfigBox.setObjectName("soundConfigBox")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.soundConfigBox)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtGui.QLabel(self.soundConfigBox)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.audioSourceList = QtGui.QComboBox(self.soundConfigBox)
        self.audioSourceList.setObjectName("audioSourceList")
        self.horizontalLayout_3.addWidget(self.audioSourceList)
        self.verticalLayout_8.addWidget(self.soundConfigBox)
        self.groupBox_4 = QtGui.QGroupBox(self.tab)
        self.groupBox_4.setEnabled(False)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtGui.QLabel(self.groupBox_4)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.comboBox_3 = QtGui.QComboBox(self.groupBox_4)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.horizontalLayout_5.addWidget(self.comboBox_3)
        self.verticalLayout_8.addWidget(self.groupBox_4)
        self.tabWidget.addTab(self.tab, "")
        self.editTalksPage = QtGui.QWidget()
        self.editTalksPage.setObjectName("editTalksPage")
        self.verticalLayout = QtGui.QVBoxLayout(self.editTalksPage)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtGui.QGroupBox(self.editTalksPage)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.roomEdit = QtGui.QLineEdit(self.groupBox)
        self.roomEdit.setEnabled(False)
        self.roomEdit.setObjectName("roomEdit")
        self.gridLayout_2.addWidget(self.roomEdit, 1, 1, 1, 1)
        self.checkBox_2 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_2.addWidget(self.checkBox_2, 1, 2, 1, 1)
        self.titleEdit = QtGui.QLineEdit(self.groupBox)
        self.titleEdit.setObjectName("titleEdit")
        self.gridLayout_2.addWidget(self.titleEdit, 3, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)
        self.presenterEdit = QtGui.QLineEdit(self.groupBox)
        self.presenterEdit.setEnabled(False)
        self.presenterEdit.setObjectName("presenterEdit")
        self.gridLayout_2.addWidget(self.presenterEdit, 2, 1, 1, 1)
        self.checkBox_3 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout_2.addWidget(self.checkBox_3, 2, 2, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.addTalkButton = QtGui.QPushButton(self.groupBox)
        self.addTalkButton.setObjectName("addTalkButton")
        self.verticalLayout_3.addWidget(self.addTalkButton)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.editTalksPage)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.editTalkList = QtGui.QListWidget(self.groupBox_2)
        self.editTalkList.setObjectName("editTalkList")
        self.horizontalLayout_2.addWidget(self.editTalkList)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.removeTalkButton = QtGui.QPushButton(self.groupBox_2)
        self.removeTalkButton.setObjectName("removeTalkButton")
        self.verticalLayout_4.addWidget(self.removeTalkButton)
        self.saveButton = QtGui.QPushButton(self.groupBox_2)
        self.saveButton.setObjectName("saveButton")
        self.verticalLayout_4.addWidget(self.saveButton)
        self.resetButton = QtGui.QPushButton(self.groupBox_2)
        self.resetButton.setObjectName("resetButton")
        self.verticalLayout_4.addWidget(self.resetButton)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.tabWidget.addTab(self.editTalksPage, "")
        self.horizontalLayout_4.addWidget(self.tabWidget)
        FreeseerMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(FreeseerMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 585, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        FreeseerMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(FreeseerMainWindow)
        self.statusbar.setObjectName("statusbar")
        FreeseerMainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(FreeseerMainWindow)
        self.actionExit.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtGui.QAction(FreeseerMainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.talkLabel.setBuddy(self.talkList)
        self.label_5.setBuddy(self.audioSourceList)
        self.label_6.setBuddy(self.comboBox_3)
        self.label.setBuddy(self.roomEdit)
        self.label_3.setBuddy(self.titleEdit)
        self.label_4.setBuddy(self.presenterEdit)

        self.retranslateUi(FreeseerMainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.checkBox_2, QtCore.SIGNAL("toggled(bool)"), self.roomEdit.setEnabled)
        QtCore.QObject.connect(self.checkBox_3, QtCore.SIGNAL("toggled(bool)"), self.presenterEdit.setEnabled)
        QtCore.QObject.connect(self.localDesktopButton, QtCore.SIGNAL("toggled(bool)"), self.localDesktopBox.setVisible)
        QtCore.QObject.connect(self.hardwareButton, QtCore.SIGNAL("toggled(bool)"), self.hardwareBox.setVisible)
        QtCore.QMetaObject.connectSlotsByName(FreeseerMainWindow)
        FreeseerMainWindow.setTabOrder(self.roomEdit, self.presenterEdit)
        FreeseerMainWindow.setTabOrder(self.presenterEdit, self.titleEdit)
        FreeseerMainWindow.setTabOrder(self.titleEdit, self.addTalkButton)
        FreeseerMainWindow.setTabOrder(self.addTalkButton, self.editTalkList)
        FreeseerMainWindow.setTabOrder(self.editTalkList, self.checkBox_2)
        FreeseerMainWindow.setTabOrder(self.checkBox_2, self.checkBox_3)
        FreeseerMainWindow.setTabOrder(self.checkBox_3, self.recordButton)
        FreeseerMainWindow.setTabOrder(self.recordButton, self.talkList)
        FreeseerMainWindow.setTabOrder(self.talkList, self.audioFeedbackCheckbox)
        FreeseerMainWindow.setTabOrder(self.audioFeedbackCheckbox, self.audioFeedbackSlider)
        FreeseerMainWindow.setTabOrder(self.audioFeedbackSlider, self.tabWidget)

    def retranslateUi(self, FreeseerMainWindow):
        FreeseerMainWindow.setWindowTitle(QtGui.QApplication.translate("FreeseerMainWindow", "freeseer - video studio in a backpack", None, QtGui.QApplication.UnicodeUTF8))
        self.recordButton.setText(QtGui.QApplication.translate("FreeseerMainWindow", "Record", None, QtGui.QApplication.UnicodeUTF8))
        self.talkLabel.setText(QtGui.QApplication.translate("FreeseerMainWindow", "Title", None, QtGui.QApplication.UnicodeUTF8))
        self.talkList.setToolTip(QtGui.QApplication.translate("FreeseerMainWindow", "Title of the presentation being recorded.  For example \"Thanh Ha - Introduction to Freeseer\"", None, QtGui.QApplication.UnicodeUTF8))
        self.audioFeedbackCheckbox.setToolTip(QtGui.QApplication.translate("FreeseerMainWindow", "Enable audio feedback (plays back recording audio to speakers)", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.main), QtGui.QApplication.translate("FreeseerMainWindow", "main", None, QtGui.QApplication.UnicodeUTF8))
        self.videoConfigBox.setTitle(QtGui.QApplication.translate("FreeseerMainWindow", "Video Configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.localDesktopButton.setToolTip(QtGui.QApplication.translate("FreeseerMainWindow", "Select this option to record the local desktop. \n"
"Freeseer currently only supports recording the full desktop. \n"
"We plan to support window and area modes in future versions.", None, QtGui.QApplication.UnicodeUTF8))
        self.localDesktopButton.setText(QtGui.QApplication.translate("FreeseerMainWindow", "Local Desktop", None, QtGui.QApplication.UnicodeUTF8))
        self.hardwareButton.setToolTip(QtGui.QApplication.translate("FreeseerMainWindow", "Select hardware to record from either a usb device or firewire device.\n"
"\n"
"Freeseer finds USB devices by scanning /dev/videoX starting from index 0.\n"
"\n"
"Freeseer finds Firewire devices by scanning /dev/fwX starting from index 1.", None, QtGui.QApplication.UnicodeUTF8))
        self.hardwareButton.setText(QtGui.QApplication.translate("FreeseerMainWindow", "Hardware", None, QtGui.QApplication.UnicodeUTF8))
        self.localDesktopBox.setTitle(QtGui.QApplication.translate("FreeseerMainWindow", "Local Desktop", None, QtGui.QApplication.UnicodeUTF8))
        self.recordLocalDesktopButton.setText(QtGui.QApplication.translate("FreeseerMainWindow", "Desktop", None, QtGui.QApplication.UnicodeUTF8))
        self.recordLocalWindowButton.setToolTip(QtGui.QApplication.translate("FreeseerMainWindow", "This feature is currently not yet implemented.", None, QtGui.QApplication.UnicodeUTF8))
        self.recordLocalWindowButton.setText(QtGui.QApplication.translate("FreeseerMainWindow", "Window (Not Supported)", None, QtGui.QApplication.UnicodeUTF8))
        self.recordLocalAreaButton.setToolTip(QtGui.QApplication.translate("FreeseerMainWindow", "This feature is currently not yet implemented.", None, QtGui.QApplication.UnicodeUTF8))
        self.recordLocalAreaButton.setText(QtGui.QApplication.translate("FreeseerMainWindow", "Area (Not Supported)", None, QtGui.QApplication.UnicodeUTF8))
        self.hardwareBox.setTitle(QtGui.QApplication.translate("FreeseerMainWindow", "Hardware", None, QtGui.QApplication.UnicodeUTF8))
        self.usbsrcButton.setToolTip(QtGui.QApplication.translate("FreeseerMainWindow", "Use this option to record from a usb device.\n"
"\n"
"This option tries the v4l2src driver\n"
"and falls back to the v4lsrc driver if\n"
"v4l2src does not work.", None, QtGui.QApplication.UnicodeUTF8))
        self.usbsrcButton.setText(QtGui.QApplication.translate("FreeseerMainWindow", "usb device", None, QtGui.QApplication.UnicodeUTF8))
        self.firewiresrcButton.setToolTip(QtGui.QApplication.translate("FreeseerMainWindow", "Firewire mode uses dv1394src as the video driver.", None, QtGui.QApplication.UnicodeUTF8))
        self.firewiresrcButton.setText(QtGui.QApplication.translate("FreeseerMainWindow", "firewire device", None, QtGui.QApplication.UnicodeUTF8))
        self.videoDeviceList.setToolTip(QtGui.QApplication.translate("FreeseerMainWindow", "Select the video device to record from.", None, QtGui.QApplication.UnicodeUTF8))
        self.soundConfigBox.setTitle(QtGui.QApplication.translate("FreeseerMainWindow", "Sound Configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("FreeseerMainWindow", "Sound Source", None, QtGui.QApplication.UnicodeUTF8))
        self.audioSourceList.setToolTip(QtGui.QApplication.translate("FreeseerMainWindow", "Select the audio source to use for recording.", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setToolTip(QtGui.QApplication.translate("FreeseerMainWindow", "This feature has not yet been implemented.", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("FreeseerMainWindow", "Advanced (Not Supported)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("FreeseerMainWindow", "Video scale size", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_3.setItemText(0, QtGui.QApplication.translate("FreeseerMainWindow", "640x480", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_3.setItemText(1, QtGui.QApplication.translate("FreeseerMainWindow", "1024x768", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("FreeseerMainWindow", "configure", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("FreeseerMainWindow", "Add Title", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("FreeseerMainWindow", "Room", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("FreeseerMainWindow", "Title", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("FreeseerMainWindow", "Presenter", None, QtGui.QApplication.UnicodeUTF8))
        self.addTalkButton.setText(QtGui.QApplication.translate("FreeseerMainWindow", "add", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("FreeseerMainWindow", "Titles", None, QtGui.QApplication.UnicodeUTF8))
        self.editTalkList.setSortingEnabled(True)
        self.removeTalkButton.setText(QtGui.QApplication.translate("FreeseerMainWindow", "remove", None, QtGui.QApplication.UnicodeUTF8))
        self.saveButton.setText(QtGui.QApplication.translate("FreeseerMainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.resetButton.setText(QtGui.QApplication.translate("FreeseerMainWindow", "Reset", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.editTalksPage), QtGui.QApplication.translate("FreeseerMainWindow", "edit talks", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("FreeseerMainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("FreeseerMainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("FreeseerMainWindow", "&Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setShortcut(QtGui.QApplication.translate("FreeseerMainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("FreeseerMainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))

import resource_rc
