"""
This is going to be the main file of the project
This will involve many modules as well as SQL
"""

import mysql.connector
import re
import sys
from collections import defaultdict
import bisect
from datetime import timedelta, datetime, timezone
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox, QDialog, QListWidgetItem, QPushButton,
                                QLineEdit, QTableWidgetItem, QTableWidget, QComboBox, QListWidget, QAbstractItemView, 
                                QHeaderView, QFileDialog, QProgressBar, QVBoxLayout, QLabel, QStyledItemDelegate)
from PySide6.QtCore import Qt, QTime, Signal, QThread, QObject, QEvent, QTimer, QRegularExpression, QPointF, QDate, QtMsgType, qInstallMessageHandler
from PySide6.QtGui import QFont, QPainter, QPen, QIntValidator, QRegularExpressionValidator, QColor
from PySide6.QtCharts import QChart, QChartView, QLineSeries, QValueAxis, QCategoryAxis, QScatterSeries
from PySide6.QtUiTools import QUiLoader
import images_logos_rc

from main_dashboard_ui import Ui_MainWindow as Dasboard
from add_exercise_ui import Ui_Form as add_exercise
from add_logs_ui import Ui_Form as add_logs
from select_exercise_ui import Ui_Form as select_exercise
from exercise_logs_ui import Ui_MainWindow as exercise_logs
from user_window_ui import Ui_Form as User_window


def suppress_qt_warnings(msg_type, msg_log_context, msg_string):
    if msg_type == QtMsgType.QtWarningMsg:
        if "Unknown property" in msg_string:
            return  # Ignore specific warnings
    print(msg_string)  # Let others through (optional)

# Install the custom message handler
qInstallMessageHandler(suppress_qt_warnings)


class Main_Dashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Dasboard()
        self.ui.setupUi(self)

        try: 
            self.mydb = mysql.connector.connect(
                host="localhost",
                user="Group_F",
                password="CPET-8L-TUPCROOM",
                database="gym_tracker",
                ssl_disabled=True,  # This should fix it
                autocommit=False
            )
            self.mycursor = self.mydb.cursor(buffered=True)     
            print('connection successful')
        except mysql.connector.Error as err:
            self.errorDisplay(err.errno, err.sqlstate, err.msg) 

        self.add_user() # checks if user is already in system, else adds it

        self.resulted_data = None
        self.load_exercise_list()
        # Sidebar
        self.ui.dashbtns_groupBox_2.setHidden(True)
        # connections
        self.ui.logs_btn.clicked.connect(lambda: self.ui.main_dashboard.setCurrentIndex(0))
        self.ui.logs_btn_short.clicked.connect(lambda: self.ui.main_dashboard.setCurrentIndex(0))
        self.ui.progress_btn.clicked.connect(lambda: self.ui.main_dashboard.setCurrentIndex(2))
        self.ui.progress_btn_short.clicked.connect(lambda: self.ui.main_dashboard.setCurrentIndex(2))

        self.ui.dashboard_btn.clicked.connect(lambda: self.ui.main_dashboard.setCurrentIndex(1))
        self.ui.dashboard_btn_short.clicked.connect(lambda: self.ui.main_dashboard.setCurrentIndex(1))

        self.ui.pushButton_2.clicked.connect(self.open_user)
        self.ui.pushButton_4.clicked.connect(self.open_user)
        self.ui.pushButton.clicked.connect(self.add_exercise)
        self.ui.pushButton_3.clicked.connect(self.add_exercise)

        self.ui.Add_log.clicked.connect(self.add_log)
        self.ui.Add_exercise_btn.clicked.connect(self.open_select_exercise)

        self.ui.general_progress_analysis_textedit.setFocusPolicy(Qt.NoFocus)
        self.ui.general_progress_analysis_textedit.setReadOnly(True)
        self.ui.frequency_analysis.setFocusPolicy(Qt.NoFocus)
        self.ui.frequency_analysis.setReadOnly(True)
        self.ui.progress_analysis.setFocusPolicy(Qt.NoFocus)
        self.ui.progress_analysis.setReadOnly(True)

        self.ui.View_log.clicked.connect(self.open_logs)
        self.num_window_opened = 0

        # mostly will be used for changing stuff and else
        self.monthly_data_gen = []
        self.yearly_data_gen = []

        self.load_general_data_analysis() # loads needed data also setting up the charts itself

        self.ui.log_list.itemSelectionChanged.connect(self.selected_exer_view)
        self.ui.exercise_list.itemSelectionChanged.connect(self.log_exer_view)
        self.ui.info_log_plaintext.setReadOnly(True)

        self.timestamps_logs = [] # will be used for referencing later on
        self.load_logs()
        self.ui.label_4.setText("Progress Overview")

        self.ui.searchlog_lineEdit.textChanged.connect(self.perform_searchlog)
        self.ui.searchlog_lineEdit.setPlaceholderText("Type name of exercise...")

        self.ui.radioButton_bodyweight.setDisabled(True)
        self.ui.radioButton_weighted.setDisabled(True)

        self.ui.radioButton_bodyweight.clicked.connect(lambda: self.load_specific_exer_data_cali('bodyweight'))
        self.ui.radioButton_weighted.clicked.connect(lambda: self.load_specific_exer_data_cali('weighted'))
    
        # Will be used for specific exercises
        self.setup_exercise_frequency()
        self.setup_exercise_progress()
        self.ui.Filter_Year.currentIndexChanged.connect(lambda: self.update_general_monthly(self.ui.Filter_Year.currentText()))
        self.ui.filter_year.currentIndexChanged.connect(lambda: self.update_dataplots_yearly(self.ui.filter_year.currentText()))
        self.ui.filter_year.currentIndexChanged.connect(lambda: self.update_frequency_dataplots(self.ui.filter_year.currentText()))
        self.ui.refresh_btn.clicked.connect(self.refresh_analysis)

        # For deleting logs based on what is currently selected
        self.ui.Del_log.clicked.connect(self.del_logs)

        # referencing used for refreshing
        self.exer_name = None
        self.exer_type = None

    def sql_helper(self):
        sql_info = {
            "host": "localhost",
            "user": "Group_F",
            "password": "CPET-8L-TUPCROOM",
            "database": "gym_tracker",
            "ssl_disabled": True,  
            "autocommit": False
        }
        return sql_info

    def load_general_data_analysis(self):
        try:
            self.thread_loader = QThread()
            self.thread_worker = General_Analysis()
            self.thread_worker.moveToThread(self.thread_loader)

            self.thread_loader.started.connect(self.thread_worker.run)
            self.thread_worker.finished.connect(self.load_actual_gen_data)
            self.thread_worker.finished.connect(self.thread_loader.quit)
            self.thread_worker.finished.connect(self.thread_worker.deleteLater)
            self.thread_loader.finished.connect(self.thread_loader.deleteLater)
            
            self.thread_worker.err_sql.connect(self.errorDisplay)
            self.thread_worker.error.connect(self.err_load_general_data)

            self.thread_loader.start()
            
        except mysql.connector.Error as err:
            self.errorDisplay(err.errno, err.sqlstate, err.msg)
            return

    def err_load_general_data(self, msg):
        QMessageBox.warning(None, "Error", f"Unexpected error occurred in loading general analysis: {msg}")
        return

    def load_actual_gen_data(self, monthly_data, yearly_data):
        self.monthly_data_gen = monthly_data
        self.yearly_data_gen = yearly_data
        self.setup_general_year_filter(self.monthly_data_gen) # setups filter here first then stuff
        self.setup_progress_series_yearly(yearly_data)
        self.setup_progress_series_monthly(monthly_data)
        return
        
    def perform_searchlog(self, text):
        try:
            search_text = text

            if not search_text:
                self.load_logs()
                return

            else:
                query = """
                    SELECT exercise_name, timestamp_logs FROM exercise_logs
                    WHERE exercise_name LIKE UPPER(%s)
                    ORDER BY timestamp_logs DESC LIMIT 10
                        """
                self.mycursor.execute(query, (f"%{search_text}%",))

            results = self.mycursor.fetchall()

            if not results:
                self.ui.log_list.clear()
                self.ui.log_list.addItem('No match found')
                return

            self.ui.log_list.clear()  # Assuming QListWidget
            self.timestamps_logs.clear() # Avoiding any problems hopefully

            for name, timestamp in results:
                formatted_time = str(timestamp.split('.')[0])
                original_timestamp = {
                    'name': name,
                    'formatted': formatted_time,
                    'timestamp': timestamp
                }
                self.timestamps_logs.append(original_timestamp)
                recent_stffs = name + " - " + formatted_time
                item = QListWidgetItem(recent_stffs)
                item.setTextAlignment(Qt.AlignLeft)
                self.ui.log_list.addItem(item)

            return

        except mysql.connector.Error as err:
            self.errorDisplay(err.errno, err.sqlstate, err.msg)

    def add_user(self):
        try:
            first_name = "Carl Lloyd"
            last_name = "Sayson"
            weight = 56.0

            #checks user first if existing
            self.mycursor.execute("SELECT COUNT(*) FROM user_account")
            result = self.mycursor.fetchone()[0]

            if result == 0:
                self.mycursor.execute("""
            INSERT INTO user_account (first_name, last_name, weight)
            VALUES (%s, %s, %s)
            """, (first_name, last_name, weight))

            self.mydb.commit()

        except mysql.connector.Error as err:
            self.errorDisplay(err.errno, err.sqlstate, err.msg)

    def load_logs(self):
        log_list = self.ui.log_list
        self.timestamps_logs.clear()
        log_list.clear()
        try:
            query = """
            SELECT exercise_name, timestamp_logs FROM exercise_logs
            ORDER BY timestamp_logs DESC LIMIT 10
                """
            self.mycursor.execute(query)
            list_recent = self.mycursor.fetchall()

            for name, timestamp in list_recent:
                formatted_time = str(timestamp.split('.')[0])
                original_timestamp = {
                    'name': name,
                    'formatted': formatted_time,
                    'timestamp': timestamp
                }
                self.timestamps_logs.append(original_timestamp)
                recent_stffs = name + " - " + formatted_time
                item = QListWidgetItem(recent_stffs)
                item.setTextAlignment(Qt.AlignLeft)
                log_list.addItem(item)

        except mysql.connector.Error as err:
            self.errorDisplay(err.errno, err.sqlstate, err.msg)

    def errorDisplay(self, errno, sqlstate, msg):
        """Displays detailed error information to the user."""
        self.mydb.rollback()
        # Construct the error message
        error_message = f"Error Code: {errno}\nSQLSTATE: {sqlstate}\nMessage: {msg}"

        # Create and show a critical error message box with the detailed error
        QMessageBox.critical(None, "Database Error", error_message)

