# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\dashboard.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

import cv2
import africastalking
import numpy as np
import os
import math
import random
import sqlite3
from time import gmtime, strftime
import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from vehicle import Ui_Vehicledetails
from admin import Ui_Admin

class Ui_Dashboard(QDialog):
    def __init__(self):
        super(Ui_Dashboard, self).__init__()
        self.numb=0
    def adminwindow(self):
        self.adminWindow = QtWidgets.QDialog()
        self.ui = Ui_Admin()
        self.ui.setupUi(self.adminWindow)
        #Login.hide()
        self.adminWindow.show()

    def admincheck(self):
        self.adminwindow()

    def addvehiclewindow(self):
        self.addvehicleWindow = QtWidgets.QDialog()
        self.ui = Ui_Vehicledetails()
        self.ui.setupUi(self.addvehicleWindow)
        #Login.hide()
        self.addvehicleWindow.show()

    def addvehiclecheck(self):
        self.addvehiclewindow()

    def loadClicked(self):
        print("Load clicked")
        fname,filter =QFileDialog.getOpenFileName(self,'Open File', 'C:\\', "Image Files(*.jpg)")
        if fname:
            self.image = cv2.imread(fname)
            self.displayImage()
            self.plate_label.clear()
            self.fname_label.clear()
            self.fname_label.clear()
            self.lname_label.clear()
            self.ID_label.clear()
            self.designation_label.clear()
            self.color_label.clear()
            self.model_label.clear()
            self.description_label.clear()
        else:
            print("Invalid image loaded")

    def detectClicked(self):
        #print(nist)
        he(self)
        self.plate_label.setText(self.numb)
        self.displayNewImage()
        connection = sqlite3.connect("parking.db")
        result = connection.execute("SELECT * FROM VEHICLES WHERE PLATE=?", (self.numb,))

        if(len(result.fetchall()) > 0):
            #self.description_label.setText("VEHICLE FOUND")
            rest = connection.execute("SELECT * FROM VEHICLES WHERE PLATE=?", (self.numb,))

            row = rest.fetchone()
            self.fname_label.setText(row[0])
            self.lname_label.setText(row[1])
            self.ID_label.setText(row[2])
            self.designation_label.setText(row[4])
            self.color_label.setText(row[6])
            self.model_label.setText(row[7])
            self.description_label.setText(row[8])
            n = strftime("%Y-%m-%d %H:%M:%S")
            africastalking.initialize(username='gyankellah', api_key='3edf5114ee4a53da50718e885f9df2c9788adb16b22373f5a58a039e59db501f')
            sms = africastalking.SMS
            Name = row[0]
            Plate= self.numb
            Contact = row[3]
            rest = sms.send(message='Dear ' + Name + ', your car '+Plate+' was scanned at Multimedia University of Kenya gate A at'+n, recipients=[Contact])

        else:
            self.description_label.setText("VEHICLE NOT FOUND")
            #self.showMessageBox("warning", "Invalid Username or password entered")
        x = strftime("%Y-%m-%d %H:%M:%S")
        connection.execute("INSERT INTO LOGS (`numberPlate`,`time`) VALUES(?,?)", (self.numb, x))
        connection.commit()
        print('Log Added')
        connection.close()


    def displayImage(self):
        qformat=QImage.Format_Indexed8
        re = cv2.resize(self.image, (511, 401))
        if len(re.shape)==3:#
            if(re.shape[2])==4:
                qformat=QImage.Format_RGBA8888
            else:
                qformat=QImage.Format_RGB888
        img=QImage(re, re.shape[1], re.shape[0], re.strides[0], qformat)
        #BGR > RGB
        img = img.rgbSwapped()
        self.imgLabel.setPixmap(QPixmap.fromImage(img))
        self.imgLabel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)

    def displayNewImage(self):
        qformat=QImage.Format_Indexed8
        re = cv2.resize(self.mascene, (511, 401))
        if len(re.shape)==3:#
            if(re.shape[2])==4:
                qformat=QImage.Format_RGBA8888
            else:
                qformat=QImage.Format_RGB888
        img=QImage(re, re.shape[1], re.shape[0], re.strides[0], qformat)
        #BGR > RGB
        img = img.rgbSwapped()
        self.imgLabel.setPixmap(QPixmap.fromImage(img))
        self.imgLabel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)

    def setupUi(self, Dashboard):
        Dashboard.setObjectName("Dashboard")
        Dashboard.resize(850, 530)
        Dashboard.setStyleSheet("QToolTip\n"
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
        self.imgLabel = QtWidgets.QLabel(Dashboard)
        self.imgLabel.setGeometry(QtCore.QRect(10, 80, 511, 401))
        self.imgLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.imgLabel.setText("")
        self.imgLabel.setObjectName("imgLabel")
        self.frame = QtWidgets.QFrame(Dashboard)
        self.frame.setGeometry(QtCore.QRect(540, 170, 291, 171))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(6, 10, 281, 151))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.fname_label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.fname_label.setFont(font)
        self.fname_label.setFrameShape(QtWidgets.QFrame.Box)
        self.fname_label.setText("")
        self.fname_label.setObjectName("fname_label")
        self.gridLayout.addWidget(self.fname_label, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.lname_label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lname_label.setFont(font)
        self.lname_label.setFrameShape(QtWidgets.QFrame.Box)
        self.lname_label.setText("")
        self.lname_label.setObjectName("lname_label")
        self.gridLayout.addWidget(self.lname_label, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.ID_label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ID_label.setFont(font)
        self.ID_label.setFrameShape(QtWidgets.QFrame.Box)
        self.ID_label.setText("")
        self.ID_label.setObjectName("ID_label")
        self.gridLayout.addWidget(self.ID_label, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.designation_label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.designation_label.setFont(font)
        self.designation_label.setFrameShape(QtWidgets.QFrame.Box)
        self.designation_label.setText("")
        self.designation_label.setObjectName("designation_label")
        self.gridLayout.addWidget(self.designation_label, 3, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(Dashboard)
        self.label_5.setGeometry(QtCore.QRect(540, 129, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.progressBar = QtWidgets.QProgressBar(Dashboard)
        self.progressBar.setGeometry(QtCore.QRect(10, 500, 511, 23))
        self.progressBar.setProperty("value", 99)
        self.progressBar.setObjectName("progressBar")
        self.layoutWidget1 = QtWidgets.QWidget(Dashboard)
        self.layoutWidget1.setGeometry(QtCore.QRect(539, 10, 291, 41))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.plate_label = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.plate_label.setFont(font)
        self.plate_label.setFrameShape(QtWidgets.QFrame.Box)
        self.plate_label.setText("")
        self.plate_label.setObjectName("plate_label")
        self.horizontalLayout_2.addWidget(self.plate_label)
        self.layoutWidget2 = QtWidgets.QWidget(Dashboard)
        self.layoutWidget2.setGeometry(QtCore.QRect(539, 360, 291, 31))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.description_label = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.description_label.setFont(font)
        self.description_label.setFrameShape(QtWidgets.QFrame.Box)
        self.description_label.setText("")
        self.description_label.setObjectName("description_label")
        self.horizontalLayout_3.addWidget(self.description_label)
        self.layoutWidget3 = QtWidgets.QWidget(Dashboard)
        self.layoutWidget3.setGeometry(QtCore.QRect(540, 80, 291, 31))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_5.addWidget(self.label_9)
        self.color_label = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.color_label.setFont(font)
        self.color_label.setFrameShape(QtWidgets.QFrame.Box)
        self.color_label.setText("")
        self.color_label.setObjectName("color_label")
        self.horizontalLayout_5.addWidget(self.color_label)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_5.addWidget(self.label_10)
        self.model_label = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.model_label.setFont(font)
        self.model_label.setFrameShape(QtWidgets.QFrame.Box)
        self.model_label.setText("")
        self.model_label.setObjectName("model_label")
        self.horizontalLayout_5.addWidget(self.model_label)
        self.splitter_2 = QtWidgets.QSplitter(Dashboard)
        self.splitter_2.setGeometry(QtCore.QRect(540, 416, 291, 41))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.newvehicle_btn = QtWidgets.QPushButton(self.splitter_2)
        self.newvehicle_btn.setObjectName("newvehicle_btn")
        #########
        self.newvehicle_btn.clicked.connect(self.addvehiclecheck)
        ###############
        self.admin_btn = QtWidgets.QPushButton(self.splitter_2)
        self.admin_btn.setObjectName("admin_btn")
        #########
        self.admin_btn.clicked.connect(self.admincheck)
        ##############
        self.detectButton = QtWidgets.QToolButton(Dashboard)
        self.detectButton.setGeometry(QtCore.QRect(420, 10, 91, 61))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("find.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.detectButton.setIcon(icon1)
        self.detectButton.setIconSize(QtCore.QSize(32, 32))
        self.detectButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.detectButton.setObjectName("detectButton")
        #########
        self.detectButton.clicked.connect(self.detectClicked)
        self.loadButton = QtWidgets.QToolButton(Dashboard)
        self.loadButton.setGeometry(QtCore.QRect(20, 10, 91, 61))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("cctv.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.loadButton.setIcon(icon2)
        self.loadButton.setIconSize(QtCore.QSize(32, 32))
        self.loadButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.loadButton.setObjectName("loadButton")
        #########
        self.loadButton.clicked.connect(self.loadClicked)
        self.detectButton.raise_()
        self.loadButton.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.splitter_2.raise_()
        self.frame.raise_()
        self.imgLabel.raise_()
        self.layoutWidget.raise_()
        self.label_5.raise_()
        self.progressBar.raise_()
        self.retranslateUi(Dashboard)
        QtCore.QMetaObject.connectSlotsByName(Dashboard)

    def retranslateUi(self, Dashboard):
        _translate = QtCore.QCoreApplication.translate
        Dashboard.setWindowTitle(_translate("Dashboard", "Dashboard"))
        self.label_2.setText(_translate("Dashboard", "First Name"))
        self.label_3.setText(_translate("Dashboard", "Last Name"))
        self.label_6.setText(_translate("Dashboard", "ID number"))
        self.label_4.setText(_translate("Dashboard", "Designation"))
        self.label_5.setText(_translate("Dashboard", "Vehicle Owner Details"))
        self.label.setText(_translate("Dashboard", "Detected Number Plate"))
        self.label_7.setText(_translate("Dashboard", "Approval status"))
        self.label_9.setText(_translate("Dashboard", "COLOR"))
        self.label_10.setText(_translate("Dashboard", "MODEL"))
        self.newvehicle_btn.setText(_translate("Dashboard", "ADD NEW VEHICLE"))
        self.admin_btn.setText(_translate("Dashboard", "ADMIN PANEL"))
        #self.toolButton.setText(_translate("Dashboard", "logout"))
        self.detectButton.setText(_translate("Dashboard", "Detect"))
        self.loadButton.setText(_translate("Dashboard", "Capture Image"))
def he(self):

    # module level variables ##########################################################################
    SCALAR_WHITE = (0.0, 0.0, 0.0)
    SCALAR_BLACK = (255.0, 255.0, 255.0)
    SCALAR_YELLOW = (0.0, 255.0, 255.0)
    SCALAR_GREEN = (0.0, 255.0, 0.0)
    SCALAR_RED = (0.0, 0.0, 255.0)
    PLATE_WIDTH_PADDING_FACTOR = 1.3
    PLATE_HEIGHT_PADDING_FACTOR = 1.5

    GAUSSIAN_SMOOTH_FILTER_SIZE = (5, 5)
    ADAPTIVE_THRESH_BLOCK_SIZE = 19
    ADAPTIVE_THRESH_WEIGHT = 9

    kNearest = cv2.ml.KNearest_create()

            # constants for checkIfPossibleChar, this checks one possible char only (does not compare to another char)
    MIN_PIXEL_WIDTH = 2
    MIN_PIXEL_HEIGHT = 8

    MIN_ASPECT_RATIO = 0.25
    MAX_ASPECT_RATIO = 1.0

    MIN_PIXEL_AREA = 80

            # constants for comparing two chars
    MIN_DIAG_SIZE_MULTIPLE_AWAY = 0.3
    MAX_DIAG_SIZE_MULTIPLE_AWAY = 5.0

    MAX_CHANGE_IN_AREA = 0.5

    MAX_CHANGE_IN_WIDTH = 0.8
    MAX_CHANGE_IN_HEIGHT = 0.2

    MAX_ANGLE_BETWEEN_CHARS = 12.0

            # other constants
    MIN_NUMBER_OF_MATCHING_CHARS = 3

    RESIZED_CHAR_IMAGE_WIDTH = 20
    RESIZED_CHAR_IMAGE_HEIGHT = 30

    MIN_CONTOUR_AREA = 100

    showSteps = False

    ###################################################################################################
    def ngori(self):

        blnKNNTrainingSuccessful = loadKNNDataAndTrainKNN()         # attempt KNN training

        if blnKNNTrainingSuccessful == False:                               # if KNN training was not successful
            print ("\nerror: KNN traning was not successful\n")               # show error message
            return                                                          # and exit program
        # end if

        imgOriginalScene  = self.image               # open image

        if imgOriginalScene is None:                            # if image was not read successfully
            print ("\nerror: image not read from file \n\n")      # print error message to std out
            os.system("pause")                                  # pause so user can see error message
            return                                              # and exit program
        # end if

        listOfPossiblePlates = detectPlatesInScene(imgOriginalScene)           # detect plates

        listOfPossiblePlates = detectCharsInPlates(listOfPossiblePlates)        # detect chars in plates

        #cv2.imshow("imgOriginalScene", imgOriginalScene)            # show scene image

        if len(listOfPossiblePlates) == 0:                          # if no plates were found
            print ("\nno license plates were detected\n")             # inform user no plates were found
        else:                                                       # else
                    # if we get in here list of possible plates has at leat one plate

                    # sort the list of possible plates in DESCENDING order (most number of chars to least number of chars)
            listOfPossiblePlates.sort(key = lambda possiblePlate: len(possiblePlate.strChars), reverse = True)

                    # suppose the plate with the most recognized chars (the first plate in sorted by string length descending order) is the actual plate
            licPlate = listOfPossiblePlates[0]

            #cv2.imshow("imgPlate", licPlate.imgPlate)           # show crop of plate and threshold of plate
            #cv2.imshow("imgThresh", licPlate.imgThresh)

            if len(licPlate.strChars) == 0:                     # if no chars were found in the plate
                print ("\nno characters were detected\n\n")       # show message
                return                                          # and exit program
            # end if

            drawRedRectangleAroundPlate(imgOriginalScene, licPlate)             # draw red rectangle around plate

            #print ("\nlicense plate read from image = " + licPlate.strChars + "\n")       # write license plate text to std out
            #print ("----------------------------------------")
            self.numb = licPlate.strChars
            writeLicensePlateCharsOnImage(imgOriginalScene, licPlate)           # write license plate text on the image

            #cv2.imshow("imgOriginalScene", imgOriginalScene)                # re-show scene image
            self.mascene = imgOriginalScene
            cv2.imwrite("imgOriginalScene.png", imgOriginalScene)           # write image out to file

        # end if else

        cv2.waitKey(0)					# hold windows open until user presses a key

        return
    # end main


    ###################################################################################################
    def drawRedRectangleAroundPlate(imgOriginalScene, licPlate):

        p2fRectPoints = cv2.boxPoints(licPlate.rrLocationOfPlateInScene)            # get 4 vertices of rotated rect

        cv2.line(imgOriginalScene, tuple(p2fRectPoints[0]), tuple(p2fRectPoints[1]), SCALAR_RED, 2)         # draw 4 red lines
        cv2.line(imgOriginalScene, tuple(p2fRectPoints[1]), tuple(p2fRectPoints[2]), SCALAR_RED, 2)
        cv2.line(imgOriginalScene, tuple(p2fRectPoints[2]), tuple(p2fRectPoints[3]), SCALAR_RED, 2)
        cv2.line(imgOriginalScene, tuple(p2fRectPoints[3]), tuple(p2fRectPoints[0]), SCALAR_RED, 2)
    # end function

    ###################################################################################################
    def writeLicensePlateCharsOnImage(imgOriginalScene, licPlate):
        ptCenterOfTextAreaX = 0                             # this will be the center of the area the text will be written to
        ptCenterOfTextAreaY = 0

        ptLowerLeftTextOriginX = 0                          # this will be the bottom left of the area that the text will be written to
        ptLowerLeftTextOriginY = 0

        sceneHeight, sceneWidth, sceneNumChannels = imgOriginalScene.shape
        plateHeight, plateWidth, plateNumChannels = licPlate.imgPlate.shape

        intFontFace = cv2.FONT_HERSHEY_SIMPLEX                      # choose a plain jane font
        fltFontScale = float(plateHeight) / 30.0                    # base font scale on height of plate area
        intFontThickness = int(round(fltFontScale * 1.5))           # base font thickness on font scale

        textSize, baseline = cv2.getTextSize(licPlate.strChars, intFontFace, fltFontScale, intFontThickness)        # call getTextSize

                # unpack roatated rect into center point, width and height, and angle
        ( (intPlateCenterX, intPlateCenterY), (intPlateWidth, intPlateHeight), fltCorrectionAngleInDeg ) = licPlate.rrLocationOfPlateInScene

        intPlateCenterX = int(intPlateCenterX)              # make sure center is an integer
        intPlateCenterY = int(intPlateCenterY)

        ptCenterOfTextAreaX = int(intPlateCenterX)         # the horizontal location of the text area is the same as the plate

        if intPlateCenterY < (sceneHeight * 0.75):                                                  # if the license plate is in the upper 3/4 of the image
            ptCenterOfTextAreaY = int(round(intPlateCenterY)) + int(round(plateHeight * 1.6))      # write the chars in below the plate
        else:                                                                                       # else if the license plate is in the lower 1/4 of the image
            ptCenterOfTextAreaY = int(round(intPlateCenterY)) - int(round(plateHeight * 1.6))      # write the chars in above the plate
        # end if

        textSizeWidth, textSizeHeight = textSize                # unpack text size width and height

        ptLowerLeftTextOriginX = int(ptCenterOfTextAreaX - (textSizeWidth / 2))           # calculate the lower left origin of the text area
        ptLowerLeftTextOriginY = int(ptCenterOfTextAreaY + (textSizeHeight / 2))          # based on the text area center, width, and height

                # write the text on the image
        cv2.putText(imgOriginalScene, licPlate.strChars, (ptLowerLeftTextOriginX, ptLowerLeftTextOriginY), intFontFace, fltFontScale, SCALAR_YELLOW, intFontThickness)
    # end function

    ###################################################################################################

    ###################################################################################################
    def detectPlatesInScene(imgOriginalScene):
        listOfPossiblePlates = []                   # this will be the return value

        height, width, numChannels = imgOriginalScene.shape

        imgGrayscaleScene = np.zeros((height, width, 1), np.uint8)
        imgThreshScene = np.zeros((height, width, 1), np.uint8)
        imgContours = np.zeros((height, width, 3), np.uint8)

        #cv2.destroyAllWindows()

        if showSteps == True: # show steps #######################################################
            cv2.imshow("0", imgOriginalScene)
        # end if # show steps #########################################################################

        imgGrayscaleScene, imgThreshScene = preprocess(imgOriginalScene)         # preprocess to get grayscale and threshold images

        if showSteps == True: # show steps #######################################################
            cv2.imshow("1a", imgGrayscaleScene)
            cv2.imshow("1b", imgThreshScene)
        # end if # show steps #########################################################################

                # find all possible chars in the scene,
                # this function first finds all contours, then only includes contours that could be chars (without comparison to other chars yet)
        listOfPossibleCharsInScene = findPossibleCharsInScene(imgThreshScene)

        if showSteps == True: # show steps #######################################################
            print ("step 2 - len(listOfPossibleCharsInScene) = " + str(len(listOfPossibleCharsInScene)))         # 131 with MCLRNF1 image

            imgContours = np.zeros((height, width, 3), np.uint8)

            contours = []

            for possibleChar in listOfPossibleCharsInScene:
                contours.append(possibleChar.contour)
            # end for

            cv2.drawContours(imgContours, contours, -1,SCALAR_WHITE)
            cv2.imshow("2b", imgContours)
        # end if # show steps #########################################################################

                # given a list of all possible chars, find groups of matching chars
                # in the next steps each group of matching chars will attempt to be recognized as a plate
        listOfListsOfMatchingCharsInScene = findListOfListsOfMatchingChars(listOfPossibleCharsInScene)

        if showSteps == True: # show steps #######################################################
            print ("step 3 - listOfListsOfMatchingCharsInScene.Count = " + str(len(listOfListsOfMatchingCharsInScene)))    # 13 with MCLRNF1 image

            imgContours = np.zeros((height, width, 3), np.uint8)

            for listOfMatchingChars in listOfListsOfMatchingCharsInScene:
                intRandomBlue = random.randint(0, 255)
                intRandomGreen = random.randint(0, 255)
                intRandomRed = random.randint(0, 255)

                contours = []

                for matchingChar in listOfMatchingChars:
                    contours.append(matchingChar.contour)
                # end for

                cv2.drawContours(imgContours, contours, -1, (intRandomBlue, intRandomGreen, intRandomRed))
            # end for

            cv2.imshow("3", imgContours)
        # end if # show steps #########################################################################

        for listOfMatchingChars in listOfListsOfMatchingCharsInScene:                   # for each group of matching chars
            possiblePlate = extractPlate(imgOriginalScene, listOfMatchingChars)         # attempt to extract plate

            if possiblePlate.imgPlate is not None:                          # if plate was found
                listOfPossiblePlates.append(possiblePlate)                  # add to list of possible plates
            # end if
        # end for

        #print ("\n" + str(len(listOfPossiblePlates)) + " possible plates found")          # 13 with MCLRNF1 image

        if showSteps == True: # show steps #######################################################
            print ("\n")
            cv2.imshow("4a", imgContours)

            for i in range(0, len(listOfPossiblePlates)):
                p2fRectPoints = cv2.boxPoints(listOfPossiblePlates[i].rrLocationOfPlateInScene)

                cv2.line(imgContours, tuple(p2fRectPoints[0]), tuple(p2fRectPoints[1]), SCALAR_RED, 2)
                cv2.line(imgContours, tuple(p2fRectPoints[1]), tuple(p2fRectPoints[2]), SCALAR_RED, 2)
                cv2.line(imgContours, tuple(p2fRectPoints[2]), tuple(p2fRectPoints[3]), SCALAR_RED, 2)
                cv2.line(imgContours, tuple(p2fRectPoints[3]), tuple(p2fRectPoints[0]), SCALAR_RED, 2)

                cv2.imshow("4a", imgContours)

                print ("possible plate " + str(i) + ", click on any image and press a key to continue . . .")

                cv2.imshow("4b", listOfPossiblePlates[i].imgPlate)
                cv2.waitKey(0)
            # end for

            print ("\nplate detection complete, click on any image and press a key to begin char recognition . . .\n")
            cv2.waitKey(0)
        # end if # show steps #########################################################################

        return listOfPossiblePlates
    # end function

    ###################################################################################################
    def findPossibleCharsInScene(imgThresh):
        listOfPossibleChars = []                # this will be the return value

        intCountOfPossibleChars = 0

        imgThreshCopy = imgThresh.copy()

        contours, npaHierarchy = cv2.findContours(imgThreshCopy, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)   # find all contours

        height, width = imgThresh.shape
        imgContours = np.zeros((height, width, 3), np.uint8)

        for i in range(0, len(contours)):                       # for each contour

            if showSteps == True: # show steps ###################################################
                cv2.drawContours(imgContours, contours, i, SCALAR_WHITE)
            # end if # show steps #####################################################################

            possibleChar = PossibleChar(contours[i])

            if checkIfPossibleChar(possibleChar):                   # if contour is a possible char, note this does not compare to other chars (yet) . . .
                intCountOfPossibleChars = intCountOfPossibleChars + 1           # increment count of possible chars
                listOfPossibleChars.append(possibleChar)                        # and add to list of possible chars
            # end if
        # end for

        if showSteps == True: # show steps #######################################################
            print ("\nstep 2 - len(contours) = " + str(len(contours)))                       # 2362 with MCLRNF1 image
            print ("step 2 - intCountOfPossibleChars = " + str(intCountOfPossibleChars))       # 131 with MCLRNF1 image
            cv2.imshow("2a", imgContours)
        # end if # show steps #########################################################################

        return listOfPossibleChars
    # end function


    ###################################################################################################
    def extractPlate(imgOriginal, listOfMatchingChars):
        possiblePlate = PossiblePlate()           # this will be the return value

        listOfMatchingChars.sort(key = lambda matchingChar: matchingChar.intCenterX)        # sort chars from left to right based on x position

                # calculate the center point of the plate
        fltPlateCenterX = (listOfMatchingChars[0].intCenterX + listOfMatchingChars[len(listOfMatchingChars) - 1].intCenterX) / 2.0
        fltPlateCenterY = (listOfMatchingChars[0].intCenterY + listOfMatchingChars[len(listOfMatchingChars) - 1].intCenterY) / 2.0

        ptPlateCenter = fltPlateCenterX, fltPlateCenterY

                # calculate plate width and height
        intPlateWidth = int((listOfMatchingChars[len(listOfMatchingChars) - 1].intBoundingRectX + listOfMatchingChars[len(listOfMatchingChars) - 1].intBoundingRectWidth - listOfMatchingChars[0].intBoundingRectX) * PLATE_WIDTH_PADDING_FACTOR)

        intTotalOfCharHeights = 0

        for matchingChar in listOfMatchingChars:
            intTotalOfCharHeights = intTotalOfCharHeights + matchingChar.intBoundingRectHeight
        # end for

        fltAverageCharHeight = intTotalOfCharHeights / len(listOfMatchingChars)

        intPlateHeight = int(fltAverageCharHeight * PLATE_HEIGHT_PADDING_FACTOR)

                # calculate correction angle of plate region
        fltOpposite = listOfMatchingChars[len(listOfMatchingChars) - 1].intCenterY - listOfMatchingChars[0].intCenterY
        fltHypotenuse = distanceBetweenChars(listOfMatchingChars[0], listOfMatchingChars[len(listOfMatchingChars) - 1])
        fltCorrectionAngleInRad = math.asin(fltOpposite / fltHypotenuse)
        fltCorrectionAngleInDeg = fltCorrectionAngleInRad * (180.0 / math.pi)

                # pack plate region center point, width and height, and correction angle into rotated rect member variable of plate
        possiblePlate.rrLocationOfPlateInScene = ( tuple(ptPlateCenter), (intPlateWidth, intPlateHeight), fltCorrectionAngleInDeg )

                # final steps are to perform the actual rotation

                # get the rotation matrix for our calculated correction angle
        rotationMatrix = cv2.getRotationMatrix2D(tuple(ptPlateCenter), fltCorrectionAngleInDeg, 1.0)

        height, width, numChannels = imgOriginal.shape      # unpack original image width and height

        imgRotated = cv2.warpAffine(imgOriginal, rotationMatrix, (width, height))       # rotate the entire image

        imgCropped = cv2.getRectSubPix(imgRotated, (intPlateWidth, intPlateHeight), tuple(ptPlateCenter))

        possiblePlate.imgPlate = imgCropped         # copy the cropped plate image into the applicable member variable of the possible plate

        return possiblePlate
    # end function


    ###################################################################################################
    def loadKNNDataAndTrainKNN():
        allContoursWithData = []                # declare empty lists,
        validContoursWithData = []              # we will fill these shortly

        try:
            npaClassifications = np.loadtxt("classifications.txt", np.float32)                  # read in training classifications
        except:                                                                                 # if file could not be opened
            print ("error, unable to open classifications.txt, exiting program\n")                # show error message
            os.system("pause")
            return False                                                                        # and return False
        # end try

        try:
            npaFlattenedImages = np.loadtxt("flattened_images.txt", np.float32)                 # read in training images
        except:                                                                                 # if file could not be opened
            print ("error, unable to open flattened_images.txt, exiting program\n")               # show error message
            os.system("pause")
            return False                                                                        # and return False
        # end try

        npaClassifications = npaClassifications.reshape((npaClassifications.size, 1))       # reshape numpy array to 1d, necessary to pass to call to train

        kNearest.setDefaultK(1)                                                             # set default K to 1

        kNearest.train(npaFlattenedImages, cv2.ml.ROW_SAMPLE, npaClassifications)           # train KNN object

        return True                             # if we got here training was successful so return true
    # end function

    ###################################################################################################
    def detectCharsInPlates(listOfPossiblePlates):
        intPlateCounter = 0
        imgContours = None
        contours = []

        if len(listOfPossiblePlates) == 0:          # if list of possible plates is empty
            return listOfPossiblePlates             # return
        # end if

                # at this point we can be sure the list of possible plates has at least one plate

        for possiblePlate in listOfPossiblePlates:          # for each possible plate, this is a big for loop that takes up most of the function

            possiblePlate.imgGrayscale, possiblePlate.imgThresh = preprocess(possiblePlate.imgPlate)     # preprocess to get grayscale and threshold images

            if showSteps == True: # show steps ###################################################
                cv2.imshow("5a", possiblePlate.imgPlate)
                cv2.imshow("5b", possiblePlate.imgGrayscale)
                cv2.imshow("5c", possiblePlate.imgThresh)
            # end if # show steps #####################################################################

                    # increase size of plate image for easier viewing and char detection
            possiblePlate.imgThresh = cv2.resize(possiblePlate.imgThresh, (0, 0), fx = 1.6, fy = 1.6)

                    # threshold again to eliminate any gray areas
            thresholdValue, possiblePlate.imgThresh = cv2.threshold(possiblePlate.imgThresh, 0.0, 255.0, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

            if showSteps == True: # show steps ###################################################
                cv2.imshow("5d", possiblePlate.imgThresh)
            # end if # show steps #####################################################################

                    # find all possible chars in the plate,
                    # this function first finds all contours, then only includes contours that could be chars (without comparison to other chars yet)
            listOfPossibleCharsInPlate = findPossibleCharsInPlate(possiblePlate.imgGrayscale, possiblePlate.imgThresh)

            if showSteps == True: # show steps ###################################################
                height, width, numChannels = possiblePlate.imgPlate.shape
                imgContours = np.zeros((height, width, 3), np.uint8)
                del contours[:]                                         # clear the contours list

                for possibleChar in listOfPossibleCharsInPlate:
                    contours.append(possibleChar.contour)
                # end for

                cv2.drawContours(imgContours, contours, -1, SCALAR_WHITE)

                cv2.imshow("6", imgContours)
            # end if # show steps #####################################################################

                    # given a list of all possible chars, find groups of matching chars within the plate
            listOfListsOfMatchingCharsInPlate = findListOfListsOfMatchingChars(listOfPossibleCharsInPlate)

            if showSteps == True: # show steps ###################################################
                imgContours = np.zeros((height, width, 3), np.uint8)
                del contours[:]

                for listOfMatchingChars in listOfListsOfMatchingCharsInPlate:
                    intRandomBlue = random.randint(0, 255)
                    intRandomGreen = random.randint(0, 255)
                    intRandomRed = random.randint(0, 255)

                    for matchingChar in listOfMatchingChars:
                        contours.append(matchingChar.contour)
                    # end for
                    cv2.drawContours(imgContours, contours, -1, (intRandomBlue, intRandomGreen, intRandomRed))
                # end for
                cv2.imshow("7", imgContours)
            # end if # show steps #####################################################################

            if (len(listOfListsOfMatchingCharsInPlate) == 0):			# if no groups of matching chars were found in the plate

                if showSteps == True: # show steps ###############################################
                    print ("chars found in plate number " + str(intPlateCounter) + " = (none), click on any image and press a key to continue . . .")
                    intPlateCounter = intPlateCounter + 1
                    cv2.destroyWindow("8")
                    cv2.destroyWindow("9")
                    cv2.destroyWindow("10")
                    cv2.waitKey(0)
                # end if # show steps #################################################################

                possiblePlate.strChars = ""
                continue						# go back to top of for loop
            # end if

            for i in range(0, len(listOfListsOfMatchingCharsInPlate)):                              # within each list of matching chars
                listOfListsOfMatchingCharsInPlate[i].sort(key = lambda matchingChar: matchingChar.intCenterX)        # sort chars from left to right
                listOfListsOfMatchingCharsInPlate[i] = removeInnerOverlappingChars(listOfListsOfMatchingCharsInPlate[i])              # and remove inner overlapping chars
            # end for

            if showSteps == True: # show steps ###################################################
                imgContours = np.zeros((height, width, 3), np.uint8)

                for listOfMatchingChars in listOfListsOfMatchingCharsInPlate:
                    intRandomBlue = random.randint(0, 255)
                    intRandomGreen = random.randint(0, 255)
                    intRandomRed = random.randint(0, 255)

                    del contours[:]

                    for matchingChar in listOfMatchingChars:
                        contours.append(matchingChar.contour)
                    # end for

                    cv2.drawContours(imgContours, contours, -1, (intRandomBlue, intRandomGreen, intRandomRed))
                # end for
                cv2.imshow("8", imgContours)
            # end if # show steps #####################################################################

                    # within each possible plate, suppose the longest list of potential matching chars is the actual list of chars
            intLenOfLongestListOfChars = 0
            intIndexOfLongestListOfChars = 0

                    # loop through all the vectors of matching chars, get the index of the one with the most chars
            for i in range(0, len(listOfListsOfMatchingCharsInPlate)):
                if len(listOfListsOfMatchingCharsInPlate[i]) > intLenOfLongestListOfChars:
                    intLenOfLongestListOfChars = len(listOfListsOfMatchingCharsInPlate[i])
                    intIndexOfLongestListOfChars = i
                # end if
            # end for

                    # suppose that the longest list of matching chars within the plate is the actual list of chars
            longestListOfMatchingCharsInPlate = listOfListsOfMatchingCharsInPlate[intIndexOfLongestListOfChars]

            if showSteps == True: # show steps ###################################################
                imgContours = np.zeros((height, width, 3), np.uint8)
                del contours[:]

                for matchingChar in longestListOfMatchingCharsInPlate:
                    contours.append(matchingChar.contour)
                # end for

                cv2.drawContours(imgContours, contours, -1, SCALAR_WHITE)

                cv2.imshow("9", imgContours)
            # end if # show steps #####################################################################

            possiblePlate.strChars = recognizeCharsInPlate(possiblePlate.imgThresh, longestListOfMatchingCharsInPlate)

            if showSteps == True: # show steps ###################################################
                print ("chars found in plate number " + str(intPlateCounter) + " = " + possiblePlate.strChars + ", click on any image and press a key to continue . . .")
                intPlateCounter = intPlateCounter + 1
                cv2.waitKey(0)
            # end if # show steps #####################################################################

        # end of big for loop that takes up most of the function

        if showSteps == True:
            print ("\nchar detection complete, click on any image and press a key to continue . . .\n")
            cv2.waitKey(0)
        # end if

        return listOfPossiblePlates
    # end function

    ###################################################################################################
    def findPossibleCharsInPlate(imgGrayscale, imgThresh):
        listOfPossibleChars = []                        # this will be the return value
        contours = []
        imgThreshCopy = imgThresh.copy()

                # find all contours in plate
        contours, npaHierarchy = cv2.findContours(imgThreshCopy, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:                        # for each contour
            possibleChar = PossibleChar(contour)

            if checkIfPossibleChar(possibleChar):              # if contour is a possible char, note this does not compare to other chars (yet) . . .
                listOfPossibleChars.append(possibleChar)       # add to list of possible chars
            # end if
        # end if

        return listOfPossibleChars
    # end function

    ###################################################################################################
    def checkIfPossibleChar(possibleChar):
                # this function is a 'first pass' that does a rough check on a contour to see if it could be a char,
                # note that we are not (yet) comparing the char to other chars to look for a group
        if (possibleChar.intBoundingRectArea > MIN_PIXEL_AREA and
            possibleChar.intBoundingRectWidth > MIN_PIXEL_WIDTH and possibleChar.intBoundingRectHeight > MIN_PIXEL_HEIGHT and
            MIN_ASPECT_RATIO < possibleChar.fltAspectRatio and possibleChar.fltAspectRatio < MAX_ASPECT_RATIO):
            return True
        else:
            return False
        # end if
    # end function

    ###################################################################################################
    def findListOfListsOfMatchingChars(listOfPossibleChars):
                # with this function, we start off with all the possible chars in one big list
                # the purpose of this function is to re-arrange the one big list of chars into a list of lists of matching chars,
                # note that chars that are not found to be in a group of matches do not need to be considered further
        listOfListsOfMatchingChars = []                  # this will be the return value

        for possibleChar in listOfPossibleChars:                        # for each possible char in the one big list of chars
            listOfMatchingChars = findListOfMatchingChars(possibleChar, listOfPossibleChars)        # find all chars in the big list that match the current char

            listOfMatchingChars.append(possibleChar)                # also add the current char to current possible list of matching chars

            if len(listOfMatchingChars) < MIN_NUMBER_OF_MATCHING_CHARS:     # if current possible list of matching chars is not long enough to constitute a possible plate
                continue                            # jump back to the top of the for loop and try again with next char, note that it's not necessary
                                                    # to save the list in any way since it did not have enough chars to be a possible plate
            # end if

                                                    # if we get here, the current list passed test as a "group" or "cluster" of matching chars
            listOfListsOfMatchingChars.append(listOfMatchingChars)      # so add to our list of lists of matching chars

            listOfPossibleCharsWithCurrentMatchesRemoved = []

                                                    # remove the current list of matching chars from the big list so we don't use those same chars twice,
                                                    # make sure to make a new big list for this since we don't want to change the original big list
            listOfPossibleCharsWithCurrentMatchesRemoved = list(set(listOfPossibleChars) - set(listOfMatchingChars))

            recursiveListOfListsOfMatchingChars = findListOfListsOfMatchingChars(listOfPossibleCharsWithCurrentMatchesRemoved)      # recursive call

            for recursiveListOfMatchingChars in recursiveListOfListsOfMatchingChars:        # for each list of matching chars found by recursive call
                listOfListsOfMatchingChars.append(recursiveListOfMatchingChars)             # add to our original list of lists of matching chars
            # end for

            break       # exit for

        # end for

        return listOfListsOfMatchingChars
    # end function

    ###################################################################################################
    def findListOfMatchingChars(possibleChar, listOfChars):
                # the purpose of this function is, given a possible char and a big list of possible chars,
                # find all chars in the big list that are a match for the single possible char, and return those matching chars as a list
        listOfMatchingChars = []                # this will be the return value

        for possibleMatchingChar in listOfChars:                # for each char in big list
            if possibleMatchingChar == possibleChar:    # if the char we attempting to find matches for is the exact same char as the char in the big list we are currently checking
                                                        # then we should not include it in the list of matches b/c that would end up double including the current char
                continue                                # so do not add to list of matches and jump back to top of for loop
            # end if
                        # compute stuff to see if chars are a match
            fltDistanceBetweenChars = distanceBetweenChars(possibleChar, possibleMatchingChar)

            fltAngleBetweenChars = angleBetweenChars(possibleChar, possibleMatchingChar)

            fltChangeInArea = float(abs(possibleMatchingChar.intBoundingRectArea - possibleChar.intBoundingRectArea)) / float(possibleChar.intBoundingRectArea)

            fltChangeInWidth = float(abs(possibleMatchingChar.intBoundingRectWidth - possibleChar.intBoundingRectWidth)) / float(possibleChar.intBoundingRectWidth)
            fltChangeInHeight = float(abs(possibleMatchingChar.intBoundingRectHeight - possibleChar.intBoundingRectHeight)) / float(possibleChar.intBoundingRectHeight)

                    # check if chars match
            if (fltDistanceBetweenChars < (possibleChar.fltDiagonalSize * MAX_DIAG_SIZE_MULTIPLE_AWAY) and
                fltAngleBetweenChars < MAX_ANGLE_BETWEEN_CHARS and
                fltChangeInArea < MAX_CHANGE_IN_AREA and
                fltChangeInWidth < MAX_CHANGE_IN_WIDTH and
                fltChangeInHeight < MAX_CHANGE_IN_HEIGHT):

                listOfMatchingChars.append(possibleMatchingChar)        # if the chars are a match, add the current char to list of matching chars
            # end if
        # end for

        return listOfMatchingChars                  # return result
    # end function

    ###################################################################################################
    # use Pythagorean theorem to calculate distance between two chars
    def distanceBetweenChars(firstChar, secondChar):
        intX = abs(firstChar.intCenterX - secondChar.intCenterX)
        intY = abs(firstChar.intCenterY - secondChar.intCenterY)

        return math.sqrt((intX ** 2) + (intY ** 2))
    # end function

    ###################################################################################################
    # use basic trigonometry (SOH CAH TOA) to calculate angle between chars
    def angleBetweenChars(firstChar, secondChar):
        fltAdj = float(abs(firstChar.intCenterX - secondChar.intCenterX))
        fltOpp = float(abs(firstChar.intCenterY - secondChar.intCenterY))

        if fltAdj != 0.0:                           # check to make sure we do not divide by zero if the center X positions are equal, float division by zero will cause a crash in Python
            fltAngleInRad = math.atan(fltOpp / fltAdj)      # if adjacent is not zero, calculate angle
        else:
            fltAngleInRad = 1.5708                          # if adjacent is zero, use this as the angle, this is to be consistent with the C++ version of this program
        # end if

        fltAngleInDeg = fltAngleInRad * (180.0 / math.pi)       # calculate angle in degrees

        return fltAngleInDeg
    # end function

    ###################################################################################################
    # if we have two chars overlapping or to close to each other to possibly be separate chars, remove the inner (smaller) char,
    # this is to prevent including the same char twice if two contours are found for the same char,
    # for example for the letter 'O' both the inner ring and the outer ring may be found as contours, but we should only include the char once
    def removeInnerOverlappingChars(listOfMatchingChars):
        listOfMatchingCharsWithInnerCharRemoved = list(listOfMatchingChars)                # this will be the return value

        for currentChar in listOfMatchingChars:
            for otherChar in listOfMatchingChars:
                if currentChar != otherChar:        # if current char and other char are not the same char . . .
                                                                                # if current char and other char have center points at almost the same location . . .
                    if distanceBetweenChars(currentChar, otherChar) < (currentChar.fltDiagonalSize * MIN_DIAG_SIZE_MULTIPLE_AWAY):
                                    # if we get in here we have found overlapping chars
                                    # next we identify which char is smaller, then if that char was not already removed on a previous pass, remove it
                        if currentChar.intBoundingRectArea < otherChar.intBoundingRectArea:         # if current char is smaller than other char
                            if currentChar in listOfMatchingCharsWithInnerCharRemoved:              # if current char was not already removed on a previous pass . . .
                                listOfMatchingCharsWithInnerCharRemoved.remove(currentChar)         # then remove current char
                            # end if
                        else:                                                                       # else if other char is smaller than current char
                            if otherChar in listOfMatchingCharsWithInnerCharRemoved:                # if other char was not already removed on a previous pass . . .
                                listOfMatchingCharsWithInnerCharRemoved.remove(otherChar)           # then remove other char
                            # end if
                        # end if
                    # end if
                # end if
            # end for
        # end for

        return listOfMatchingCharsWithInnerCharRemoved
    # end function

    ###################################################################################################
    # this is where we apply the actual char recognition
    def recognizeCharsInPlate(imgThresh, listOfMatchingChars):
        strChars = ""               # this will be the return value, the chars in the lic plate

        height, width = imgThresh.shape

        imgThreshColor = np.zeros((height, width, 3), np.uint8)

        listOfMatchingChars.sort(key = lambda matchingChar: matchingChar.intCenterX)        # sort chars from left to right

        cv2.cvtColor(imgThresh, cv2.COLOR_GRAY2BGR, imgThreshColor)                     # make color version of threshold image so we can draw contours in color on it

        for currentChar in listOfMatchingChars:                                         # for each char in plate
            pt1 = (currentChar.intBoundingRectX, currentChar.intBoundingRectY)
            pt2 = ((currentChar.intBoundingRectX + currentChar.intBoundingRectWidth), (currentChar.intBoundingRectY + currentChar.intBoundingRectHeight))

            cv2.rectangle(imgThreshColor, pt1, pt2, SCALAR_GREEN, 2)           # draw green box around the char

                    # crop char out of threshold image
            imgROI = imgThresh[currentChar.intBoundingRectY : currentChar.intBoundingRectY + currentChar.intBoundingRectHeight,
                               currentChar.intBoundingRectX : currentChar.intBoundingRectX + currentChar.intBoundingRectWidth]

            imgROIResized = cv2.resize(imgROI, (RESIZED_CHAR_IMAGE_WIDTH, RESIZED_CHAR_IMAGE_HEIGHT))           # resize image, this is necessary for char recognition

            npaROIResized = imgROIResized.reshape((1, RESIZED_CHAR_IMAGE_WIDTH * RESIZED_CHAR_IMAGE_HEIGHT))        # flatten image into 1d numpy array

            npaROIResized = np.float32(npaROIResized)               # convert from 1d numpy array of ints to 1d numpy array of floats

            retval, npaResults, neigh_resp, dists = kNearest.findNearest(npaROIResized, k = 1)              # finally we can call findNearest !!!

            strCurrentChar = str(chr(int(npaResults[0][0])))            # get character from results

            strChars = strChars + strCurrentChar                        # append current char to full string

        # end for

        if showSteps == True: # show steps #######################################################
            cv2.imshow("10", imgThreshColor)
        # end if # show steps #########################################################################

        return strChars
    # end function

    ###################################################################################################
    def preprocess(imgOriginal):
        imgGrayscale = extractValue(imgOriginal)

        imgMaxContrastGrayscale = maximizeContrast(imgGrayscale)

        height, width = imgGrayscale.shape

        imgBlurred = np.zeros((height, width, 1), np.uint8)

        imgBlurred = cv2.GaussianBlur(imgMaxContrastGrayscale, GAUSSIAN_SMOOTH_FILTER_SIZE, 0)

        imgThresh = cv2.adaptiveThreshold(imgBlurred, 255.0, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, ADAPTIVE_THRESH_BLOCK_SIZE, ADAPTIVE_THRESH_WEIGHT)

        return imgGrayscale, imgThresh
    # end function

    ###################################################################################################
    def extractValue(imgOriginal):
        height, width, numChannels = imgOriginal.shape

        imgHSV = np.zeros((height, width, 3), np.uint8)

        imgHSV = cv2.cvtColor(imgOriginal, cv2.COLOR_BGR2HSV)

        imgHue, imgSaturation, imgValue = cv2.split(imgHSV)

        return imgValue
    # end function

    ###################################################################################################
    def maximizeContrast(imgGrayscale):

        height, width = imgGrayscale.shape

        imgTopHat = np.zeros((height, width, 1), np.uint8)
        imgBlackHat = np.zeros((height, width, 1), np.uint8)

        structuringElement = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

        imgTopHat = cv2.morphologyEx(imgGrayscale, cv2.MORPH_TOPHAT, structuringElement)
        imgBlackHat = cv2.morphologyEx(imgGrayscale, cv2.MORPH_BLACKHAT, structuringElement)

        imgGrayscalePlusTopHat = cv2.add(imgGrayscale, imgTopHat)
        imgGrayscalePlusTopHatMinusBlackHat = cv2.subtract(imgGrayscalePlusTopHat, imgBlackHat)

        return imgGrayscalePlusTopHatMinusBlackHat
    # end function

    ###################################################################################################
    class PossibleChar:

        # constructor #################################################################################
        def __init__(self, _contour):
            self.contour = _contour

            self.boundingRect = cv2.boundingRect(self.contour)

            [intX, intY, intWidth, intHeight] = self.boundingRect

            self.intBoundingRectX = intX
            self.intBoundingRectY = intY
            self.intBoundingRectWidth = intWidth
            self.intBoundingRectHeight = intHeight

            self.intBoundingRectArea = self.intBoundingRectWidth * self.intBoundingRectHeight

            self.intCenterX = (self.intBoundingRectX + self.intBoundingRectX + self.intBoundingRectWidth) / 2
            self.intCenterY = (self.intBoundingRectY + self.intBoundingRectY + self.intBoundingRectHeight) / 2

            self.fltDiagonalSize = math.sqrt((self.intBoundingRectWidth ** 2) + (self.intBoundingRectHeight ** 2))

            self.fltAspectRatio = float(self.intBoundingRectWidth) / float(self.intBoundingRectHeight)
        # end constructor

    # end class
     #def logout_view(request):
   # logout(request)
    ###################################################################################################
    class PossiblePlate:

        # constructor #################################################################################
        def __init__(self):
            self.imgPlate = None
            self.imgGrayscale = None
            self.imgThresh = None

            self.rrLocationOfPlateInScene = None

            self.strChars = ""
        # end constructor

    # end class
    ngori(self)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dashboard = QtWidgets.QDialog()
    ui = Ui_Dashboard()
    ui.setupUi(Dashboard)
    Dashboard.show()
    sys.exit(app.exec_())

