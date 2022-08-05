# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\vehicle.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Vehicledetails(object):
    def insertCar(self):
        print("Add vehicles clicked")
        fname = self.fname_lineEdit.text()
        lname = self.lname_lineEdit.text()
        ID = self.ID_lineEdit.text()
        contact = self.contact_lineEdit.text()
        designation = self.designation_lineEdit.text()
        plate = self.plate_lineEdit.text()
        color = self.color_lineEdit.text()
        model = self.model_lineEdit.text()
        description = self.description_lineEdit.text()
       
        conn = sqlite3.connect("parking.db")
        conn.execute("INSERT INTO VEHICLES VALUES(?,?,?,?,?,?,?,?,?)", (fname, lname, ID, contact, designation, plate, color, model, description,))
        #self.submit_btn.clicked.conn()
        print('Vehicle added')
        conn.commit()
        conn.close()
        
        
        
    def addcarcheck(self):
        self.insertCar()
        
    def setupUi(self, Vehicledetails):
        Vehicledetails.setObjectName("Vehicledetails")
        Vehicledetails.resize(630, 485)
        Vehicledetails.setStyleSheet("QToolTip\n"
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
        self.label = QtWidgets.QLabel(Vehicledetails)
        self.label.setGeometry(QtCore.QRect(170, 10, 253, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.fname_label = QtWidgets.QLabel(Vehicledetails)
        self.fname_label.setGeometry(QtCore.QRect(10, 70, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.fname_label.setFont(font)
        self.fname_label.setObjectName("fname_label")
        self.fname_lineEdit = QtWidgets.QLineEdit(Vehicledetails)
        self.fname_lineEdit.setGeometry(QtCore.QRect(170, 70, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.fname_lineEdit.setFont(font)
        self.fname_lineEdit.setObjectName("fname_lineEdit")
        self.lname_label = QtWidgets.QLabel(Vehicledetails)
        self.lname_label.setGeometry(QtCore.QRect(340, 70, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lname_label.setFont(font)
        self.lname_label.setObjectName("lname_label")
        self.lname_lineEdit = QtWidgets.QLineEdit(Vehicledetails)
        self.lname_lineEdit.setGeometry(QtCore.QRect(460, 70, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lname_lineEdit.setFont(font)
        self.lname_lineEdit.setObjectName("lname_lineEdit")
        self.plate_lineEdit = QtWidgets.QLineEdit(Vehicledetails)
        self.plate_lineEdit.setGeometry(QtCore.QRect(170, 220, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.plate_lineEdit.setFont(font)
        self.plate_lineEdit.setObjectName("plate_lineEdit")
        self.plate_label = QtWidgets.QLabel(Vehicledetails)
        self.plate_label.setGeometry(QtCore.QRect(10, 220, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.plate_label.setFont(font)
        self.plate_label.setObjectName("plate_label")
        self.ID_label = QtWidgets.QLabel(Vehicledetails)
        self.ID_label.setGeometry(QtCore.QRect(10, 120, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ID_label.setFont(font)
        self.ID_label.setObjectName("ID_label")
        self.ID_lineEdit = QtWidgets.QLineEdit(Vehicledetails)
        self.ID_lineEdit.setGeometry(QtCore.QRect(170, 120, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ID_lineEdit.setFont(font)
        self.ID_lineEdit.setObjectName("ID_lineEdit")
        self.contact_label = QtWidgets.QLabel(Vehicledetails)
        self.contact_label.setGeometry(QtCore.QRect(340, 120, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.contact_label.setFont(font)
        self.contact_label.setObjectName("contact_label")
        self.contact_lineEdit = QtWidgets.QLineEdit(Vehicledetails)
        self.contact_lineEdit.setGeometry(QtCore.QRect(460, 120, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.contact_lineEdit.setFont(font)
        self.contact_lineEdit.setObjectName("contact_lineEdit")
        self.description_label = QtWidgets.QLabel(Vehicledetails)
        self.description_label.setGeometry(QtCore.QRect(10, 320, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.description_label.setFont(font)
        self.description_label.setObjectName("description_label")
        self.description_lineEdit = QtWidgets.QLineEdit(Vehicledetails)
        self.description_lineEdit.setGeometry(QtCore.QRect(170, 320, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.description_lineEdit.setFont(font)
        self.description_lineEdit.setObjectName("description_lineEdit")
        self.designation_lineEdit = QtWidgets.QLineEdit(Vehicledetails)
        self.designation_lineEdit.setGeometry(QtCore.QRect(170, 170, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.designation_lineEdit.setFont(font)
        self.designation_lineEdit.setObjectName("designation_lineEdit")
        self.designation_label = QtWidgets.QLabel(Vehicledetails)
        self.designation_label.setGeometry(QtCore.QRect(11, 170, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.designation_label.setFont(font)
        self.designation_label.setObjectName("designation_label")
        self.color_label = QtWidgets.QLabel(Vehicledetails)
        self.color_label.setGeometry(QtCore.QRect(10, 270, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.color_label.setFont(font)
        self.color_label.setObjectName("color_label")
        self.color_lineEdit = QtWidgets.QLineEdit(Vehicledetails)
        self.color_lineEdit.setGeometry(QtCore.QRect(170, 270, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.color_lineEdit.setFont(font)
        self.color_lineEdit.setObjectName("color_lineEdit")
        self.model_lineEdit = QtWidgets.QLineEdit(Vehicledetails)
        self.model_lineEdit.setGeometry(QtCore.QRect(460, 270, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.model_lineEdit.setFont(font)
        self.model_lineEdit.setObjectName("model_lineEdit")
        self.model_label = QtWidgets.QLabel(Vehicledetails)
        self.model_label.setGeometry(QtCore.QRect(340, 270, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.model_label.setFont(font)
        self.model_label.setObjectName("model_label")
        self.submit_btn = QtWidgets.QPushButton(Vehicledetails)
        self.submit_btn.setGeometry(QtCore.QRect(170, 400, 151, 51))
        self.submit_btn.setObjectName("submit_btn")
        ##########button Event############
        self.submit_btn.clicked.connect(self.insertCar)
        ############################
        self.pushButton_2 = QtWidgets.QPushButton(Vehicledetails)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 400, 151, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.description_label_2 = QtWidgets.QLabel(Vehicledetails)
        self.description_label_2.setGeometry(QtCore.QRect(340, 320, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.description_label_2.setFont(font)
        self.description_label_2.setText("")
        self.description_label_2.setObjectName("description_label_2")
        self.fname_label.raise_()
        self.fname_lineEdit.raise_()
        self.lname_label.raise_()
        self.lname_lineEdit.raise_()
        self.plate_lineEdit.raise_()
        self.plate_label.raise_()
        self.ID_label.raise_()
        self.ID_lineEdit.raise_()
        self.contact_label.raise_()
        self.contact_lineEdit.raise_()
        self.designation_lineEdit.raise_()
        self.designation_label.raise_()
        self.color_label.raise_()
        self.color_lineEdit.raise_()
        self.model_lineEdit.raise_()
        self.model_label.raise_()
        self.submit_btn.raise_()
        self.pushButton_2.raise_()
        self.label.raise_()
        self.description_lineEdit.raise_()
        self.description_label.raise_()
        self.description_label_2.raise_()

        self.retranslateUi(Vehicledetails)
        QtCore.QMetaObject.connectSlotsByName(Vehicledetails)
        Vehicledetails.setTabOrder(self.fname_lineEdit, self.lname_lineEdit)
        Vehicledetails.setTabOrder(self.lname_lineEdit, self.ID_lineEdit)
        Vehicledetails.setTabOrder(self.ID_lineEdit, self.contact_lineEdit)
        Vehicledetails.setTabOrder(self.contact_lineEdit, self.designation_lineEdit)
        Vehicledetails.setTabOrder(self.designation_lineEdit, self.plate_lineEdit)
        Vehicledetails.setTabOrder(self.plate_lineEdit, self.color_lineEdit)
        Vehicledetails.setTabOrder(self.color_lineEdit, self.model_lineEdit)
        Vehicledetails.setTabOrder(self.model_lineEdit, self.description_lineEdit)
        Vehicledetails.setTabOrder(self.description_lineEdit, self.submit_btn)
        Vehicledetails.setTabOrder(self.submit_btn, self.pushButton_2)

    def retranslateUi(self, Vehicledetails):
        _translate = QtCore.QCoreApplication.translate
        Vehicledetails.setWindowTitle(_translate("Vehicledetails", "Add Vehicle"))
        self.label.setText(_translate("Vehicledetails", "Add vehicle details"))
        self.fname_label.setText(_translate("Vehicledetails", "FIRST NAME"))
        self.lname_label.setText(_translate("Vehicledetails", "LAST NAME"))
        self.ID_label.setText(_translate("Vehicledetails", "ID NUMBER"))
        self.contact_label.setText(_translate("Vehicledetails", "CONTACT"))
        self.designation_label.setText(_translate("Vehicledetails", "DESIGNATION"))
        self.plate_label.setText(_translate("Vehicledetails", "NUMBER PLATE"))
        self.color_label.setText(_translate("Vehicledetails", "COLOR"))
        self.model_label.setText(_translate("Vehicledetails", "MODEL"))
        self.description_label.setText(_translate("Vehicledetails", "DESCRIPTION"))
        self.submit_btn.setText(_translate("Vehicledetails", "SUBMIT"))
        self.pushButton_2.setText(_translate("Vehicledetails", "CLEAR"))
        
    
 

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Vehicledetails = QtWidgets.QDialog()
    ui = Ui_Vehicledetails()
    ui.setupUi(Vehicledetails)
    Vehicledetails.show()
    sys.exit(app.exec_())

