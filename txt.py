import json
from PyQt5.QtWidgets import QWidget,QMainWindow,QPushButton,QLineEdit,QLabel,QVBoxLayout,QHBoxLayout,QFrame,QGridLayout,QComboBox,QTableWidget,QTableWidgetItem
from DataBaseOperation import DBOperation
from PyQt5.QtWidgets import QHeaderView,qApp
import PyQt5.QtGui
import sys
import os
#from InstallWindow import InstallWindow
#from LoginWindow import LoginScreen
from PyQt5.QtWidgets import QApplication,QSplashScreen,QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt,QTimer

class BillingScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Billing")
        self.resize(800, 600)

        layout = QVBoxLayout()

        self.table = QTableWidget()
        self.table.setStyleSheet("background:#fff")
        self.table.setRowCount(0)
        self.table.setColumnCount(4)

        self.table.setHorizontalHeaderItem(0, QTableWidgetItem("Vehicle No"))
        self.table.setHorizontalHeaderItem(1, QTableWidgetItem("Entry Time"))
        self.table.setHorizontalHeaderItem(2, QTableWidgetItem("Exit Time"))
        self.table.setHorizontalHeaderItem(3, QTableWidgetItem("Charges"))

        layout.addWidget(self.table)

        self.refreshBilling()

        self.setLayout(layout)

    def refreshBilling(self):
        data = self.dbOperation.getAllVehicle()
        self.table.setRowCount(len(data))
        for row, vehicle in enumerate(data):
            self.table.setItem(row, 0, QTableWidgetItem(str(vehicle[6])))
            self.table.setItem(row, 1, QTableWidgetItem(str(vehicle[3])))
            self.table.setItem(row, 2, QTableWidgetItem(str(vehicle[4])))

            # Calculate charges based on parking duration and any logic you have
            # For example, you can calculate charges as (parking_duration_hours * hourly_rate)
            hourly_rate = 10  # Adjust the hourly rate as needed
            entry_time = datetime.strptime(vehicle[3], "%Y-%m-%d %H:%M:%S")
            exit_time = datetime.strptime(vehicle[4], "%Y-%m-%d %H:%M:%S")
            parking_duration = (exit_time - entry_time).seconds / 3600
            charges = parking_duration * hourly_rate

            self.table.setItem(row, 3, QTableWidgetItem(str(charges)))


# ... Rest of your code ...

class HomeScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        # ... Existing code ...

        self.btn_billing = QPushButton("Billing")
        self.btn_billing.setStyleSheet("width:200px;height:160px;font-size:20px;background:#A4866F;color:#fff;font-weight:bold;border:1px solid white")
        self.btn_billing.clicked.connect(self.showBilling)
        menu_vertical_layout.addWidget(self.btn_billing)

        # ... Rest of your code ...

    def showBilling(self):
        self.btn_home.setStyleSheet("width:200px;height:160px;font-size:20px;background:#A4866F;color:#fff;font-weight:bold;border:1px solid white")
        self.btn_add.setStyleSheet("width:200px;height:160px;font-size:20px;background:#A4866F;color:#fff;font-weight:bold;border:1px solid white")
        self.btn_manage.setStyleSheet("width:200px;height:160px;font-size:20px;background:#A4866F;color:#fff;font-weight:bold;border:1px solid white")
        self.btn_history.setStyleSheet("width:200px;height:160px;font-size:20px;background:#A4866F;color:#fff;font-weight:bold;border:1px solid white")
        self.btn_billing.setStyleSheet("width:200px;height:160px;font-size:20px;background:#1A3668;color:#fff;font-weight:bold;border:1px solid white")

        self.frame_1.hide()
        self.frame_2.hide()
        self.frame_3.hide()
        self.frame_4.hide()
        self.frame_5.show()

# ... Rest of your code ...










self.button_exit=QPushButton("Exit")
            self.button_exit.setStyleSheet("color:#fff;padding:8px 0px;font-size:20px;background:green;border:1px solid white")
            self.table.setCellWidget(loop,6,self.button_exit)
            self.button_exit.clicked.connect(self.exitCall)
            loop=loop+1

        frame=QFrame()
        layout=QVBoxLayout()
        button=QPushButton("Refresh")
        button.setStyleSheet("color:#fff;padding:8px 0px;font-size:20px;background:green;border:1px solid white")
        button.clicked.connect(self.refreshManage)
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        layout.addWidget(button)
        layout.addWidget(self.table)
        frame.setLayout(layout)
        frame.setContentsMargins(0,0,0,0)
        frame.setMaximumWidth(self.width())
        frame.setMinimumWidth(self.width())
        frame.setMaximumHeight(self.height())
        frame.setMinimumHeight(self.height())
        self.vertical_3.addWidget(frame)
        self.vertical_3.addStretch()