# SETUP FOR GENERAL ANALYSIS

    def setup_progress_series_yearly(self, yearly_data):
        # Create the line series
        aggregated_data = defaultdict(float)
        for entry in yearly_data:
            year = entry[2]
            progress = entry[1]
            aggregated_data[year] += progress

        # Convert to sorted list of (year, total_progress)
        summed_yearly_data = sorted(aggregated_data.items())
        
        if not yearly_data:
            self.series = QLineSeries()
            self.series.setName("No Data Yet")
            self.series.setColor(QColor('orange'))

            # Optional: Show 3 fake years with zero progress
            placeholder_years = [2023, 2024, 2025]
            for year in placeholder_years:
                self.series.append(QPointF(year, 0))
            display_years = placeholder_years
            title_year = "—"
        else:
            display_years = [entry[0] for entry in summed_yearly_data]
            self.series = QLineSeries() if len(display_years) > 1 else QScatterSeries()
            self.series.setName("Yearly Progress")
            self.series.setColor(QColor('orange'))
            if isinstance(self.series, QScatterSeries):
                self.series.setBorderColor(QColor('orange'))

            for year, progress_value in summed_yearly_data:
                self.series.append(QPointF(year, progress_value))
            title_year = f"{min(display_years)} - {max(display_years)}"

        # Create chart
        self.chart = QChart()
        self.chart.addSeries(self.series)
        self.chart.setTitle(f"Yearly Progress Summary ({title_year})")

        # Setup X-axis (Years)
        x_axis = QValueAxis()
        x_axis.setTitleText("Year")
        x_axis.setLabelFormat("%d")

        if display_years:
            if len(display_years) == 1:
                x_axis.setRange(display_years[0] - 1, display_years[0] + 1)
            else:
                x_axis.setRange(min(display_years), max(display_years))
        else:
            x_axis.setRange(2023, 2025)

        # Setup Y-axis
        y_axis = QValueAxis()
        y_axis.setTitleText("Progress")
        y_axis.setLabelFormat("%.1f")
        y_axis.setRange(0, 10 if not yearly_data else max(entry[1] for entry in yearly_data) + 10)

        # Add and attach the X axis
        self.chart.addAxis(x_axis, Qt.AlignmentFlag.AlignBottom)
        self.series.attachAxis(x_axis)

        # Add and attach the Y axis
        self.chart.addAxis(y_axis, Qt.AlignmentFlag.AlignLeft)
        self.series.attachAxis(y_axis)

        self.chart_view = QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.clear_layout(self.ui.verticalLayout_progress)
        self.ui.verticalLayout_progress.addWidget(self.chart_view)

    def setup_progress_series_monthly(self, monthly_data):
        # Create the line series
        month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

        if not monthly_data:
            self.series = QLineSeries() # if no data yet, defuaults to line series
            # Optional: Placeholder data or zero line
            self.series.setName("No Data Yet")
            for i in range(1, 4):  # Show fake months 1 to 3 with 0 progress
                self.series.append(QPointF(i, 0))
            target_year = "—"
            self.series.setColor(QColor('orange'))
        else:          
            month_progress = {}
            years = [entry[3] for entry in monthly_data]
            target_year = max(years)
            for entry in monthly_data:
                if entry[3] != target_year:
                    continue
                month = entry[0].month
                progress = entry[2]
                
                if month not in month_progress:
                    month_progress[month] = progress
                else:
                    month_progress[month] += progress
            self.series = QLineSeries() if len(month_progress) > 1 else QScatterSeries()
        
            
            self.series.setName("Monthly Progress")
            self.series.setColor(QColor('orange'))
            if isinstance(self.series, QScatterSeries):
                self.series.setBorderColor(QColor('orange'))
                
            for month_num in sorted(month_progress.keys()):
                self.series.append(QPointF(int(month_num), month_progress[month_num]))

        # Chart setup
        self.chart = QChart()
        self.chart.addSeries(self.series)
        self.chart.setTitle(f"Monthly Progress for {target_year}")

        # X-axis setup
        x_axis = QCategoryAxis()
        x_axis.setTitleText("Month")

        if monthly_data:
            for month_num in sorted(month_progress.keys()):
                x_axis.append(month_names[month_num - 1], month_num)
            
            # Fix: Handle single data point case
            if len(month_progress) == 1:
                single_month = list(month_progress.keys())[0]
                x_axis.setRange(single_month - 0.5, single_month + 0.5)
            else:
                x_axis.setRange(min(month_progress), max(month_progress))
        else:
            x_axis.append("Jan", 1)
            x_axis.append("Feb", 2)
            x_axis.append("Mar", 3)
            x_axis.setRange(1, 3)

        # Y-axis
        y_axis = QValueAxis()
        y_axis.setTitleText("Progress")
        y_axis.setLabelFormat("%.1f")
        y_axis.setRange(0, 10 if not monthly_data else max(entry[2] for entry in monthly_data) + 10)
        print(monthly_data)

        self.chart.addAxis(x_axis, Qt.AlignmentFlag.AlignBottom)
        self.series.attachAxis(x_axis)

        self.chart.addAxis(y_axis, Qt.AlignmentFlag.AlignLeft)
        self.series.attachAxis(y_axis)

        self.chart_view = QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.clear_layout(self.ui.verticalLayout_frequency)
        self.ui.verticalLayout_frequency.addWidget(self.chart_view)

    def setup_general_year_filter(self, monthly_data):
        years = sorted(set([year[3] for year in monthly_data]), reverse=True)
        for year in list(years):
            self.ui.Filter_Year.addItem(str(year))

    def update_general_monthly(self, item_changed):
        month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        month_progress = {}
        target_year = item_changed

        for entry in self.monthly_data_gen:
            if str(entry[3]) != target_year:
                continue
            month = entry[0].month
            progress = entry[2]
            if month not in month_progress:
                month_progress[month] = progress
            else:
                month_progress[month] += progress

        self.series = QLineSeries() if len(month_progress) > 1 else QScatterSeries()
        self.series.setName("Monthly Progress")
        self.series.setColor(QColor('orange'))
        if isinstance(self.series, QScatterSeries):
            self.series.setBorderColor(QColor('orange'))
        for month_num in sorted(month_progress.keys()):
            self.series.append(QPointF(month_num, month_progress[month_num]))

        # Chart setup
        self.chart = QChart()
        self.chart.addSeries(self.series)
        self.chart.setTitle(f"Monthly Progress for {target_year}")

        # X-axis setup
        x_axis = QCategoryAxis()
        x_axis.setTitleText("Month")

        if self.monthly_data_gen:
            for month_num in sorted(month_progress.keys()):
                x_axis.append(month_names[month_num - 1], month_num)
            x_axis.setRange(min(month_progress), max(month_progress))
        else:
            x_axis.append("Jan", 1)
            x_axis.append("Feb", 2)
            x_axis.append("Mar", 3)
            x_axis.setRange(1, 3)
            self.series.append(QPointF(1, 0))
            self.series.append(QPointF(2, 0))
            self.series.append(QPointF(3, 0))
            self.chart.setTitle(f"No data for {target_year}")

        # Y-axis
        y_axis = QValueAxis()
        y_axis.setTitleText("Progress")
        y_axis.setLabelFormat("%.1f")
        if not self.monthly_data_gen:
            y_axis.setRange(0, 10)  # Show empty 0–10 scale if no data

        if len(month_progress) == 1:
            x = list(month_progress.keys())[0]
            y = list(month_progress.values())[0]
            x_axis.setRange(x - 1, x + 1)
            y_axis.setRange(0, y + 10)

        self.chart.addAxis(x_axis, Qt.AlignmentFlag.AlignBottom)
        self.series.attachAxis(x_axis)

        self.chart.addAxis(y_axis, Qt.AlignmentFlag.AlignLeft)
        self.series.attachAxis(y_axis)

        self.chart_view = QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.clear_layout(self.ui.verticalLayout_frequency)
        self.ui.verticalLayout_frequency.addWidget(self.chart_view)

# FOR RESETTING LAYOUT

    def clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

