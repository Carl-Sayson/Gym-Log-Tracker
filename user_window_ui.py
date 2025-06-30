# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_window.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(504, 319)
        Form.setMinimumSize(QSize(392, 275))
        Form.setMaximumSize(QSize(504, 319))
        Form.setStyleSheet(u"background-color: rgb(57, 57, 57);\n"
"")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setFamilies([u"Eras Medium ITC"])
        font.setPointSize(12)
        self.label_9.setFont(font)

        self.gridLayout.addWidget(self.label_9, 0, 0, 1, 2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 50))
        self.label_6.setFont(font)

        self.horizontalLayout.addWidget(self.label_6)

        self.first_name = QLineEdit(Form)
        self.first_name.setObjectName(u"first_name")
        self.first_name.setMinimumSize(QSize(250, 0))
        self.first_name.setMaximumSize(QSize(550, 16777215))
        self.first_name.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout.addWidget(self.first_name)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 50))
        self.label_7.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_7)

        self.last_name = QLineEdit(Form)
        self.last_name.setObjectName(u"last_name")
        self.last_name.setMinimumSize(QSize(250, 0))
        self.last_name.setMaximumSize(QSize(550, 16777215))
        self.last_name.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_2.addWidget(self.last_name)


        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 50))
        self.label_8.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_8)

        self.weight = QLineEdit(Form)
        self.weight.setObjectName(u"weight")
        self.weight.setMinimumSize(QSize(250, 0))
        self.weight.setMaximumSize(QSize(550, 16777215))
        self.weight.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_3.addWidget(self.weight)


        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 0, 1, 2)

        self.clear_fill = QPushButton(Form)
        self.clear_fill.setObjectName(u"clear_fill")
        self.clear_fill.setMinimumSize(QSize(105, 27))
        self.clear_fill.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.clear_fill.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(255, 140, 0); /* Darker orange */\n"
"    color: black; /* Consistent text color */\n"
"    border-radius: 10px;\n"
"    padding: 5px 15px; /* Horizontal padding for better look */\n"
"    font-size: 14px; /* Optional: adjust font size */\n"
"    transition: background-color 0.3s, border-color 0.3s; /* Smooth transitions */\n"
" min-width: 75px; \n"
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

        self.gridLayout.addWidget(self.clear_fill, 4, 0, 1, 1, Qt.AlignLeft)

        self.save_user = QPushButton(Form)
        self.save_user.setObjectName(u"save_user")
        self.save_user.setMinimumSize(QSize(105, 27))
        self.save_user.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.save_user.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(255, 140, 0); /* Darker orange */\n"
"    color: black; /* Consistent text color */\n"
"    border-radius: 10px;\n"
"    padding: 5px 15px; /* Horizontal padding for better look */\n"
"    font-size: 14px; /* Optional: adjust font size */\n"
"    transition: background-color 0.3s, border-color 0.3s; /* Smooth transitions */\n"
" min-width: 75px; \n"
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

        self.gridLayout.addWidget(self.save_user, 4, 1, 1, 1, Qt.AlignRight)

#if QT_CONFIG(shortcut)
        self.label_9.setBuddy(self.first_name)
        self.label_6.setBuddy(self.first_name)
        self.label_7.setBuddy(self.last_name)
        self.label_8.setBuddy(self.weight)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_9.setStyleSheet(QCoreApplication.translate("Form", u"font: 12pt \"Eras Medium ITC\";\n"
"color: rgb(255, 255, 255);", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"User Credentials", None))
        self.label_6.setStyleSheet(QCoreApplication.translate("Form", u"font: 12pt \"Eras Medium ITC\";\n"
"color: rgb(255, 255, 255);", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"First Name:", None))
        self.first_name.setPlaceholderText("")
        self.label_7.setStyleSheet(QCoreApplication.translate("Form", u"font: 12pt \"Eras Medium ITC\";\n"
"color: rgb(255, 255, 255);", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Last Name:", None))
        self.last_name.setPlaceholderText("")
        self.label_8.setStyleSheet(QCoreApplication.translate("Form", u"font: 12pt \"Eras Medium ITC\";\n"
"color: rgb(255, 255, 255);", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Weight (Kg):", None))
        self.weight.setPlaceholderText("")
        self.clear_fill.setText(QCoreApplication.translate("Form", u"Clear", None))
        self.save_user.setText(QCoreApplication.translate("Form", u"Save", None))
    # retranslateUi

