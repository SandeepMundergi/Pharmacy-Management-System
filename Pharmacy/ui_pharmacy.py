# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pharmacycUkMtP.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1458, 757)
        MainWindow.setStyleSheet(u"QMessageBox {\n"
"    background-color: #333333;\n"
"}\n"
"\n"
"QMessageBox QLabel {\n"
"    color: #aaa;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"border:1px solid border;\n"
"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.login = QWidget()
        self.login.setObjectName(u"login")
        self.login.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 211), stop:1 rgba(255, 255, 255, 255));\n"
"border:none;")
        self.horizontalLayout_32 = QHBoxLayout(self.login)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.frame_33 = QFrame(self.login)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setMinimumSize(QSize(400, 500))
        self.frame_33.setMaximumSize(QSize(400, 500))
        self.frame_33.setStyleSheet(u"border-radius:50px;\n"
"background-color: rgba(207, 207, 207,0.5);\n"
"border:5px solid  rgb(199, 199, 199);\n"
"\n"
"")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.label_6 = QLabel(self.frame_33)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(130, 60, 150, 150))
        self.label_6.setMinimumSize(QSize(150, 150))
        self.label_6.setStyleSheet(u"border-radius:70px;\n"
"background-color: rgba(207, 207, 207,0.5);\n"
"border:5px solid  rgb(199, 199, 199);\n"
"\n"
"")
        self.label_6.setPixmap(QPixmap(u"icons/user.png"))
        self.label_6.setScaledContents(True)
        self.label_78 = QLabel(self.frame_33)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setGeometry(QRect(20, 250, 30, 30))
        self.label_78.setMinimumSize(QSize(30, 30))
        self.label_78.setMaximumSize(QSize(30, 30))
        self.label_78.setStyleSheet(u"border:none;\n"
"background-color:transparent;")
        self.label_78.setPixmap(QPixmap(u":/icons/icons/mail.svg"))
        self.label_78.setScaledContents(True)
        self.label_79 = QLabel(self.frame_33)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setGeometry(QRect(20, 320, 30, 30))
        self.label_79.setMinimumSize(QSize(30, 30))
        self.label_79.setMaximumSize(QSize(30, 30))
        self.label_79.setStyleSheet(u"border:none;\n"
"background-color:transparent;")
        self.label_79.setPixmap(QPixmap(u":/icons/icons/shield-lock.svg"))
        self.label_80 = QLabel(self.frame_33)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setGeometry(QRect(60, 250, 91, 30))
        self.label_80.setMinimumSize(QSize(0, 30))
        self.label_80.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_80.setFont(font)
        self.label_80.setStyleSheet(u"border:none;\n"
"background-color:transparent;;")
        self.label_86 = QLabel(self.frame_33)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setGeometry(QRect(50, 320, 91, 30))
        self.label_86.setMinimumSize(QSize(0, 30))
        self.label_86.setMaximumSize(QSize(16777215, 30))
        self.label_86.setFont(font)
        self.label_86.setStyleSheet(u"border:none;\n"
"background-color:transparent;")
        self.email = QLineEdit(self.frame_33)
        self.email.setObjectName(u"email")
        self.email.setGeometry(QRect(150, 250, 220, 30))
        self.email.setMinimumSize(QSize(220, 30))
        self.email.setMaximumSize(QSize(220, 30))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setWeight(75)
        self.email.setFont(font1)
        self.email.setStyleSheet(u"QLineEdit{\n"
"border:1px solid;\n"
"border-bottom-color: rgb(0, 0, 0);\n"
"border-right-color: transparent;\n"
"border-left-color: transparent;\n"
"border-top-color: transparent;\n"
"background-color:transparent;\n"
"color:black;\n"
"}\n"
"QLineEdit:hover{\n"
"border:2px solid;\n"
"border-bottom-color:  rgb(0, 149, 223);\n"
"border-right-color: transparent;\n"
"border-left-color: transparent;\n"
"border-top-color: transparent;\n"
"background-color:transparent;\n"
"color:black;\n"
"}\n"
"\n"
"\n"
"")
        self.password = QLineEdit(self.frame_33)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(150, 320, 220, 30))
        self.password.setMinimumSize(QSize(220, 30))
        self.password.setMaximumSize(QSize(220, 30))
        self.password.setFont(font1)
        self.password.setStyleSheet(u"QLineEdit{\n"
"border:1px solid;\n"
"border-bottom-color: rgb(0, 0, 0);\n"
"border-right-color: transparent;\n"
"border-left-color: transparent;\n"
"border-top-color: transparent;\n"
"background-color:transparent;\n"
"color:black;\n"
"}\n"
"QLineEdit:hover{\n"
"border:2px solid;\n"
"border-bottom-color:  rgb(0, 149, 223);\n"
"border-right-color: transparent;\n"
"border-left-color: transparent;\n"
"border-top-color: transparent;\n"
"background-color:transparent;\n"
"color:black;\n"
"}\n"
"\n"
"\n"
"")
        self.password.setEchoMode(QLineEdit.Password)
        self.login_btn = QPushButton(self.frame_33)
        self.login_btn.setObjectName(u"login_btn")
        self.login_btn.setGeometry(QRect(30, 390, 341, 50))
        self.login_btn.setMinimumSize(QSize(341, 50))
        self.login_btn.setMaximumSize(QSize(341, 16777215))
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(True)
        font2.setWeight(75)
        self.login_btn.setFont(font2)
        self.login_btn.setStyleSheet(u"QPushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(186, 27, 156, 255), stop:1 rgba(219, 91, 34, 247));\n"
"color:#fff;\n"
"border-radius:20px;\n"
"border:none;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(186, 101, 27, 255), stop:1 rgba(219, 34, 184, 247));\n"
"color:#fff;\n"
"border-radius:20px;\n"
"border:none;\n"
"}\n"
"")

        self.horizontalLayout_32.addWidget(self.frame_33)

        self.stackedWidget.addWidget(self.login)
        self.main = QWidget()
        self.main.setObjectName(u"main")
        self.horizontalLayout_30 = QHBoxLayout(self.main)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.main)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.main_ui_window = QFrame(self.frame_2)
        self.main_ui_window.setObjectName(u"main_ui_window")
        self.main_ui_window.setFrameShape(QFrame.StyledPanel)
        self.main_ui_window.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.main_ui_window)
        self.verticalLayout_17.setSpacing(5)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(5, 5, 5, 5)
        self.header = QFrame(self.main_ui_window)
        self.header.setObjectName(u"header")
        self.header.setStyleSheet(u"border:2px solid black;\n"
"border-radius:12px;\n"
"padding:1px;")
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 10, 0, 10)
        self.logo = QFrame(self.header)
        self.logo.setObjectName(u"logo")
        self.logo.setStyleSheet(u"border:none;")
        self.logo.setFrameShape(QFrame.StyledPanel)
        self.logo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.logo)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(50, 0, 0, 0)
        self.label_4 = QLabel(self.logo)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(50, 60))
        self.label_4.setMaximumSize(QSize(50, 60))
        self.label_4.setStyleSheet(u"")
        self.label_4.setPixmap(QPixmap(u":/icons/icons/caduceus.svg"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label_4, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.logo, 0, Qt.AlignLeft|Qt.AlignTop)

        self.name = QFrame(self.header)
        self.name.setObjectName(u"name")
        self.name.setStyleSheet(u"border:none;")
        self.name.setFrameShape(QFrame.StyledPanel)
        self.name.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.name)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.name)
        self.label_3.setObjectName(u"label_3")
        font3 = QFont()
        font3.setPointSize(18)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_3.setFont(font3)

        self.horizontalLayout_3.addWidget(self.label_3, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.horizontalLayout_2.addWidget(self.name, 0, Qt.AlignRight)

        self.contact_detail = QFrame(self.header)
        self.contact_detail.setObjectName(u"contact_detail")
        self.contact_detail.setStyleSheet(u"border:none;")
        self.contact_detail.setFrameShape(QFrame.StyledPanel)
        self.contact_detail.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.contact_detail)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_37 = QLabel(self.contact_detail)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMinimumSize(QSize(30, 30))
        self.label_37.setMaximumSize(QSize(30, 30))
        self.label_37.setPixmap(QPixmap(u":/icons/icons/phone.svg"))
        self.label_37.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.label_37, 0, Qt.AlignRight)

        self.label_2 = QLabel(self.contact_detail)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.horizontalLayout_5.addWidget(self.label_2)


        self.horizontalLayout_2.addWidget(self.contact_detail, 0, Qt.AlignRight)

        self.log_out_frame = QFrame(self.header)
        self.log_out_frame.setObjectName(u"log_out_frame")
        self.log_out_frame.setStyleSheet(u"border:none;")
        self.log_out_frame.setFrameShape(QFrame.StyledPanel)
        self.log_out_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.log_out_frame)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 10, 0)
        self.label = QLabel(self.log_out_frame)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1, Qt.AlignLeft)

        self.logout_btn = QPushButton(self.log_out_frame)
        self.logout_btn.setObjectName(u"logout_btn")
        icon = QIcon()
        icon.addFile(u":/icons/icons/logout.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.logout_btn.setIcon(icon)
        self.logout_btn.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.logout_btn, 0, 1, 1, 1, Qt.AlignRight)


        self.horizontalLayout_2.addWidget(self.log_out_frame, 0, Qt.AlignRight)


        self.verticalLayout_17.addWidget(self.header)

        self.main_body = QFrame(self.main_ui_window)
        self.main_body.setObjectName(u"main_body")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_body.sizePolicy().hasHeightForWidth())
        self.main_body.setSizePolicy(sizePolicy)
        self.main_body.setStyleSheet(u"border:none;")
        self.main_body.setFrameShape(QFrame.StyledPanel)
        self.main_body.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.main_body)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.left_menu = QFrame(self.main_body)
        self.left_menu.setObjectName(u"left_menu")
        self.left_menu.setStyleSheet(u"border:2px solid black;\n"
"border-radius:12px;\n"
"padding:5px;")
        self.left_menu.setFrameShape(QFrame.StyledPanel)
        self.left_menu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.left_menu)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.menu = QFrame(self.left_menu)
        self.menu.setObjectName(u"menu")
        self.menu.setStyleSheet(u"border:none;\n"
"color:#fff;")
        self.menu.setFrameShape(QFrame.StyledPanel)
        self.menu.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.menu)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.inventory_btn = QPushButton(self.menu)
        self.inventory_btn.setObjectName(u"inventory_btn")
        self.inventory_btn.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/building-store.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.inventory_btn.setIcon(icon1)
        self.inventory_btn.setIconSize(QSize(30, 30))

        self.gridLayout_2.addWidget(self.inventory_btn, 4, 0, 1, 1)

        self.purchase_btn = QPushButton(self.menu)
        self.purchase_btn.setObjectName(u"purchase_btn")
        self.purchase_btn.setFont(font)
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/archive.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.purchase_btn.setIcon(icon2)
        self.purchase_btn.setIconSize(QSize(30, 30))

        self.gridLayout_2.addWidget(self.purchase_btn, 3, 0, 1, 1)

        self.dashboard_btn = QPushButton(self.menu)
        self.dashboard_btn.setObjectName(u"dashboard_btn")
        self.dashboard_btn.setFont(font)
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/dashboard.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.dashboard_btn.setIcon(icon3)
        self.dashboard_btn.setIconSize(QSize(30, 30))

        self.gridLayout_2.addWidget(self.dashboard_btn, 0, 0, 2, 2)

        self.description_btn = QPushButton(self.menu)
        self.description_btn.setObjectName(u"description_btn")
        self.description_btn.setFont(font)
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/template.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.description_btn.setIcon(icon4)
        self.description_btn.setIconSize(QSize(30, 30))

        self.gridLayout_2.addWidget(self.description_btn, 8, 0, 1, 2)

        self.customer_btn = QPushButton(self.menu)
        self.customer_btn.setObjectName(u"customer_btn")
        self.customer_btn.setFont(font)
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.customer_btn.setIcon(icon5)
        self.customer_btn.setIconSize(QSize(30, 30))

        self.gridLayout_2.addWidget(self.customer_btn, 5, 0, 1, 1)

        self.report_btn = QPushButton(self.menu)
        self.report_btn.setObjectName(u"report_btn")
        self.report_btn.setFont(font)
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/report-search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.report_btn.setIcon(icon6)
        self.report_btn.setIconSize(QSize(30, 30))

        self.gridLayout_2.addWidget(self.report_btn, 10, 0, 1, 1)


        self.horizontalLayout_7.addWidget(self.menu, 0, Qt.AlignLeft|Qt.AlignTop)


        self.horizontalLayout_6.addWidget(self.left_menu, 0, Qt.AlignLeft)

        self.stackedWidget_2 = QStackedWidget(self.main_body)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setStyleSheet(u"border:2px solid black;\n"
"border-radius:12px;\n"
"padding:5px;")
        self.Dashboard = QWidget()
        self.Dashboard.setObjectName(u"Dashboard")
        self.Dashboard.setStyleSheet(u"border:none;")
        self.horizontalLayout_13 = QHBoxLayout(self.Dashboard)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.right_body = QFrame(self.Dashboard)
        self.right_body.setObjectName(u"right_body")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.right_body.sizePolicy().hasHeightForWidth())
        self.right_body.setSizePolicy(sizePolicy1)
        self.right_body.setFrameShape(QFrame.StyledPanel)
        self.right_body.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.right_body)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.right_body)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(490, 0))
        self.frame_4.setStyleSheet(u"border:2px solid black;\n"
"border-radius:12px;\n"
"padding:5px;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_11.setSpacing(10)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.customer_frame = QFrame(self.frame_4)
        self.customer_frame.setObjectName(u"customer_frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.customer_frame.sizePolicy().hasHeightForWidth())
        self.customer_frame.setSizePolicy(sizePolicy2)
        self.customer_frame.setMinimumSize(QSize(200, 150))
        self.customer_frame.setMaximumSize(QSize(200, 150))
        self.customer_frame.setStyleSheet(u"border:none;")
        self.customer_frame.setFrameShape(QFrame.StyledPanel)
        self.customer_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.customer_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.customer_frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_7)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(0)
        self.gridLayout_4.setVerticalSpacing(10)
        self.gridLayout_4.setContentsMargins(10, 10, 0, 0)
        self.label_18 = QLabel(self.frame_7)
        self.label_18.setObjectName(u"label_18")
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_18.setFont(font4)

        self.gridLayout_4.addWidget(self.label_18, 1, 1, 1, 1, Qt.AlignHCenter)

        self.label_17 = QLabel(self.frame_7)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font4)

        self.gridLayout_4.addWidget(self.label_17, 0, 1, 1, 1, Qt.AlignHCenter)

        self.label_16 = QLabel(self.frame_7)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(60, 60))
        self.label_16.setMaximumSize(QSize(60, 50))
        self.label_16.setPixmap(QPixmap(u":/icons/icons/user.svg"))
        self.label_16.setScaledContents(True)

        self.gridLayout_4.addWidget(self.label_16, 0, 0, 2, 1, Qt.AlignVCenter)


        self.verticalLayout_2.addWidget(self.frame_7, 0, Qt.AlignTop)

        self.frame_6 = QFrame(self.customer_frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.frame_6)
        self.label_15.setObjectName(u"label_15")
        font5 = QFont()
        font5.setPointSize(10)
        self.label_15.setFont(font5)

        self.horizontalLayout_8.addWidget(self.label_15)

        self.customer_btn_2 = QPushButton(self.frame_6)
        self.customer_btn_2.setObjectName(u"customer_btn_2")
        font6 = QFont()
        font6.setPointSize(8)
        font6.setBold(False)
        font6.setWeight(50)
        self.customer_btn_2.setFont(font6)
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/arrow-narrow-right.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.customer_btn_2.setIcon(icon7)
        self.customer_btn_2.setIconSize(QSize(25, 25))

        self.horizontalLayout_8.addWidget(self.customer_btn_2, 0, Qt.AlignVCenter)


        self.verticalLayout_2.addWidget(self.frame_6, 0, Qt.AlignBottom)


        self.horizontalLayout_11.addWidget(self.customer_frame)

        self.Sales_frame = QFrame(self.frame_4)
        self.Sales_frame.setObjectName(u"Sales_frame")
        sizePolicy2.setHeightForWidth(self.Sales_frame.sizePolicy().hasHeightForWidth())
        self.Sales_frame.setSizePolicy(sizePolicy2)
        self.Sales_frame.setMinimumSize(QSize(200, 150))
        self.Sales_frame.setMaximumSize(QSize(200, 150))
        self.Sales_frame.setStyleSheet(u"border:none;")
        self.Sales_frame.setFrameShape(QFrame.StyledPanel)
        self.Sales_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.Sales_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.Sales_frame)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_9)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(0)
        self.gridLayout_5.setVerticalSpacing(10)
        self.gridLayout_5.setContentsMargins(10, 10, 0, 0)
        self.label_20 = QLabel(self.frame_9)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font4)

        self.gridLayout_5.addWidget(self.label_20, 0, 1, 1, 1, Qt.AlignHCenter)

        self.label_21 = QLabel(self.frame_9)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font4)

        self.gridLayout_5.addWidget(self.label_21, 1, 1, 1, 1, Qt.AlignHCenter)

        self.label_22 = QLabel(self.frame_9)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(40, 50))
        self.label_22.setMaximumSize(QSize(40, 50))
        self.label_22.setPixmap(QPixmap(u":/icons/icons/Indian-Rupee-symbol.svg"))
        self.label_22.setScaledContents(True)

        self.gridLayout_5.addWidget(self.label_22, 0, 0, 2, 1, Qt.AlignVCenter)


        self.verticalLayout_3.addWidget(self.frame_9, 0, Qt.AlignTop)

        self.frame_8 = QFrame(self.Sales_frame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.frame_8)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font5)

        self.horizontalLayout_9.addWidget(self.label_19, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.sale_btn = QPushButton(self.frame_8)
        self.sale_btn.setObjectName(u"sale_btn")
        self.sale_btn.setFont(font6)
        self.sale_btn.setIcon(icon7)
        self.sale_btn.setIconSize(QSize(25, 25))

        self.horizontalLayout_9.addWidget(self.sale_btn, 0, Qt.AlignVCenter)


        self.verticalLayout_3.addWidget(self.frame_8, 0, Qt.AlignBottom)


        self.horizontalLayout_11.addWidget(self.Sales_frame)

        self.Stock_frame = QFrame(self.frame_4)
        self.Stock_frame.setObjectName(u"Stock_frame")
        sizePolicy2.setHeightForWidth(self.Stock_frame.sizePolicy().hasHeightForWidth())
        self.Stock_frame.setSizePolicy(sizePolicy2)
        self.Stock_frame.setMinimumSize(QSize(200, 150))
        self.Stock_frame.setMaximumSize(QSize(200, 150))
        self.Stock_frame.setStyleSheet(u"border:none;")
        self.Stock_frame.setFrameShape(QFrame.StyledPanel)
        self.Stock_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.Stock_frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.Stock_frame)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_11)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(0)
        self.gridLayout_6.setVerticalSpacing(10)
        self.gridLayout_6.setContentsMargins(10, 10, 0, 0)
        self.label_26 = QLabel(self.frame_11)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(60, 60))
        self.label_26.setMaximumSize(QSize(60, 50))
        self.label_26.setPixmap(QPixmap(u":/icons/icons/building-store.svg"))
        self.label_26.setScaledContents(True)

        self.gridLayout_6.addWidget(self.label_26, 0, 0, 2, 1, Qt.AlignVCenter)

        self.d_stock = QLabel(self.frame_11)
        self.d_stock.setObjectName(u"d_stock")
        self.d_stock.setFont(font4)

        self.gridLayout_6.addWidget(self.d_stock, 0, 1, 1, 1, Qt.AlignHCenter)

        self.label_25 = QLabel(self.frame_11)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font4)

        self.gridLayout_6.addWidget(self.label_25, 1, 1, 1, 1, Qt.AlignHCenter)


        self.verticalLayout_4.addWidget(self.frame_11, 0, Qt.AlignTop)

        self.frame_10 = QFrame(self.Stock_frame)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_23 = QLabel(self.frame_10)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font5)

        self.horizontalLayout_10.addWidget(self.label_23)

        self.stock_btn = QPushButton(self.frame_10)
        self.stock_btn.setObjectName(u"stock_btn")
        self.stock_btn.setFont(font6)
        self.stock_btn.setIcon(icon7)
        self.stock_btn.setIconSize(QSize(25, 25))

        self.horizontalLayout_10.addWidget(self.stock_btn, 0, Qt.AlignVCenter)


        self.verticalLayout_4.addWidget(self.frame_10, 0, Qt.AlignBottom)


        self.horizontalLayout_11.addWidget(self.Stock_frame)


        self.verticalLayout_5.addWidget(self.frame_4, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_3 = QFrame(self.right_body)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_12.setSpacing(5)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"border:2px solid black;\n"
"border-radius:12px;\n"
"padding:5px;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_5)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(10, 0, 5, 5)
        self.label_38 = QLabel(self.frame_5)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font4)
        self.label_38.setStyleSheet(u"border:none;")

        self.verticalLayout_7.addWidget(self.label_38, 0, Qt.AlignBottom)

        self.table = QFrame(self.frame_5)
        self.table.setObjectName(u"table")
        sizePolicy2.setHeightForWidth(self.table.sizePolicy().hasHeightForWidth())
        self.table.setSizePolicy(sizePolicy2)
        self.table.setStyleSheet(u"border:none;\n"
"padding:0;\n"
"text-align:center;")
        self.table.setFrameShape(QFrame.StyledPanel)
        self.table.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.table)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.dashboard_table = QTableWidget(self.table)
        if (self.dashboard_table.columnCount() < 7):
            self.dashboard_table.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.dashboard_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        self.dashboard_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font);
        self.dashboard_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font);
        self.dashboard_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font);
        self.dashboard_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font);
        self.dashboard_table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font);
        self.dashboard_table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.dashboard_table.setObjectName(u"dashboard_table")

        self.verticalLayout_12.addWidget(self.dashboard_table)


        self.verticalLayout_7.addWidget(self.table)


        self.horizontalLayout_12.addWidget(self.frame_5)

        self.frame_12 = QFrame(self.frame_3)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"border:2px solid black;\n"