# FOR SPECIFIC EXERCISES CHOSEN ANALYSIS

    def setup_exercise_progress(self):
       # Dummy line series
        self.series = QLineSeries()
        self.series.setName("Exercise Progress (No Selected Exercise)")
        self.series.append(QPointF(1, 0))
        self.series.append(QPointF(2, 0))
        self.series.append(QPointF(3, 0))
        self.series.setColor(QColor('orange'))

        # Chart setup
        self.chart = QChart()
        self.chart.addSeries(self.series)
        self.chart.setTitle("Exercise Progress (Waiting for Data)")

        # Axes
        x_axis = QValueAxis()
        x_axis.setTitleText("Session")
        x_axis.setRange(1, 3)

        y_axis = QValueAxis()
        y_axis.setTitleText("Progress")
        y_axis.setRange(0, 10)

        self.chart.addAxis(x_axis, Qt.AlignmentFlag.AlignBottom)
        self.series.attachAxis(x_axis)

        self.chart.addAxis(y_axis, Qt.AlignmentFlag.AlignLeft)
        self.series.attachAxis(y_axis)

        # Chart view
        self.chart_view = QChartView(self.chart)
        self.chart_view.setMinimumHeight(300)
        self.chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)
        # Replace existing chart
        self.clear_layout(self.ui.verticalLayout_exercise_progress)
        self.ui.verticalLayout_exercise_progress.addWidget(self.chart_view)

    def setup_exercise_frequency(self):
       # Dummy line series
        self.series = QLineSeries()
        self.series.setName("Exercise Frequency (No Selected Exercise)")
        self.series.append(QPointF(1, 0))
        self.series.append(QPointF(2, 0))
        self.series.append(QPointF(3, 0))
        self.series.setColor(QColor('orange'))

        # Chart setup
        self.chart = QChart()
        self.chart.addSeries(self.series)
        self.chart.setTitle("Exercise Frequency (Waiting for Data)")

        # Axes
        x_axis = QValueAxis()
        x_axis.setTitleText("Session")
        x_axis.setRange(1, 3)

        y_axis = QValueAxis()
        y_axis.setTitleText("Count")
        y_axis.setRange(0, 10)

        self.chart.addAxis(x_axis, Qt.AlignmentFlag.AlignBottom)
        self.series.attachAxis(x_axis)

        self.chart.addAxis(y_axis, Qt.AlignmentFlag.AlignLeft)
        self.series.attachAxis(y_axis)

        # Chart view
        self.chart_view = QChartView(self.chart)
        self.chart_view.setMinimumHeight(300)
        self.chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)
        # Replace existing chart
        self.clear_layout(self.ui.verticalLayout_frequency_exercise)
        self.ui.verticalLayout_frequency_exercise.addWidget(self.chart_view)
   
    def open_select_exercise(self):
        self.select_window = Select_exercise(self.mycursor, self.mydb)
        self.select_window.Selected_exercise.connect(self.load_specific_exercise_analysis)
        self.select_window.exec() 
        
    def load_specific_exercise_analysis(self, exercise_name, exer_type):     
        if not exercise_name:
            return
        self.exer_name = exercise_name
        self.exer_type = exer_type

        if self.ui.radioButton_bodyweight.isChecked():
            active_radio = self.ui.radioButton_bodyweight
        else:
            active_radio = self.ui.radioButton_weighted
        self.auto_unselect(active_radio)

        if self.exer_type == 'Calisthenic':
            self.ui.radioButton_bodyweight.setDisabled(False)
            self.ui.radioButton_weighted.setDisabled(False)
        else:
            self.ui.radioButton_bodyweight.setDisabled(True)
            self.ui.radioButton_weighted.setDisabled(True)

            if self.ui.radioButton_bodyweight.isChecked():
                active_radio = self.ui.radioButton_bodyweight
            else:
                active_radio = self.ui.radioButton_weighted
            self.auto_unselect(active_radio)
            self.load_specific_exer_data(self.exer_name)

    def auto_unselect(self, active_radio):
        active_radio.setAutoExclusive(False)
        active_radio.setChecked(False)
        active_radio.setAutoExclusive(True)
        
    def load_specific_exer_data(self, exer_name):
        try:    
            info = self.sql_helper()

            self.thread_exer = QThread()
            self.worker_exer = Retrieve_Data_Exer(exer_name, info)
            self.worker_exer.moveToThread(self.thread_exer)

            self.thread_exer.started.connect(self.worker_exer.run_freeweight)
            self.worker_exer.finished.connect(self.successful_load_exer_data)
            self.worker_exer.finished.connect(self.thread_exer.quit)
            self.worker_exer.finished.connect(self.worker_exer.deleteLater)
            self.thread_exer.finished.connect(self.thread_exer.deleteLater)

            self.worker_exer.err_sql.connect(self.errorDisplay)
            self.worker_exer.error.connect(self.err_load_exer_data)

            self.thread_exer.start()

        except Exception as err:
            QMessageBox.warning(None, 'Error', f'An error occurred in loading the data {err}')
            return

    def load_specific_exer_data_cali(self, cali_type):
        try:
            exer_type_cali = 'Bodyweight' if cali_type == "bodyweight" else None

            info = self.sql_helper()

            if not exer_type_cali: # For weighted data in Calisthenics
                self.thread_exer = QThread()
                self.worker_exer = Retrieve_Data_Exer(self.exer_name, info)
                self.worker_exer.moveToThread(self.thread_exer)

                self.thread_exer.started.connect(self.worker_exer.run_weighted)
                self.worker_exer.finished.connect(self.successful_load_exer_data)
                self.worker_exer.finished.connect(self.thread_exer.quit)
                self.worker_exer.finished.connect(self.worker_exer.deleteLater)
                self.thread_exer.finished.connect(self.thread_exer.deleteLater)

                self.worker_exer.err_sql.connect(self.errorDisplay)
                self.worker_exer.error.connect(self.err_load_exer_data)

                self.thread_exer.start()
            
            else:
                self.thread_exer = QThread()
                self.worker_exer = Retrieve_Data_Exer(self.exer_name, info)
                self.worker_exer.moveToThread(self.thread_exer)

                self.thread_exer.started.connect(self.worker_exer.run_bodyweight)
                self.worker_exer.finished.connect(self.successful_load_exer_data)
                self.worker_exer.finished.connect(self.thread_exer.quit)
                self.worker_exer.finished.connect(self.worker_exer.deleteLater)
                self.thread_exer.finished.connect(self.thread_exer.deleteLater)

                self.worker_exer.err_sql.connect(self.errorDisplay)
                self.worker_exer.error.connect(self.err_load_exer_data)

                self.thread_exer.start()

        except Exception as err:
            QMessageBox.warning(None, 'Error', f'An error occurred in loading the data {err}')
            return

    def successful_load_exer_data(self, data_retrieved):
        self.specific_exer_data =  data_retrieved
        
        monthly_totals = defaultdict(float)
        if not self.specific_exer_data:
            self.load_actual_dataplots(self.specific_exer_data)
            self.ui.filter_year.clear() # clear years per exercise to avoid redundancy
            return
        self.ui.filter_year.clear() # clear years per exercise to avoid redundancy
        years = sorted(set([year.year for year, _ in self.specific_exer_data]), reverse=True)  
        for year in list(years):
            self.ui.filter_year.addItem(str(year))  
        max_year = max(years)

         # Sum values per (year, month)
        for date_obj, value in self.specific_exer_data:
            if max_year == date_obj.year:
                key = (date_obj.year, date_obj.month)
                monthly_totals[key] += value
        sorted_totals = sorted(monthly_totals.items(), reverse=True)

        self.load_actual_dataplots(sorted_totals)
        self.count_frequency_data(self.specific_exer_data, max_year=max_year)

    def count_frequency_data(self, data_list, max_year):
        session_count = defaultdict(float)

        for date, _ in data_list:
            if max_year == date.year:
                key = (date.year, date.month)
                session_count[key] += 1 # workout frequency I have done
        
        sorted_session_count = sorted(session_count.items(), reverse=True)
        self.load_frequency_dataplots(sorted_session_count)

    def load_actual_dataplots(self, sorted_total):
        if not sorted_total:
            # No data available
            self.series = QLineSeries()
            self.series.setName("No Data Yet")
            self.series.setColor(QColor('orange'))

            current_year = QDate.currentDate().year()
            placeholder_months = [6, 7, 8]
            for month in placeholder_months:
                self.series.append(QPointF(month, 0))

            display_months = placeholder_months
            title_year = str(current_year)
        else:
            # Extract year from first tuple
            title_year = sorted_total[0][0][0]
            display_months = [month for (year, month), _ in sorted_total]

            # Use QLineSeries or QScatterSeries depending on how many points there are
            self.series = QLineSeries() if len(display_months) > 1 else QScatterSeries()
            self.series.setName("Exercise Progress")
            self.series.setColor(QColor('orange'))

            if isinstance(self.series, QScatterSeries):
                self.series.setBorderColor(QColor('orange'))

            for (year, month), progress_sum in sorted_total:
                self.series.append(QPointF(month, round(progress_sum, 2)))

        # Create chart
        self.chart = QChart()
        self.chart.addSeries(self.series)
        self.chart.setTitle(f"Monthly Progress Summary ({title_year})")

        # X-axis setup (Month numbers)
        x_axis = QValueAxis()
        x_axis.setTitleText("Month")
        x_axis.setLabelFormat("%d")
        if display_months:
            if len(display_months) == 1:
                x_axis.setRange(display_months[0] - 1, display_months[0] + 1)
            else:
                x_axis.setRange(min(display_months), max(display_months))
        else:
            x_axis.setRange(1, 12)

        # Y-axis setup
        y_axis = QValueAxis()
        y_axis.setTitleText("Total Progress")
        y_axis.setLabelFormat("%.1f")
        y_axis.setRange(0, 10 if not sorted_total else max(val for (_, val) in sorted_total) + 10)

        self.chart.addAxis(x_axis, Qt.AlignmentFlag.AlignBottom)
        self.series.attachAxis(x_axis)

        self.chart.addAxis(y_axis, Qt.AlignmentFlag.AlignLeft)
        self.series.attachAxis(y_axis)

        self.chart_view = QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Replace existing chart
        self.clear_layout(self.ui.verticalLayout_exercise_progress)
        self.ui.verticalLayout_exercise_progress.addWidget(self.chart_view)

    def update_dataplots_yearly(self, year):
        target_year = year
        monthly_totals = defaultdict(float)

         # Sum values per (year, month)
        for date_obj, value in self.specific_exer_data:
            if target_year == str(date_obj.year):
                key = (date_obj.year, date_obj.month)
                monthly_totals[key] += value

        sorted_total = sorted(monthly_totals.items())

        if not sorted_total:
            self.series = QLineSeries()
            self.series.setName("No Data Yet")
            self.series.setColor(QColor('orange'))

            # Show 3 months as placeholders with zero values
            placeholder_months = [6, 7, 8]
            for month in placeholder_months:
                self.series.append(QPointF(month, 0))

            display_months = placeholder_months
            title_year = str(target_year)
        else:
            # Extract real chart data
            title_year = sorted_total[0][0][0]
            display_months = [month for (year, month), _ in sorted_total]

            self.series = QLineSeries() if len(display_months) > 1 else QScatterSeries()
            self.series.setName("Exercise Progress")
            self.series.setColor(QColor('orange'))

            if isinstance(self.series, QScatterSeries):
                self.series.setBorderColor(QColor('orange'))

            for (year, month), progress_sum in sorted_total:
                self.series.append(QPointF(month, progress_sum))

        # Create chart
        self.chart = QChart()
        self.chart.addSeries(self.series)
        self.chart.setTitle(f"Monthly Progress Summary ({title_year})")

        # X-axis setup (Month numbers)
        x_axis = QValueAxis()
        x_axis.setTitleText("Month")
        x_axis.setLabelFormat("%d")
        if display_months:
            if len(display_months) == 1:
                x_axis.setRange(display_months[0] - 1, display_months[0] + 1)
            else:
                x_axis.setRange(min(display_months), max(display_months))
        else:
            x_axis.setRange(1, 12)

        # Y-axis setup
        y_axis = QValueAxis()
        y_axis.setTitleText("Total Progress")
        y_axis.setLabelFormat("%.1f")
        y_axis.setRange(0, 10 if not sorted_total else max(val for (_, val) in sorted_total) + 10)

        self.chart.addAxis(x_axis, Qt.AlignmentFlag.AlignBottom)
        self.series.attachAxis(x_axis)

        self.chart.addAxis(y_axis, Qt.AlignmentFlag.AlignLeft)
        self.series.attachAxis(y_axis)

        self.chart_view = QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Replace existing chart
        self.clear_layout(self.ui.verticalLayout_exercise_progress)
        self.ui.verticalLayout_exercise_progress.addWidget(self.chart_view)

    def err_load_exer_data(self, msg):
        QMessageBox.warning(None, "Error", f"Unexpected error occurred in loading analysis: {msg}")
        return

    def refresh_analysis(self):
        if not self.exer_name:
            return
        if self.exer_type == 'Calisthenic':
            if self.ui.radioButton_bodyweight.isChecked():
                self.load_specific_exer_data_cali('bodyweight')
            elif self.ui.radioButton_weighted.isChecked():
                self.load_specific_exer_data_cali('weighted')
        else:
            self.load_specific_exer_data(self.exer_name)

    def load_frequency_dataplots(self, sorted_total):
        if not sorted_total: # sorted total is the total count of sessions conducted monthly per year
            # No data available
            self.series = QLineSeries()
            self.series.setName("No Data Yet")
            self.series.setColor(QColor('orange'))

            current_year = QDate.currentDate().year()
            placeholder_months = [6, 7, 8]
            for month in placeholder_months:
                self.series.append(QPointF(month, 0))

            display_months = placeholder_months
            title_year = str(current_year)
        else:
            # Extract year from first tuple
            title_year = sorted_total[0][0][0]
            display_months = [month for (year, month), _ in sorted_total]

            # Use QLineSeries or QScatterSeries depending on how many points there are
            self.series = QLineSeries() if len(display_months) > 1 else QScatterSeries()
            self.series.setName("Exercise Frequency")
            self.series.setColor(QColor('orange'))

            if isinstance(self.series, QScatterSeries):
                self.series.setBorderColor(QColor('orange'))

            for (year, month), progress_sum in sorted_total:
                self.series.append(QPointF(month, round(progress_sum, 2)))

        # Create chart
        self.chart = QChart()
        self.chart.addSeries(self.series)
        self.chart.setTitle(f"Monthly Frequency Summary ({title_year})")

        # X-axis setup (Month numbers)
        x_axis = QValueAxis()
        x_axis.setTitleText("Month")
        x_axis.setLabelFormat("%d")
        if display_months:
            if len(display_months) == 1:
                x_axis.setRange(display_months[0] - 1, display_months[0] + 1)
            else:
                x_axis.setRange(min(display_months), max(display_months))
        else:
            x_axis.setRange(1, 12)

        # Y-axis setup
        y_axis = QValueAxis()
        y_axis.setTitleText("Total Frequency")
        y_axis.setLabelFormat("%.1f")
        y_axis.setRange(0, 10 if not sorted_total else max(val for (_, val) in sorted_total) + 10)

        self.chart.addAxis(x_axis, Qt.AlignmentFlag.AlignBottom)
        self.series.attachAxis(x_axis)

        self.chart.addAxis(y_axis, Qt.AlignmentFlag.AlignLeft)
        self.series.attachAxis(y_axis)

        self.chart_view = QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Replace existing chart
        self.clear_layout(self.ui.verticalLayout_frequency_exercise)
        self.ui.verticalLayout_frequency_exercise.addWidget(self.chart_view)

    def update_frequency_dataplots(self, year):
        session_count = defaultdict(float)
        target_year = year

        for date, _ in self.specific_exer_data:
            if target_year == str(date.year):
                key = (date.year, date.month)
                session_count[key] += 1 # workout frequency I have done
        
        sorted_total = sorted(session_count.items())
        if not sorted_total: # sorted total is the total count of sessions conducted monthly per year
            # No data available
            self.series = QLineSeries()
            self.series.setName("No Data Yet")
            self.series.setColor(QColor('orange'))

            current_year = QDate.currentDate().year()
            placeholder_months = [6, 7, 8]
            for month in placeholder_months:
                self.series.append(QPointF(month, 0))

            display_months = placeholder_months
            title_year = str(current_year)
        else:
            # Extract year from first tuple
            title_year = sorted_total[0][0][0]
            display_months = [month for (year, month), _ in sorted_total]

            # Use QLineSeries or QScatterSeries depending on how many points there are
            self.series = QLineSeries() if len(display_months) > 1 else QScatterSeries()
            self.series.setName("Exercise Frequency")
            self.series.setColor(QColor('orange'))

            if isinstance(self.series, QScatterSeries):
                self.series.setBorderColor(QColor('orange'))

            for (year, month), progress_sum in sorted_total:
                self.series.append(QPointF(month, round(progress_sum, 2)))

        # Create chart
        self.chart = QChart()
        self.chart.addSeries(self.series)
        self.chart.setTitle(f"Monthly Frequency Summary ({title_year})")

        # X-axis setup (Month numbers)
        x_axis = QValueAxis()
        x_axis.setTitleText("Month")
        x_axis.setLabelFormat("%d")
        if display_months:
            if len(display_months) == 1:
                x_axis.setRange(display_months[0] - 1, display_months[0] + 1)
            else:
                x_axis.setRange(min(display_months), max(display_months))
        else:
            x_axis.setRange(1, 12)

        # Y-axis setup
        y_axis = QValueAxis()
        y_axis.setTitleText("Total Frequency")
        y_axis.setLabelFormat("%.1f")
        y_axis.setRange(0, 10 if not sorted_total else max(val for (_, val) in sorted_total) + 10)

        self.chart.addAxis(x_axis, Qt.AlignmentFlag.AlignBottom)
        self.series.attachAxis(x_axis)

        self.chart.addAxis(y_axis, Qt.AlignmentFlag.AlignLeft)
        self.series.attachAxis(y_axis)

        self.chart_view = QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Replace existing chart
        self.clear_layout(self.ui.verticalLayout_frequency_exercise)
        self.ui.verticalLayout_frequency_exercise.addWidget(self.chart_view)

