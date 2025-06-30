# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_dashboard.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QPlainTextEdit,
    QPushButton, QRadioButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)
import images_logos_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1209, 607)
        MainWindow.setStyleSheet(u"background-color: rgb(57, 57, 57);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_11 = QGridLayout(self.centralwidget)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.dashbtns_groupBox_2 = QGroupBox(self.centralwidget)
        self.dashbtns_groupBox_2.setObjectName(u"dashbtns_groupBox_2")
        self.dashbtns_groupBox_2.setMinimumSize(QSize(100, 50))
        self.dashbtns_groupBox_2.setStyleSheet(u"background-color: rgb(38, 38, 38);\n"
"QFrame {\n"
"   border: 2px solid orange;\n"
"}")
        self.gridLayout_3 = QGridLayout(self.dashbtns_groupBox_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setVerticalSpacing(15)
        self.gridLayout_3.setContentsMargins(11, 10, 11, 0)
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_5, 9, 0, 1, 1)

        self.dashboard_btn_short = QPushButton(self.dashbtns_groupBox_2)
        self.dashboard_btn_short.setObjectName(u"dashboard_btn_short")
        self.dashboard_btn_short.setMinimumSize(QSize(0, 40))
        font = QFont()
        font.setPointSize(10)
        self.dashboard_btn_short.setFont(font)
        self.dashboard_btn_short.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.dashboard_btn_short.setStyleSheet(u"QPushButton {\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"	image: url(:/images/home.png);\n"
"}\n"
"\n"
"img {\n"
"  width: calc(100% + 10px); /* Increase width by 10px */\n"
"  height: auto;\n"
"}\n"
"/* Hover state */\n"
"QPushButton:hover {\n"
"     /* Lighter orange on hover */\n"
"	background-color: rgb(103, 103, 103);\n"
"}\n"
"\n"
"/* Pressed state */\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 140, 0); /* Darker orange when pressed */\n"
"}")
        self.dashboard_btn_short.setIconSize(QSize(30, 30))

        self.gridLayout_3.addWidget(self.dashboard_btn_short, 3, 0, 1, 1)

        self.progress_btn_short = QPushButton(self.dashbtns_groupBox_2)
        self.progress_btn_short.setObjectName(u"progress_btn_short")
        self.progress_btn_short.setMinimumSize(QSize(0, 40))
        self.progress_btn_short.setFont(font)
        self.progress_btn_short.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.progress_btn_short.setStyleSheet(u"QPushButton {\n"
"    \n"
"	image: url(:/images/bar_graph.png);\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"/* Hover state */\n"
"QPushButton:hover {\n"
"     /* Lighter orange on hover */\n"
"	background-color: rgb(103, 103, 103);\n"
"}\n"
"\n"
"/* Pressed state */\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 140, 0); /* Darker orange when pressed */\n"
"}")

        self.gridLayout_3.addWidget(self.progress_btn_short, 4, 0, 1, 1)

        self.menu_btn_short = QPushButton(self.dashbtns_groupBox_2)
        self.menu_btn_short.setObjectName(u"menu_btn_short")
        self.menu_btn_short.setMinimumSize(QSize(0, 35))
        self.menu_btn_short.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.menu_btn_short.setStyleSheet(u"QPushButton {\n"
"     /* Darker orange */\n"
"	background-color: rgb(48, 48, 48);\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"	image: url(:/images/menu.png);\n"
"}\n"
"\n"
"/* Hover state */\n"
"QPushButton:hover {\n"
"    /* Lighter orange on hover */\n"
"background-color: rgb(103, 103, 103);\n"
"}\n"
"\n"
"/* Pressed state */\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 140, 0); /* Darker orange when pressed */\n"
"}")
        self.menu_btn_short.setIconSize(QSize(50, 50))
        self.menu_btn_short.setCheckable(True)

        self.gridLayout_3.addWidget(self.menu_btn_short, 2, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 1, 0, 1, 1)

        self.verticalSpacer_short = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_short, 6, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.dashbtns_groupBox_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 40))
        self.pushButton_3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"  \n"
