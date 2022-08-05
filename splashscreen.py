# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\splashscreen.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import PyQt5
import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import sqlite3
from dashboard import Ui_Dashboard

class Ui_Splashscreen(object):
    def dashboardwindowshow(self):
        self.dashboardWindow = QtWidgets.QDialog()
        self.ui = Ui_Dashboard()
        self.ui.setupUi(self.dashboardWindow)
        Splashscreen.hide()
        self.dashboardWindow.show()

    def loginCheck(self):
        username = self.username_lineEdit.text()
        password = self.pass_lineEdit.text()

        connection = sqlite3.connect("parking.db")
        result = connection.execute("SELECT * FROM USERS WHERE USERNAME= ? AND PASSWORD = ?",(username,password))
        if(len(result.fetchall()) > 0):
            print("User found")
            self.dashboardwindowshow()
        else:
            print("User not found")

        connection.close()
    def insertData(self):
        fname = self.fname_lineEdit.text()
        lname = self.lname_lineEdit.text()
        username = self.uname_lineEdit.text()
        idnum = self.ID_lineEdit.text()
        contact = self.contact_lineEdit.text()
        email = self.email_lineEdit.text()
        password = self.password_lineEdit.text()

        conn = sqlite3.connect("parking.db")
        conn.execute("INSERT INTO USERS VALUES(?,?,?,?,?,?,?)", (fname, lname, idnum, contact, username, email, password))
        print('User Added')
        conn.commit()
        conn.close()

    def signupCheck(self):
        print("Signup Button clicked")
        self.insertData()
    

    def setupUi(self, Splashscreen):
        Splashscreen.setObjectName("Splashscreen")
        Splashscreen.resize(630, 485)
        Splashscreen.setStyleSheet("QToolTip\n"
"{\n"
"     border: 1px solid black;\n"
"     background-color: #ffa02f;\n"
"     padding: 1px;\n"
"     border-radius: 3px;\n"
"     opacity: 100;\n"
"}\n"
"\n"
"QWidget\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QWidget:item:hover\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #ca0619);\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background: transparent;\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    background: #444;\n"
"    border: 1px solid #000;\n"
"    background-color: QLinearGradient(\n"
"        x1:0, y1:0,\n"
"        x2:0, y2:1,\n"
"        stop:1 #212121,\n"
"        stop:0.4 #343434/*,\n"
"        stop:0.2 #343434,\n"
"        stop:0.1 #ffaa00*/\n"
"    );\n"
"    margin-bottom:-1px;\n"
"    padding-bottom:1px;\n"
"}\n"
"\n"
"QMenu\n"
"{\n"
"    border: 1px solid #000;\n"
"}\n"
"\n"
"QMenu::item\n"
"{\n"
"    padding: 2px 20px 2px 20px;\n"
"}\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:disabled\n"
"{\n"
"    color: #404040;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QAbstractItemView\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0.1 #646464, stop: 1 #5d5d5d);\n"
"}\n"
"\n"
"QWidget:focus\n"
"{\n"
"    /*border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);*/\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    font-size: 12px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"}\n"
"\n"
"QToolButton:hover\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #ca0619);\n"
"    color: #000000;\n"
"}\n"
"\n"
"QToolButton\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    font-size: 12px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"QToolButton:pressed\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #ffaa00;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QComboBox:hover,QPushButton:hover\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"    selection-background-color: #ffaa00;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    border: 2px solid darkgray;\n"
"    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 15px;\n"
"\n"
"     border-left-width: 0px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 3px;\n"
" }\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"     image: url(:/down_arrow.png);\n"
"}\n"
"\n"
"QGroupBox:focus\n"
"{\n"
"border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QTextEdit:focus\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"     border: 1px solid #222222;\n"
"     background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"     height: 7px;\n"
"     margin: 0px 16px 0 16px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"      subcontrol-position: right;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal, QScrollBar::left-arrow:horizontal\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"      width: 7px;\n"
"      margin: 16px 0 16px 0;\n"
"      border: 1px solid #222222;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      height: 14px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #d7801a, stop: 1 #ffa02f);\n"
"      height: 14px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QPlainTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QCheckBox:disabled\n"
"{\n"
"color: #414141;\n"
"}\n"
"\n"
"QDockWidget::title\n"
"{\n"
"    text-align: center;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button, QDockWidget::float-button\n"
"{\n"
"    text-align: center;\n"
"    spacing: 1px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button:hover, QDockWidget::float-button:hover\n"
"{\n"
"    background: #242424;\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed, QDockWidget::float-button:pressed\n"
"{\n"
"    padding: 1px -1px -1px 1px;\n"
"}\n"
"\n"
"QMainWindow::separator\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #4c4c4c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QMainWindow::separator:hover\n"
"{\n"
"\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #d7801a, stop:0.5 #b56c17 stop:1 #ffa02f);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QToolBar::handle\n"
"{\n"
"     spacing: 3px; /* spacing between items in the tool bar */\n"
"     background: url(:/images/handle.png);\n"
"}\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 2px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"QProgressBar\n"
"{\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: #d7801a;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #444;\n"
"    border-bottom-style: none;\n"
"    background-color: #323232;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 3px;\n"
"    padding-bottom: 2px;\n"
"    margin-right: -1px;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #444;\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabBar::tab:last\n"
"{\n"
"    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
"    border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:first:!selected\n"
"{\n"
" margin-left: 0px; /* the last selected tab has nothing to overlap with on the right */\n"
"\n"
"\n"
"    border-top-left-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    border-bottom-style: solid;\n"
"    margin-top: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:.4 #343434);\n"
"}\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    margin-bottom: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover\n"
"{\n"
"    /*border-top: 2px solid #ffaa00;\n"
"    padding-bottom: 3px;*/\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:0.4 #343434, stop:0.2 #343434, stop:0.1 #ffaa00);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked\n"
"{\n"
"    background-color: qradialgradient(\n"
"        cx: 0.5, cy: 0.5,\n"
"        fx: 0.5, fy: 0.5,\n"
"        radius: 1.0,\n"
"        stop: 0.25 #ffaa00,\n"
"        stop: 0.3 #323232\n"
"    );\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    width: 9px;\n"
"    height: 9px;\n"
"}\n"
"\n"
"QRadioButton::indicator\n"
"{\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover, QCheckBox::indicator:hover\n"
"{\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image:url(:/images/checkbox.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:disabled, QRadioButton::indicator:disabled\n"
"{\n"
"    border: 1px solid #444;\n"
"}")
        self.label = QtWidgets.QLabel(Splashscreen)
        self.label.setGeometry(QtCore.QRect(220, 20, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tabWidget = QtWidgets.QTabWidget(Splashscreen)
        self.tabWidget.setGeometry(QtCore.QRect(10, 80, 601, 391))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tabWidget.setFont(font)
        self.tabWidget.setIconSize(QtCore.QSize(16, 20))
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.login_tab = QtWidgets.QWidget()
        self.login_tab.setObjectName("login_tab")
        self.label_3 = QtWidgets.QLabel(self.login_tab)
        self.label_3.setGeometry(QtCore.QRect(220, 30, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Noto Sans CJK SC")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.login_btn = QtWidgets.QPushButton(self.login_tab)
        self.login_btn.setGeometry(QtCore.QRect(190, 260, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.login_btn.setFont(font)
        self.login_btn.setObjectName("login_btn")
        ##########button Event############
        self.login_btn.clicked.connect(self.loginCheck)
        ############################
        self.username_lineEdit = QtWidgets.QLineEdit(self.login_tab)
        self.username_lineEdit.setGeometry(QtCore.QRect(310, 110, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.username_lineEdit.setFont(font)
        self.username_lineEdit.setObjectName("username_lineEdit")
        self.username_label = QtWidgets.QLabel(self.login_tab)
        self.username_label.setGeometry(QtCore.QRect(90, 110, 161, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        self.username_label.setFont(font)
        self.username_label.setObjectName("username_label")
        self.pass_lineEdit = QtWidgets.QLineEdit(self.login_tab)
        self.pass_lineEdit.setGeometry(QtCore.QRect(310, 180, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.pass_lineEdit.setFont(font)
        self.pass_lineEdit.setObjectName("pass_lineEdit")
        self.pass_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)

        self.pass_label = QtWidgets.QLabel(self.login_tab)
        self.pass_label.setGeometry(QtCore.QRect(90, 180, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pass_label.setFont(font)
        self.pass_label.setObjectName("pass_label")
        self.tabWidget.addTab(self.login_tab, "")
        self.register_tab = QtWidgets.QWidget()
        self.register_tab.setObjectName("register_tab")
        self.label_2 = QtWidgets.QLabel(self.register_tab)
        self.label_2.setGeometry(QtCore.QRect(170, 10, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Noto Sans CJK SC")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.signup_btn = QtWidgets.QPushButton(self.register_tab)
        self.signup_btn.setGeometry(QtCore.QRect(260, 300, 151, 51))
        self.signup_btn.setObjectName("signup_btn")
        ##########button Event############
        self.signup_btn.clicked.connect(self.signupCheck)

        self.fname_lineEdit = QtWidgets.QLineEdit(self.register_tab)
        self.fname_lineEdit.setGeometry(QtCore.QRect(170, 50, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.fname_lineEdit.setFont(font)
        self.fname_lineEdit.setObjectName("fname_lineEdit")
        self.fname_label = QtWidgets.QLabel(self.register_tab)
        self.fname_label.setGeometry(QtCore.QRect(10, 50, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.fname_label.setFont(font)
        self.fname_label.setObjectName("fname_label")
        self.lname_lineEdit = QtWidgets.QLineEdit(self.register_tab)
        self.lname_lineEdit.setGeometry(QtCore.QRect(450, 50, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lname_lineEdit.setFont(font)
        self.lname_lineEdit.setObjectName("lname_lineEdit")
        self.lname_label = QtWidgets.QLabel(self.register_tab)
        self.lname_label.setGeometry(QtCore.QRect(330, 50, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lname_label.setFont(font)
        self.lname_label.setObjectName("lname_label")
        self.uname_label = QtWidgets.QLabel(self.register_tab)
        self.uname_label.setGeometry(QtCore.QRect(10, 150, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.uname_label.setFont(font)
        self.uname_label.setObjectName("uname_label")
        self.uname_lineEdit = QtWidgets.QLineEdit(self.register_tab)
        self.uname_lineEdit.setGeometry(QtCore.QRect(170, 150, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.uname_lineEdit.setFont(font)
        self.uname_lineEdit.setObjectName("uname_lineEdit")
        self.ID_label = QtWidgets.QLabel(self.register_tab)
        self.ID_label.setGeometry(QtCore.QRect(10, 100, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.ID_label.setFont(font)
        self.ID_label.setObjectName("ID_label")
        self.ID_lineEdit = QtWidgets.QLineEdit(self.register_tab)
        self.ID_lineEdit.setGeometry(QtCore.QRect(170, 100, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.ID_lineEdit.setFont(font)
        self.ID_lineEdit.setObjectName("ID_lineEdit")
        self.contact_label = QtWidgets.QLabel(self.register_tab)
        self.contact_label.setGeometry(QtCore.QRect(336, 100, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.contact_label.setFont(font)
        self.contact_label.setObjectName("contact_label")
        self.contact_lineEdit = QtWidgets.QLineEdit(self.register_tab)
        self.contact_lineEdit.setGeometry(QtCore.QRect(450, 100, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.contact_lineEdit.setFont(font)
        self.contact_lineEdit.setObjectName("contact_lineEdit")
        self.email_label = QtWidgets.QLabel(self.register_tab)
        self.email_label.setGeometry(QtCore.QRect(10, 200, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.email_label.setFont(font)
        self.email_label.setObjectName("email_label")
        self.email_lineEdit = QtWidgets.QLineEdit(self.register_tab)
        self.email_lineEdit.setGeometry(QtCore.QRect(170, 200, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.email_lineEdit.setFont(font)
        self.email_lineEdit.setObjectName("email_lineEdit")
        self.password_label = QtWidgets.QLabel(self.register_tab)
        self.password_label.setGeometry(QtCore.QRect(10, 250, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.password_label.setFont(font)
        self.password_label.setObjectName("password_label")
        self.password_lineEdit = QtWidgets.QLineEdit(self.register_tab)
        self.password_lineEdit.setGeometry(QtCore.QRect(170, 250, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.password_lineEdit.setFont(font)
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)

        self.tabWidget.addTab(self.register_tab, "")

        self.retranslateUi(Splashscreen)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Splashscreen)
        Splashscreen.setTabOrder(self.tabWidget, self.username_lineEdit)
        Splashscreen.setTabOrder(self.username_lineEdit, self.pass_lineEdit)
        Splashscreen.setTabOrder(self.pass_lineEdit, self.login_btn)
        Splashscreen.setTabOrder(self.login_btn, self.fname_lineEdit)
        Splashscreen.setTabOrder(self.fname_lineEdit, self.lname_lineEdit)
        Splashscreen.setTabOrder(self.lname_lineEdit, self.uname_lineEdit)
        Splashscreen.setTabOrder(self.uname_lineEdit, self.contact_lineEdit)
        Splashscreen.setTabOrder(self.contact_lineEdit, self.ID_lineEdit)
        Splashscreen.setTabOrder(self.ID_lineEdit, self.email_lineEdit)
        Splashscreen.setTabOrder(self.email_lineEdit, self.password_lineEdit)
        Splashscreen.setTabOrder(self.password_lineEdit, self.signup_btn)

    def retranslateUi(self, Splashscreen):
        _translate = QtCore.QCoreApplication.translate
        Splashscreen.setWindowTitle(_translate("Splashscreen", "Splashscreen"))
        self.label.setText(_translate("Splashscreen", "Welcome"))
        self.label_3.setText(_translate("Splashscreen", "Sign In "))
        self.login_btn.setText(_translate("Splashscreen", "Login"))
        self.username_lineEdit.setPlaceholderText(_translate("Splashscreen", "Type username here ...."))
        self.username_label.setText(_translate("Splashscreen", "USERNAME"))
        self.pass_lineEdit.setPlaceholderText(_translate("Splashscreen", "Type password here ...."))
        self.pass_label.setText(_translate("Splashscreen", "PASSWORD"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.login_tab), _translate("Splashscreen", "Signin"))
        self.label_2.setText(_translate("Splashscreen", "Create Account "))
        self.signup_btn.setText(_translate("Splashscreen", "Sign Up"))
        self.fname_label.setText(_translate("Splashscreen", "FIRST NAME"))
        self.lname_label.setText(_translate("Splashscreen", "LAST NAME"))
        self.uname_label.setText(_translate("Splashscreen", "USERNAME"))
        self.ID_label.setText(_translate("Splashscreen", "ID NUMBER"))
        self.contact_label.setText(_translate("Splashscreen", "CONTACT"))
        self.email_label.setText(_translate("Splashscreen", "EMAIL"))
        self.password_label.setText(_translate("Splashscreen", "PASSWORD"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.register_tab), _translate("Splashscreen", "Register"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Splashscreen = QtWidgets.QDialog()
    ui = Ui_Splashscreen()
    ui.setupUi(Splashscreen)
    Splashscreen.show()
    sys.exit(app.exec_())