# Opening of Windows

    def add_exercise(self):
        self.exercise_window = Add_exercise(self.mycursor, self.mydb)
        self.exercise_window.exec()

    def add_log(self):
        self.add_log_window = Add_logs(self.mycursor, self.mydb)
        self.add_log_window.window_closed.connect(self.load_logs)
        self.add_log_window.window_closed.connect(self.load_general_data_analysis)
        self.add_log_window.exec() 
        
    def open_user(self):
        self.user_window = UserWindow(self.mydb, self.mycursor)
        self.user_window.exec()

    def open_logs(self):
        try:
            exercise_item = self.ui.exercise_list.currentItem()
            log_item = self.ui.log_list.currentItem()

            if not exercise_item and not log_item:
                QMessageBox.warning(None, "No Selection", "Please select an exercise or a log to view details.")
                return
            else:
                actual_log_time = None

                if exercise_item:
                    exercise_name = exercise_item.text().strip()
                    if exercise_name == 'No match found':
                        QMessageBox.warning(None, "No match found", "Invalid log. Log not found")
                        return

                elif log_item:
                    selected_log = log_item.text().strip()
                    exercise_name, _ = selected_log.split('-', 1)
                    actual_log_time = self.actual_log_time
                    
                self.num_window_opened += 1
                if self.num_window_opened > 1:
                    return
                self.log_window = Exercise_Logs(self.mycursor, self.mydb, exercise_name, actual_log_time)
                
                self.log_window.show()
                self.num_window_opened = 0

        except Exception as err:
            QMessageBox.warning(None, "Error", f"Unexpected error occurred: {err}")
            return

    def update_exercise_list(self, exercise_names):
        self.resulted_data = exercise_names
        self.ui.exercise_list.clear() 

        if exercise_names:
            for exercise in exercise_names:
                item = QListWidgetItem(exercise["name"])
                item.setTextAlignment(Qt.AlignCenter)
                self.ui.exercise_list.addItem(item)
            return
        else:
            self.ui.exercise_list.addItem("No exercises found.")

    def load_exercise_list(self):
        self.ui.exercise_list.clear()
        self.load_thread = QThread()
        self.load_worker = ListWorker(self.mycursor)
        self.load_worker.moveToThread(self.load_thread)

        self.load_thread.started.connect(self.load_worker.run)
        self.load_worker.finished.connect(self.update_exercise_list)
        self.load_worker.finished.connect(self.load_thread.quit)
        self.load_worker.finished.connect(self.load_worker.deleteLater)
        self.load_thread.finished.connect(self.load_thread.deleteLater)

        self.load_worker.error.connect(self.errorDisplay)

        self.load_thread.start()

    def selected_exer_view(self):
        try:
            if self.ui.log_list.selectedItems():
                self.ui.exercise_list.clearSelection()
                self.ui.exercise_list.setCurrentItem(None)
                selected_log = self.ui.log_list.currentItem().text()                
                name, log_time = selected_log.split('-', 1)
                actual_date, actual_time = log_time.strip().split(' ')

                exer_name = name.strip().upper() # PARA SURE LANG

                query = """
                SELECT exercise_type, exercise_target FROM exercises
                WHERE specific_exercise_name = %s
                """
                self.mycursor.execute(query, (exer_name,))
                result_exer = self.mycursor.fetchone()

                if not result_exer:
                    QMessageBox.warning(None, "Error", "No exercise found for this log.")
                    return

                type_exer, target_exer = result_exer # Type at target duh

                stripped_log = log_time.strip()
                self.actual_log_time = self.find_timestamp_binary(exer_name, stripped_log)

                if not self.actual_log_time:
                    QMessageBox.warning(None, "Error", "No log time found for this log.")
                    return

                query_ulit = """
                    SELECT computed_MAX FROM exercise_logs
                    WHERE timestamp_logs = %s AND exercise_name = %s
                    """
                self.mycursor.execute(query_ulit, (self.actual_log_time, exer_name))
                max_effort = self.mycursor.fetchone()
                if not max_effort:
                    QMessageBox.warning(None, "Error", "No max effort found for this log.")
                    return

                text = (
                    f'EXERCISE: {exer_name}\n'
                    f'TYPE: {type_exer.upper()}\n'
                    f'TARGET: {target_exer.upper()}\n\n'
                    f'LOG DATE: {actual_date} - LOG TIME: {actual_time}\n\n'
                    f'MAX EFFORT RATING: {max_effort[0]}'
                )
                self.ui.info_log_plaintext.setPlainText(text)
           
        except mysql.connector.Error as err:
            self.errorDisplay(err.errno, err.sqlstate, err.msg)

    def find_timestamp_binary(self, name, formatted_time):
        key = (name, formatted_time)
        self.timestamps_logs.sort(key=lambda x: (x['name'], x['formatted'])) #sort first to make it easier
        # Define a custom key list just for binary search
        keys_list = [(entry['name'], entry['formatted']) for entry in self.timestamps_logs]

        index = bisect.bisect_left(keys_list, key)

        if index < len(self.timestamps_logs):
            entry = self.timestamps_logs[index]
            if entry['name'] == name and entry['formatted'] == formatted_time:
                return entry['timestamp']

        return None  # Not found
        
    def log_exer_view(self):
        try:
            if self.ui.exercise_list.selectedItems():
                self.ui.log_list.clearSelection()
                self.ui.log_list.setCurrentItem(None)
                exer_name = self.ui.exercise_list.currentItem().text().strip().upper()

                query = """
                SELECT exercise_type, exercise_target FROM exercises
                WHERE specific_exercise_name = %s
                """
                self.mycursor.execute(query, (exer_name,))
                result_exer = self.mycursor.fetchone()

                if not result_exer:
                    QMessageBox.warning(None, "Error", "No exercise found for this log.")
                    return

                type_exer, target_exer = result_exer # Type at target that was copy pasted lol

                text = (
                        f'EXERCISE: {exer_name}\n'
                        f'TYPE: {type_exer.upper()}\n'
                        f'TARGET: {target_exer.upper()}\n\n'
                    )
                self.ui.info_log_plaintext.setPlainText(text)  

        except mysql.connector.Error as err:
            self.errorDisplay(err.errno, err.sqlstate, err.msg) 

# FOR DELETING LOGS BASED FROM WHAT IS GIVEN

    def del_logs(self):
        try:
            selected_log = self.ui.log_list.currentItem()
            selected_exer_logs = self.ui.exercise_list.currentItem()

            if selected_log: # TODO: workout on how would you extract the data from here to make it appropriate in SQL
                msg = "Are you sure you want to delete this log?"
                selected_log_text = selected_log.text()
                selected_name, log_time = selected_log_text.split('-', 1)
                self.selected_name = selected_name.strip().upper()
                stripped_log = log_time.strip()
                self.actual_log_time = self.find_timestamp_binary(self.selected_name, stripped_log)
                print(log_time, self.actual_log_time)
                              
            elif selected_exer_logs:
                msg = "Are you sure you want to delete all logs to this exercise?"
                self.selected_name = selected_exer_logs.text().strip().upper()  
                self.actual_log_time = None 
            else:
                QMessageBox.warning(None, 'Nothing Selected', "Please select a log or logs of exercise to delete")
                return
            
            confirm = QMessageBox.question(
                    None, "Confirm Deletion",
                    msg, # delete message for what is specifically selected
                    QMessageBox.Yes | QMessageBox.No
                )
            if confirm != QMessageBox.Yes:
                return
            
            self.mycursor.execute("SELECT COUNT(*) FROM exercise_logs WHERE exercise_name = %s", (self.selected_name,))
            count_res = self.mycursor.fetchone() # See if it is None
            if not count_res:
                QMessageBox.warning(None, "Error", "No logs to delete.")
                return
            
            self.update_computed_data(self.selected_name, self.actual_log_time) # hopefully it works
            
        except mysql.connector.Error as err:
            self.errorDisplay(err.errno, err.sqlstate, err.msg)
            return
        
    def err_data_update_del(self, msg):
        QMessageBox.warning(None, "Error", f"Unexpected error occurred in updating data: {msg}")
        self.thread_update_compute.quit
        self.worker_update_compute.deleteLater
        self.thread_update_compute.deleteLater
        return
        
    def delete_log(self):
        try:
            if self.actual_log_time:
                exer_query = """
                        DELETE FROM exercise_logs WHERE exercise_name = %s AND timestamp_logs  = %s
                        """
                self.mycursor.execute(exer_query, (self.selected_name, self.actual_log_time))
                self.mydb.commit()
            else:
                exer_query = """
                        DELETE FROM exercise_logs WHERE exercise_name = %s
                        """
                self.mycursor.execute(exer_query, (self.selected_name,))
                self.mydb.commit()

            self.load_logs()
            self.load_general_data_analysis()

            QMessageBox.information(None, 'Success', "Logs related to the exercise is successfully deleted!")
            return
                  
        except mysql.connector.Error as err:
            self.errorDisplay(err.errno, err.sqlstate, err.msg)
            return
        except Exception as err:
            QMessageBox.warning(None, 'Error', f'An unexpected error occurred {err}')
            return

    def update_computed_data(self, exer_name, timestamp=None):
        try: # TODO: finish the stuff still needed to be added here
            info = self.sql_helper()

            self.thread_update_compute = QThread()
            self.worker_update_compute = UpdateComputationDeletion(info, exer_name, timestamp)
            self.worker_update_compute.moveToThread(self.thread_update_compute)

            self.thread_update_compute.started.connect(self.worker_update_compute.run)
            self.worker_update_compute.finished.connect(self.delete_log)
            self.worker_update_compute.finished.connect(self.thread_update_compute.quit)
            self.worker_update_compute.finished.connect(self.worker_update_compute.deleteLater)
            self.thread_update_compute.finished.connect(self.thread_update_compute.deleteLater)

            self.worker_update_compute.err_sql.connect(self.errorDisplay)
            self.worker_update_compute.error.connect(self.err_data_update_del)

            self.thread_update_compute.start()

        except Exception as err:
            QMessageBox.warning(None, 'Error', f'An unexpected error occurred {err}')
            return


class UpdateComputationDeletion(QObject):
    finished = Signal()
    error = Signal(str)
    err_sql = Signal(str, str, str)

    def __init__(self, info, exer_name, timestamp): # if timestamp is none then it will do massive deduction in computed max rm
        super().__init__()
        self.exer_name = exer_name
        self.sql_info = info
        self.mydb = mysql.connector.connect(**self.sql_info)
        self.mycursor = self.mydb.cursor(buffered=True)
        self.timestamp = timestamp # can be none
        self.logs = {}

    def run(self):
        try:
            if self.timestamp: # if timestamp is none, code of computation is here
                print(self.timestamp, type(self.timestamp))
                query = """
                    SELECT date, computed_MAX FROM exercise_logs WHERE exercise_name = %s AND timestamp_logs = %s 
                    """
                self.mycursor.execute(query, (self.exer_name, self.timestamp))
                result_log = self.mycursor.fetchone()

                if not result_log:
                    self.error.emit('Unable to find the specific log. Please try again')
                    return
                
                self.deduct_log(result_log)
            else:   
                # continuation of code here. Finds first the all of the related logs to deduct in the code
                self.mycursor.execute("SELECT date, computed_MAX FROM exercise_logs WHERE exercise_name = %s", (self.exer_name,))
                logs = self.mycursor.fetchall()

                if not logs:
                    self.error.emit("No logs to delete from the exercise")
                    return
                self.deduct_all_from_exer(logs)

        except mysql.connector.Error as err:
            self.mydb.rollback()
            self.err_sql.emit(err.errno, err.sqlstate, err.msg)
            return

        except Exception as err:
            self.mydb.rollback()
            self.error.emit(str(err))
            return
        
    def deduct_log(self, find_log):
        try:
            date = find_log[0] # unpack the values
            max_rm = find_log[1]

            start_of_week = date - timedelta(days=date.weekday())
            end_of_week = start_of_week + timedelta(days=6)

            # For yearly and monthly computation
            year = date.year
            month_num = date.month
            
            weekly_query = """
                UPDATE weekly_progress SET weekly_computation = weekly_computation - %s 
                WHERE date BETWEEN %s AND %s
                """
            self.mycursor.execute(weekly_query, (max_rm, start_of_week, end_of_week))
            self.mydb.commit()

            monthly_query = """ 
                UPDATE monthly_progress SET monthly_computation = monthly_computation - %s
                WHERE MONTH(date) = %s AND specific_year = %s           
                """
            self.mycursor.execute(monthly_query, (max_rm, month_num, year))
            self.mydb.commit()

            yearly_query = """
                UPDATE yearly_progress SET yearly_computation = yearly_computation - %s
                WHERE specific_year = %s
                """
            self.mycursor.execute(yearly_query, (max_rm, year))
            self.mydb.commit()
            self.check_if_zero()
        
        except mysql.connector.Error as err:
            self.mydb.rollback()
            self.err_sql.emit(err.errno, err.sqlstate, err.msg)
            return

        except Exception as err:
            self.mydb.rollback()
            self.error.emit(str(err))
            return

    def deduct_all_from_exer(self, logs):
        try:
            weekly_query = """
                UPDATE weekly_progress 
                SET weekly_computation = weekly_computation - %s
                WHERE date BETWEEN %s AND %s
            """
            
            monthly_query = """
                UPDATE monthly_progress 
                SET monthly_computation = monthly_computation - %s
                WHERE MONTH(date) = %s AND specific_year = %s
            """
        
            yearly_query = """
                UPDATE yearly_progress 
                SET yearly_computation = yearly_computation - %s
                WHERE specific_year = %s
            """

            for date, max_rm in logs: # para maayos lol
                # Range to be used for computations
                start_of_week = date - timedelta(days=date.weekday())
                end_of_week = start_of_week + timedelta(days=6)

                # For yearly and monthly computation
                year = date.year
                month_num = date.month     

                            # Update weekly
                self.mycursor.execute(weekly_query, (max_rm, start_of_week, end_of_week))

                # Update monthly
                self.mycursor.execute(monthly_query, (max_rm, month_num, year))

                # Update yearly
                self.mycursor.execute(yearly_query, (max_rm, year))

                self.mydb.commit()
            self.check_if_zero()

        except mysql.connector.Error as err:
            self.mydb.rollback()
            self.err_sql.emit(err.errno, err.sqlstate, err.msg)
            return

        except Exception as err:
            self.mydb.rollback()
            self.error.emit(str(err))

    def check_if_zero(self):
        try:
            # checks if values are zero, then it will be officially deleted
            weekly_query = """
                DELETE FROM weekly_progress 
                WHERE weekly_computation <= 1
            """
            
            monthly_query = """
                DELETE FROM monthly_progress 
                WHERE monthly_computation <= 1
            """
        
            yearly_query = """
                DELETE FROM yearly_progress
                WHERE yearly_computation <= 1
            """

            # Update weekly
            self.mycursor.execute(weekly_query)

            # Update monthly
            self.mycursor.execute(monthly_query)

            # Update yearly
            self.mycursor.execute(yearly_query)

            self.mydb.commit()
            self.finished.emit()
            return

        except mysql.connector.Error as err:
            self.mydb.rollback()
            self.err_sql.emit(err.errno, err.sqlstate, err.msg)
            return

        except Exception as err:
            self.mydb.rollback()
            self.error.emit(str(err))