"	image: url(:/images/main_logo.png);\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"}\n"
"/* Hover state */\n"
"QPushButton:hover {\n"
"     /* Lighter orange on hover */\n"
"	background-color: rgb(103, 103, 103);\n"
"}\n"
"/* Pressed state */\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 140, 0); /* Darker orange when pressed */\n"
"}")

        self.gridLayout_3.addWidget(self.pushButton_3, 8, 0, 1, 1)

        self.label_2 = QLabel(self.dashbtns_groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 43))
        self.label_2.setMaximumSize(QSize(76, 50))
        font1 = QFont()
        font1.setPointSize(22)
        self.label_2.setFont(font1)
        self.label_2.setTextFormat(Qt.PlainText)
        self.label_2.setPixmap(QPixmap(u":/images/main_logo.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)

        self.logs_btn_short = QPushButton(self.dashbtns_groupBox_2)
        self.logs_btn_short.setObjectName(u"logs_btn_short")
        self.logs_btn_short.setMinimumSize(QSize(0, 40))
        self.logs_btn_short.setFont(font)
        self.logs_btn_short.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.logs_btn_short.setStyleSheet(u"QPushButton {\n"
"  \n"
"	image: url(:/images/notes.png);\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"}\n"
"/* Hover state */\n"
"QPushButton:hover {\n"
"     /* Lighter orange on hover */\n"
"	background-color: rgb(103, 103, 103);\n"
"}\n"
"/* Pressed state */\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 140, 0); /* Darker orange when pressed */\n"
"}")
        self.logs_btn_short.setIconSize(QSize(40, 40))

        self.gridLayout_3.addWidget(self.logs_btn_short, 5, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.dashbtns_groupBox_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(0, 40))
        self.pushButton_4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_4.setStyleSheet(u"QPushButton {\n"
"  \n"
"	\n"
"	image: url(:/images/Screenshot_2025-06-10_144407-removebg-preview.png);\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"}\n"
"/* Hover state */\n"
"QPushButton:hover {\n"
"     /* Lighter orange on hover */\n"
"	background-color: rgb(103, 103, 103);\n"
"}\n"
"/* Pressed state */\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 140, 0); /* Darker orange when pressed */\n"
"}")

        self.gridLayout_3.addWidget(self.pushButton_4, 7, 0, 1, 1)


        self.gridLayout_11.addWidget(self.dashbtns_groupBox_2, 0, 1, 1, 1)

        self.dashbtns_groupBox = QGroupBox(self.centralwidget)
        self.dashbtns_groupBox.setObjectName(u"dashbtns_groupBox")
        self.dashbtns_groupBox.setMinimumSize(QSize(300, 50))
        self.dashbtns_groupBox.setStyleSheet(u"background-color: rgb(38, 38, 38);\n"
"border-color: rgb(100, 100, 100);\n"
"QFrame {\n"
"    border: 2px solid orange;\n"
"}")
        self.gridLayout = QGridLayout(self.dashbtns_groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(15)
        self.gridLayout.setContentsMargins(0, 10, 0, 0)
        self.pushButton = QPushButton(self.dashbtns_groupBox)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(255, 140, 0); /* Darker orange */\n"
"    border-radius: 30;\n"
"    padding: 5px;\n"
"qproperty-icon: url(:/images/Screenshot_2025-06-10_144341-removebg-preview.png);\n"
"qproperty-iconSize: 30px 30px;\n"
"}\n"
"\n"
"/* Hover state */\n"
"QPushButton:hover {\n"
"    background-color: rgb(255, 200, 0); /* Lighter orange on hover */\n"
"}\n"
"\n"
"/* Pressed state */\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 140, 0); /* Darker orange when pressed */\n"
"}")

        self.gridLayout.addWidget(self.pushButton, 8, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.dashbtns_groupBox)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(255, 140, 0); /* Darker orange */\n"
"    border-radius: 30;\n"
"    padding: 5px;\n"
"qproperty-icon:  url(:/images/Screenshot_2025-06-10_144412-removebg-preview.png);\n"
"qproperty-iconSize: 30px 30px;\n"
"}\n"
"\n"
"/* Hover state */\n"
"QPushButton:hover {\n"
"    background-color: rgb(255, 200, 0); /* Lighter orange on hover */\n"
"}\n"
"\n"
"/* Pressed state */\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 140, 0); /* Darker orange when pressed */\n"
"}")

        self.gridLayout.addWidget(self.pushButton_2, 7, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 9, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 6, 0, 1, 1)

        self.logs_btn = QPushButton(self.dashbtns_groupBox)
        self.logs_btn.setObjectName(u"logs_btn")
        self.logs_btn.setMinimumSize(QSize(0, 35))
        self.logs_btn.setFont(font)
        self.logs_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.logs_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(255, 140, 0); /* Darker orange */\n"
"    border-radius: 30;\n"
"    padding: 5px;\n"
"qproperty-icon: url(:/images/Screenshot_2025-06-10_125200-removebg-preview.png);\n"
"qproperty-iconSize: 30px 30px;\n"
"}\n"
"\n"
"/* Hover state */\n"
"QPushButton:hover {\n"
"    background-color: rgb(255, 200, 0); /* Lighter orange on hover */\n"
"}\n"
"\n"
"/* Pressed state */\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 140, 0); /* Darker orange when pressed */\n"
"}")
        self.logs_btn.setIconSize(QSize(30, 30))

        self.gridLayout.addWidget(self.logs_btn, 5, 0, 1, 1)

        self.progress_btn = QPushButton(self.dashbtns_groupBox)
        self.progress_btn.setObjectName(u"progress_btn")
        self.progress_btn.setMinimumSize(QSize(0, 35))
        self.progress_btn.setFont(font)
        self.progress_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.progress_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(255, 140, 0); /* Darker orange */\n"
"border-radius: 30px;\n"
"    padding: 5px;\n"
"qproperty-icon:  url(:/images/Screenshot_2025-06-10_125207-removebg-preview.png);\n"
"qproperty-iconSize: 30px 30px;\n"
"}\n"
"\n"
"/* Hover state */\n"
"QPushButton:hover {\n"
"    background-color: rgb(255, 200, 0); /* Lighter orange on hover */\n"
"}\n"
"\n"
"/* Pressed state */\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 140, 0); /* Darker orange when pressed */\n"
"}")

        self.gridLayout.addWidget(self.progress_btn, 4, 0, 1, 1)

        self.dashboard_btn = QPushButton(self.dashbtns_groupBox)
        self.dashboard_btn.setObjectName(u"dashboard_btn")
        self.dashboard_btn.setMinimumSize(QSize(0, 35))
        self.dashboard_btn.setFont(font)
        self.dashboard_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.dashboard_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(255, 140, 0); /* Darker orange */\n"