"border-radius:12px;\n"
"padding:5px;")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_12)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 0, 5, 5)
        self.label_39 = QLabel(self.frame_12)
        self.label_39.setObjectName(u"label_39")
        font7 = QFont()
        font7.setPointSize(16)
        font7.setBold(True)
        font7.setWeight(75)
        self.label_39.setFont(font7)
        self.label_39.setStyleSheet(u"border:none;")

        self.verticalLayout_6.addWidget(self.label_39)

        self.details = QFrame(self.frame_12)
        self.details.setObjectName(u"details")
        self.details.setStyleSheet(u"border:none;")
        self.details.setFrameShape(QFrame.StyledPanel)
        self.details.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.details)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(10)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setContentsMargins(0, 0, 10, 0)
        self.d_product = QLabel(self.details)
        self.d_product.setObjectName(u"d_product")
        self.d_product.setFont(font4)

        self.gridLayout_3.addWidget(self.d_product, 0, 1, 1, 1)

        self.label_27 = QLabel(self.details)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font2)

        self.gridLayout_3.addWidget(self.label_27, 0, 0, 1, 1)

        self.label_28 = QLabel(self.details)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font2)

        self.gridLayout_3.addWidget(self.label_28, 1, 0, 1, 1)

        self.label_30 = QLabel(self.details)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font2)

        self.gridLayout_3.addWidget(self.label_30, 2, 0, 1, 1)

        self.label_31 = QLabel(self.details)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font2)

        self.gridLayout_3.addWidget(self.label_31, 3, 0, 1, 1)

        self.label_33 = QLabel(self.details)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font4)

        self.gridLayout_3.addWidget(self.label_33, 1, 1, 1, 1)

        self.label_36 = QLabel(self.details)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font4)

        self.gridLayout_3.addWidget(self.label_36, 3, 1, 1, 1)

        self.label_35 = QLabel(self.details)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font4)

        self.gridLayout_3.addWidget(self.label_35, 2, 1, 1, 1)

        self.label_28.raise_()
        self.label_30.raise_()
        self.label_31.raise_()
        self.label_27.raise_()
        self.d_product.raise_()
        self.label_33.raise_()
        self.label_35.raise_()
        self.label_36.raise_()

        self.verticalLayout_6.addWidget(self.details, 0, Qt.AlignLeft)


        self.horizontalLayout_12.addWidget(self.frame_12, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout_5.addWidget(self.frame_3)

        self.frame_19 = QFrame(self.right_body)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setStyleSheet(u"border:none;")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_14.setSpacing(5)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.Download = QPushButton(self.frame_19)
        self.Download.setObjectName(u"Download")
        self.Download.setFont(font)
        self.Download.setStyleSheet(u"border:2px solid black;\n"
"border-radius:12px;\n"
"padding:5px;")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/download.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Download.setIcon(icon8)
        self.Download.setIconSize(QSize(25, 25))

        self.horizontalLayout_14.addWidget(self.Download)

        self.dashboard_clear_btn = QPushButton(self.frame_19)
        self.dashboard_clear_btn.setObjectName(u"dashboard_clear_btn")
        self.dashboard_clear_btn.setFont(font)
        self.dashboard_clear_btn.setStyleSheet(u"border:2px solid black;\n"
"border-radius:12px;\n"
"padding:5px;")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/recycle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.dashboard_clear_btn.setIcon(icon9)
        self.dashboard_clear_btn.setIconSize(QSize(25, 25))

        self.horizontalLayout_14.addWidget(self.dashboard_clear_btn)


        self.verticalLayout_5.addWidget(self.frame_19, 0, Qt.AlignLeft|Qt.AlignBottom)


        self.horizontalLayout_13.addWidget(self.right_body)

        self.stackedWidget_2.addWidget(self.Dashboard)
        self.Purchase = QWidget()
        self.Purchase.setObjectName(u"Purchase")
        self.Purchase.setStyleSheet(u"border:none;\n"
"padding:0px;")
        self.horizontalLayout_38 = QHBoxLayout(self.Purchase)
        self.horizontalLayout_38.setSpacing(0)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.frame_47 = QFrame(self.Purchase)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setStyleSheet(u"")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_47)
        self.verticalLayout_23.setSpacing(5)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.frame_48 = QFrame(self.frame_47)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setStyleSheet(u"")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.frame_48)
        self.horizontalLayout_40.setSpacing(5)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.purchase_historybtn = QPushButton(self.frame_48)
        self.purchase_historybtn.setObjectName(u"purchase_historybtn")
        self.purchase_historybtn.setFont(font)
        self.purchase_historybtn.setStyleSheet(u"border:2px solid black;\n"
"border-radius:12px;\n"
"padding:5px;")

        self.horizontalLayout_40.addWidget(self.purchase_historybtn)

        self.Customer_search_btn = QPushButton(self.frame_48)
        self.Customer_search_btn.setObjectName(u"Customer_search_btn")
        self.Customer_search_btn.setFont(font)
        self.Customer_search_btn.setStyleSheet(u"border:2px solid black;\n"
"border-radius:12px;\n"
"padding:5px;")

        self.horizontalLayout_40.addWidget(self.Customer_search_btn)

        self.customer_deletebtn = QPushButton(self.frame_48)
        self.customer_deletebtn.setObjectName(u"customer_deletebtn")
        self.customer_deletebtn.setFont(font)
        self.customer_deletebtn.setStyleSheet(u"border:2px solid black;\n"
"border-radius:12px;\n"
"padding:5px;")

        self.horizontalLayout_40.addWidget(self.customer_deletebtn)


        self.verticalLayout_23.addWidget(self.frame_48, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.frame_49 = QFrame(self.frame_47)
        self.frame_49.setObjectName(u"frame_49")
        sizePolicy.setHeightForWidth(self.frame_49.sizePolicy().hasHeightForWidth())
        self.frame_49.setSizePolicy(sizePolicy)
        self.frame_49.setStyleSheet(u"border:none;\n"
"padding:0px;")
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.frame_49)
        self.horizontalLayout_41.setSpacing(0)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_4 = QStackedWidget(self.frame_49)
        self.stackedWidget_4.setObjectName(u"stackedWidget_4")
        self.stackedWidget_4.setStyleSheet(u"border:2px solid black;\n"
"border-radius:12px;\n"
"padding:5px;")
        self.purchase_history = QWidget()
        self.purchase_history.setObjectName(u"purchase_history")
        self.purchase_history.setStyleSheet(u"border:none;\n"
"padding:0px;")
        self.verticalLayout_18 = QVBoxLayout(self.purchase_history)
        self.verticalLayout_18.setSpacing(5)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.purchase_history_show_btn = QPushButton(self.purchase_history)
        self.purchase_history_show_btn.setObjectName(u"purchase_history_show_btn")
        self.purchase_history_show_btn.setFont(font)
        self.purchase_history_show_btn.setStyleSheet(u"border:2px solid black;\n"
"border-radius:12px;\n"
"padding:5px;")

        self.verticalLayout_18.addWidget(self.purchase_history_show_btn, 0, Qt.AlignHCenter)

        self.Purchase_history_table = QTableWidget(self.purchase_history)
        if (self.Purchase_history_table.columnCount() < 7):
            self.Purchase_history_table.setColumnCount(7)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font);
        self.Purchase_history_table.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font);
        self.Purchase_history_table.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font);
        self.Purchase_history_table.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font);
        self.Purchase_history_table.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font);
        self.Purchase_history_table.setHorizontalHeaderItem(4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font);
        self.Purchase_history_table.setHorizontalHeaderItem(5, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFont(font);
        self.Purchase_history_table.setHorizontalHeaderItem(6, __qtablewidgetitem13)
        self.Purchase_history_table.setObjectName(u"Purchase_history_table")

        self.verticalLayout_18.addWidget(self.Purchase_history_table)

        self.stackedWidget_4.addWidget(self.purchase_history)
        self.purchase_delete = QWidget()
        self.purchase_delete.setObjectName(u"purchase_delete")
        self.purchase_delete.setStyleSheet(u"border:none;\n"
"padding:0px;")
        self.horizontalLayout_43 = QHBoxLayout(self.purchase_delete)
        self.horizontalLayout_43.setSpacing(0)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.frame_50 = QFrame(self.purchase_delete)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_50)
        self.verticalLayout_24.setSpacing(5)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.frame_51 = QFrame(self.frame_50)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.gridLayout_18 = QGridLayout(self.frame_51)
        self.gridLayout_18.setSpacing(5)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setContentsMargins(0, 0, 0, 0)
        self.customer_search = QLineEdit(self.frame_51)
        self.customer_search.setObjectName(u"customer_search")
        self.customer_search.setMinimumSize(QSize(200, 0))
        self.customer_search.setMaximumSize(QSize(200, 16777215))
        self.customer_search.setFont(font)
        self.customer_search.setStyleSheet(u"border:2px solid black;\n"
"border-radius:12px;\n"
"padding:5px;")

        self.gridLayout_18.addWidget(self.customer_search, 0, 1, 1, 1)

        self.customer_search_btn = QPushButton(self.frame_51)
        self.customer_search_btn.setObjectName(u"customer_search_btn")
        self.customer_search_btn.setFont(font)
        self.customer_search_btn.setStyleSheet(u"border:2px solid black;\n"
"border-radius:12px;\n"
"padding:5px;")
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.customer_search_btn.setIcon(icon10)
        self.customer_search_btn.setIconSize(QSize(25, 25))

        self.gridLayout_18.addWidget(self.customer_search_btn, 0, 2, 1, 1)

        self.label_85 = QLabel(self.frame_51)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setFont(font)
        self.label_85.setStyleSheet(u"border:2px solid black;\n"
"border-radius:12px;\n"
"padding:5px;")

        self.gridLayout_18.addWidget(self.label_85, 0, 0, 1, 1)

        self.customer_confirm_delete_btn = QPushButton(self.frame_51)
        self.customer_confirm_delete_btn.setObjectName(u"customer_confirm_delete_btn")
        self.customer_confirm_delete_btn.setMinimumSize(QSize(100, 0))
        self.customer_confirm_delete_btn.setMaximumSize(QSize(100, 16777215))
        self.customer_confirm_delete_btn.setFont(font)
        self.customer_confirm_delete_btn.setStyleSheet(u"border:2px solid black;\n"
"border-radius:12px;\n"
"padding:5px;")

        self.gridLayout_18.addWidget(self.customer_confirm_delete_btn, 1, 1, 1, 1, Qt.AlignHCenter)


        self.verticalLayout_24.addWidget(self.frame_51, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.frame_52 = QFrame(self.frame_50)
        self.frame_52.setObjectName(u"frame_52")
        sizePolicy.setHeightForWidth(self.frame_52.sizePolicy().hasHeightForWidth())
        self.frame_52.setSizePolicy(sizePolicy)
        self.frame_52.setStyleSheet(u"border:2px solid black;\n"
"border-radius:12px;\n"
"padding:5px;")
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.frame_52)
        self.horizontalLayout_44.setSpacing(0)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.purchase_delete_table = QTableWidget(self.frame_52)
        if (self.purchase_delete_table.columnCount() < 7):
            self.purchase_delete_table.setColumnCount(7)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFont(font);
        self.purchase_delete_table.setHorizontalHeaderItem(0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setFont(font);
        self.purchase_delete_table.setHorizontalHeaderItem(1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setFont(font);
        self.purchase_delete_table.setHorizontalHeaderItem(2, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setFont(font);
        self.purchase_delete_table.setHorizontalHeaderItem(3, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setFont(font);
        self.purchase_delete_table.setHorizontalHeaderItem(4, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setFont(font);
        self.purchase_delete_table.setHorizontalHeaderItem(5, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setFont(font);
        self.purchase_delete_table.setHorizontalHeaderItem(6, __qtablewidgetitem20)
        self.purchase_delete_table.setObjectName(u"purchase_delete_table")
        self.purchase_delete_table.setStyleSheet(u"border:none;\n"
"padding:0px;")

        self.horizontalLayout_44.addWidget(self.purchase_delete_table)


        self.verticalLayout_24.addWidget(self.frame_52)


        self.horizontalLayout_43.addWidget(self.frame_50)

        self.stackedWidget_4.addWidget(self.purchase_delete)
        self.Customer_search_page = QWidget()
        self.Customer_search_page.setObjectName(u"Customer_search_page")
        self.Customer_search_page.setStyleSheet(u"border:none;")
        self.horizontalLayout_34 = QHBoxLayout(self.Customer_search_page)
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.frame_34 = QFrame(self.Customer_search_page)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_34)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.frame_35 = QFrame(self.frame_34)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setStyleSheet(u"border:2px solid black;\n"
"border-radius:12px;\n"
"padding:5px;")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_42.setSpacing(5)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.p_item = QComboBox(self.frame_35)
        self.p_item.addItem("")
        self.p_item.addItem("")
        self.p_item.setObjectName(u"p_item")
        self.p_item.setMinimumSize(QSize(100, 0))
        self.p_item.setMaximumSize(QSize(100, 16777215))
        self.p_item.setFont(font)

        self.horizontalLayout_42.addWidget(self.p_item)

        self.p_search = QLineEdit(self.frame_35)
        self.p_search.setObjectName(u"p_search")
        self.p_search.setMinimumSize(QSize(200, 0))
        self.p_search.setMaximumSize(QSize(200, 16777215))
        self.p_search.setFont(font)

        self.horizontalLayout_42.addWidget(self.p_search)

        self.p_serch_btn = QPushButton(self.frame_35)
        self.p_serch_btn.setObjectName(u"p_serch_btn")
        self.p_serch_btn.setFont(font)
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/user-search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.p_serch_btn.setIcon(icon11)
        self.p_serch_btn.setIconSize(QSize(30, 30))
        self.p_serch_btn.setFlat(False)

        self.horizontalLayout_42.addWidget(self.p_serch_btn)


        self.verticalLayout_19.addWidget(self.frame_35, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.frame_53 = QFrame(self.frame_34)
        self.frame_53.setObjectName(u"frame_53")
        sizePolicy.setHeightForWidth(self.frame_53.sizePolicy().hasHeightForWidth())
        self.frame_53.setSizePolicy(sizePolicy)
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_53)
        self.verticalLayout_25.setSpacing(5)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.frame_54 = QFrame(self.frame_53)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setStyleSheet(u"border:2px solid black;\n"
"border-radius:12px;\n"
"padding:5px;")
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.gridLayout_19 = QGridLayout(self.frame_54)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setContentsMargins(0, 0, 0, 0)
        self.p_contact = QLabel(self.frame_54)
        self.p_contact.setObjectName(u"p_contact")
        self.p_contact.setFont(font)
        self.p_contact.setAlignment(Qt.AlignCenter)

        self.gridLayout_19.addWidget(self.p_contact, 1, 1, 1, 1)

        self.p_gender = QLabel(self.frame_54)
        self.p_gender.setObjectName(u"p_gender")
        self.p_gender.setFont(font)
        self.p_gender.setAlignment(Qt.AlignCenter)

        self.gridLayout_19.addWidget(self.p_gender, 1, 2, 1, 1)

        self.p_name = QLabel(self.frame_54)
        self.p_name.setObjectName(u"p_name")
        self.p_name.setFont(font)
        self.p_name.setAlignment(Qt.AlignCenter)

        self.gridLayout_19.addWidget(self.p_name, 1, 0, 1, 1)

        self.p_date = QLabel(self.frame_54)
        self.p_date.setObjectName(u"p_date")
        self.p_date.setFont(font)
        self.p_date.setAlignment(Qt.AlignCenter)

        self.gridLayout_19.addWidget(self.p_date, 2, 0, 1, 1)

        self.p_cost = QLabel(self.frame_54)
        self.p_cost.setObjectName(u"p_cost")
        self.p_cost.setFont(font)
        self.p_cost.setAlignment(Qt.AlignCenter)

        self.gridLayout_19.addWidget(self.p_cost, 2, 1, 1, 1)

        self.p_qty = QLabel(self.frame_54)
        self.p_qty.setObjectName(u"p_qty")
        self.p_qty.setFont(font)
        self.p_qty.setAlignment(Qt.AlignCenter)

        self.gridLayout_19.addWidget(self.p_qty, 2, 2, 1, 1)

        self.p_id = QLabel(self.frame_54)
        self.p_id.setObjectName(u"p_id")
        self.p_id.setFont(font)
        self.p_id.setAlignment(Qt.AlignCenter)

        self.gridLayout_19.addWidget(self.p_id, 0, 1, 1, 1)


        self.verticalLayout_25.addWidget(self.frame_54)

        self.frame_55 = QFrame(self.frame_53)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setStyleSheet(u"border:2px solid black;\n"
"border-radius:12px;\n"
"padding:5px;")
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.frame_55)
        self.horizontalLayout_45.setSpacing(0)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.purchase_customer_table = QTableWidget(self.frame_55)
        if (self.purchase_customer_table.columnCount() < 4):
            self.purchase_customer_table.setColumnCount(4)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setFont(font);
        self.purchase_customer_table.setHorizontalHeaderItem(0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setFont(font);
        self.purchase_customer_table.setHorizontalHeaderItem(1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setFont(font);
        self.purchase_customer_table.setHorizontalHeaderItem(2, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setFont(font);
        self.purchase_customer_table.setHorizontalHeaderItem(3, __qtablewidgetitem24)
        self.purchase_customer_table.setObjectName(u"purchase_customer_table")
        self.purchase_customer_table.setStyleSheet(u"border:none;\n"
"padding:0px;")

        self.horizontalLayout_45.addWidget(self.purchase_customer_table)


        self.verticalLayout_25.addWidget(self.frame_55)


        self.verticalLayout_19.addWidget(self.frame_53)


        self.horizontalLayout_34.addWidget(self.frame_34)

        self.stackedWidget_4.addWidget(self.Customer_search_page)

        self.horizontalLayout_41.addWidget(self.stackedWidget_4)


        self.verticalLayout_23.addWidget(self.frame_49)


        self.horizontalLayout_38.addWidget(self.frame_47)

        self.stackedWidget_2.addWidget(self.Purchase)
        self.Inventory = QWidget()
        self.Inventory.setObjectName(u"Inventory")
        self.Inventory.setStyleSheet(u"border:none;")
        self.horizontalLayout_18 = QHBoxLayout(self.Inventory)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.frame_14 = QFrame(self.Inventory)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_14)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.Inventory_menu = QFrame(self.frame_14)
        self.Inventory_menu.setObjectName(u"Inventory_menu")
        self.Inventory_menu.setStyleSheet(u"QPushButton{\n"
"border:2px solid black;\n"
"border-radius:12px;\n"
"padding:10px;\n"
"}\n"
"QPushButton:hover{\n"
"border:2px solid black;\n"
"background-color: cyan;\n"
"color:black;\n"
"border-radius:12px;\n"
"padding:10px;\n"
"}")
        self.Inventory_menu.setFrameShape(QFrame.StyledPanel)
        self.Inventory_menu.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.Inventory_menu)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setHorizontalSpacing(5)
        self.gridLayout_7.setVerticalSpacing(0)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.insert_btn = QPushButton(self.Inventory_menu)
        self.insert_btn.setObjectName(u"insert_btn")
        self.insert_btn.setFont(font)

        self.gridLayout_7.addWidget(self.insert_btn, 0, 0, 1, 1)

        self.update_btn = QPushButton(self.Inventory_menu)
        self.update_btn.setObjectName(u"update_btn")
        self.update_btn.setFont(font)

        self.gridLayout_7.addWidget(self.update_btn, 0, 1, 1, 1)

        self.view_btn = QPushButton(self.Inventory_menu)
        self.view_btn.setObjectName(u"view_btn")
        self.view_btn.setFont(font)

        self.gridLayout_7.addWidget(self.view_btn, 0, 2, 1, 1)


        self.verticalLayout_10.addWidget(self.Inventory_menu, 0, Qt.AlignTop)

        self.Inventory_body = QFrame(self.frame_14)
        self.Inventory_body.setObjectName(u"Inventory_body")
        sizePolicy.setHeightForWidth(self.Inventory_body.sizePolicy().hasHeightForWidth())
        self.Inventory_body.setSizePolicy(sizePolicy)
        self.Inventory_body.setStyleSheet(u"border:2px solid black;\n"
"border-radius:12px;\n"
"padding:5px;")
        self.Inventory_body.setFrameShape(QFrame.StyledPanel)
        self.Inventory_body.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.Inventory_body)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_3 = QStackedWidget(self.Inventory_body)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.stackedWidget_3.setStyleSheet(u"border:none;")
        self.Insert = QWidget()
        self.Insert.setObjectName(u"Insert")
        self.gridLayout_9 = QGridLayout(self.Insert)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_16 = QFrame(self.Insert)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMaximumSize(QSize(2000, 16777215))
        font8 = QFont()
        font8.setBold(False)
        font8.setWeight(50)
        self.frame_16.setFont(font8)
        self.frame_16.setStyleSheet(u"border:2px solid black;\n"
"border-radius:12px;\n"
"padding:5px;")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.insert_table = QTableWidget(self.frame_16)
        if (self.insert_table.columnCount() < 7):
            self.insert_table.setColumnCount(7)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setFont(font);
        self.insert_table.setHorizontalHeaderItem(0, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setFont(font);
        self.insert_table.setHorizontalHeaderItem(1, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setFont(font);
        self.insert_table.setHorizontalHeaderItem(2, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setFont(font);
        self.insert_table.setHorizontalHeaderItem(3, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setFont(font);
        self.insert_table.setHorizontalHeaderItem(4, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setFont(font);
        self.insert_table.setHorizontalHeaderItem(5, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setFont(font);
        self.insert_table.setHorizontalHeaderItem(6, __qtablewidgetitem31)
        self.insert_table.setObjectName(u"insert_table")
        sizePolicy.setHeightForWidth(self.insert_table.sizePolicy().hasHeightForWidth())
        self.insert_table.setSizePolicy(sizePolicy)
        self.insert_table.setMaximumSize(QSize(16777215, 16777215))
        self.insert_table.setStyleSheet(u"border:none;\n"
"padding:0px;")

        self.horizontalLayout_20.addWidget(self.insert_table)


        self.gridLayout_9.addWidget(self.frame_16, 1, 0, 1, 1)

        self.frame_15 = QFrame(self.Insert)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(600, 200))
        self.frame_15.setStyleSheet(u"")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_15)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(5, 0, 0, 0)
        self.frame_18 = QFrame(self.frame_15)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setStyleSheet(u"border:2px solid black;\n"
"border-radius:12px;\n"
"padding:5px;\n"
"\n"
"QLineEdit{\n"
"color:white;\n"
"}\n"
"")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_18)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.m_name = QLineEdit(self.frame_18)
        self.m_name.setObjectName(u"m_name")
        self.m_name.setFont(font)
        self.m_name.setClearButtonEnabled(True)

        self.gridLayout_10.addWidget(self.m_name, 1, 1, 1, 1)

        self.label_43 = QLabel(self.frame_18)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setFont(font)

        self.gridLayout_10.addWidget(self.label_43, 1, 0, 1, 1)

        self.label_44 = QLabel(self.frame_18)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setFont(font)

        self.gridLayout_10.addWidget(self.label_44, 3, 0, 1, 1)

        self.best_before = QLineEdit(self.frame_18)
        self.best_before.setObjectName(u"best_before")
        self.best_before.setFont(font)

        self.gridLayout_10.addWidget(self.best_before, 4, 3, 1, 1)

        self.label_45 = QLabel(self.frame_18)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setFont(font)

        self.gridLayout_10.addWidget(self.label_45, 3, 2, 1, 1)

        self.Id = QLabel(self.frame_18)
        self.Id.setObjectName(u"Id")
        self.Id.setFont(font)
        self.Id.setStyleSheet(u"background-color: rgb(35, 38, 41);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_10.addWidget(self.Id, 0, 1, 1, 1)

        self.label_41 = QLabel(self.frame_18)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setFont(font)

        self.gridLayout_10.addWidget(self.label_41, 0, 0, 1, 1)

        self.label_46 = QLabel(self.frame_18)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setFont(font)

        self.gridLayout_10.addWidget(self.label_46, 4, 0, 1, 1)

        self.m_mfd = QDateEdit(self.frame_18)
        self.m_mfd.setObjectName(u"m_mfd")
        self.m_mfd.setFont(font)

        self.gridLayout_10.addWidget(self.m_mfd, 4, 1, 1, 1)

        self.m_sell = QLineEdit(self.frame_18)
        self.m_sell.setObjectName(u"m_sell")
        self.m_sell.setFont(font)
        self.m_sell.setClearButtonEnabled(True)

        self.gridLayout_10.addWidget(self.m_sell, 3, 3, 1, 1)

        self.label_24 = QLabel(self.frame_18)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font)

        self.gridLayout_10.addWidget(self.label_24, 4, 2, 1, 1)

        self.m_cost = QLineEdit(self.frame_18)
        self.m_cost.setObjectName(u"m_cost")
        self.m_cost.setFont(font)
        self.m_cost.setClearButtonEnabled(True)

        self.gridLayout_10.addWidget(self.m_cost, 3, 1, 1, 1)

        self.m_Exd = QLabel(self.frame_18)
        self.m_Exd.setObjectName(u"m_Exd")
        self.m_Exd.setFont(font)
        self.m_Exd.setStyleSheet(u"background-color: rgb(35, 38, 41);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_10.addWidget(self.m_Exd, 6, 1, 1, 1)

        self.label_47 = QLabel(self.frame_18)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setFont(font)

        self.gridLayout_10.addWidget(self.label_47, 6, 0, 1, 1)

        self.label_49 = QLabel(self.frame_18)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setFont(font)

        self.gridLayout_10.addWidget(self.label_49, 6, 2, 1, 1)

        self.m_Qty = QLineEdit(self.frame_18)
        self.m_Qty.setObjectName(u"m_Qty")
        self.m_Qty.setFont(font)
        self.m_Qty.setClearButtonEnabled(True)

        self.gridLayout_10.addWidget(self.m_Qty, 6, 3, 1, 1)


        self.verticalLayout_11.addWidget(self.frame_18)

        self.frame_17 = QFrame(self.frame_15)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setStyleSheet(u"QPushButton{\n"
"border:2px solid black;\n"
"border-radius:12px;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:2px solid black;\n"
"color:black;\n"
"background-color:cyan;\n"
"border-radius:12px;\n"
"padding:10px;\n"
"}")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_21.setSpacing(10)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.m_Add = QPushButton(self.frame_17)
        self.m_Add.setObjectName(u"m_Add")
        self.m_Add.setFont(font4)

        self.horizontalLayout_21.addWidget(self.m_Add)

        self.m_show = QPushButton(self.frame_17)
        self.m_show.setObjectName(u"m_show")
        self.m_show.setFont(font4)

        self.horizontalLayout_21.addWidget(self.m_show)


        self.verticalLayout_11.addWidget(self.frame_17, 0, Qt.AlignTop)


        self.gridLayout_9.addWidget(self.frame_15, 0, 0, 1, 1, Qt.AlignLeft|Qt.AlignTop)

        self.stackedWidget_3.addWidget(self.Insert)
        self.Update = QWidget()
        self.Update.setObjectName(u"Update")
        self.Update.setStyleSheet(u"border:none;\n"
"border-radius:0px;")
        self.verticalLayout_15 = QVBoxLayout(self.Update)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_29 = QFrame(self.Update)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_29)
        self.verticalLayout_16.setSpacing(5)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_25 = QFrame(self.frame_29)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setStyleSheet(u"border:2px solid black;\n"
"border-radius:12px;\n"
"padding:5px;")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_27.setSpacing(5)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.label_55 = QLabel(self.frame_25)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setFont(font)

        self.horizontalLayout_27.addWidget(self.label_55)

        self.update_search = QLineEdit(self.frame_25)
        self.update_search.setObjectName(u"update_search")
        self.update_search.setFont(font)
        self.update_search.setClearButtonEnabled(True)

        self.horizontalLayout_27.addWidget(self.update_search)

        self.update_search_btn = QPushButton(self.frame_25)
        self.update_search_btn.setObjectName(u"update_search_btn")
        self.update_search_btn.setFont(font)
        self.update_search_btn.setIcon(icon10)
        self.update_search_btn.setIconSize(QSize(25, 25))

        self.horizontalLayout_27.addWidget(self.update_search_btn)

        self.pushButton_3 = QPushButton(self.frame_25)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font)
        self.pushButton_3.setIcon(icon9)
        self.pushButton_3.setIconSize(QSize(25, 25))

        self.horizontalLayout_27.addWidget(self.pushButton_3)


        self.verticalLayout_16.addWidget(self.frame_25, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.frame_26 = QFrame(self.frame_29)
        self.frame_26.setObjectName(u"frame_26")
        sizePolicy.setHeightForWidth(self.frame_26.sizePolicy().hasHeightForWidth())
        self.frame_26.setSizePolicy(sizePolicy)
        self.frame_26.setMinimumSize(QSize(0, 0))
        self.frame_26.setMaximumSize(QSize(16777215, 16777215))
        self.frame_26.setStyleSheet(u"border:none;")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_26.setSpacing(5)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.frame_27 = QFrame(self.frame_26)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setStyleSheet(u"border:2px solid black;\n"
"border-radius:12px;\n"
"padding:5px;")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_27)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.label_56 = QLabel(self.frame_27)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setFont(font4)

        self.gridLayout_11.addWidget(self.label_56, 0, 0, 1, 1)

        self.u_id1 = QLabel(self.frame_27)
        self.u_id1.setObjectName(u"u_id1")
        self.u_id1.setFont(font)

        self.gridLayout_11.addWidget(self.u_id1, 0, 1, 1, 1)

        self.label_58 = QLabel(self.frame_27)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setFont(font4)

        self.gridLayout_11.addWidget(self.label_58, 1, 0, 1, 1)

        self.label_59 = QLabel(self.frame_27)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setFont(font4)

        self.gridLayout_11.addWidget(self.label_59, 2, 0, 1, 1)

        self.label_60 = QLabel(self.frame_27)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setFont(font4)

        self.gridLayout_11.addWidget(self.label_60, 3, 0, 1, 1)

        self.label_61 = QLabel(self.frame_27)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setFont(font4)

        self.gridLayout_11.addWidget(self.label_61, 4, 0, 1, 1)

        self.label_62 = QLabel(self.frame_27)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setFont(font4)

        self.gridLayout_11.addWidget(self.label_62, 5, 0, 1, 1)

        self.label_63 = QLabel(self.frame_27)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setFont(font4)

        self.gridLayout_11.addWidget(self.label_63, 6, 0, 1, 1)

        self.uname1 = QLabel(self.frame_27)
        self.uname1.setObjectName(u"uname1")
        self.uname1.setFont(font)

        self.gridLayout_11.addWidget(self.uname1, 1, 1, 1, 1)

        self.u_cprice1 = QLabel(self.frame_27)
        self.u_cprice1.setObjectName(u"u_cprice1")
        self.u_cprice1.setFont(font)

        self.gridLayout_11.addWidget(self.u_cprice1, 2, 1, 1, 1)

        self.u_sprice1 = QLabel(self.frame_27)
        self.u_sprice1.setObjectName(u"u_sprice1")
        self.u_sprice1.setFont(font)

        self.gridLayout_11.addWidget(self.u_sprice1, 3, 1, 1, 1)

        self.u_mfd1 = QLabel(self.frame_27)
        self.u_mfd1.setObjectName(u"u_mfd1")
        self.u_mfd1.setFont(font)

        self.gridLayout_11.addWidget(self.u_mfd1, 4, 1, 1, 1)

        self.u_exd1 = QLabel(self.frame_27)
        self.u_exd1.setObjectName(u"u_exd1")
        self.u_exd1.setFont(font)

        self.gridLayout_11.addWidget(self.u_exd1, 5, 1, 1, 1)

        self.u_qty1 = QLabel(self.frame_27)
        self.u_qty1.setObjectName(u"u_qty1")
        self.u_qty1.setFont(font)

        self.gridLayout_11.addWidget(self.u_qty1, 6, 1, 1, 1)


        self.horizontalLayout_26.addWidget(self.frame_27)

        self.frame_28 = QFrame(self.frame_26)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setStyleSheet(u"border:2px solid black;\n"
"border-radius:12px;\n"
"padding:5px;")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_28)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.label_73 = QLabel(self.frame_28)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setFont(font4)

        self.gridLayout_12.addWidget(self.label_73, 4, 0, 1, 1)

        self.label_76 = QLabel(self.frame_28)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setFont(font4)

        self.gridLayout_12.addWidget(self.label_76, 2, 0, 1, 1)

        self.u_sprice2 = QLineEdit(self.frame_28)
        self.u_sprice2.setObjectName(u"u_sprice2")
        self.u_sprice2.setFont(font)
        self.u_sprice2.setClearButtonEnabled(True)

        self.gridLayout_12.addWidget(self.u_sprice2, 3, 1, 1, 1)

        self.u_cprice2 = QLineEdit(self.frame_28)
        self.u_cprice2.setObjectName(u"u_cprice2")
        self.u_cprice2.setFont(font)
        self.u_cprice2.setClearButtonEnabled(True)

        self.gridLayout_12.addWidget(self.u_cprice2, 2, 1, 1, 1)

        self.u_mfd2 = QDateEdit(self.frame_28)
        self.u_mfd2.setObjectName(u"u_mfd2")
        self.u_mfd2.setFont(font)

        self.gridLayout_12.addWidget(self.u_mfd2, 4, 1, 1, 1)

        self.u_qty2 = QLineEdit(self.frame_28)
        self.u_qty2.setObjectName(u"u_qty2")
        self.u_qty2.setFont(font)
        self.u_qty2.setClearButtonEnabled(True)

        self.gridLayout_12.addWidget(self.u_qty2, 5, 1, 1, 1)

        self.label_72 = QLabel(self.frame_28)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setFont(font4)

        self.gridLayout_12.addWidget(self.label_72, 3, 0, 1, 1)

        self.label_70 = QLabel(self.frame_28)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setFont(font4)

        self.gridLayout_12.addWidget(self.label_70, 0, 0, 1, 1)

        self.u_id2 = QLabel(self.frame_28)
        self.u_id2.setObjectName(u"u_id2")
        self.u_id2.setFont(font)

        self.gridLayout_12.addWidget(self.u_id2, 0, 1, 1, 1)

        self.label_75 = QLabel(self.frame_28)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setFont(font4)

        self.gridLayout_12.addWidget(self.label_75, 5, 0, 1, 1)

        self.uname2 = QLineEdit(self.frame_28)
        self.uname2.setObjectName(u"uname2")
        self.uname2.setFont(font)
        self.uname2.setClearButtonEnabled(True)

        self.gridLayout_12.addWidget(self.uname2, 1, 1, 1, 1)

        self.label_71 = QLabel(self.frame_28)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setFont(font4)

        self.gridLayout_12.addWidget(self.label_71, 1, 0, 1, 1)


        self.horizontalLayout_26.addWidget(self.frame_28, 0, Qt.AlignTop)


        self.verticalLayout_16.addWidget(self.frame_26, 0, Qt.AlignHCenter)

        self.frame_30 = QFrame(self.frame_29)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setStyleSheet(u"")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.confirm_update_btn = QPushButton(self.frame_30)
        self.confirm_update_btn.setObjectName(u"confirm_update_btn")
        self.confirm_update_btn.setFont(font)
        self.confirm_update_btn.setStyleSheet(u"border:2px solid black;\n"
"border-radius:12px;\n"
"padding:5px;")

        self.horizontalLayout_28.addWidget(self.confirm_update_btn)


        self.verticalLayout_16.addWidget(self.frame_30, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.frame_30.raise_()
        self.frame_26.raise_()
        self.frame_25.raise_()

        self.verticalLayout_15.addWidget(self.frame_29, 0, Qt.AlignTop)

        self.stackedWidget_3.addWidget(self.Update)
        self.View = QWidget()
        self.View.setObjectName(u"View")
        self.View.setStyleSheet(u"")
        self.horizontalLayout_24 = QHBoxLayout(self.View)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.frame_22 = QFrame(self.View)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_22)
        self.verticalLayout_14.setSpacing(10)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_23 = QFrame(self.frame_22)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setStyleSheet(u"border:none;\n"
"padding:0px;")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_25.setSpacing(10)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(5, 5, 5, 5)
        self.label_32 = QLabel(self.frame_23)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font4)
        self.label_32.setStyleSheet(u"border:2px solid black;\n"
"border-radius:12px;\n"
"padding:5px;")

        self.horizontalLayout_25.addWidget(self.label_32)

        self.view_search = QLineEdit(self.frame_23)
        self.view_search.setObjectName(u"view_search")
        self.view_search.setFont(font4)
        self.view_search.setStyleSheet(u"border:2px solid black;\n"
"border-radius:12px;\n"
"padding:5px;")
        self.view_search.setClearButtonEnabled(True)

        self.horizontalLayout_25.addWidget(self.view_search)

        self.view_search_btn = QPushButton(self.frame_23)
        self.view_search_btn.setObjectName(u"view_search_btn")
        self.view_search_btn.setFont(font4)
        self.view_search_btn.setStyleSheet(u"border:2px solid black;\n"
"border-radius:12px;\n"
"padding:5px;")
        self.view_search_btn.setIcon(icon10)
        self.view_search_btn.setIconSize(QSize(25, 25))

        self.horizontalLayout_25.addWidget(self.view_search_btn)

        self.view_clear_btn = QPushButton(self.frame_23)
        self.view_clear_btn.setObjectName(u"view_clear_btn")
        self.view_clear_btn.setFont(font)
        self.view_clear_btn.setStyleSheet(u"border:2px solid black;\n"
"border-radius:12px;\n"
"padding:5px;")
        self.view_clear_btn.setIcon(icon9)
        self.view_clear_btn.setIconSize(QSize(25, 25))

        self.horizontalLayout_25.addWidget(self.view_clear_btn)


        self.verticalLayout_14.addWidget(self.frame_23, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.frame_24 = QFrame(self.frame_22)
        self.frame_24.setObjectName(u"frame_24")
        sizePolicy.setHeightForWidth(self.frame_24.sizePolicy().hasHeightForWidth())
        self.frame_24.setSizePolicy(sizePolicy)
        self.frame_24.setMinimumSize(QSize(600, 400))
        self.frame_24.setMaximumSize(QSize(600, 16777215))
        self.frame_24.setStyleSheet(u"border:none;\n"
"padding:0px;")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_24)
        self.gridLayout_8.setSpacing(5)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_50 = QLabel(self.frame_24)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setFont(font1)
        self.label_50.setStyleSheet(u"border:2px solid black;\n"
"border-radius:12px;\n"
"padding:5px;")
        self.label_50.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_50, 2, 0, 1, 1)

        self.label_42 = QLabel(self.frame_24)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setFont(font1)
        self.label_42.setStyleSheet(u"border:2px solid black;\n"
"border-radius:12px;\n"
"padding:5px;")
        self.label_42.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_42, 0, 0, 1, 1)

        self.label_54 = QLabel(self.frame_24)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setFont(font1)
        self.label_54.setStyleSheet(u"border:2px solid black;\n"
"border-radius:12px;\n"
"padding:5px;")
        self.label_54.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_54, 6, 0, 1, 1)

        self.label_51 = QLabel(self.frame_24)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setFont(font1)
        self.label_51.setStyleSheet(u"border:2px solid black;\n"
"border-radius:12px;\n"
"padding:5px;")
        self.label_51.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_51, 4, 0, 1, 1)

        self.label_53 = QLabel(self.frame_24)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setFont(font1)
        self.label_53.setStyleSheet(u"border:2px solid black;\n"
"border-radius:12px;\n"
"padding:5px;")
        self.label_53.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_53, 3, 0, 1, 1)

        self.label_48 = QLabel(self.frame_24)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setFont(font1)
        self.label_48.setStyleSheet(u"border:2px solid black;\n"
"border-radius:12px;\n"
"padding:5px;")
        self.label_48.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_48, 1, 0, 1, 1)

        self.label_52 = QLabel(self.frame_24)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setFont(font1)
        self.label_52.setStyleSheet(u"border:2px solid black;\n"
"border-radius:12px;\n"
"padding:5px;")
        self.label_52.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_52, 5, 0, 1, 1)

        self.view_id = QLabel(self.frame_24)
        self.view_id.setObjectName(u"view_id")
        self.view_id.setFont(font)
        self.view_id.setStyleSheet(u"border:2px solid black;\n"
"border-radius:12px;\n"
"padding:5px;")
        self.view_id.setAlignment(Qt.AlignCenter)
        self.view_id.setWordWrap(True)

        self.gridLayout_8.addWidget(self.view_id, 0, 1, 1, 1)

        self.view_name = QLabel(self.frame_24)
        self.view_name.setObjectName(u"view_name")
        self.view_name.setFont(font)
        self.view_name.setStyleSheet(u"border:2px solid black;\n"
"border-radius:12px;\n"
"padding:5px;")
        self.view_name.setAlignment(Qt.AlignCenter)
        self.view_name.setWordWrap(True)

        self.gridLayout_8.addWidget(self.view_name, 1, 1, 1, 1)

        self.view_cost = QLabel(self.frame_24)
        self.view_cost.setObjectName(u"view_cost")
        self.view_cost.setFont(font)
        self.view_cost.setStyleSheet(u"border:2px solid black;\n"
"border-radius:12px;\n"
"padding:5px;")
        self.view_cost.setAlignment(Qt.AlignCenter)
        self.view_cost.setWordWrap(True)

        self.gridLayout_8.addWidget(self.view_cost, 2, 1, 1, 1)

        self.view_sell = QLabel(self.frame_24)
        self.view_sell.setObjectName(u"view_sell")
        self.view_sell.setFont(font)
        self.view_sell.setStyleSheet(u"border:2px solid black;\n"
"border-radius:12px;\n"
"padding:5px;")
        self.view_sell.setAlignment(Qt.AlignCenter)
        self.view_sell.setWordWrap(True)

        self.gridLayout_8.addWidget(self.view_sell, 3, 1, 1, 1)

        self.view_mfd = QLabel(self.frame_24)
        self.view_mfd.setObjectName(u"view_mfd")
        self.view_mfd.setFont(font)
        self.view_mfd.setStyleSheet(u"border:2px solid black;\n"
"border-radius:12px;\n"
"padding:5px;")
        self.view_mfd.setAlignment(Qt.AlignCenter)
        self.view_mfd.setWordWrap(True)

        self.gridLayout_8.addWidget(self.view_mfd, 4, 1, 1, 1)

        self.view_exd = QLabel(self.frame_24)
        self.view_exd.setObjectName(u"view_exd")
        self.view_exd.setFont(font)
        self.view_exd.setStyleSheet(u"border:2px solid black;\n"
"border-radius:12px;\n"
"padding:5px;")
        self.view_exd.setAlignment(Qt.AlignCenter)
        self.view_exd.setWordWrap(True)

        self.gridLayout_8.addWidget(self.view_exd, 5, 1, 1, 1)

        self.view_qty = QLabel(self.frame_24)
        self.view_qty.setObjectName(u"view_qty")
        self.view_qty.setFont(font)
        self.view_qty.setStyleSheet(u"border:2px solid black;\n"
"border-radius:12px;\n"
"padding:5px;")
        self.view_qty.setAlignment(Qt.AlignCenter)
        self.view_qty.setWordWrap(True)

        self.gridLayout_8.addWidget(self.view_qty, 6, 1, 1, 1)


        self.verticalLayout_14.addWidget(self.frame_24, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_24.addWidget(self.frame_22, 0, Qt.AlignTop)

        self.stackedWidget_3.addWidget(self.View)

        self.horizontalLayout_19.addWidget(self.stackedWidget_3)


        self.verticalLayout_10.addWidget(self.Inventory_body)


        self.horizontalLayout_18.addWidget(self.frame_14)

        self.stackedWidget_2.addWidget(self.Inventory)
        self.Customer = QWidget()
        self.Customer.setObjectName(u"Customer")
        self.Customer.setStyleSheet(u"border:none;\n"
"padding:0px;")
        self.horizontalLayout_33 = QHBoxLayout(self.Customer)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.frame_36 = QFrame(self.Customer)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setStyleSheet(u"border:none;\n"
"padding:0px;")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.frame_36)
        self.gridLayout_13.setSpacing(5)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_39 = QFrame(self.frame_36)
        self.frame_39.setObjectName(u"frame_39")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_39.sizePolicy().hasHeightForWidth())
        self.frame_39.setSizePolicy(sizePolicy3)
        self.frame_39.setMinimumSize(QSize(500, 0))
        self.frame_39.setMaximumSize(QSize(500, 16777215))
        self.frame_39.setStyleSheet(u"border:none;")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_36.setSpacing(0)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.frame_42 = QFrame(self.frame_39)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setStyleSheet(u"border:2px solid black;\n"
"border-radius:12px;\n"
"padding:5px;")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_42)
        self.verticalLayout_20.setSpacing(5)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_43 = QFrame(self.frame_42)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setStyleSheet(u"border:none;")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.gridLayout_16 = QGridLayout(self.frame_43)
        self.gridLayout_16.setSpacing(0)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_46 = QFrame(self.frame_43)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setStyleSheet(u"border:none;")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.gridLayout_17 = QGridLayout(self.frame_46)
        self.gridLayout_17.setSpacing(0)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setContentsMargins(0, 0, 0, 0)
        self.customer_totalcost = QLabel(self.frame_46)
        self.customer_totalcost.setObjectName(u"customer_totalcost")
        self.customer_totalcost.setFont(font1)

        self.gridLayout_17.addWidget(self.customer_totalcost, 2, 1, 1, 1)

        self.customer_date = QLabel(self.frame_46)
        self.customer_date.setObjectName(u"customer_date")
        self.customer_date.setFont(font1)

        self.gridLayout_17.addWidget(self.customer_date, 0, 1, 1, 1)

        self.customer_show_id = QLabel(self.frame_46)
        self.customer_show_id.setObjectName(u"customer_show_id")
        self.customer_show_id.setFont(font1)

        self.gridLayout_17.addWidget(self.customer_show_id, 1, 1, 1, 1)

        self.label_82 = QLabel(self.frame_46)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setFont(font4)

        self.gridLayout_17.addWidget(self.label_82, 0, 0, 1, 1)

        self.label_83 = QLabel(self.frame_46)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setFont(font4)

        self.gridLayout_17.addWidget(self.label_83, 1, 0, 1, 1)

        self.label_84 = QLabel(self.frame_46)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setFont(font4)

        self.gridLayout_17.addWidget(self.label_84, 2, 0, 1, 1)


        self.gridLayout_16.addWidget(self.frame_46, 2, 1, 1, 1, Qt.AlignHCenter|Qt.AlignTop)

        self.label_67 = QLabel(self.frame_43)
        self.label_67.setObjectName(u"label_67")
        font9 = QFont()
        font9.setPointSize(13)
        font9.setBold(True)
        font9.setWeight(75)
        self.label_67.setFont(font9)

        self.gridLayout_16.addWidget(self.label_67, 1, 1, 1, 1, Qt.AlignHCenter)

        self.label_66 = QLabel(self.frame_43)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setFont(font2)

        self.gridLayout_16.addWidget(self.label_66, 0, 1, 1, 1, Qt.AlignHCenter)


        self.verticalLayout_20.addWidget(self.frame_43)

        self.frame_44 = QFrame(self.frame_42)
        self.frame_44.setObjectName(u"frame_44")
        sizePolicy.setHeightForWidth(self.frame_44.sizePolicy().hasHeightForWidth())
        self.frame_44.setSizePolicy(sizePolicy)
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_44)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.frame_41 = QFrame(self.frame_44)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setStyleSheet(u"border:none;\n"
"border-radius:0px;\n"
"\n"
"padding:1px;")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_39.setSpacing(2)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 5)
        self.label_68 = QLabel(self.frame_41)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setFont(font)
        self.label_68.setStyleSheet(u"background-color: rgb(35, 38, 41);\n"
"color: rgb(255, 255, 255);")
        self.label_68.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_39.addWidget(self.label_68)

        self.label_69 = QLabel(self.frame_41)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setFont(font)
        self.label_69.setStyleSheet(u"background-color: rgb(35, 38, 41);\n"
"color: rgb(255, 255, 255);")
        self.label_69.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_39.addWidget(self.label_69)

        self.label_74 = QLabel(self.frame_41)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setFont(font)
        self.label_74.setStyleSheet(u"background-color: rgb(35, 38, 41);\n"
"color: rgb(255, 255, 255);")
        self.label_74.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_39.addWidget(self.label_74)


        self.verticalLayout_21.addWidget(self.frame_41)

        self.scrollArea_2 = QScrollArea(self.frame_44)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setStyleSheet(u"border:none;\n"
"padding:1px;")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 449, 347))
        self.verticalLayout_22 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.custome_data_field = QLabel(self.scrollAreaWidgetContents_2)
        self.custome_data_field.setObjectName(u"custome_data_field")
        sizePolicy.setHeightForWidth(self.custome_data_field.sizePolicy().hasHeightForWidth())
        self.custome_data_field.setSizePolicy(sizePolicy)
        font10 = QFont()
        font10.setPointSize(10)
        font10.setBold(False)
        font10.setWeight(50)
        self.custome_data_field.setFont(font10)
        self.custome_data_field.setWordWrap(True)

        self.verticalLayout_22.addWidget(self.custome_data_field)

        self.customer_qrcode = QLabel(self.scrollAreaWidgetContents_2)
        self.customer_qrcode.setObjectName(u"customer_qrcode")
        sizePolicy3.setHeightForWidth(self.customer_qrcode.sizePolicy().hasHeightForWidth())
        self.customer_qrcode.setSizePolicy(sizePolicy3)
        self.customer_qrcode.setMinimumSize(QSize(300, 300))
        self.customer_qrcode.setMaximumSize(QSize(300, 300))
        self.customer_qrcode.setFont(font10)
        self.customer_qrcode.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border:2px solid black;\n"