class Retrieve_Data_Exer(QObject):
    finished = Signal(list)
    err_sql = Signal(str, str, str)
    error = Signal(str)

    def __init__(self, exer_name, sql_info):
        super().__init__()
        self.exer_name = exer_name
        self.sql_info = sql_info
        self.mydb = mysql.connector.connect(**self.sql_info)
        self.mycursor = self.mydb.cursor(buffered=True)

    def run_bodyweight(self):
        try:
            # just gets the bodyweight version of the calisthenic exercise
            load_query = """
                SELECT el.date, el.computed_MAX
                FROM exercise_logs as el
                JOIN reps_and_weights as rw ON el.id_gym_logs = rw.related_exercise_log
                WHERE el.exercise_name = %s AND rw.weights = 'Bodyweight'
                """
            self.mycursor.execute(load_query, (self.exer_name,))
            data_result = self.mycursor.fetchall()
            self.finished.emit(data_result)
            self.mydb.commit()

        except mysql.connector.Error as err:
            self.mydb.rollback()
            self.err_sql.emit(err.errno, err.sqlstate, err.msg)
            return
        
        except Exception as err:
            self.mydb.rollback()
            self.error.emit(str(err))
            return

    def run_weighted(self):
        try:
            # just gets the weighted version of the calisthenic exercise
            load_query = """
                SELECT el.date, el.computed_MAX
                FROM exercise_logs as el
                JOIN reps_and_weights as rw ON el.id_gym_logs = rw.related_exercise_log
                WHERE el.exercise_name = %s AND rw.weights != 'Bodyweight'
                """
            self.mycursor.execute(load_query, (self.exer_name,))
            data_result = self.mycursor.fetchall()
            self.finished.emit(data_result)
            self.mydb.commit()

        except mysql.connector.Error as err:
            self.mydb.rollback()
            self.err_sql.emit(err.errno, err.sqlstate, err.msg)
            return
        
        except Exception as err:
            self.mydb.rollback()
            self.error.emit(str(err))
            return

    def run_freeweight(self):
        try:
            # just gets the free weight exercises
            load_query = """
                SELECT el.date, el.computed_MAX
                FROM exercise_logs as el
                JOIN reps_and_weights as rw ON el.id_gym_logs = rw.related_exercise_log
                WHERE el.exercise_name = %s 
                """
            self.mycursor.execute(load_query, (self.exer_name,))
            data_result = self.mycursor.fetchall()
            self.finished.emit(data_result)
            self.mydb.commit()

        except mysql.connector.Error as err:
            self.mydb.rollback()
            self.err_sql.emit(err.errno, err.sqlstate, err.msg)
            return
        
        except Exception as err:
            self.mydb.rollback()
            self.error.emit(str(err))
            return


class General_Analysis(QObject):
    finished = Signal(list, list)
    err_sql = Signal(str, str, str)
    error = Signal(str)

    def __init__(self):
        super().__init__()
        self.mydb = mysql.connector.connect(
                host="localhost",
                user="Group_F",
                password="CPET-8L-TUPCROOM",
                database="gym_tracker",
                ssl_disabled=True,  # This should fix it
                autocommit=False
            )
        self.mycursor = self.mydb.cursor(buffered=True) 
    
    def run(self):
        try:
            self.mycursor.execute('SELECT date, month_num, monthly_computation, specific_year FROM monthly_progress')
            general_monthly_data = self.mycursor.fetchall() or []

            self.mycursor.execute('SELECT date, yearly_computation, specific_year FROM yearly_progress')
            general_yearly_data = self.mycursor.fetchall() or []

            self.mydb.commit()
            self.mycursor.close()
            self.mydb.close()
            self.finished.emit(general_monthly_data, general_yearly_data)

        except mysql.connector.Error as err:
            self.mydb.rollback()
            self.err_sql.emit(err.errno, err.sqlstate, err.msg)
            return
        except Exception as err:
            self.mydb.rollback()
            self.error.emit(str(err))
            return    


class Add_logs(QDialog):
    window_closed = Signal()

    def __init__(self, db_cursor, db_connection):
        super().__init__()
        self.ui = add_logs()
        self.ui.setupUi(self)
        self.mycursor = db_cursor
        self.mydb = db_connection

        self.ui.tableWidget.setWordWrap(True)
        self.ui.tableWidget.resizeColumnsToContents()
        self.ui.tableWidget.resizeRowsToContents()
        self.ui.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.ui.exercise_list.itemClicked.connect(self.exercise_determiner)
        # For determining exercise type
        self.exercise_type = None

        self.ui.dateEdit.setMinimumDate(QDate(2000, 1, 1))
        self.ui.dateEdit.setMaximumDate(QDate.currentDate())
        self.ui.dateEdit.setDate(QDate.currentDate())
        self.ui.dateEdit.setCalendarPopup(True)

        self.ui.radioButton_bodyweight.toggled.connect(lambda: self.calisthenic_type('bodyweight'))
        self.ui.radioButton_weighted.toggled.connect(lambda: self.calisthenic_type('weighted'))

        self.ui.radioButton_weighted.setDisabled(True)
        self.ui.radioButton_bodyweight.setDisabled(True)

        self.ui.tableWidget.itemChanged.connect(self.validate_column_2_input)
        self.ui.tableWidget.itemChanged.connect(self.center_edited_item)
        self.ui.tableWidget.itemChanged.connect(self.check_int_col_one)

        self._updating_table = False
        self.load_exercise_list()
        self.current_mode = None
        self.resulted_data = None
        self.saved_log_reps_weight = [] # will be used in saving data

        self.ui.filter_exercise.currentIndexChanged.connect(lambda: self.filter_exercises_by_type(self.ui.filter_exercise.currentText()))
        self.ui.clear_log.clicked.connect(self.clear_logs)
        self.ui.searchlog_lineEdit.textChanged.connect(self.searching)
        self.ui.save_log.clicked.connect(self.save_log)

    def closeEvent(self, event):
        self.window_closed.emit()
        event.accept()

    def check_int_col_one(self, item):
        if not item or item.column() != 0:
            return  # Exit early if not column 2
        text = item.text().strip()
        if not re.fullmatch(r'\d+(\.\d+)?', text):
            item.setText('')
            return

    def save_log(self):      
        try:
            self.type = None # gamit para macheck if free weight or calisthenic
            self.timestamp = datetime.now(timezone.utc) # timestamp of the log for recent logs

            if not self.ui.exercise_list.currentItem():
                QMessageBox.warning(None, "No Selected", "Please select an exercise to view its logs")
                return
            if not self.ui.tableWidget.item(0, 0):
                QMessageBox.warning(None, "No Data", "Please enter the number of reps done")
                return
            if not self.ui.tableWidget.item(0, 1):
                QMessageBox.warning(None, "No Data", "Please enter the number of weight done")
                return
            
            exercise_name = self.ui.exercise_list.currentItem().text().strip()

            for indexes in self.resulted_data: # check if data is calisthenic or free weight
                if indexes["name"] == exercise_name:
                    self.type = indexes["type"]
                    break

            # Just for this purpose
            if self.type == 'calisthenic': 
                if not self.ui.radioButton_bodyweight.isChecked() or not self.ui.radioButton_weighted.isChecked():
                    QMessageBox.warning(None, "No Checked", "Please check if the exercise if" \
                    "bodyweight or weighted in calisthenic exercises")
                    return

            log_date = self.ui.dateEdit.dateTime().toString("yyyy-MM-dd")

            for sets in range(self.ui.tableWidget.rowCount()):
                if not self.ui.tableWidget.item(sets, 0):
                    break
                if not self.ui.tableWidget.item(sets, 1):
                    break
                reps = int(self.ui.tableWidget.item(sets, 0).text().strip())
                weight = self.ui.tableWidget.item(sets, 1).text().strip()
                self.saved_log_reps_weight.append(
                    {"set": sets,
                     "reps": reps,
                     "weight": weight,
                    }
                )

            last_set = self.saved_log_reps_weight[-1:] # get the max set
            num_sets = last_set[0]['set']
 
            self.load_thread = QThread()
            self.load_worker = SaveLogWorker(self.mycursor, self.mydb, log_date, num_sets, 
                                             self.saved_log_reps_weight, exercise_name, self.timestamp)
            self.load_worker.moveToThread(self.load_thread)

            self.load_thread.started.connect(self.load_worker.run)
            self.load_worker.finished.connect(self.save_complete)
            self.load_worker.finished.connect(self.load_thread.quit)
            self.load_worker.finished.connect(self.load_worker.deleteLater)
            self.load_thread.finished.connect(self.load_thread.deleteLater)

            self.load_worker.error.connect(self.error_saving)
            self.load_thread.start()

        except Exception as err:
            QMessageBox.warning(None, "Error", f"Unexpected error was encountered: {err}")
            self.clear_logs()
            return

    def error_saving(self, error_msg):
        QMessageBox.warning(None, "Error in Saving", f"Unexpected error was encountered: {error_msg}")
        self.load_thread.quit()
        self.load_worker.deleteLater()
        self.load_thread.deleteLater()
        self.clear_logs()
    
    def save_complete(self):
        QMessageBox.information(None, "Save Complete", "Log successfully saved!")
        self.clear_logs()
        self.computation_progress() # checks computation weekly first

    def computation_progress(self):

        log_date = self.ui.dateEdit.dateTime().toString("yyyy-MM-dd") # ito dapat
        today = datetime.strptime(log_date, "%Y-%m-%d")
        
        # Range to be used for computations
        start_of_week = today - timedelta(days=today.weekday())
        end_of_week = start_of_week + timedelta(days=6)

        # For yearly and monthly computation
        year = today.year
        specific_month = f"{year}-{today.month:02d}"
        month_num = today.month

        self.loadthread= QThread()
        self.computation_worker = ProgressUpdate(self.mydb, self.mycursor, today, start_of_week, 
                                                 end_of_week, year, month_num, specific_month)
        self.computation_worker.moveToThread(self.loadthread)

        self.loadthread.started.connect(self.computation_worker.run)
        self.computation_worker.finished.connect(self.finished_reset_date)
        self.computation_worker.finished.connect(self.loadthread.quit)
        self.computation_worker.finished.connect(self.computation_worker.deleteLater)
        self.loadthread.finished.connect(self.loadthread.deleteLater)

        self.computation_worker.error.connect(self.error)
        self.computation_worker.sql_error.connect(self.errorDisplay)
        self.loadthread.start()

    def finished_reset_date(self):
        self.ui.dateEdit.setDate(QDate.currentDate()) # to avoid issues with date in updating progress

    def error(self, msg):
        QMessageBox.warning(None, "Error in Computation", f"Unexpected error was encountered: {msg}")
        self.loadthread.quit()
        self.computation_worker.deleteLater()
        self.loadthread.deleteLater()

    def center_edited_item(self, item):
        if item:
            self.ui.tableWidget.blockSignals(True)
            item.setTextAlignment(Qt.AlignCenter)
            self.ui.tableWidget.blockSignals(False)

    def clear_logs(self):
        self.load_exercise_list()
        self.setdisabler_radiobutton()
        self.ui.tableWidget.clearContents()
        self.saved_log_reps_weight.clear()

    def searching(self):
        search = self.ui.searchlog_lineEdit.text().strip().upper()
        self.ui.exercise_list.clear()

        if not search:
            # Show all if search is empty
            for exercise in self.resulted_data:
                item = QListWidgetItem(exercise["name"])
                item.setTextAlignment(Qt.AlignCenter)
                self.ui.exercise_list.addItem(item)
            return

        results = []
        for exercise in self.resulted_data:
            if search in exercise["name"].upper():
                results.append(exercise["name"])

        if results:
            for name in results:
                item = QListWidgetItem(name)
                item.setTextAlignment(Qt.AlignCenter)
                self.ui.exercise_list.addItem(item)
        else:
            item = QListWidgetItem("No match found.")
            item.setTextAlignment(Qt.AlignCenter)
            self.ui.exercise_list.addItem(item)

    def calisthenic_type(self, exer_type):
        if self.exercise_type == 'calisthenic': 
            self.current_mode = exer_type
            try:
                for row in range(self.ui.tableWidget.rowCount()):
                    item = self.ui.tableWidget.item(row, 1)
                    if not item:
                        item = QTableWidgetItem("")
                        self.ui.tableWidget.setItem(row, 1, item)

                    if exer_type == 'bodyweight':
                        item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                        item.setText('Bodyweight')  # optional: auto-reset
                    else:
                        item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable)
                        item.setText('')  # Clear any "Bodyweight" text

            except Exception as err:
                QMessageBox.warning(None, "Error", "An error occurred, please try again.")
                return

    def validate_column_2_input(self, item):
        if self._updating_table:
            return
        
        if not item or item.column() != 1:
            return  # Exit early if not column 2

        text = item.text().strip()  # <-- text is only defined *after* the column check

        try:
            self._updating_table = True

            if self.exercise_type == 'calisthenic':
                if self.current_mode == "bodyweight":
                    if any(char.isdigit() for char in text) or '.' in text:
                        item.setText('Bodyweight')
                elif self.current_mode == "weighted":
                    if not re.fullmatch(r'\d+(\.\d+)?', text):
                        item.setText('')
            else:
                if not re.fullmatch(r'\d+(\.\d+)?', text):
                    item.setText('')
        finally:
            self._updating_table = False

    def exercise_determiner(self, selected_exercise_name: QListWidgetItem):
        try:
            exercise_name = selected_exercise_name.text()
            self.mycursor.execute("SELECT exercise_type FROM exercises WHERE specific_exercise_name = %s", (exercise_name,))
            self.exercise_type = self.mycursor.fetchone()[0]
            if not self.exercise_type:
                QMessageBox.warning(None, "Error", "Exercise selected is not recorded in the database")
                return
            if self.exercise_type == "free weights":
                self.setdisabler_radiobutton()
                return
            else:
                self.setabler_radiobutton()
                return
        
        except mysql.connector.Error as err:
            self.errorDisplay(err.errno, err.sqlstate, err.msg)

    def filter_exercises_by_type(self, selected_type):
        self.ui.exercise_list.clear()   
        for ex in self.resulted_data:
            if ex["type"] == selected_type:
                item = QListWidgetItem(ex["name"])
                item.setTextAlignment(Qt.AlignCenter)
                self.ui.exercise_list.addItem(item)
            elif ex["target"] == selected_type:
                item = QListWidgetItem(ex["name"])
                item.setTextAlignment(Qt.AlignCenter)
                self.ui.exercise_list.addItem(item)

    def update_exercise_list(self, exercise_names):
        self.resulted_data = exercise_names
        self.ui.exercise_list.clear() 

        if exercise_names:
            for exercise in exercise_names:
                item = QListWidgetItem(exercise["name"])
                item.setTextAlignment(Qt.AlignCenter)
                self.ui.exercise_list.addItem(item)
            return
        else:
            self.ui.exercise_list.addItem("No exercises found.")

    def load_exercise_list(self):
        self.ui.exercise_list.clear()
        self.load_thread = QThread()
        self.load_worker = ListWorker(self.mycursor)
        self.load_worker.moveToThread(self.load_thread)

        self.load_thread.started.connect(self.load_worker.run)
        self.load_worker.finished.connect(self.update_exercise_list)
        self.load_worker.finished.connect(self.load_thread.quit)
        self.load_worker.finished.connect(self.load_worker.deleteLater)
        self.load_thread.finished.connect(self.load_thread.deleteLater)

        self.load_worker.error.connect(self.errorDisplay)

        self.load_thread.start()

    def setdisabler_radiobutton(self):
        self.ui.radioButton_weighted.setDisabled(True)
        self.ui.radioButton_bodyweight.setDisabled(True)
        currently_checked_button = None
        if self.ui.radioButton_bodyweight.isChecked():
            currently_checked_button = self.ui.radioButton_bodyweight
        elif self.ui.radioButton_weighted.isChecked():
            currently_checked_button = self.ui.radioButton_weighted
        # ... add more if you have more radio buttons in the same implicit group

        if currently_checked_button:
            # Temporarily disable autoExclusive for the *current* button
            # This allows it to be unchecked without another one taking its place.
            currently_checked_button.setAutoExclusive(False)
            currently_checked_button.setChecked(False)
            currently_checked_button.setAutoExclusive(True) # Re-enable for future use
        return

    def setabler_radiobutton(self):
        self.ui.radioButton_weighted.setDisabled(False)
        self.ui.radioButton_bodyweight.setDisabled(False)
        return

    def errorDisplay(self, errno, sqlstate, msg):
        """Displays detailed error information to the user."""
        self.mydb.rollback()
        # Construct the error message
        error_message = f"Error Code: {errno}\nSQLSTATE: {sqlstate}\nMessage: {msg}"

        # Create and show a critical error message box with the detailed error
        QMessageBox.critical(None, "Database Error", error_message)