"    border-radius: 30px;\n"
"    padding: 5px;\n"
"	qproperty-icon: url(:/images/Screenshot_2025-06-10_125203-removebg-preview.png);\n"
"qproperty-iconSize: 30px 30px;\n"
"}\n"
"\n"
"\n"
"/* Hover state */\n"
"QPushButton:hover {\n"
"    background-color: rgb(255, 200, 0); /* Lighter orange on hover */\n"
"}\n"
"\n"
"/* Pressed state */\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 140, 0); /* Darker orange when pressed */\n"
"}")

        self.gridLayout.addWidget(self.dashboard_btn, 3, 0, 1, 1)

        self.menu_btn_long = QPushButton(self.dashbtns_groupBox)
        self.menu_btn_long.setObjectName(u"menu_btn_long")
        self.menu_btn_long.setMinimumSize(QSize(50, 35))
        self.menu_btn_long.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.menu_btn_long.setStyleSheet(u"QPushButton {\n"
"image: url(:/images/menu.png);\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"/* Hover state */\n"
"QPushButton:hover {\n"
"    /* Lighter orange on hover */\n"
"background-color: rgb(103, 103, 103);\n"
"}\n"
"\n"
"\n"
"/* Pressed state */\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 140, 0); /* Darker orange when pressed */\n"
"}")
        self.menu_btn_long.setCheckable(True)

        self.gridLayout.addWidget(self.menu_btn_long, 2, 0, 1, 1, Qt.AlignLeft)

        self.label = QLabel(self.dashbtns_groupBox)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setFamilies([u"Eras Bold ITC"])
        font2.setPointSize(22)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"color: rgb(255, 170, 0);")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1, Qt.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 1, 0, 1, 1)


        self.gridLayout_11.addWidget(self.dashbtns_groupBox, 0, 0, 1, 1)

        self.main_dashboard = QStackedWidget(self.centralwidget)
        self.main_dashboard.setObjectName(u"main_dashboard")
        self.main_dashboard.setMinimumSize(QSize(795, 607))
        self.main_dashboard.setFrameShape(QFrame.NoFrame)
        self.Logs = QWidget()
        self.Logs.setObjectName(u"Logs")
        self.gridLayout_6 = QGridLayout(self.Logs)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(-1, 30, 25, -1)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.searchlog_lineEdit = QLineEdit(self.Logs)
        self.searchlog_lineEdit.setObjectName(u"searchlog_lineEdit")
        self.searchlog_lineEdit.setMinimumSize(QSize(300, 0))
        self.searchlog_lineEdit.setMaximumSize(QSize(550, 16777215))
        self.searchlog_lineEdit.setStyleSheet(u"QLineEdit {\n"
"    background-color: #2b2b2b; /* Dark background */\n"
"    color: white; /* White text for good contrast */\n"
"    border: 2px solid orange; /* Orange border to match theme */\n"
"    border-radius: 8px;\n"
"    padding: 4px 8px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #ff8c00; /* Slightly lighter orange for active state */\n"
"    background-color: #3a3a3a; /* Slightly lighter background */\n"
"}")

        self.horizontalLayout_3.addWidget(self.searchlog_lineEdit)

        self.filter_logs_comboBox = QComboBox(self.Logs)
        self.filter_logs_comboBox.addItem("")
        self.filter_logs_comboBox.addItem("")
        self.filter_logs_comboBox.addItem("")
        self.filter_logs_comboBox.addItem("")
        self.filter_logs_comboBox.setObjectName(u"filter_logs_comboBox")
        self.filter_logs_comboBox.setStyleSheet(u"/* ComboBox */\n"
"QComboBox {\n"
"    background-color: #2b2b2b;  /* Dark background */\n"
"    color: white;\n"
"    border: 2px solid orange;\n"
"    border-radius: 8px;\n"
"    padding: 5px;\n"
"    min-width: 100px;\n"
"    min-height: 10px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
" \n"
"	image: url(:/images/Screenshot_2025-06-10_142412-removebg-preview.png);\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #2b2b2b;\n"
"    color: white;\n"
"    border: 1px solid orange;\n"
"    selection-background-color: #ff8c00;\n"
"    selection-color: white;\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.filter_logs_comboBox)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)


        self.gridLayout_6.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.Add_log = QPushButton(self.Logs)
        self.Add_log.setObjectName(u"Add_log")
        self.Add_log.setMinimumSize(QSize(100, 30))
        font3 = QFont()
        self.Add_log.setFont(font3)
        self.Add_log.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Add_log.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(255, 140, 0); /* Darker orange */\n"
"    color: black; /* Consistent text color */\n"
"    border-radius: 10px;\n"
"    padding: 5px 15px; /* Horizontal padding for better look */\n"
"    font-size: 14px; /* Optional: adjust font size */\n"
"    transition: background-color 0.3s, border-color 0.3s; /* Smooth transitions */\n"
"}\n"
"\n"
"/* Hover state */\n"
"QPushButton:hover {\n"
"    background-color: rgb(255, 200, 0); /* Lighter orange on hover */\n"
"}\n"
"\n"
"/* Pressed state */\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 140, 0); /* Darker orange when pressed */\n"
"}\n"
"\n"
"/* Optional: Change cursor on hover */\n"
"QPushButton:hover {\n"
"    cursor: pointer;\n"
"}")

        self.verticalLayout_6.addWidget(self.Add_log, 0, Qt.AlignRight)

        self.widget = QWidget(self.Logs)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(550, 16777215))
        self.gridLayout_5 = QGridLayout(self.widget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(200, 375))
        self.label_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 2px solid orange;\n"
