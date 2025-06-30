# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'select_exercise.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import images_logos_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(501, 599)
        Form.setMinimumSize(QSize(501, 599))
        Form.setMaximumSize(QSize(501, 599))
        Form.setStyleSheet(u"background-color: rgb(57, 57, 57);")
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setFamilies([u"Eras Medium ITC"])
        font.setPointSize(12)
        self.label_6.setFont(font)

        self.verticalLayout.addWidget(self.label_6)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.searchlog_lineEdit = QLineEdit(Form)
        self.searchlog_lineEdit.setObjectName(u"searchlog_lineEdit")
        self.searchlog_lineEdit.setMinimumSize(QSize(250, 0))
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

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_16 = QLabel(Form)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font)
        self.label_16.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.label_16)

        self.filter_exercise = QComboBox(Form)
        self.filter_exercise.addItem("")
        self.filter_exercise.addItem("")
        self.filter_exercise.addItem("")
        self.filter_exercise.addItem("")
        self.filter_exercise.setObjectName(u"filter_exercise")
        self.filter_exercise.setMinimumSize(QSize(114, 24))
        self.filter_exercise.setMaximumSize(QSize(200, 16777215))
        self.filter_exercise.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.filter_exercise.setStyleSheet(u"/* ComboBox */\n"
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
"	\n"
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

        self.horizontalLayout_2.addWidget(self.filter_exercise)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.exercise_list = QListWidget(Form)
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

        self.verticalLayout.addWidget(self.exercise_list)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.select_exercise = QPushButton(Form)
        self.select_exercise.setObjectName(u"select_exercise")
        self.select_exercise.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.select_exercise.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(255, 140, 0); /* Darker orange */\n"
"    color: black; /* Consistent text color */\n"
"    border-radius: 10px;\n"
"    padding: 5px 15px; /* Horizontal padding for better look */\n"
"    font-size: 14px; /* Optional: adjust font size */\n"
"    transition: background-color 0.3s, border-color 0.3s; /* Smooth transitions */\n"
" min-width: 100px; \n"
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

        self.verticalLayout_2.addWidget(self.select_exercise, 0, Qt.AlignHCenter)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_6.setStyleSheet(QCoreApplication.translate("Form", u"font: 12pt \"Eras Medium ITC\";\n"
"color: rgb(255, 255, 255);", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Select Exercise:", None))
        self.searchlog_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Search...", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"Filter:", None))
        self.filter_exercise.setItemText(0, QCoreApplication.translate("Form", u"Calisthenic", None))
        self.filter_exercise.setItemText(1, QCoreApplication.translate("Form", u"Free Weights", None))
        self.filter_exercise.setItemText(2, QCoreApplication.translate("Form", u"Upper", None))
        self.filter_exercise.setItemText(3, QCoreApplication.translate("Form", u"Lower", None))


        __sortingEnabled = self.exercise_list.isSortingEnabled()
        self.exercise_list.setSortingEnabled(False)
        ___qlistwidgetitem = self.exercise_list.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Form", u"testing", None));
        ___qlistwidgetitem1 = self.exercise_list.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Form", u"isa pa", None));
        self.exercise_list.setSortingEnabled(__sortingEnabled)

        self.select_exercise.setText(QCoreApplication.translate("Form", u"Select", None))
    # retranslateUi

