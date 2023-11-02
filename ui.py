# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStackedWidget, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(311, 333)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setToolTipDuration(-1)
        self.centralwidget.setStyleSheet(u"QWidget#centralwidget {\n"
"	background-color: rgb(33, 37, 43);\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.top_menu = QFrame(self.centralwidget)
        self.top_menu.setObjectName(u"top_menu")
        self.top_menu.setMinimumSize(QSize(0, 0))
        self.top_menu.setStyleSheet(u"")
        self.top_menu.setFrameShape(QFrame.NoFrame)
        self.top_menu.setFrameShadow(QFrame.Raised)
        self.top_menu.setLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.top_menu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.bg = QFrame(self.top_menu)
        self.bg.setObjectName(u"bg")
        self.bg.setMinimumSize(QSize(245, 0))
        self.bg.setMaximumSize(QSize(16777215, 16777215))
        self.bg.setStyleSheet(u"background-color: rgb(57, 63, 74);")
        self.bg.setFrameShape(QFrame.NoFrame)
        self.bg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.bg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.menu = QFrame(self.bg)
        self.menu.setObjectName(u"menu")
        self.menu.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"}\n"
"\n"
"#minimize_button {\n"
"	background-color: qlineargradient(spread:pad, x1:0.465909, y1:0, x2:0.511, y2:1, stop:0 rgba(31, 31, 31, 255), stop:0.289773 rgba(19, 19, 19, 255));\n"
"}\n"
"\n"
"#minimize_button:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:0.534, y1:1, x2:0.562, y2:0, stop:0.0852273 rgba(23, 26, 30, 255), stop:0.477273 rgba(36, 39, 46, 255));\n"
"}\n"
"\n"
"#menu {\n"
"	background-color: qlineargradient(spread:pad, x1:0.465909, y1:0, x2:0.511, y2:1, stop:0 rgba(31, 31, 31, 255), stop:0.289773 rgba(19, 19, 19, 255));\n"
"}")
        self.menu.setFrameShape(QFrame.NoFrame)
        self.menu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.menu)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(8, 0, 0, 0)
        self.xo_label = QLabel(self.menu)
        self.xo_label.setObjectName(u"xo_label")
        self.xo_label.setMaximumSize(QSize(40, 16777215))
        self.xo_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: transparent;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")

        self.horizontalLayout.addWidget(self.xo_label)

        self.wl = QLabel(self.menu)
        self.wl.setObjectName(u"wl")
        self.wl.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 11pt \"Microsoft New Tai Lue\" Bold;\n"