"    border-radius: 8px;\n"
"    padding: 6px;")
        self.label_3.setFrameShape(QFrame.Panel)

        self.gridLayout_5.addWidget(self.label_3, 0, 0, 1, 1)

        self.info_log_plaintext = QPlainTextEdit(self.widget)
        self.info_log_plaintext.setObjectName(u"info_log_plaintext")
        self.info_log_plaintext.setMaximumSize(QSize(16777215, 375))
        self.info_log_plaintext.setStyleSheet(u"QPlainTextEdit {\n"
"    background-color: #2b2b2b;\n"
"    color: white;\n"
"    border: 2px solid orange;\n"
"    border-radius: 8px;\n"
"    padding: 6px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border: 2px solid #ff8c00;\n"
"    background-color: #3a3a3a;\n"
"}")

        self.gridLayout_5.addWidget(self.info_log_plaintext, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Del_log = QPushButton(self.widget)
        self.Del_log.setObjectName(u"Del_log")
        self.Del_log.setMinimumSize(QSize(100, 35))
        self.Del_log.setFont(font3)
        self.Del_log.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Del_log.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(255, 140, 0); /* Darker orange */\n"
"    color: black; /* Consistent text color */\n"
"    border-radius: 10px;\n"
"    padding: 5px 15px; /* Horizontal padding for better look */\n"
"    font-size: 14px; /* Optional: adjust font size */\n"
"    transition: background-color 0.3s, border-color 0.3s; /* Smooth transitions */\n"
"}\n"
"\n"
"/* Hover state */\n"
"QPushButton:hover {\n"
"    background-color: rgb(255, 200, 0); /* Lighter orange on hover */\n"
"}\n"
"\n"
"/* Pressed state */\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 140, 0); /* Darker orange when pressed */\n"
"}\n"
"\n"
"/* Optional: Change cursor on hover */\n"
"QPushButton:hover {\n"
"    cursor: pointer;\n"
"}")

        self.horizontalLayout.addWidget(self.Del_log, 0, Qt.AlignLeft)

        self.View_log = QPushButton(self.widget)
        self.View_log.setObjectName(u"View_log")
        self.View_log.setMinimumSize(QSize(100, 35))
        self.View_log.setFont(font3)
        self.View_log.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.View_log.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(255, 140, 0); /* Darker orange */\n"
