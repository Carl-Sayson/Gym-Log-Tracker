# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_exercise.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(892, 498)
        Form.setMinimumSize(QSize(892, 498))
        Form.setMaximumSize(QSize(892, 707))
        Form.setStyleSheet(u"background-color: rgb(57, 57, 57);")
        self.gridLayout_3 = QGridLayout(Form)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setFamilies([u"Eras Medium ITC"])
        font.setPointSize(12)
        self.label_6.setFont(font)

        self.verticalLayout_2.addWidget(self.label_6)

        self.name_exercise = QLineEdit(Form)
        self.name_exercise.setObjectName(u"name_exercise")
        self.name_exercise.setMinimumSize(QSize(250, 0))
        self.name_exercise.setMaximumSize(QSize(550, 16777215))
        self.name_exercise.setStyleSheet(u"QLineEdit {\n"
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

        self.verticalLayout_2.addWidget(self.name_exercise)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 50))
        self.label_7.setFont(font)

        self.verticalLayout_2.addWidget(self.label_7)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.Calisthenic = QRadioButton(self.widget)
        self.Calisthenic.setObjectName(u"Calisthenic")
        font1 = QFont()
        font1.setFamilies([u"Eras Medium ITC"])
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        self.Calisthenic.setFont(font1)
        self.Calisthenic.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Calisthenic.setStyleSheet(u"\n"
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

        self.horizontalLayout_3.addWidget(self.Calisthenic)

        self.Free_weight = QRadioButton(self.widget)
        self.Free_weight.setObjectName(u"Free_weight")
        self.Free_weight.setFont(font1)
        self.Free_weight.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Free_weight.setStyleSheet(u"\n"
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

        self.horizontalLayout_3.addWidget(self.Free_weight)


        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.widget)

        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 50))
        self.label_8.setFont(font)

        self.verticalLayout_2.addWidget(self.label_8)

        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout = QGridLayout(self.widget_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lower = QRadioButton(self.widget_2)
        self.lower.setObjectName(u"lower")
        self.lower.setFont(font1)
        self.lower.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.lower.setStyleSheet(u"\n"
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

        self.horizontalLayout_2.addWidget(self.lower)

        self.upper = QRadioButton(self.widget_2)
        self.upper.setObjectName(u"upper")
        self.upper.setFont(font1)
        self.upper.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.upper.setStyleSheet(u"\n"
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

        self.horizontalLayout_2.addWidget(self.upper)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.widget_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.De_Exer = QPushButton(Form)
        self.De_Exer.setObjectName(u"De_Exer")
        self.De_Exer.setMinimumSize(QSize(105, 27))
        self.De_Exer.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.De_Exer.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_6.addWidget(self.De_Exer)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Edit_exer = QPushButton(Form)
        self.Edit_exer.setObjectName(u"Edit_exer")
        self.Edit_exer.setMinimumSize(QSize(105, 27))
        self.Edit_exer.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Edit_exer.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout.addWidget(self.Edit_exer)

        self.Add_exercise = QPushButton(Form)
        self.Add_exercise.setObjectName(u"Add_exercise")
        self.Add_exercise.setMinimumSize(QSize(105, 27))
        self.Add_exercise.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Add_exercise.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout.addWidget(self.Add_exercise)


        self.horizontalLayout_6.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

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

        self.verticalLayout_2.addWidget(self.clear_fill, 0, Qt.AlignLeft)


        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 50))
        self.label_9.setFont(font)

        self.verticalLayout.addWidget(self.label_9)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
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

        self.horizontalLayout_4.addWidget(self.searchlog_lineEdit)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_16 = QLabel(Form)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font)
        self.label_16.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_5.addWidget(self.label_16)

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

        self.horizontalLayout_5.addWidget(self.filter_exercise)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_5)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

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


        self.gridLayout_3.addLayout(self.verticalLayout, 0, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_6.setStyleSheet(QCoreApplication.translate("Form", u"font: 12pt \"Eras Medium ITC\";\n"
"color: rgb(255, 255, 255);", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Add Exercise:", None))
        self.name_exercise.setPlaceholderText("")
        self.label_7.setStyleSheet(QCoreApplication.translate("Form", u"font: 12pt \"Eras Medium ITC\";\n"
"color: rgb(255, 255, 255);", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Exercise Type:", None))
        self.Calisthenic.setText(QCoreApplication.translate("Form", u"Calisthenic", None))
        self.Free_weight.setText(QCoreApplication.translate("Form", u"Free Weight", None))
        self.label_8.setStyleSheet(QCoreApplication.translate("Form", u"font: 12pt \"Eras Medium ITC\";\n"
"color: rgb(255, 255, 255);", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Target:", None))
        self.lower.setText(QCoreApplication.translate("Form", u"Lower", None))
        self.upper.setText(QCoreApplication.translate("Form", u"Upper", None))
        self.De_Exer.setText(QCoreApplication.translate("Form", u"Delete", None))
        self.Edit_exer.setText(QCoreApplication.translate("Form", u"Edit", None))
        self.Add_exercise.setText(QCoreApplication.translate("Form", u"Add", None))
        self.clear_fill.setText(QCoreApplication.translate("Form", u"Clear", None))
        self.label_9.setStyleSheet(QCoreApplication.translate("Form", u"font: 12pt \"Eras Medium ITC\";\n"
"color: rgb(255, 255, 255);", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Select Exercise:", None))
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

    # retranslateUi