class Add_exercise(QDialog):
    def __init__(self, cursor, db_connection):
        super().__init__()
        self.ui = add_exercise()
        self.ui.setupUi(self)
        self.mycursor = cursor
        self.mydb = db_connection
        self.exercise_names = None

        self.load_exercise_list()

         # Create a Regular Expression for letters only
        reg_exp = QRegularExpression(r"[a-zA-Z\s]+")  # Only a-z and A-Z

        # Create a validator with the regular expression
        validator = QRegularExpressionValidator(reg_exp)

        self.ui.name_exercise.setValidator(validator)

        self.exercise_type = None
        self.exercise_target = None

        self.old_exercise_name = None # for updating

        self.ui.Add_exercise.clicked.connect(self.save_exercise)
        self.ui.clear_fill.clicked.connect(self.clear_stuff)
        self.ui.De_Exer.clicked.connect(self.del_exer)
        self.ui.Edit_exer.clicked.connect(self.edit_exer)
        self.ui.Edit_exer.setDisabled(True)
        self.ui.exercise_list.itemClicked.connect(self.fill_stuff)

        self.ui.searchlog_lineEdit.textChanged.connect(self.searching)
        self.ui.filter_exercise.currentIndexChanged.connect(lambda: self.filter_exercises_by_type(self.ui.filter_exercise.currentText()))

        self.selected_radiobuttons = []

    def searching(self):
        search = self.ui.searchlog_lineEdit.text().strip().upper()
        self.ui.exercise_list.clear()

        if not search:
            # Show all if search is empty
            for exercise in self.exercise_names:
                item = QListWidgetItem(exercise["name"])
                item.setTextAlignment(Qt.AlignCenter)
                self.ui.exercise_list.addItem(item)
            return

        results = []
        for exercise in self.exercise_names:
            if search in exercise["name"].upper():
                results.append(exercise["name"])

        if results:
            for name in results:
                item = QListWidgetItem(name)
                item.setTextAlignment(Qt.AlignCenter)
                self.ui.exercise_list.addItem(item)
        else:
            item = QListWidgetItem("No match found.")
            item.setTextAlignment(Qt.AlignCenter)
            self.ui.exercise_list.addItem(item)

    def filter_exercises_by_type(self, selected_type):
        self.ui.exercise_list.clear()   
        for ex in self.exercise_names:
            if ex["type"] == selected_type:
                item = QListWidgetItem(ex["name"])
                item.setTextAlignment(Qt.AlignCenter)
                self.ui.exercise_list.addItem(item)
            elif ex["target"] == selected_type:
                item = QListWidgetItem(ex["name"])
                item.setTextAlignment(Qt.AlignCenter)
                self.ui.exercise_list.addItem(item)

    def save_exercise(self):
        exercise_name = self.ui.name_exercise.text().strip().upper()

        if self.ui.Calisthenic.isChecked():
            self.exercise_type = "calisthenic"
        elif self.ui.Free_weight.isChecked():
            self.exercise_type = "free weights"
        else:
            QMessageBox.warning(None, "No selected", "Please select the exercise type.")
            return

        if self.ui.upper.isChecked():
            self.exercise_target = "upper"
        elif self.ui.lower.isChecked():
            self.exercise_target = "lower"
        else:
            QMessageBox.warning(None, "No selected", "Please select the exercise target.")
            return
        
        if not exercise_name:
            QMessageBox.warning(None, "No exercise", "Please enter an appropriate exercise to add in the system.")
            return

        try:
            # check if name already existing
            self.mycursor.execute("SELECT COUNT(*) FROM exercises WHERE specific_exercise_name = %s", (exercise_name,))
            result = self.mycursor.fetchone()[0] 
            if result > 0:
                QMessageBox.warning(None, "Exercise already exists", "This exercise already exists in the system.")
                return

            self.mycursor.execute("INSERT INTO exercises (specific_exercise_name, exercise_type, exercise_target) VALUES(%s, %s, %s)", 
                                  (exercise_name, self.exercise_type, self.exercise_target))
            self.mydb.commit()
            QMessageBox.information(None, "Exercise added", "Exercise added successfully.")

            self.ui.name_exercise.clear()
            
            if self.ui.upper.isChecked():
                self.selected_radiobuttons.append(self.ui.upper)
            elif self.ui.lower.isChecked():
                self.selected_radiobuttons.append(self.ui.lower)
            # ... add more if you have more radio buttons in the same implicit group

            if self.ui.Calisthenic.isChecked():
                self.selected_radiobuttons.append(self.ui.Calisthenic)
            elif self.ui.Free_weight.isChecked():
                self.selected_radiobuttons.append(self.ui.Free_weight)
            # ... add more if you have more radio buttons in the same implicit group

            for currently_checked_button in self.selected_radiobuttons:
                # Temporarily disable autoExclusive for the *current* button
                # This allows it to be unchecked without another one taking its place.
                currently_checked_button.setAutoExclusive(False)
                currently_checked_button.setChecked(False)
                currently_checked_button.setAutoExclusive(True)
            self.selected_radiobuttons.clear()
            self.load_exercise_list()

            return
        
        except mysql.connector.Error as err:
            self.errorDisplay(err.errno, err.sqlstate, err.msg) 
    
    def load_exercise_list(self):
            self.ui.exercise_list.clear()
            self.load_thread = QThread()
            self.load_worker = ListWorker(self.mycursor)
            self.load_worker.moveToThread(self.load_thread)

            self.load_thread.started.connect(self.load_worker.run)
            self.load_worker.finished.connect(self.load_exercises)
            self.load_worker.finished.connect(self.load_thread.quit)
            self.load_worker.finished.connect(self.load_worker.deleteLater)
            self.load_thread.finished.connect(self.load_thread.deleteLater)

            self.load_worker.error.connect(self.errorDisplay)

            self.load_thread.start()

    def load_exercises(self, exercises):
        self.exercise_names = exercises
        self.ui.exercise_list.clear()
        if self.exercise_names:
            for exercises in self.exercise_names:
                item = QListWidgetItem(exercises["name"])
                item.setTextAlignment(Qt.AlignCenter)
                self.ui.exercise_list.addItem(item)
            return
        else:
            self.ui.exercise_list.addItem("No exercises found.")

    def clear_stuff(self):
        self.disabler_btn_adding()
        self.exercise_type = None
        self.exercise_target = None
        self.old_exercise_name = None # for updating
        self.load_exercise_list()
        self.ui.name_exercise.clear()

        if self.ui.upper.isChecked():
            self.selected_radiobuttons.append(self.ui.upper)
        elif self.ui.lower.isChecked():
            self.selected_radiobuttons.append(self.ui.lower)
        # ... add more if you have more radio buttons in the same implicit group

        if self.ui.Calisthenic.isChecked():
            self.selected_radiobuttons.append(self.ui.Calisthenic)
        elif self.ui.Free_weight.isChecked():
            self.selected_radiobuttons.append(self.ui.Free_weight)
        # ... add more if you have more radio buttons in the same implicit group

        for currently_checked_button in self.selected_radiobuttons:
            # Temporarily disable autoExclusive for the *current* button
            # This allows it to be unchecked without another one taking its place.
            currently_checked_button.setAutoExclusive(False)
            currently_checked_button.setChecked(False)
            currently_checked_button.setAutoExclusive(True)
        self.selected_radiobuttons.clear()

    def fill_stuff(self, selected_exercise_name: QListWidgetItem):
        try:
            self.disabler_btn_editing() # for editing purposes
            exercise_name = selected_exercise_name.text()
            self.old_exercise_name = exercise_name # to be used later for updating
            self.mycursor.execute("SELECT exercise_type, exercise_target FROM exercises WHERE specific_exercise_name = %s", (exercise_name,))
            self.exercise_selected = self.mycursor.fetchone()
            if not self.exercise_selected:
                QMessageBox.warning(None, "Error", "Exercise selected is not recorded in the database")
                return
            
            self.ui.name_exercise.setText(exercise_name)

            if self.exercise_selected[0] == 'free weights':
                self.ui.Free_weight.setChecked(True)
            else:
                self.ui.Calisthenic.setChecked(True)

            if self.exercise_selected[1] == 'upper':
                self.ui.upper.setChecked(True)
            else:
                self.ui.lower.setChecked(True)

            if self.ui.upper.isChecked():
                self.exercise_target = "upper"
            elif self.ui.lower.isChecked():
                self.exercise_target = "lower"

            if self.ui.Calisthenic.isChecked():
                self.exercise_type = "calisthenic"
            elif self.ui.Free_weight.isChecked():
                self.exercise_type = "free weights"

        except mysql.connector.Error as err:
            self.errorDisplay(err.errno, err.sqlstate, err.msg)

    def edit_exer(self):
        confirm = QMessageBox.question(
                    None, "Confirm Deletion",
                    "Are you sure you want to change this exercise?",
                    QMessageBox.Yes | QMessageBox.No
                )
        if confirm != QMessageBox.Yes:
            return

        exercise_name = self.ui.name_exercise.text().strip().upper()

        if not exercise_name:
            QMessageBox.warning(None, "No exercise", "Please enter an appropriate exercise name.")
            return

        try:
            if self.ui.upper.isChecked():
                self.exercise_target = "upper"
            else:
                self.exercise_target = "lower"

            if self.ui.Calisthenic.isChecked():
                self.exercise_type = "calisthenic"
            else:
                self.exercise_type = "free weights"

            self.mycursor.execute("""UPDATE exercises SET specific_exercise_name = %s,
                                    exercise_target = %s,
                                    exercise_type = %s
                                WHERE specific_exercise_name = %s    
                                  """, (exercise_name, self.exercise_target, self.exercise_type, self.old_exercise_name))
            self.mydb.commit()
            QMessageBox.information(None, 'Success', 'Exercise successfully changed!')

        except mysql.connector.Error as err:
            self.errorDisplay(err.errno, err.sqlstate, err.msg)
        finally:
            self.clear_stuff()

    def del_exer(self):
        confirm = QMessageBox.question(
                    None, "Confirm Deletion",
                    "Are you sure you want to delete this exercise?",
                    QMessageBox.Yes | QMessageBox.No
                )
        if confirm != QMessageBox.Yes:
            return
        
        exercise_name = self.ui.name_exercise.text().strip().upper()

        if not exercise_name:
            QMessageBox.warning(None, "No exercise", "Please enter an appropriate exercise name.")
            return

        try:
            self.mycursor.execute("DELETE FROM exercises WHERE specific_exercise_name = %s", (exercise_name,))
            self.mydb.commit()
            QMessageBox.information(None, 'Success', 'Exercise successfully deleted!')

        except mysql.connector.Error as err:
            self.errorDisplay(err.errno, err.sqlstate, err.msg)
        finally:
            self.clear_stuff()

    def disabler_btn_editing(self):
        self.ui.Add_exercise.setDisabled(True)
        self.ui.Edit_exer.setDisabled(False)

    def disabler_btn_adding(self):
        self.ui.Add_exercise.setDisabled(False)
        self.ui.Edit_exer.setDisabled(True)

    def errorDisplay(self, errno, sqlstate, msg):
        """Displays detailed error information to the user."""
        self.mydb.rollback()
        # Construct the error message
        error_message = f"Error Code: {errno}\nSQLSTATE: {sqlstate}\nMessage: {msg}"

        # Create and show a critical error message box with the detailed error
        QMessageBox.critical(None, "Database Error", error_message)