"    color: black; /* Consistent text color */\n"
"    border-radius: 10px;\n"
"    padding: 5px 15px; /* Horizontal padding for better look */\n"
"    font-size: 14px; /* Optional: adjust font size */\n"
"    transition: background-color 0.3s, border-color 0.3s; /* Smooth transitions */\n"
"}\n"
"\n"
"/* Hover state */\n"
"QPushButton:hover {\n"
"    background-color: rgb(255, 200, 0); /* Lighter orange on hover */\n"
"}\n"
"\n"
"/* Pressed state */\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 140, 0); /* Darker orange when pressed */\n"
"}\n"
"\n"
"/* Optional: Change cursor on hover */\n"
"QPushButton:hover {\n"
"    cursor: pointer;\n"
"}")

        self.horizontalLayout.addWidget(self.View_log, 0, Qt.AlignRight)


        self.gridLayout_5.addLayout(self.horizontalLayout, 2, 0, 1, 1)


        self.verticalLayout_6.addWidget(self.widget)


        self.gridLayout_6.addLayout(self.verticalLayout_6, 0, 1, 2, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_16 = QLabel(self.Logs)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Eras Medium ITC\";")

        self.verticalLayout_5.addWidget(self.label_16, 0, Qt.AlignHCenter)

        self.log_list = QListWidget(self.Logs)
        QListWidgetItem(self.log_list)
        QListWidgetItem(self.log_list)
        self.log_list.setObjectName(u"log_list")
        self.log_list.setStyleSheet(u"QListWidget {\n"
"    background-color: #2b2b2b; /* Dark background */\n"
"    color: white; /* White text */\n"
"    border: 2px solid orange;\n"
"    border-radius: 8px;\n"
"    padding: 4px;\n"
"font: 14pt \"Eras Medium ITC\";\n"
"\n"
"}\n"
"\n"
"/* Hover state for list items */\n"
"QListWidget::item:hover {\n"
"    background-color: orange; /* Orange highlight on hover */\n"
"    color: black; /* Black text for contrast */\n"
"    border-radius: 4px; /* Optional: slight rounding */\n"
"}\n"
"\n"
"\n"
"QListWidget::item:selected {\n"
"    background-color: orange; /* Orange highlight for selection */\n"
"    color: black; /* Black text for selected item */\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    background: #2b2b2b;\n"
"    width: 10px;\n"
"    margin: 2px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: orange;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"")

        self.verticalLayout_5.addWidget(self.log_list)

        self.label_14 = QLabel(self.Logs)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Eras Medium ITC\";")

        self.verticalLayout_5.addWidget(self.label_14, 0, Qt.AlignHCenter)

        self.exercise_list = QListWidget(self.Logs)
        QListWidgetItem(self.exercise_list)
        QListWidgetItem(self.exercise_list)
        self.exercise_list.setObjectName(u"exercise_list")
        self.exercise_list.setStyleSheet(u"QListWidget {\n"
"    background-color: #2b2b2b; /* Dark background */\n"
"    color: white; /* White text */\n"
"    border: 2px solid orange;\n"
"    border-radius: 8px;\n"
"    padding: 4px;\n"
"font: 14pt \"Eras Medium ITC\";\n"
"\n"
"}\n"
"\n"
"/* Hover state for list items */\n"
"QListWidget::item:hover {\n"
"    background-color: orange; /* Orange highlight on hover */\n"
"    color: black; /* Black text for contrast */\n"
"    border-radius: 4px; /* Optional: slight rounding */\n"
"}\n"
"\n"
"\n"
"QListWidget::item:selected {\n"
"    background-color: orange; /* Orange highlight for selection */\n"
"    color: black; /* Black text for selected item */\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    background: #2b2b2b;\n"
"    width: 10px;\n"
"    margin: 2px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: orange;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"")

        self.verticalLayout_5.addWidget(self.exercise_list)


        self.gridLayout_6.addLayout(self.verticalLayout_5, 1, 0, 1, 1)

        self.main_dashboard.addWidget(self.Logs)
        self.dashboard = QWidget()
        self.dashboard.setObjectName(u"dashboard")
        self.gridLayout_7 = QGridLayout(self.dashboard)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(-1, 30, 25, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget_progress = QWidget(self.dashboard)
        self.widget_progress.setObjectName(u"widget_progress")
        self.gridLayout_4 = QGridLayout(self.widget_progress)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalLayout_progress = QVBoxLayout()
        self.verticalLayout_progress.setObjectName(u"verticalLayout_progress")

        self.gridLayout_4.addLayout(self.verticalLayout_progress, 0, 0, 1, 1)

        self.progress_analysis = QPlainTextEdit(self.widget_progress)
        self.progress_analysis.setObjectName(u"progress_analysis")
        self.progress_analysis.setMaximumSize(QSize(16777215, 100))
        self.progress_analysis.setStyleSheet(u"QPlainTextEdit {\n"
"    background-color: #2b2b2b;\n"
"    color: white;\n"
"    border: 2px solid orange;\n"
"    border-radius: 8px;\n"
"    padding: 6px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border: 2px solid #ff8c00;\n"
"    background-color: #3a3a3a;\n"
"}")
        self.progress_analysis.setFrameShape(QFrame.NoFrame)
        self.progress_analysis.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout_4.addWidget(self.progress_analysis, 2, 0, 1, 1)

        self.label_9 = QLabel(self.widget_progress)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 25))
        font4 = QFont()
        font4.setFamilies([u"Eras Medium ITC"])
        font4.setPointSize(12)
        font4.setBold(False)
        font4.setItalic(False)
        self.label_9.setFont(font4)
        self.label_9.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Eras Medium ITC\";")

        self.gridLayout_4.addWidget(self.label_9, 1, 0, 1, 1, Qt.AlignLeft)


        self.horizontalLayout_2.addWidget(self.widget_progress)

        self.widget_frequency = QWidget(self.dashboard)
        self.widget_frequency.setObjectName(u"widget_frequency")
        self.gridLayout_2 = QGridLayout(self.widget_frequency)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_frequency = QVBoxLayout()
        self.verticalLayout_frequency.setObjectName(u"verticalLayout_frequency")

        self.gridLayout_2.addLayout(self.verticalLayout_frequency, 0, 0, 1, 1)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_10 = QLabel(self.widget_frequency)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(16777215, 25))
        self.label_10.setFont(font4)
        self.label_10.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Eras Medium ITC\";")

        self.horizontalLayout_7.addWidget(self.label_10)

        self.Filter_Year = QComboBox(self.widget_frequency)
        self.Filter_Year.setObjectName(u"Filter_Year")
        self.Filter_Year.setStyleSheet(u"/* ComboBox */\n"
"QComboBox {\n"
"    background-color: #2b2b2b;  /* Dark background */\n"
"    color: white;\n"
"    border: 2px solid orange;\n"
"    border-radius: 8px;\n"
"    padding: 5px;\n"
"    min-width: 100px;\n"
"    min-height: 10px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
" \n"
"	image: url(:/images/Screenshot_2025-06-10_142412-removebg-preview.png);\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #2b2b2b;\n"
"    color: white;\n"
"    border: 1px solid orange;\n"
"    selection-background-color: #ff8c00;\n"
"    selection-color: white;\n"
"}\n"
"")

        self.horizontalLayout_7.addWidget(self.Filter_Year)


        self.verticalLayout_7.addLayout(self.horizontalLayout_7)

        self.frequency_analysis = QPlainTextEdit(self.widget_frequency)
        self.frequency_analysis.setObjectName(u"frequency_analysis")
        self.frequency_analysis.setMaximumSize(QSize(16777215, 100))
        self.frequency_analysis.setStyleSheet(u"QPlainTextEdit {\n"
"    background-color: #2b2b2b;\n"
"    color: white;\n"
"    border: 2px solid orange;\n"
"    border-radius: 8px;\n"
"    padding: 6px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border: 2px solid #ff8c00;\n"
"    background-color: #3a3a3a;\n"
"}")
        self.frequency_analysis.setFrameShape(QFrame.NoFrame)
        self.frequency_analysis.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_7.addWidget(self.frequency_analysis)


        self.gridLayout_2.addLayout(self.verticalLayout_7, 1, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.widget_frequency)


        self.gridLayout_7.addLayout(self.horizontalLayout_2, 3, 0, 1, 3)

        self.general_progress_analysis_textedit = QPlainTextEdit(self.dashboard)
        self.general_progress_analysis_textedit.setObjectName(u"general_progress_analysis_textedit")
        self.general_progress_analysis_textedit.setMaximumSize(QSize(16777215, 100))
        self.general_progress_analysis_textedit.setStyleSheet(u"QPlainTextEdit {\n"
"    background-color: #2b2b2b;\n"
"    color: white;\n"
"    border: 2px solid orange;\n"
"    border-radius: 8px;\n"
"    padding: 6px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border: 2px solid #ff8c00;\n"
"    background-color: #3a3a3a;\n"
"}")
        self.general_progress_analysis_textedit.setFrameShape(QFrame.NoFrame)
        self.general_progress_analysis_textedit.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout_7.addWidget(self.general_progress_analysis_textedit, 2, 0, 1, 3)

        self.horizontalSpacer_2 = QSpacerItem(522, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)

        self.label_4 = QLabel(self.dashboard)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 50))
        font5 = QFont()
        font5.setFamilies([u"Eras Medium ITC"])
        font5.setPointSize(18)
        self.label_4.setFont(font5)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_7.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_8 = QLabel(self.dashboard)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font4)
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Eras Medium ITC\";")

        self.gridLayout_7.addWidget(self.label_8, 1, 0, 1, 1)

        self.main_dashboard.addWidget(self.dashboard)
        self.progress_board = QWidget()
        self.progress_board.setObjectName(u"progress_board")
        self.gridLayout_12 = QGridLayout(self.progress_board)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(-1, 30, 25, -1)
        self.label_5 = QLabel(self.progress_board)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 50))
        font6 = QFont()
        font6.setFamilies([u"Eras Medium ITC"])
        font6.setPointSize(20)
        font6.setBold(False)
        font6.setItalic(False)
        self.label_5.setFont(font6)
        self.label_5.setStyleSheet(u"font: 20pt \"Eras Medium ITC\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_12.addWidget(self.label_5, 0, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_6 = QLabel(self.progress_board)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 50))
        font7 = QFont()
        font7.setFamilies([u"Eras Medium ITC"])
        font7.setPointSize(12)
        self.label_6.setFont(font7)

        self.horizontalLayout_5.addWidget(self.label_6, 0, Qt.AlignLeft)

        self.Add_exercise_btn = QPushButton(self.progress_board)
        self.Add_exercise_btn.setObjectName(u"Add_exercise_btn")
        self.Add_exercise_btn.setMinimumSize(QSize(130, 35))
        self.Add_exercise_btn.setFont(font3)
        self.Add_exercise_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Add_exercise_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(255, 140, 0); /* Darker orange */\n"
"    color: black; /* Consistent text color */\n"
"    border-radius: 10px;\n"
"    padding: 5px 15px; /* Horizontal padding for better look */\n"
"    font-size: 14px; /* Optional: adjust font size */\n"
"    transition: background-color 0.3s, border-color 0.3s; /* Smooth transitions */\n"
" min-width: 100px; \n"
"\n"
"}\n"
"\n"
"/* Hover state */\n"
"QPushButton:hover {\n"
"    background-color: rgb(255, 200, 0); /* Lighter orange on hover */\n"
"}\n"
"\n"
"/* Pressed state */\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 140, 0); /* Darker orange when pressed */\n"
"}\n"
"\n"
"/* Optional: Change cursor on hover */\n"
"QPushButton:hover {\n"
"    cursor: pointer;\n"
"}")

        self.horizontalLayout_5.addWidget(self.Add_exercise_btn)


        self.gridLayout_12.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.label_11 = QLabel(self.progress_board)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(16777215, 50))
        self.label_11.setFont(font7)

        self.horizontalLayout_4.addWidget(self.label_11)

        self.radioButton_weighted = QRadioButton(self.progress_board)
        self.radioButton_weighted.setObjectName(u"radioButton_weighted")
        font8 = QFont()
        font8.setFamilies([u"Eras Medium ITC"])
        font8.setPointSize(10)
        font8.setBold(False)
        font8.setItalic(False)
        self.radioButton_weighted.setFont(font8)
        self.radioButton_weighted.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.radioButton_weighted.setStyleSheet(u"\n"
"QRadioButton {\n"
"    spacing: 8px;\n"
"    min-height: 20px;\n"
"font: 10pt \"Eras Medium ITC\";\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: orange;\n"
"    border: 2px solid black;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color: #2b2b2b;\n"
"    border: 2px solid orange;\n"
"    border-radius: 8px;\n"
"}")

        self.horizontalLayout_4.addWidget(self.radioButton_weighted)

        self.radioButton_bodyweight = QRadioButton(self.progress_board)
        self.radioButton_bodyweight.setObjectName(u"radioButton_bodyweight")
        self.radioButton_bodyweight.setFont(font8)
        self.radioButton_bodyweight.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.radioButton_bodyweight.setStyleSheet(u"\n"
"QRadioButton {\n"
"    spacing: 8px;\n"
"    min-height: 20px;\n"
"font: 10pt \"Eras Medium ITC\";\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: orange;\n"
"    border: 2px solid black;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color: #2b2b2b;\n"
"    border: 2px solid orange;\n"
"    border-radius: 8px;\n"
"}r")

        self.horizontalLayout_4.addWidget(self.radioButton_bodyweight)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.refresh_btn = QPushButton(self.progress_board)
        self.refresh_btn.setObjectName(u"refresh_btn")
        self.refresh_btn.setMinimumSize(QSize(50, 40))
        self.refresh_btn.setStyleSheet(u"QPushButton {\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"	\n"
"	image: url(:/images/refresh_img.png);\n"
"}\n"
"\n"
"img {\n"
"  width: calc(100% + 10px); /* Increase width by 10px */\n"
"  height: auto;\n"
"}\n"
"/* Hover state */\n"
"QPushButton:hover {\n"
"     /* Lighter orange on hover */\n"
"	background-color: rgb(103, 103, 103);\n"
"}\n"
"\n"
"/* Pressed state */\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 140, 0); /* Darker orange when pressed */\n"
"}")

        self.horizontalLayout_4.addWidget(self.refresh_btn)


        self.gridLayout_12.addLayout(self.horizontalLayout_4, 1, 1, 1, 1)

        self.label_7 = QLabel(self.progress_board)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 50))
        font9 = QFont()
        font9.setFamilies([u"Eras Medium ITC"])
        font9.setPointSize(15)
        font9.setBold(False)
        font9.setItalic(False)
        self.label_7.setFont(font9)
        self.label_7.setStyleSheet(u"font: 15pt \"Eras Medium ITC\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_12.addWidget(self.label_7, 2, 0, 1, 1)

        self.General_analysis_per_exer_text = QPlainTextEdit(self.progress_board)
        self.General_analysis_per_exer_text.setObjectName(u"General_analysis_per_exer_text")
        self.General_analysis_per_exer_text.setMaximumSize(QSize(16777215, 100))
        self.General_analysis_per_exer_text.setStyleSheet(u"QPlainTextEdit {\n"
"    background-color: #2b2b2b;\n"
"    color: white;\n"
"    border: 2px solid orange;\n"
"    border-radius: 8px;\n"
"    padding: 6px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border: 2px solid #ff8c00;\n"
"    background-color: #3a3a3a;\n"
"}")

        self.gridLayout_12.addWidget(self.General_analysis_per_exer_text, 3, 0, 1, 2)

        self.scrollArea = QScrollArea(self.progress_board)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"/* QScrollArea main frame */\n"
"QScrollArea {\n"
"    border: 2px solid orange;  /* Orange border, adjust as needed */\n"
"    border-radius: 8px;\n"
"    background: #2b2b2b;  /* Dark background for gym vibe */\n"
"}\n"
"\n"
"/* The actual content area (viewport) */\n"
"QScrollArea QWidget {\n"
"    background: #2b2b2b;  /* Match background */\n"
"}\n"
"\n"
"/* Vertical scrollbar styling */\n"
"QScrollBar:vertical {\n"
"    background: #1e1e1e;  /* Dark background for scrollbar track */\n"
"    width: 12px;\n"
"    margin: 2px;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: orange;\n"
"    min-height: 20px;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical {\n"
"    background: #ff8c00;\n"
"    height: 12px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: transparent;\n"
"    image: u"
                        "rl(:/icons/arrow_up.png);  /* Optional: Replace with your orange/black arrow images */\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"/* Horizontal scrollbar styling (similar idea) */\n"
"QScrollBar:horizontal {\n"
"    background: #1e1e1e;\n"
"    height: 12px;\n"
"    margin: 2px;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: orange;\n"
"    min-width: 20px;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal,\n"
"QScrollBar::sub-line:horizontal {\n"
"    background: #ff8c00;\n"
"    width: 12px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal, QScrollBar::right-arrow:horizontal {\n"
"    background: transparent;\n"
"    image: url(:/icons/arrow_left.png);  /* Optional icon */\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 763, 1222))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(741, 1200))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_15 = QLabel(self.frame)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font7)
        self.label_15.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_6.addWidget(self.label_15, 0, Qt.AlignLeft)

        self.filter_year = QComboBox(self.frame)
        self.filter_year.setObjectName(u"filter_year")
        self.filter_year.setStyleSheet(u"/* ComboBox */\n"
"QComboBox {\n"
"    background-color: #2b2b2b;  /* Dark background */\n"
"    color: white;\n"
"    border: 2px solid orange;\n"
"    border-radius: 8px;\n"
"    padding: 5px;\n"
"    min-width: 100px;\n"
"    min-height: 10px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
" \n"
"	image: url(:/images/Screenshot_2025-06-10_142412-removebg-preview.png);\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #2b2b2b;\n"
"    color: white;\n"
"    border: 1px solid orange;\n"
"    selection-background-color: #ff8c00;\n"
"    selection-color: white;\n"
"}\n"
"")

        self.horizontalLayout_6.addWidget(self.filter_year)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.widget_2 = QWidget(self.frame)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(0, 300))
        self.gridLayout_10 = QGridLayout(self.widget_4)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.verticalLayout_exercise_progress = QVBoxLayout()
        self.verticalLayout_exercise_progress.setObjectName(u"verticalLayout_exercise_progress")

        self.gridLayout_10.addLayout(self.verticalLayout_exercise_progress, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.widget_4)

        self.label_12 = QLabel(self.widget_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(16777215, 25))
        self.label_12.setFont(font4)
        self.label_12.setStyleSheet(u"font: 12pt \"Eras Medium ITC\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.label_12)

        self.text_analysis_exercise_progress = QPlainTextEdit(self.widget_2)
        self.text_analysis_exercise_progress.setObjectName(u"text_analysis_exercise_progress")
        self.text_analysis_exercise_progress.setMaximumSize(QSize(16777215, 100))
        self.text_analysis_exercise_progress.setStyleSheet(u"QPlainTextEdit {\n"
"    background-color: #2b2b2b;\n"
"    color: white;\n"
"    border: 2px solid orange;\n"
"    border-radius: 8px;\n"
"    padding: 6px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border: 2px solid #ff8c00;\n"
"    background-color: #3a3a3a;\n"
"}")

        self.verticalLayout_2.addWidget(self.text_analysis_exercise_progress)


        self.verticalLayout_4.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.frame)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout = QVBoxLayout(self.widget_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_5 = QWidget(self.widget_3)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(0, 300))
        self.gridLayout_13 = QGridLayout(self.widget_5)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.verticalLayout_frequency_exercise = QVBoxLayout()
        self.verticalLayout_frequency_exercise.setObjectName(u"verticalLayout_frequency_exercise")

        self.gridLayout_13.addLayout(self.verticalLayout_frequency_exercise, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.widget_5)

        self.label_13 = QLabel(self.widget_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(16777215, 25))
        self.label_13.setFont(font4)
        self.label_13.setStyleSheet(u"font: 12pt \"Eras Medium ITC\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.label_13)

        self.text_analysis_frequency_exercise = QPlainTextEdit(self.widget_3)
        self.text_analysis_frequency_exercise.setObjectName(u"text_analysis_frequency_exercise")
        self.text_analysis_frequency_exercise.setMaximumSize(QSize(16777215, 100))
        self.text_analysis_frequency_exercise.setStyleSheet(u"QPlainTextEdit {\n"
"    background-color: #2b2b2b;\n"
"    color: white;\n"
"    border: 2px solid orange;\n"
"    border-radius: 8px;\n"
"    padding: 6px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border: 2px solid #ff8c00;\n"
"    background-color: #3a3a3a;\n"
"}")

        self.verticalLayout.addWidget(self.text_analysis_frequency_exercise)


        self.verticalLayout_4.addWidget(self.widget_3)


        self.verticalLayout_3.addWidget(self.frame)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_12.addWidget(self.scrollArea, 4, 0, 1, 2)

        self.main_dashboard.addWidget(self.progress_board)

        self.gridLayout_11.addWidget(self.main_dashboard, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.menu_btn_long.clicked["bool"].connect(self.dashbtns_groupBox.setHidden)
        self.menu_btn_long.clicked["bool"].connect(self.dashbtns_groupBox_2.setVisible)
        self.menu_btn_short.clicked["bool"].connect(self.dashbtns_groupBox.setVisible)
        self.menu_btn_short.clicked["bool"].connect(self.dashbtns_groupBox_2.setHidden)

        self.main_dashboard.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.dashbtns_groupBox_2.setTitle("")
        self.dashboard_btn_short.setText("")
        self.progress_btn_short.setText("")
        self.menu_btn_short.setText("")
        self.pushButton_3.setText("")
        self.label_2.setText("")
        self.logs_btn_short.setText("")
        self.pushButton_4.setText("")
        self.dashbtns_groupBox.setTitle("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Exercises", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"User", None))
        self.logs_btn.setText(QCoreApplication.translate("MainWindow", u"Logs", None))
        self.progress_btn.setText(QCoreApplication.translate("MainWindow", u"Progress", None))
        self.dashboard_btn.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.menu_btn_long.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Gym Tracker", None))
        self.searchlog_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search...", None))
        self.filter_logs_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Latest", None))
        self.filter_logs_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Oldest", None))
        self.filter_logs_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"A-Z", None))
        self.filter_logs_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Z-A", None))

        self.Add_log.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"pic if upper or lower", None))
        self.Del_log.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.View_log.setText(QCoreApplication.translate("MainWindow", u"View", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Exercise Logs", None))

        __sortingEnabled = self.log_list.isSortingEnabled()
        self.log_list.setSortingEnabled(False)
        ___qlistwidgetitem = self.log_list.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"testing", None));
        ___qlistwidgetitem1 = self.log_list.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"isa pa", None));
        self.log_list.setSortingEnabled(__sortingEnabled)

        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Exercises", None))

        __sortingEnabled1 = self.exercise_list.isSortingEnabled()
        self.exercise_list.setSortingEnabled(False)
        ___qlistwidgetitem2 = self.exercise_list.item(0)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"testing", None));
        ___qlistwidgetitem3 = self.exercise_list.item(1)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"isa pa", None));
        self.exercise_list.setSortingEnabled(__sortingEnabled1)

        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Analysis:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Analysis:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"General Progress", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Analysis:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Exercise Progress", None))
        self.label_6.setStyleSheet(QCoreApplication.translate("MainWindow", u"font: 12pt \"Eras Medium ITC\";\n"
"color: rgb(255, 255, 255);", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Select Exercise:", None))
        self.Add_exercise_btn.setText(QCoreApplication.translate("MainWindow", u"Exercises", None))
        self.label_11.setStyleSheet(QCoreApplication.translate("MainWindow", u"font: 12pt \"Eras Medium ITC\";\n"
"color: rgb(255, 255, 255);", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Select Variation:", None))
        self.radioButton_weighted.setText(QCoreApplication.translate("MainWindow", u"Weighted", None))
        self.radioButton_bodyweight.setText(QCoreApplication.translate("MainWindow", u"Bodyweight", None))
        self.refresh_btn.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"General Analysis:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Filter:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Analysis:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Analysis:", None))
    # retranslateUi