"border-radius:12px;\n"
"padding:5px;")
        self.customer_qrcode.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.customer_qrcode, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_21.addWidget(self.scrollArea_2)


        self.verticalLayout_20.addWidget(self.frame_44)

        self.frame_45 = QFrame(self.frame_42)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setStyleSheet(u"border:none;")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_45)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.frame_45)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(u"\n"
"QPushButton{\n"
"border:2px solid black;\n"
"border-radius:12px;\n"
"padding:5px;\n"
"}\n"
"QPushButton:hover{\n"
"border:2px solid black;\n"
"background-color: cyan;\n"
"color:black;\n"
"border-radius:12px;\n"
"padding:5px;\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/printer.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon12)
        self.pushButton_2.setIconSize(QSize(25, 25))

        self.horizontalLayout_37.addWidget(self.pushButton_2)

        self.customer_clear = QPushButton(self.frame_45)
        self.customer_clear.setObjectName(u"customer_clear")
        self.customer_clear.setFont(font)
        self.customer_clear.setStyleSheet(u"\n"
"QPushButton{\n"
"border:2px solid black;\n"
"border-radius:12px;\n"
"padding:5px;\n"
"}\n"
"QPushButton:hover{\n"
"border:2px solid black;\n"
"background-color: cyan;\n"
"color:black;\n"
"border-radius:12px;\n"
"padding:5px;\n"
"}")
        self.customer_clear.setIcon(icon9)
        self.customer_clear.setIconSize(QSize(25, 25))

        self.horizontalLayout_37.addWidget(self.customer_clear)


        self.verticalLayout_20.addWidget(self.frame_45, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.horizontalLayout_36.addWidget(self.frame_42)


        self.gridLayout_13.addWidget(self.frame_39, 0, 3, 2, 1, Qt.AlignRight)

        self.frame_38 = QFrame(self.frame_36)
        self.frame_38.setObjectName(u"frame_38")
        sizePolicy2.setHeightForWidth(self.frame_38.sizePolicy().hasHeightForWidth())
        self.frame_38.setSizePolicy(sizePolicy2)
        self.frame_38.setMinimumSize(QSize(0, 0))
        self.frame_38.setMaximumSize(QSize(16777215, 16777215))
        self.frame_38.setStyleSheet(u"border:2px solid black;\n"
"border-radius:12px;\n"
"padding:3px;")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.customer_table = QTableWidget(self.frame_38)
        if (self.customer_table.columnCount() < 4):
            self.customer_table.setColumnCount(4)
        __qtablewidgetitem32 = QTableWidgetItem()
        __qtablewidgetitem32.setFont(font);
        self.customer_table.setHorizontalHeaderItem(0, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        __qtablewidgetitem33.setFont(font);
        self.customer_table.setHorizontalHeaderItem(1, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        __qtablewidgetitem34.setFont(font);
        self.customer_table.setHorizontalHeaderItem(2, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        __qtablewidgetitem35.setFont(font);
        self.customer_table.setHorizontalHeaderItem(3, __qtablewidgetitem35)
        self.customer_table.setObjectName(u"customer_table")
        self.customer_table.setStyleSheet(u"border:none;\n"
"padding:0px;")

        self.horizontalLayout_35.addWidget(self.customer_table)


        self.gridLayout_13.addWidget(self.frame_38, 1, 0, 1, 3)

        self.frame_37 = QFrame(self.frame_36)
        self.frame_37.setObjectName(u"frame_37")
        sizePolicy1.setHeightForWidth(self.frame_37.sizePolicy().hasHeightForWidth())
        self.frame_37.setSizePolicy(sizePolicy1)
        self.frame_37.setMinimumSize(QSize(700, 270))
        self.frame_37.setMaximumSize(QSize(700, 270))
        self.frame_37.setStyleSheet(u"border:none;")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.gridLayout_15 = QGridLayout(self.frame_37)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setHorizontalSpacing(5)
        self.gridLayout_15.setVerticalSpacing(0)
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_40 = QFrame(self.frame_37)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setStyleSheet(u"border:2px solid black;\n"
"border-radius:12px;\n"
"padding:5px;\n"
"")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.frame_40)
        self.gridLayout_14.setSpacing(5)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_77 = QLabel(self.frame_40)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setFont(font4)

        self.gridLayout_14.addWidget(self.label_77, 5, 0, 1, 1)

        self.c_add_btn = QPushButton(self.frame_40)
        self.c_add_btn.setObjectName(u"c_add_btn")
        self.c_add_btn.setFont(font)
        self.c_add_btn.setStyleSheet(u"QPushButton{\n"
"border:2px solid black;\n"
"border-radius:12px;\n"
"padding:5px;\n"
"}\n"
"QPushButton:hover{\n"
"border:2px solid black;\n"
"background-color: cyan;\n"
"color:black;\n"
"border-radius:12px;\n"
"padding:5px;\n"
"}")

        self.gridLayout_14.addWidget(self.c_add_btn, 6, 2, 1, 1)

        self.c_phno = QLineEdit(self.frame_40)
        self.c_phno.setObjectName(u"c_phno")
        self.c_phno.setFont(font)
        self.c_phno.setClearButtonEnabled(True)

        self.gridLayout_14.addWidget(self.c_phno, 2, 1, 1, 1)

        self.c_display_cost = QLabel(self.frame_40)
        self.c_display_cost.setObjectName(u"c_display_cost")
        font11 = QFont()
        font11.setPointSize(22)
        font11.setBold(True)
        font11.setWeight(75)
        self.c_display_cost.setFont(font11)
        self.c_display_cost.setAlignment(Qt.AlignCenter)

        self.gridLayout_14.addWidget(self.c_display_cost, 0, 2, 6, 3)

        self.c_m_id = QLineEdit(self.frame_40)
        self.c_m_id.setObjectName(u"c_m_id")
        self.c_m_id.setFont(font)
        self.c_m_id.setClearButtonEnabled(True)

        self.gridLayout_14.addWidget(self.c_m_id, 4, 1, 1, 1)

        self.label_57 = QLabel(self.frame_40)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setFont(font4)

        self.gridLayout_14.addWidget(self.label_57, 2, 0, 1, 1)

        self.label_64 = QLabel(self.frame_40)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setFont(font4)

        self.gridLayout_14.addWidget(self.label_64, 3, 0, 1, 1)

        self.c_name = QLineEdit(self.frame_40)
        self.c_name.setObjectName(u"c_name")
        self.c_name.setFont(font)
        self.c_name.setClearButtonEnabled(True)

        self.gridLayout_14.addWidget(self.c_name, 1, 1, 1, 1)

        self.label_65 = QLabel(self.frame_40)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setFont(font4)

        self.gridLayout_14.addWidget(self.label_65, 4, 0, 1, 1)

        self.c_new_id_btn = QPushButton(self.frame_40)
        self.c_new_id_btn.setObjectName(u"c_new_id_btn")
        self.c_new_id_btn.setFont(font)
        self.c_new_id_btn.setStyleSheet(u"QPushButton{\n"
"border:2px solid black;\n"
"border-radius:12px;\n"
"padding:5px;\n"
"}\n"
"QPushButton:hover{\n"
"border:2px solid black;\n"
"background-color: cyan;\n"
"color:black;\n"
"border-radius:12px;\n"
"padding:5px;\n"
"}")

        self.gridLayout_14.addWidget(self.c_new_id_btn, 6, 3, 1, 1)

        self.c_id = QLabel(self.frame_40)
        self.c_id.setObjectName(u"c_id")
        font12 = QFont()
        font12.setPointSize(9)
        font12.setBold(True)
        font12.setWeight(75)
        self.c_id.setFont(font12)
        self.c_id.setStyleSheet(u"background-color: rgb(35, 38, 41);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_14.addWidget(self.c_id, 0, 1, 1, 1, Qt.AlignTop)

        self.label_81 = QLabel(self.frame_40)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setFont(font4)

        self.gridLayout_14.addWidget(self.label_81, 0, 0, 1, 1, Qt.AlignTop)

        self.label_11 = QLabel(self.frame_40)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font4)

        self.gridLayout_14.addWidget(self.label_11, 1, 0, 1, 1)

        self.c_show_btn = QPushButton(self.frame_40)
        self.c_show_btn.setObjectName(u"c_show_btn")
        self.c_show_btn.setFont(font)
        self.c_show_btn.setStyleSheet(u"QPushButton{\n"
"border:2px solid black;\n"
"border-radius:12px;\n"
"padding:5px;\n"
"}\n"
"QPushButton:hover{\n"
"border:2px solid black;\n"
"background-color: cyan;\n"
"color:black;\n"
"border-radius:12px;\n"
"padding:5px;\n"
"}")

        self.gridLayout_14.addWidget(self.c_show_btn, 6, 4, 1, 1)

        self.c_m_qty = QLineEdit(self.frame_40)
        self.c_m_qty.setObjectName(u"c_m_qty")
        self.c_m_qty.setFont(font)
        self.c_m_qty.setClearButtonEnabled(True)

        self.gridLayout_14.addWidget(self.c_m_qty, 5, 1, 1, 1)

        self.c_gender = QComboBox(self.frame_40)
        self.c_gender.addItem("")
        self.c_gender.addItem("")
        self.c_gender.setObjectName(u"c_gender")
        self.c_gender.setFont(font)

        self.gridLayout_14.addWidget(self.c_gender, 3, 1, 1, 1)


        self.gridLayout_15.addWidget(self.frame_40, 1, 0, 1, 1)


        self.gridLayout_13.addWidget(self.frame_37, 0, 0, 1, 1)

        self.frame_37.raise_()
        self.frame_39.raise_()
        self.frame_38.raise_()

        self.horizontalLayout_33.addWidget(self.frame_36)

        self.stackedWidget_2.addWidget(self.Customer)
        self.Report = QWidget()
        self.Report.setObjectName(u"Report")
        self.Report.setStyleSheet(u"border:none;\n"
"padding:0px;")
        self.horizontalLayout_22 = QHBoxLayout(self.Report)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.frame_20 = QFrame(self.Report)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setStyleSheet(u"border:none;")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_20)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_21 = QFrame(self.frame_20)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.frame_58 = QFrame(self.frame_21)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setStyleSheet(u"border:2px solid black;\n"
"border-radius:12px;\n"
"padding:5px;\n"
"")
        self.frame_58.setFrameShape(QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.gridLayout_21 = QGridLayout(self.frame_58)
        self.gridLayout_21.setSpacing(5)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setContentsMargins(5, 5, 5, 5)
        self.label_89 = QLabel(self.frame_58)
        self.label_89.setObjectName(u"label_89")
        self.label_89.setMinimumSize(QSize(200, 0))
        self.label_89.setFont(font)

        self.gridLayout_21.addWidget(self.label_89, 5, 1, 1, 1)

        self.label_10 = QLabel(self.frame_58)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(200, 0))
        self.label_10.setFont(font)

        self.gridLayout_21.addWidget(self.label_10, 1, 1, 1, 1)

        self.label_88 = QLabel(self.frame_58)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setMinimumSize(QSize(200, 0))
        self.label_88.setFont(font)

        self.gridLayout_21.addWidget(self.label_88, 4, 1, 1, 1)

        self.label_29 = QLabel(self.frame_58)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font9)

        self.gridLayout_21.addWidget(self.label_29, 5, 0, 1, 1)

        self.label_12 = QLabel(self.frame_58)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font9)

        self.gridLayout_21.addWidget(self.label_12, 2, 0, 1, 1)

        self.label_14 = QLabel(self.frame_58)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font9)

        self.gridLayout_21.addWidget(self.label_14, 4, 0, 1, 1)

        self.label_9 = QLabel(self.frame_58)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font9)

        self.gridLayout_21.addWidget(self.label_9, 1, 0, 1, 1)

        self.label_13 = QLabel(self.frame_58)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font9)

        self.gridLayout_21.addWidget(self.label_13, 3, 0, 1, 1)

        self.label_34 = QLabel(self.frame_58)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(200, 0))
        self.label_34.setFont(font)

        self.gridLayout_21.addWidget(self.label_34, 2, 1, 1, 1)

        self.label_87 = QLabel(self.frame_58)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setMinimumSize(QSize(200, 0))
        self.label_87.setFont(font)

        self.gridLayout_21.addWidget(self.label_87, 3, 1, 1, 1)

        self.label_7 = QLabel(self.frame_58)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font9)

        self.gridLayout_21.addWidget(self.label_7, 0, 0, 1, 1)

        self.label_8 = QLabel(self.frame_58)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(200, 0))
        self.label_8.setFont(font)

        self.gridLayout_21.addWidget(self.label_8, 0, 1, 1, 1)

        self.report_show_btn = QPushButton(self.frame_58)
        self.report_show_btn.setObjectName(u"report_show_btn")
        self.report_show_btn.setFont(font9)

        self.gridLayout_21.addWidget(self.report_show_btn, 6, 1, 1, 1)


        self.horizontalLayout_46.addWidget(self.frame_58)

        self.frame_57 = QFrame(self.frame_21)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setMinimumSize(QSize(500, 300))
        self.frame_57.setMaximumSize(QSize(500, 300))
        self.frame_57.setStyleSheet(u"border:2px solid black;\n"
"border-radius:12px;\n"
"padding:5px;\n"
"")
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_57)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.calendarWidget = QCalendarWidget(self.frame_57)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setFont(font)
        self.calendarWidget.setStyleSheet(u"border:none;")

        self.horizontalLayout_23.addWidget(self.calendarWidget)


        self.horizontalLayout_46.addWidget(self.frame_57)


        self.verticalLayout_13.addWidget(self.frame_21, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_56 = QFrame(self.frame_20)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setStyleSheet(u"border:2px solid black;\n"
"border-radius:12px;\n"
"padding:1px;\n"
"")
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_47 = QHBoxLayout(self.frame_56)
        self.horizontalLayout_47.setSpacing(0)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.Purchase_history_table_2 = QTableWidget(self.frame_56)
        if (self.Purchase_history_table_2.columnCount() < 7):
            self.Purchase_history_table_2.setColumnCount(7)
        __qtablewidgetitem36 = QTableWidgetItem()
        __qtablewidgetitem36.setFont(font);
        self.Purchase_history_table_2.setHorizontalHeaderItem(0, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        __qtablewidgetitem37.setFont(font);
        self.Purchase_history_table_2.setHorizontalHeaderItem(1, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        __qtablewidgetitem38.setFont(font);
        self.Purchase_history_table_2.setHorizontalHeaderItem(2, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        __qtablewidgetitem39.setFont(font);
        self.Purchase_history_table_2.setHorizontalHeaderItem(3, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        __qtablewidgetitem40.setFont(font);
        self.Purchase_history_table_2.setHorizontalHeaderItem(4, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        __qtablewidgetitem41.setFont(font);
        self.Purchase_history_table_2.setHorizontalHeaderItem(5, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        __qtablewidgetitem42.setFont(font);
        self.Purchase_history_table_2.setHorizontalHeaderItem(6, __qtablewidgetitem42)
        self.Purchase_history_table_2.setObjectName(u"Purchase_history_table_2")
        self.Purchase_history_table_2.setStyleSheet(u"border:none;\n"
"")

        self.horizontalLayout_47.addWidget(self.Purchase_history_table_2)


        self.verticalLayout_13.addWidget(self.frame_56)


        self.horizontalLayout_22.addWidget(self.frame_20)

        self.stackedWidget_2.addWidget(self.Report)
        self.Description = QWidget()
        self.Description.setObjectName(u"Description")
        self.Description.setStyleSheet(u"border:none;")
        self.horizontalLayout_15 = QHBoxLayout(self.Description)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.frame_13 = QFrame(self.Description)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_13)
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 100, 0, 0)
        self.frame_31 = QFrame(self.frame_13)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setStyleSheet(u"border:2px solid black;\n"
"border-radius:12px;\n"
"padding:5px;")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_31)
        self.verticalLayout_9.setSpacing(10)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_40 = QLabel(self.frame_31)
        self.label_40.setObjectName(u"label_40")
        font13 = QFont()
        font13.setPointSize(22)
        font13.setBold(True)
        font13.setItalic(False)
        font13.setUnderline(False)
        font13.setWeight(75)
        self.label_40.setFont(font13)

        self.verticalLayout_9.addWidget(self.label_40, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.description_search = QLineEdit(self.frame_31)
        self.description_search.setObjectName(u"description_search")
        self.description_search.setFont(font)
        self.description_search.setStyleSheet(u"border-radius:10px;")
        self.description_search.setAlignment(Qt.AlignCenter)
        self.description_search.setClearButtonEnabled(False)

        self.verticalLayout_9.addWidget(self.description_search, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.Search_btn = QPushButton(self.frame_31)
        self.Search_btn.setObjectName(u"Search_btn")
        self.Search_btn.setFont(font)
        self.Search_btn.setIcon(icon10)
        self.Search_btn.setIconSize(QSize(20, 20))

        self.verticalLayout_9.addWidget(self.Search_btn, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_8.addWidget(self.frame_31, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.frame_32 = QFrame(self.frame_13)
        self.frame_32.setObjectName(u"frame_32")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_32.sizePolicy().hasHeightForWidth())
        self.frame_32.setSizePolicy(sizePolicy4)
        self.frame_32.setMinimumSize(QSize(500, 300))
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.frame_32)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(100, 300))
        self.scrollArea.setMaximumSize(QSize(600, 300))
        self.scrollArea.setStyleSheet(u"border:2px solid black;\n"
"border-radius:12px;\n"
"padding:5px;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 86, 286))
        self.scrollAreaWidgetContents.setStyleSheet(u"border:none;")
        self.horizontalLayout_17 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 10, 10, 0)
        self.description = QLabel(self.scrollAreaWidgetContents)
        self.description.setObjectName(u"description")
        sizePolicy.setHeightForWidth(self.description.sizePolicy().hasHeightForWidth())
        self.description.setSizePolicy(sizePolicy)
        self.description.setMinimumSize(QSize(0, 0))
        font14 = QFont()
        font14.setPointSize(11)
        font14.setBold(True)
        font14.setItalic(True)
        font14.setWeight(75)
        self.description.setFont(font14)
        self.description.setStyleSheet(u"border:none;")
        self.description.setWordWrap(True)

        self.horizontalLayout_17.addWidget(self.description, 0, Qt.AlignTop)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_16.addWidget(self.scrollArea)


        self.verticalLayout_8.addWidget(self.frame_32, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_15.addWidget(self.frame_13, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.stackedWidget_2.addWidget(self.Description)

        self.horizontalLayout_6.addWidget(self.stackedWidget_2)


        self.verticalLayout_17.addWidget(self.main_body)

        self.footer = QFrame(self.main_ui_window)
        self.footer.setObjectName(u"footer")
        self.footer.setStyleSheet(u"border:2px solid black;\n"
"border-radius:10px;\n"
"padding:1px;")
        self.footer.setFrameShape(QFrame.StyledPanel)
        self.footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.footer)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.footer)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"border:none;")

        self.horizontalLayout_29.addWidget(self.label_5, 0, Qt.AlignLeft)


        self.verticalLayout_17.addWidget(self.footer)


        self.horizontalLayout_31.addWidget(self.main_ui_window)


        self.horizontalLayout_30.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.main)

        self.horizontalLayout.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget_4.setCurrentIndex(0)
        self.stackedWidget_3.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_6.setText("")
        self.label_78.setText("")
        self.label_79.setText("")
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"Email ID", None))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.login_btn.setText(QCoreApplication.translate("MainWindow", u"LOGIN", None))
        self.label_4.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Pharmacy Management", None))
        self.label_37.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"+91 9324932294", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Admin", None))
        self.logout_btn.setText("")
        self.inventory_btn.setText(QCoreApplication.translate("MainWindow", u"Inventory", None))
        self.purchase_btn.setText(QCoreApplication.translate("MainWindow", u"Purchase ", None))
        self.dashboard_btn.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.description_btn.setText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.customer_btn.setText(QCoreApplication.translate("MainWindow", u"Customer", None))
        self.report_btn.setText(QCoreApplication.translate("MainWindow", u"Report    ", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Customer", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_16.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"View Details", None))
        self.customer_btn_2.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Sales", None))
        self.label_22.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"View Details", None))
        self.sale_btn.setText("")
        self.label_26.setText("")
        self.d_stock.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Stock", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"View Details", None))
        self.stock_btn.setText("")
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"New Product", None))
        ___qtablewidgetitem = self.dashboard_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.dashboard_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"NAME", None));
        ___qtablewidgetitem2 = self.dashboard_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"COST PRICE", None));
        ___qtablewidgetitem3 = self.dashboard_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"SELL PRICE", None));
        ___qtablewidgetitem4 = self.dashboard_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"MFD", None));
        ___qtablewidgetitem5 = self.dashboard_table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"EXD", None));
        ___qtablewidgetitem6 = self.dashboard_table.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"QTY", None));
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Details", None))
        self.d_product.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Product", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Customer", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Total Sales value", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Total Cost Value", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.Download.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.dashboard_clear_btn.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.purchase_historybtn.setText(QCoreApplication.translate("MainWindow", u"Purchase History", None))
        self.Customer_search_btn.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.customer_deletebtn.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.purchase_history_show_btn.setText(QCoreApplication.translate("MainWindow", u"Show", None))
        ___qtablewidgetitem7 = self.Purchase_history_table.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem8 = self.Purchase_history_table.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem9 = self.Purchase_history_table.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Phone number", None));
        ___qtablewidgetitem10 = self.Purchase_history_table.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Gender", None));
        ___qtablewidgetitem11 = self.Purchase_history_table.horizontalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Total Cost", None));
        ___qtablewidgetitem12 = self.Purchase_history_table.horizontalHeaderItem(5)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem13 = self.Purchase_history_table.horizontalHeaderItem(6)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Quantity", None));
        self.customer_search_btn.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"Customer ID", None))
        self.customer_confirm_delete_btn.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        ___qtablewidgetitem14 = self.purchase_delete_table.horizontalHeaderItem(0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem15 = self.purchase_delete_table.horizontalHeaderItem(1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem16 = self.purchase_delete_table.horizontalHeaderItem(2)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Phone number", None));
        ___qtablewidgetitem17 = self.purchase_delete_table.horizontalHeaderItem(3)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Gender", None));
        ___qtablewidgetitem18 = self.purchase_delete_table.horizontalHeaderItem(4)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Total Cost", None));
        ___qtablewidgetitem19 = self.purchase_delete_table.horizontalHeaderItem(5)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem20 = self.purchase_delete_table.horizontalHeaderItem(6)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Quantity", None));
        self.p_item.setItemText(0, QCoreApplication.translate("MainWindow", u"ID", None))
        self.p_item.setItemText(1, QCoreApplication.translate("MainWindow", u"Phone", None))

        self.p_serch_btn.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.p_contact.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.p_gender.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.p_name.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.p_date.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.p_cost.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.p_qty.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.p_id.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        ___qtablewidgetitem21 = self.purchase_customer_table.horizontalHeaderItem(0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem22 = self.purchase_customer_table.horizontalHeaderItem(1)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem23 = self.purchase_customer_table.horizontalHeaderItem(2)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Cost", None));
        ___qtablewidgetitem24 = self.purchase_customer_table.horizontalHeaderItem(3)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Quantity", None));
        self.insert_btn.setText(QCoreApplication.translate("MainWindow", u"Insert", None))
        self.update_btn.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.view_btn.setText(QCoreApplication.translate("MainWindow", u"View", None))
        ___qtablewidgetitem25 = self.insert_table.horizontalHeaderItem(0)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem26 = self.insert_table.horizontalHeaderItem(1)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem27 = self.insert_table.horizontalHeaderItem(2)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Cost Price", None));
        ___qtablewidgetitem28 = self.insert_table.horizontalHeaderItem(3)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Sell Price", None));
        ___qtablewidgetitem29 = self.insert_table.horizontalHeaderItem(4)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"MFD", None));
        ___qtablewidgetitem30 = self.insert_table.horizontalHeaderItem(5)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"EXD", None));
        ___qtablewidgetitem31 = self.insert_table.horizontalHeaderItem(6)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"QTY", None));
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Cost Price", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Sell Price", None))
        self.Id.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"MFD", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Best Before", None))
        self.m_Exd.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"EXD", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"QTY", None))
        self.m_Add.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.m_show.setText(QCoreApplication.translate("MainWindow", u"SHOW", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Id", None))
        self.update_search_btn.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.u_id1.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Cost Price", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Selling Price", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Manufacture Date", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Expiry Date", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Quantity", None))
        self.uname1.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.u_cprice1.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.u_sprice1.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.u_mfd1.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.u_exd1.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.u_qty1.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"Manufactore Date", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"Cost Price", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"Selling Price", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.u_id2.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"Quantity", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.confirm_update_btn.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Id", None))
        self.view_search_btn.setText(QCoreApplication.translate("MainWindow", u"search", None))
        self.view_clear_btn.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Cost Price", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Quantity", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Manufactur Date", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Sell price", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Expiry Date", None))
        self.view_id.setText("")
        self.view_name.setText("")
        self.view_cost.setText("")
        self.view_sell.setText("")
        self.view_mfd.setText("")
        self.view_exd.setText("")
        self.view_qty.setText("")
        self.customer_totalcost.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.customer_date.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.customer_show_id.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"Date :", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"Customer ID :", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"Total Price", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"contact:9324932294", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"Pharmacy Management", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"Cost price", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"Quantity", None))
        self.custome_data_field.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.customer_qrcode.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.customer_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        ___qtablewidgetitem32 = self.customer_table.horizontalHeaderItem(0)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem33 = self.customer_table.horizontalHeaderItem(1)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem34 = self.customer_table.horizontalHeaderItem(2)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Cost", None));
        ___qtablewidgetitem35 = self.customer_table.horizontalHeaderItem(3)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Quantity", None));
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"Quantity", None))
        self.c_add_btn.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.c_display_cost.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Phone number", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Gender", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.c_new_id_btn.setText(QCoreApplication.translate("MainWindow", u"New Customer", None))
        self.c_id.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"Customer ID", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.c_show_btn.setText(QCoreApplication.translate("MainWindow", u"Show", None))
        self.c_gender.setItemText(0, QCoreApplication.translate("MainWindow", u"Male", None))
        self.c_gender.setItemText(1, QCoreApplication.translate("MainWindow", u"Female", None))

        self.label_89.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_88.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Total Cost Value", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Sales", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Total Sales Value", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Stock", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Products", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Customer", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.report_show_btn.setText(QCoreApplication.translate("MainWindow", u"Show", None))
        ___qtablewidgetitem36 = self.Purchase_history_table_2.horizontalHeaderItem(0)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem37 = self.Purchase_history_table_2.horizontalHeaderItem(1)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem38 = self.Purchase_history_table_2.horizontalHeaderItem(2)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"Phone number", None));
        ___qtablewidgetitem39 = self.Purchase_history_table_2.horizontalHeaderItem(3)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"Gender", None));
        ___qtablewidgetitem40 = self.Purchase_history_table_2.horizontalHeaderItem(4)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"Total Cost", None));
        ___qtablewidgetitem41 = self.Purchase_history_table_2.horizontalHeaderItem(5)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem42 = self.Purchase_history_table_2.horizontalHeaderItem(6)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"Quantity", None));
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.description_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.Search_btn.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.description.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"copyrights", None))
    # retranslateUi