class Exercise_Logs(QMainWindow):
    def __init__(self, cursor, db_connection, selected_exercise, date=None):
        super().__init__()     
        self.ui = exercise_logs()
        self.ui.setupUi(self)
        self.mycursor = cursor
        self.mydb = db_connection 
        self.exercise = selected_exercise.strip()
        self.date = date

        self.ui.dateEdit.setMinimumDate(QDate(2000, 1, 1))
        self.ui.dateEdit.setMaximumDate(QDate.currentDate())
        self.ui.dateEdit.setDate(QDate.currentDate())

        self.ui.exer_logs.setWordWrap(True)
        self.ui.exer_logs.resizeColumnsToContents()
        self.ui.exer_logs.resizeRowsToContents()
        self.ui.exer_logs.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.exer_logs.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.ui.exercise_name.setText(self.exercise)
        self.ui.exercise_name.setReadOnly(True)

        self.data_fetched = None

        self.load_logs() # loads into table

    def load_logs(self):
        try:
            self.log_thread = QThread()
            self.log_worker = LogWorker(self.mycursor, self.mydb, self.exercise, self.date)
            self.log_worker.moveToThread(self.log_thread)

            self.log_thread.started.connect(self.log_worker.run)

            self.log_worker.finished.connect(self.success_load)
            self.log_worker.finished.connect(self.log_thread.quit)
            self.log_worker.finished.connect(self.log_worker.deleteLater)
            self.log_thread.finished.connect(self.log_thread.deleteLater)

            self.log_worker.error.connect(self.error)
            self.log_worker.sql_error.connect(self.errorDisplay)
            self.log_thread.start()

        except Exception as err:
            QMessageBox.warning(None, "Error in Logs", f"An error occurred while loading the logs: {err}")
            return

    def error(self, msg):
        QMessageBox.warning(None, 'Error', f'Unexpected Error occurred: {msg}')
        return

    def success_load(self, data_logs):
        self.ui.exer_logs.clearContents()
        self.data_fetched = data_logs
        grouped_sessions = defaultdict(lambda: {'date': None, 'sets': ['-'] * 5})

        for reps, weights, sets, full_date, logs_id in self.data_fetched:
            set_index = int(sets) - 1
            date = full_date.date()

            if weights == 'Bodyweight':
                cell_content = f'{reps} reps: {weights}'
            else:
                cell_content = f'{reps} reps: {weights} Kg'

            grouped_sessions[logs_id]['date'] = date
            grouped_sessions[logs_id]['sets'][set_index] = cell_content # Just get the ID then it will be fine, not only the date

        sorted_sessions = sorted(grouped_sessions.values(), key=lambda x: x['date'], reverse=True)

        self.ui.exer_logs.setRowCount(len(sorted_sessions))

        for row_index, session in enumerate(sorted_sessions):
            # Insert date
            date_str = session['date'].strftime("%Y-%m-%d")
            date_item = QTableWidgetItem(date_str)
            date_item.setTextAlignment(Qt.AlignCenter)
            self.ui.exer_logs.setItem(row_index, 0, date_item)

            # Insert sets 1 to 5
            for col in range(5):
                item = QTableWidgetItem(session['sets'][col])
                item.setTextAlignment(Qt.AlignCenter)
                self.ui.exer_logs.setItem(row_index, col + 1, item)

    def errorDisplay(self, errno, sqlstate, msg):
        """Displays detailed error information to the user."""
        self.mydb.rollback()
        # Construct the error message
        error_message = f"Error Code: {errno}\nSQLSTATE: {sqlstate}\nMessage: {msg}"

        # Create and show a critical error message box with the detailed error
        QMessageBox.critical(None, "Database Error", error_message)


class Select_exercise(QDialog):
    Selected_exercise = Signal(str, str)

    def __init__(self, cursor, db):
        super().__init__()
        self.ui = select_exercise()
        self.ui.setupUi(self)
        self.mycursor = cursor
        self.mydb = db
        self.resulted_data = None

        self.ui.filter_exercise.currentIndexChanged.connect(lambda: self.filter_exercises_by_type(self.ui.filter_exercise.currentText()))
        self.ui.searchlog_lineEdit.textChanged.connect(self.searching)

        self.ui.select_exercise.clicked.connect(self.select_exercise)

        self.load_exercises()
    
    def select_exercise(self):
        if not self.ui.exercise_list.currentItem():
            QMessageBox.warning(None, "No Selected", "Please select an exercise")
            return
        exercise_name = self.ui.exercise_list.currentItem().text().strip()
        if exercise_name:
            self.resulted_data.sort(key=lambda x: x['name'])

            names = [item['name'] for item in self.resulted_data]

            idx = bisect.bisect_left(names, exercise_name)

            if idx < len(self.resulted_data) and self.resulted_data[idx]['name'] == exercise_name:
                exer_type = self.resulted_data[idx]['type']
            
        self.Selected_exercise.emit(exercise_name, exer_type)
        self.close()

    def filter_exercises_by_type(self, selected_type):
        self.ui.exercise_list.clear()   
        for ex in self.resulted_data:
            if ex["type"] == selected_type:
                item = QListWidgetItem(ex["name"])
                item.setTextAlignment(Qt.AlignCenter)
                self.ui.exercise_list.addItem(item)
            elif ex["target"] == selected_type:
                item = QListWidgetItem(ex["name"])
                item.setTextAlignment(Qt.AlignCenter)
                self.ui.exercise_list.addItem(item)

    def searching(self):
        search = self.ui.searchlog_lineEdit.text().strip().upper()
        self.ui.exercise_list.clear()

        if not search:
            # Show all if search is empty
            for exercise in self.resulted_data:
                item = QListWidgetItem(exercise["name"])
                item.setTextAlignment(Qt.AlignCenter)
                self.ui.exercise_list.addItem(item)
            return

        results = []
        for exercise in self.resulted_data:
            if search in exercise["name"].upper():
                results.append(exercise["name"])

        if results:
            for name in results:
                item = QListWidgetItem(name)
                item.setTextAlignment(Qt.AlignCenter)
                self.ui.exercise_list.addItem(item)
        else:
            item = QListWidgetItem("No match found.")
            item.setTextAlignment(Qt.AlignCenter)
            self.ui.exercise_list.addItem(item)

    def update_exercise_list(self, exercise_names):
        self.resulted_data = exercise_names
        self.ui.exercise_list.clear() 

        if exercise_names:
            for exercise in exercise_names:
                item = QListWidgetItem(exercise["name"])
                item.setTextAlignment(Qt.AlignCenter)
                self.ui.exercise_list.addItem(item)
            return
        else:
            self.ui.exercise_list.addItem("No exercises found.")

    def load_exercises(self):
        self.ui.exercise_list.clear()
        self.load_thread = QThread()
        self.load_worker = ListWorker(self.mycursor)
        self.load_worker.moveToThread(self.load_thread)

        self.load_thread.started.connect(self.load_worker.run)
        self.load_worker.finished.connect(self.update_exercise_list)
        self.load_worker.finished.connect(self.load_thread.quit)
        self.load_worker.finished.connect(self.load_worker.deleteLater)
        self.load_thread.finished.connect(self.load_thread.deleteLater)

        self.load_worker.error.connect(self.errorDisplay)

        self.load_thread.start()

    def errorDisplay(self, errno, sqlstate, msg):
        """Displays detailed error information to the user."""
        self.mydb.rollback()
        # Construct the error message
        error_message = f"Error Code: {errno}\nSQLSTATE: {sqlstate}\nMessage: {msg}"

        # Create and show a critical error message box with the detailed error
        QMessageBox.critical(None, "Database Error", error_message)


class ListWorker(QObject):
    finished = Signal(list)
    error = Signal(int, str, str)

    def __init__(self, mycursor):
        super().__init__()
        self.mycursor = mycursor

    def run(self):
        try:
            self.mycursor.execute("SELECT specific_exercise_name, exercise_target, exercise_type FROM exercises")
            resulted_data = self.mycursor.fetchall()
            exercise_names = [
                {
                    "name": exercise[0],
                    "target": exercise[1].title(),
                    "type": exercise[2].title(),
                }
                for exercise in resulted_data
            ]
            self.finished.emit(sorted(exercise_names, key=lambda x: x["name"]))  # sorted before emitting
        except mysql.connector.Error as err:
            self.error.emit(err.errno, err.sqlstate, err.msg)


