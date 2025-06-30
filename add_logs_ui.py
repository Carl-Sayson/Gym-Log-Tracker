# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_logs.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import images_logos_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(930, 644)
        Form.setMinimumSize(QSize(930, 644))
        Form.setStyleSheet(u"background-color: rgb(57, 57, 57);")
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_15 = QLabel(Form)
        self.label_15.setObjectName(u"label_15")
        font = QFont()
        font.setFamilies([u"Eras Medium ITC"])
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.label_15)

        self.dateEdit = QDateEdit(Form)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setMinimumSize(QSize(0, 24))
        self.dateEdit.setStyleSheet(u"QDateEdit {\n"
"    background-color: #2b2b2b; /* Dark background */\n"
"    color: white;              /* White text */\n"
"    border: 2px solid orange;\n"
"    border-radius: 8px;\n"
"    padding: 4px 8px;\n"
"    font: 8pt \"Eras Medium ITC\";\n"
"}\n"
"\n"
"/* The arrow icon in the drop-down */\n"
"QDateEdit::down-arrow {\n"
"   \n"
"	image: url(:/images/Screenshot_2025-06-10_142412-removebg-preview.png);\n"
"    width: 4px;\n"
"    height: 4px;\n"
"}\n"
"\n"
"QDateEdit::up-arrow {\n"
"   \n"
"	image: url(:/images/Screenshot_2025-06-10_142412-removebg-preview.png);\n"
"    width: 4px;\n"
"    height: 4px;\n"
"}\n"
"\n"
"/* Calendar popup styling */\n"
"QDateEdit QAbstractItemView {\n"
"    background-color: #2b2b2b;\n"
"    color: white;\n"
"    selection-background-color: orange;\n"
"    selection-color: black;\n"
"}\n"
"\n"
"/* Optional: Focus indicator */\n"
"QDateEdit:focus {\n"
"    border: 2px solid #ff8c00; /* Slightly lighter orange border on focus */\n"
"}")

        self.horizontalLayout.addWidget(self.dateEdit)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.horizontalLayout_4.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 50))
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


        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 3, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_11 = QLabel(Form)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(16777215, 50))
        self.label_11.setFont(font)

        self.horizontalLayout_5.addWidget(self.label_11)

        self.radioButton_weighted = QRadioButton(Form)
        self.radioButton_weighted.setObjectName(u"radioButton_weighted")
        font1 = QFont()
        font1.setFamilies([u"Eras Medium ITC"])
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        self.radioButton_weighted.setFont(font1)
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

        self.horizontalLayout_5.addWidget(self.radioButton_weighted)

        self.radioButton_bodyweight = QRadioButton(Form)
        self.radioButton_bodyweight.setObjectName(u"radioButton_bodyweight")
        self.radioButton_bodyweight.setFont(font1)
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

        self.horizontalLayout_5.addWidget(self.radioButton_bodyweight)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)


        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)

        self.tableWidget = QTableWidget(Form)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.tableWidget.rowCount() < 5):
            self.tableWidget.setRowCount(5)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem6)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"QTableWidget {\n"
"    background-color: #2b2b2b; /* Dark background */\n"
"    color: white; /* White text */\n"
"    border: 2px solid orange;\n"
"    border-radius: 8px;\n"
"    gridline-color: orange;\n"
"    font: 14pt \"Eras Medium ITC\";\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #ff8c00; /* Darker orange for headers */\n"
"    color: black; /* Black text in headers */\n"
"    padding: 4px;\n"
"    border: 1px solid orange;\n"
" \n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    border: 1px solid orange;\n"
"    padding: 4px;\n"
"}\n"
"\n"
"/* Hover effect for rows */\n"
"QTableWidget::item:hover {\n"
"    background-color: orange;\n"
"    color: black;\n"
"}\n"
"\n"
"/* Selected row styling */\n"
"QTableWidget::item:selected {\n"
"    background-color: #ff8c00; /* Darker orange */\n"
"    color: black;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.tableWidget, 2, 0, 1, 1)

        self.clear_log = QPushButton(Form)
        self.clear_log.setObjectName(u"clear_log")
        self.clear_log.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.clear_log.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout.addWidget(self.clear_log, 3, 0, 1, 1, Qt.AlignLeft)

        self.save_log = QPushButton(Form)
        self.save_log.setObjectName(u"save_log")
        self.save_log.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.save_log.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout.addWidget(self.save_log, 3, 1, 1, 1, Qt.AlignRight)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Date:", None))
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

        self.label_11.setStyleSheet(QCoreApplication.translate("Form", u"font: 12pt \"Eras Medium ITC\";\n"
"color: rgb(255, 255, 255);", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Select Variation:", None))
        self.radioButton_weighted.setText(QCoreApplication.translate("Form", u"Weighted", None))
        self.radioButton_bodyweight.setText(QCoreApplication.translate("Form", u"Bodyweight", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Reps", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Weight (Kg)", None));
        ___qtablewidgetitem2 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Set 1", None));
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Set 2", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Set 3", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Set 4", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"Set 5", None));
        self.clear_log.setText(QCoreApplication.translate("Form", u"Clear", None))
        self.save_log.setText(QCoreApplication.translate("Form", u"Save", None))
    # retranslateUi

