# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'exercise_logs.ui'
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
    QMainWindow, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QWidget)
import images_logos_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(836, 667)
        MainWindow.setStyleSheet(u"background-color: rgb(57, 57, 57);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_17 = QLabel(self.centralwidget)
        self.label_17.setObjectName(u"label_17")
        font = QFont()
        font.setFamilies([u"Eras Medium ITC"])
        font.setPointSize(12)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_5.addWidget(self.label_17)

        self.exercise_name = QLineEdit(self.centralwidget)
        self.exercise_name.setObjectName(u"exercise_name")
        self.exercise_name.setMinimumSize(QSize(250, 0))
        self.exercise_name.setMaximumSize(QSize(550, 16777215))
        self.exercise_name.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_5.addWidget(self.exercise_name)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)


        self.gridLayout.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_15 = QLabel(self.centralwidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font)
        self.label_15.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.label_15)

        self.dateEdit = QDateEdit(self.centralwidget)
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


        self.horizontalLayout_4.addLayout(self.horizontalLayout)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_16 = QLabel(self.centralwidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font)
        self.label_16.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.label_16)

        self.filter_date = QComboBox(self.centralwidget)
        self.filter_date.addItem("")
        self.filter_date.addItem("")
        self.filter_date.setObjectName(u"filter_date")
        self.filter_date.setMinimumSize(QSize(114, 24))
        self.filter_date.setMaximumSize(QSize(200, 16777215))
        self.filter_date.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.filter_date.setStyleSheet(u"/* ComboBox */\n"
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

        self.horizontalLayout_2.addWidget(self.filter_date)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)


        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)

        self.exer_logs = QTableWidget(self.centralwidget)
        if (self.exer_logs.columnCount() < 6):
            self.exer_logs.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.exer_logs.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.exer_logs.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.exer_logs.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.exer_logs.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.exer_logs.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.exer_logs.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.exer_logs.setObjectName(u"exer_logs")
        self.exer_logs.setStyleSheet(u"QTableWidget {\n"
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

        self.gridLayout.addWidget(self.exer_logs, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Name of Exercise:", None))
        self.exercise_name.setPlaceholderText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Date:", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Filter:", None))
        self.filter_date.setItemText(0, QCoreApplication.translate("MainWindow", u"Latest", None))
        self.filter_date.setItemText(1, QCoreApplication.translate("MainWindow", u"Oldest", None))

        ___qtablewidgetitem = self.exer_logs.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem1 = self.exer_logs.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"SET 1", None));
        ___qtablewidgetitem2 = self.exer_logs.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"SET 2", None));
        ___qtablewidgetitem3 = self.exer_logs.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"SET 3", None));
        ___qtablewidgetitem4 = self.exer_logs.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"SET 4", None));
        ___qtablewidgetitem5 = self.exer_logs.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"SET 5", None));
    # retranslateUi