"background-color: transparent;")

        self.horizontalLayout.addWidget(self.wl)

        self.menu_buttons = QFrame(self.menu)
        self.menu_buttons.setObjectName(u"menu_buttons")
        self.menu_buttons.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.465909, y1:0, x2:0.511, y2:1, stop:0 rgba(31, 31, 31, 255), stop:0.289773 rgba(19, 19, 19, 255));")
        self.menu_buttons.setFrameShape(QFrame.NoFrame)
        self.menu_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.menu_buttons)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.minimize_button = QPushButton(self.menu_buttons)
        self.minimize_button.setObjectName(u"minimize_button")
        self.minimize_button.setMinimumSize(QSize(40, 30))
        self.minimize_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.minimize_button.setStyleSheet(u"#minimize_button {\n"
"	background-color: qlineargradient(spread:pad, x1:0.465909, y1:0, x2:0.511, y2:1, stop:0 rgba(31, 31, 31, 255), stop:0.289773 rgba(19, 19, 19, 255));\n"
"}\n"
"\n"
"#minimize_button:hover {\n"
"	background-color: rgb(57, 63, 74);\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_button.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.minimize_button)

        self.close_button = QPushButton(self.menu_buttons)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setMinimumSize(QSize(40, 30))
        self.close_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_button.setStyleSheet(u"#close_button {\n"
"	background-color: qlineargradient(spread:pad, x1:0.465909, y1:0, x2:0.511, y2:1, stop:0 rgba(31, 31, 31, 255), stop:0.289773 rgba(19, 19, 19, 255));\n"
"}\n"
"\n"
"#close_button:hover {\n"
"	background-color: rgb(170, 0, 0);\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_button.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.close_button)


        self.horizontalLayout.addWidget(self.menu_buttons, 0, Qt.AlignRight)


        self.verticalLayout_3.addWidget(self.menu, 0, Qt.AlignTop)

        self.frame_2 = QFrame(self.bg)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(34, 37, 44);")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setLineWidth(0)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pages = QStackedWidget(self.frame_2)
        self.pages.setObjectName(u"pages")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pages.sizePolicy().hasHeightForWidth())
        self.pages.setSizePolicy(sizePolicy)
        self.pages.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(57, 63, 74);\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(72, 80, 94);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(41, 45, 53);\n"
"	border: 2px solid rgb(20, 21, 26);\n"
"}")
        self.game_page = QWidget()
        self.game_page.setObjectName(u"game_page")
        self.frame = QFrame(self.game_page)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, -10, 310, 310))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(5)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setContentsMargins(10, 10, 10, 0)
        self.c_1 = QPushButton(self.frame)
        self.c_1.setObjectName(u"c_1")
        self.c_1.setMinimumSize(QSize(90, 90))
        self.c_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.c_1.setIconSize(QSize(85, 85))

        self.gridLayout_3.addWidget(self.c_1, 0, 0, 1, 1)

        self.c_2 = QPushButton(self.frame)
        self.c_2.setObjectName(u"c_2")
        self.c_2.setMinimumSize(QSize(90, 90))
        self.c_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.c_2.setIconSize(QSize(85, 85))

        self.gridLayout_3.addWidget(self.c_2, 0, 1, 1, 1)

        self.c_3 = QPushButton(self.frame)
        self.c_3.setObjectName(u"c_3")
        self.c_3.setMinimumSize(QSize(90, 90))
        self.c_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.c_3.setIconSize(QSize(85, 85))

        self.gridLayout_3.addWidget(self.c_3, 0, 2, 1, 1)

        self.c_4 = QPushButton(self.frame)
        self.c_4.setObjectName(u"c_4")
        self.c_4.setMinimumSize(QSize(90, 90))
        self.c_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.c_4.setIconSize(QSize(85, 85))

        self.gridLayout_3.addWidget(self.c_4, 1, 0, 1, 1)

        self.c_6 = QPushButton(self.frame)
        self.c_6.setObjectName(u"c_6")
        self.c_6.setMinimumSize(QSize(90, 90))
        self.c_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.c_6.setIconSize(QSize(85, 85))

        self.gridLayout_3.addWidget(self.c_6, 1, 2, 1, 1)

        self.c_5 = QPushButton(self.frame)
        self.c_5.setObjectName(u"c_5")
        self.c_5.setMinimumSize(QSize(90, 90))
        self.c_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.c_5.setIconSize(QSize(85, 85))

        self.gridLayout_3.addWidget(self.c_5, 1, 1, 1, 1)

        self.c_7 = QPushButton(self.frame)
        self.c_7.setObjectName(u"c_7")
        self.c_7.setMinimumSize(QSize(90, 90))
        self.c_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.c_7.setIconSize(QSize(85, 85))

        self.gridLayout_3.addWidget(self.c_7, 2, 0, 1, 1)

        self.c_8 = QPushButton(self.frame)
        self.c_8.setObjectName(u"c_8")
        self.c_8.setMinimumSize(QSize(90, 90))
        self.c_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.c_8.setIconSize(QSize(85, 85))

        self.gridLayout_3.addWidget(self.c_8, 2, 1, 1, 1)

        self.c_9 = QPushButton(self.frame)
        self.c_9.setObjectName(u"c_9")
        self.c_9.setMinimumSize(QSize(90, 90))
        self.c_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.c_9.setIconSize(QSize(85, 85))

        self.gridLayout_3.addWidget(self.c_9, 2, 2, 1, 1)

        self.pages.addWidget(self.game_page)
        self.connect_page = QWidget()
        self.connect_page.setObjectName(u"connect_page")
        self.connect_page.setStyleSheet(u"QLineEdit {\n"
"	padding-left: 2px;\n"
"	border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton {\n"
"	border-radius: 6px;\n"
"	color: rgb(255, 255, 255);\n"
"	font: 12pt \"MS Shell Dlg 2\";\n"
"	background-color: qlineargradient(spread:pad, x1:0.465909, y1:0, x2:0.511, y2:1, stop:0 rgba(31, 31, 31, 255), stop:0.289773 rgba(19, 19, 19, 255));\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:0.465909, y1:0, x2:0.471, y2:1, stop:0 rgba(31, 31, 31, 255), stop:0.170455 rgba(19, 19, 19, 255), stop:0.761364 rgba(19, 19, 19, 255), stop:1 rgba(0, 170, 255, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: none;\n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.471591 rgba(23, 26, 30, 255), stop:1 rgba(0, 0, 0, 255));\n"
"	color: rgb(118, 118, 118);\n"
"}")
        self.frame_4 = QFrame(self.connect_page)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(-1, -1, 311, 301))
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setSpacing(3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 71, 0, 0)
        self.frame_3 = QFrame(self.frame_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 40))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.ip_line = QLineEdit(self.frame_3)
        self.ip_line.setObjectName(u"ip_line")
        self.ip_line.setGeometry(QRect(18, 10, 211, 31))
        self.ip_line.setStyleSheet(u"border: none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Arial\";")
        self.ip_line.setInputMethodHints(Qt.ImhNone)
        self.ip_line.setMaxLength(15)
        self.ip_line.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.ip_line.setClearButtonEnabled(False)
        self.label_dots = QLabel(self.frame_3)
        self.label_dots.setObjectName(u"label_dots")
        self.label_dots.setGeometry(QRect(235, 1, 71, 41))
        self.label_dots.setStyleSheet(u"font: 48 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_dots.raise_()
        self.ip_line.raise_()

        self.verticalLayout_5.addWidget(self.frame_3)

        self.connect_label = QLabel(self.frame_4)
        self.connect_label.setObjectName(u"connect_label")
        self.connect_label.setEnabled(True)
        self.connect_label.setMaximumSize(QSize(16777215, 20))
        self.connect_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"margin-left: 15px;")

        self.verticalLayout_5.addWidget(self.connect_label)

        self.connect_button = QPushButton(self.frame_4)
        self.connect_button.setObjectName(u"connect_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.connect_button.sizePolicy().hasHeightForWidth())
        self.connect_button.setSizePolicy(sizePolicy1)
        self.connect_button.setMinimumSize(QSize(200, 39))
        self.connect_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.connect_button, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.pages.addWidget(self.connect_page)
        self.wait_page = QWidget()
        self.wait_page.setObjectName(u"wait_page")
        self.wait_label = QLabel(self.wait_page)
        self.wait_label.setObjectName(u"wait_label")
        self.wait_label.setGeometry(QRect(0, 100, 311, 61))
        self.wait_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 22pt \"MS Shell Dlg 2\";")
        self.wait_label.setTextFormat(Qt.PlainText)
        self.wait_label.setScaledContents(True)
        self.wait_label.setAlignment(Qt.AlignCenter)
        self.pages.addWidget(self.wait_page)
        self.win_page = QWidget()
        self.win_page.setObjectName(u"win_page")
        self.win_label = QLabel(self.win_page)
        self.win_label.setObjectName(u"win_label")
        self.win_label.setGeometry(QRect(0, 110, 311, 61))
        self.win_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 22pt \"MS Shell Dlg 2\";")
        self.win_label.setTextFormat(Qt.PlainText)
        self.win_label.setScaledContents(True)
        self.win_label.setAlignment(Qt.AlignCenter)
        self.pages.addWidget(self.win_page)
        self.loose_page = QWidget()
        self.loose_page.setObjectName(u"loose_page")
        self.loose_label = QLabel(self.loose_page)
        self.loose_label.setObjectName(u"loose_label")
        self.loose_label.setGeometry(QRect(0, 110, 311, 61))
        self.loose_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 22pt \"MS Shell Dlg 2\";")
        self.loose_label.setTextFormat(Qt.PlainText)
        self.loose_label.setScaledContents(True)
        self.loose_label.setAlignment(Qt.AlignCenter)
        self.pages.addWidget(self.loose_page)
        self.draw_page = QWidget()
        self.draw_page.setObjectName(u"draw_page")
        self.draw_label = QLabel(self.draw_page)
        self.draw_label.setObjectName(u"draw_label")
        self.draw_label.setGeometry(QRect(0, 110, 311, 61))
        self.draw_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 22pt \"MS Shell Dlg 2\";")
        self.draw_label.setTextFormat(Qt.PlainText)
        self.draw_label.setScaledContents(True)
        self.draw_label.setAlignment(Qt.AlignCenter)
        self.pages.addWidget(self.draw_page)

        self.verticalLayout_4.addWidget(self.pages)


        self.verticalLayout_3.addWidget(self.frame_2)


        self.verticalLayout_2.addWidget(self.bg)


        self.verticalLayout.addWidget(self.top_menu)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pages.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.xo_label.setText(QCoreApplication.translate("MainWindow", u" XO", None))
        self.wl.setText(QCoreApplication.translate("MainWindow", u"W: 0   L: 0", None))
        self.minimize_button.setText("")
        self.close_button.setText("")
        self.c_1.setText("")
        self.c_2.setText("")
        self.c_3.setText("")
        self.c_4.setText("")
        self.c_6.setText("")
        self.c_5.setText("")
        self.c_7.setText("")
        self.c_8.setText("")
        self.c_9.setText("")
        self.ip_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ip", None))
        self.label_dots.setText(QCoreApplication.translate("MainWindow", u": 9000", None))
        self.connect_label.setText("")
        self.connect_button.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.wait_label.setText(QCoreApplication.translate("MainWindow", u"Wait connection...", None))
        self.win_label.setText(QCoreApplication.translate("MainWindow", u"YOU WIN", None))
        self.loose_label.setText(QCoreApplication.translate("MainWindow", u"YOU LOOSE", None))
        self.draw_label.setText(QCoreApplication.translate("MainWindow", u"DRAW", None))
    # retranslateUi