class SaveLogWorker(QObject):
    finished = Signal()
    error = Signal(str)
    def __init__(self, mycursor, mydb, date, sets, log_data, exercise_name, timestamp):
        super().__init__()
        self.mycursor = mycursor
        self.mydb = mydb
        self.log_data = log_data
        self.date = date
        self.sets = sets + 1
        self.exercise_name = exercise_name
        self.timestamp = timestamp

    def run(self):
        try:
            # Step 1: Compute 1RM
            one_rm = self.compute_oneRM()

            # Step 2: Check for duplicates first
            check_query = """
                SELECT COUNT(*) FROM exercise_logs 
                WHERE exercise_name = %s AND date = %s 
                AND sets = %s AND computed_MAX = %s AND timestamp_logs = %s
            """
            self.mycursor.execute(check_query, (self.exercise_name, self.date, 
                                                self.sets, one_rm, self.timestamp))
            if self.mycursor.fetchone()[0] > 0:
                self.error.emit('Duplicate log, please check the logs you are trying to enter')
                return

            # Step 3: Insert the exercise log
            log_query = """
                INSERT INTO exercise_logs (exercise_name, date, sets, computed_MAX, timestamp_logs)
                VALUES (%s, %s, %s, %s, %s)
            """
            self.mycursor.execute(log_query, (self.exercise_name, self.date, self.sets, 
                                              one_rm, self.timestamp))
            log_id = self.mycursor.lastrowid  # ✅ Get it right after INSERT
            self.mydb.commit()

            for data in self.log_data:
                set_num = data['set']
                reps = data['reps']
                weight = data['weight']
                query = """
                    INSERT INTO reps_and_weights (related_exercise_log, set_value, reps, weights)
                    VALUES (%s, %s, %s, %s)
                """
                self.mycursor.execute(query, (log_id, set_num + 1, reps, weight))

            # Step 6: Commit all and emit success
            self.mydb.commit()
            self.finished.emit()


        except mysql.connector.Error as err:
            print(err)
            self.mydb.rollback()
            self.error.emit(str(err)) 
        except Exception as err:
            print(err)
            self.mydb.rollback()
            self.error.emit(str(err))

    def compute_oneRM(self):
        try:
            self.mycursor.execute('SELECT weight FROM user_account')
            weight = self.mycursor.fetchone()[0]

            exer_reverse = self.log_data[-1:]
            exer_type_or_num = exer_reverse[0]['weight']
            print(exer_type_or_num)
            exer_reps = exer_reverse[0]['reps']

            if exer_type_or_num == 'Bodyweight':
                max_RSI = (exer_reps / weight) * 100
                print('bodyweight')
                return round(max_RSI, 3)

            else: 
                # computes actual one rep 
                max_RM = (float(exer_type_or_num) * (1 + (0.0333 * exer_reps))) / (weight ** 0.67)
                print('free weight')
                return round(max_RM, 3)
            
        except Exception as err:
            self.mydb.rollback()
            self.error.emit(str(err))


class ProgressUpdate(QObject):
    finished = Signal()
    error = Signal(str)
    sql_error = Signal(str, str, str)

    def __init__(self, mydb, mycursor, today, start_week, end_week, year, month, specific_month):
        super().__init__()
        self.mycursor = mycursor
        self.mydb = mydb
        self.today = today
        self.start_week = start_week
        self.end_week = end_week
        self.year = year
        self.month = month
        self.specific_month = specific_month

    def run(self):
        try:
            self.mycursor.execute("""
                SELECT SUM(computed_MAX) FROM exercise_logs
                WHERE date BETWEEN %s AND %s
                """, (self.start_week, self.end_week))
            weekly_sum = self.mycursor.fetchone()[0] or 0

            # for weekly progress
            if weekly_sum > 0: 
                # Will be used only to indicate num of workout per month
                week_num = self.week_of_month()

                self.mycursor.execute("""
                    SELECT COUNT(*) FROM weekly_progress
                    WHERE week_num = %s AND specific_month = %s AND specific_year = %s
                                    AND date BETWEEN %s AND %s
                    """, (week_num, self.specific_month, self.year, self.start_week, self.end_week))
                existing = self.mycursor.fetchone()[0]

                if not existing: # create new weekly computation for new week
                    self.mycursor.execute("""
                        INSERT INTO weekly_progress (week_num, weekly_computation, specific_month, specific_year, date)
                        VALUES (%s, %s, %s, %s, %s)
                        """, (week_num + 1, weekly_sum, self.specific_month, self.year, self.today)) 
                    # purpose of date is the start of the week I guess to count it
                                   
                else: # Just updates per week
                    self.mycursor.execute("""
                        UPDATE weekly_progress
                        SET weekly_computation = %s
                        WHERE week_num = %s AND specific_month = %s AND specific_year = %s
                                        AND date BETWEEN %s AND %s
                    """, (weekly_sum, week_num, self.specific_month, self.year, self.start_week, self.end_week))
            else:
                self.error.emit("Cannot total progress per week")
                return

            print(f'month: {type(self.month)}\n'
                  f'year: {type(self.year)}')

            # FOR MONTHLY PROGRESS
            self.mycursor.execute("""
                SELECT SUM(computed_MAX) FROM exercise_logs
                WHERE MONTH(date) = %s AND YEAR(date) = %s                  
                """, (self.month, self.year))
            
            monthly_sum = self.mycursor.fetchone()[0] or 0

            if monthly_sum > 0:
                month_num = self.month_of_year()
                self.mycursor.execute("""
                    SELECT COUNT(*) FROM monthly_progress
                    WHERE month_num = %s AND MONTH(date) = %s AND specific_year = %s
                    """, (month_num, self.month, self.year))
                existing = self.mycursor.fetchone()[0]

                if not existing: # create new month computation for new month
                    self.mycursor.execute("""
                        INSERT INTO monthly_progress (month_num, monthly_computation, specific_year, date)
                        VALUES (%s, %s, %s, %s)
                    """, (month_num + 1, monthly_sum, self.year, self.today))
                else: # Just updates per month
                    self.mycursor.execute("""
                        UPDATE monthly_progress SET monthly_computation = %s
                        WHERE month_num = %s AND MONTH(date) = %s AND specific_year = %s
                        """, (monthly_sum, month_num, self.month, self.year))
            else: 
                self.error.emit("Cannot total progress per month")
                return

            # FOR YEARLY PROGRESS
            query = """
                SELECT SUM(computed_MAX) FROM exercise_logs
                WHERE YEAR(date) = %s
                """
            self.mycursor.execute(query, (self.year,))
            yearly_sum = self.mycursor.fetchone()[0] or 0

            if yearly_sum > 0:
                self.mycursor.execute("""
                    SELECT COUNT(*) FROM yearly_progress                  
                    WHERE specific_year = %s
                    """, (self.year,))
                existing = self.mycursor.fetchone()[0]

                if not existing: # create new year computation for new year
                    self.mycursor.execute("""
                        INSERT INTO yearly_progress (yearly_computation, specific_year, date)
                        VALUES (%s, %s, %s)
                    """, (yearly_sum, self.year, self.today))
                else: # Just updates per year
                    self.mycursor.execute("""
                        UPDATE yearly_progress SET yearly_computation = %s
                        WHERE specific_year = %s
                        """, (yearly_sum, self.year))

            else: 
                self.error.emit("Cannot total progress per year")
                return
            
            self.mydb.commit()
            self.finished.emit()

        except mysql.connector.Error as err:
            print(err)
            self.mydb.rollback()
            self.sql_error.emit(err.errno, err.sqlstate, err.msg) 
        except Exception as err:
            print(err)
            self.mydb.rollback()
            self.error.emit(str(err))
            
    def week_of_month(self):
        try:
            self.mycursor.execute("""
                SELECT COUNT(*) FROM weekly_progress 
                WHERE specific_month = %s AND specific_year = %s
            """, (self.specific_month, self.year))
            row = self.mycursor.fetchone()
            print(f'this is a row used for the weeks {row}')
            if row:
                return row[0] # Existing week num
            else:
                self.mycursor.execute("""
                    SELECT MAX(week_num) FROM weekly_progress 
                    WHERE specific_month = %s AND specific_year = %s
                """, (self.specific_month, self.year))
                last_week_num = self.mycursor.fetchone()[0] or 0
                return last_week_num + 1  # New week
        
        except mysql.connector.Error as err:
            print(err)
            self.mydb.rollback()
            self.sql_error.emit(err.errno, err.sqlstate, err.msg) 

    def month_of_year(self):
        try:
            self.mycursor.execute("""
                SELECT COUNT(*) FROM monthly_progress 
                WHERE MONTH(date) = %s AND specific_year = %s
            """, (self.month, self.year))
            row = self.mycursor.fetchone()
            print(f'this is a row used for the month {row}')
            if row:
                return row[0]
            else:
                self.mycursor.execute("""
                    SELECT MAX(month_num) FROM monthly_progress 
                    WHERE MONTH(date) = %s AND specific_year = %s
                """, (self.month, self.year))
                last_month_num = self.mycursor.fetchone()[0] or 0
                return last_month_num + 1

        except mysql.connector.Error as err:
            print(err)
            self.mydb.rollback()
            self.sql_error.emit(err.errno, err.sqlstate, err.msg) 


class LogWorker(QObject):
    error = Signal(str)
    sql_error = Signal(str, str, str)
    finished = Signal(list)

    def __init__(self, mycursor, mydb, exercise_name, date):
        super().__init__()
        self.mycursor = mycursor
        self.mydb = mydb
        self.exercise_name = exercise_name
        self.date = date

    def run(self):
        try:
            if self.date:
                print(self.date)
                load_query = """
                SELECT rw.reps, rw.weights, rw.set_value, el.date, el.id_gym_logs
                FROM exercise_logs as el
                JOIN reps_and_weights as rw ON el.id_gym_logs = rw.related_exercise_log
                WHERE el.exercise_name = %s AND el.timestamp_logs = %s
                    """

                self.mycursor.execute(load_query, (self.exercise_name, self.date))
                self.log_data = self.mycursor.fetchall()

                self.finished.emit(self.log_data)
                return
            
            else:
                load_query = """
                SELECT rw.reps, rw.weights, rw.set_value, el.date, el.id_gym_logs
                FROM exercise_logs as el
                JOIN reps_and_weights as rw ON el.id_gym_logs = rw.related_exercise_log
                WHERE exercise_name = %s
                    """

                self.mycursor.execute(load_query, (self.exercise_name,))
                self.log_data = self.mycursor.fetchall()

                self.finished.emit(self.log_data)
                return
                
                
        except Exception as err:
            self.mydb.rollback()
            self.error.emit(str(err))
            return
        except mysql.connector.Error as err:
            self.mydb.rollback()
            self.sql_error.emit(err.errno, err.sqlstate, err.msg)
            return
            

class UserWindow(QDialog):
    def __init__(self, mydb, mycursor):
        super().__init__()
        self.ui = User_window()
        self.ui.setupUi(self)

        self.mycursor = mycursor
        self.mydb = mydb

        # Create a Regular Expression for letters only
        reg_exp = QRegularExpression(r"[a-zA-Z\s]+")  # Only a-z and A-Z

        # Create a validator with the regular expression
        validator = QRegularExpressionValidator(reg_exp)

        self.ui.first_name.setValidator(validator)
        self.ui.last_name.setValidator(validator)

        self.ui.weight.setValidator(QIntValidator(35.0, 200.0))
        self.ui.weight.setMaxLength(6)

        self.ui.save_user.clicked.connect(self.save_user)
        self.ui.clear_fill.clicked.connect(self.clear_fields)

        self.load_user()

    def load_user(self):
        try:
            self.mycursor.execute("SELECT first_name, last_name, weight FROM user_account")
            result = self.mycursor.fetchone()
            if not result:
                QMessageBox.critical(None, "Error", "User not loaded, please double check the database")
                return
            self.ui.first_name.setText(result[0])
            self.ui.last_name.setText(result[1])
            self.ui.weight.setText(str(result[2]))
        except mysql.connector.Error as err:
            self.errorDisplay(err.errno, err.sqlstate, err.msg)

    def save_user(self):
        confirm = QMessageBox.question(None, "Save User",
            "Are you sure you want to save these changes?",
            QMessageBox.Yes | QMessageBox.No                                                  
            )

        if confirm != QMessageBox.Yes:
            return

        
        if not self.ui.last_name.text(): 
            QMessageBox.warning(None, "Unfilled Data", "Please complete the first name for changing the user.")
            return
        
        if not self.ui.first_name.text():
            QMessageBox.warning(None, "Unfilled Data", "Please complete the last name for changing the user.")
            return
        
        if not self.ui.weight.text():              
            QMessageBox.warning(None, "Unfilled Data", "Please complete the weight for changing the user.")
            return

        first_name = self.ui.first_name.text().strip()
        last_name = self.ui.last_name.text().strip()
        weight = float(self.ui.weight.text().strip())

        if first_name == last_name:
            QMessageBox.warning(None, "Redundant Data", 'First and last name are similar, please double check your credentials')
            return
        
        try: 
            self.mycursor.execute("""
                    UPDATE user_account SET first_name = %s,
                                  last_name = %s,
                                  weight = %s      
                                  """,  (first_name, last_name, weight))
            self.mydb.commit()

            QMessageBox.information(None, "User Saved", "User successfully saved!")
            return

        except mysql.connector.Error as err:
            self.errorDisplay(err.errno, err.sqlstate, err.msg)

    def clear_fields(self):
        self.ui.first_name.clear()
        self.ui.last_name.clear()
        self.ui.weight.clear()

    def errorDisplay(self, errno, sqlstate, msg):
        """Displays detailed error information to the user."""
        self.mydb.rollback()
        # Construct the error message
        error_message = f"Error Code: {errno}\nSQLSTATE: {sqlstate}\nMessage: {msg}"

        # Create and show a critical error message box with the detailed error
        QMessageBox.critical(None, "Database Error", error_message)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main_Dashboard()
    window.show()
    sys.exit(app.exec())   