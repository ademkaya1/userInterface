# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Patient_Finder.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def connect_data(self):
        connection = sqlite3.connect("sqlite/patient_info.sqlite")
        query = "SELECT * FROM patients_inf"
        result = connection.execute(query)
        self.tableWidget_Patient_List.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget_Patient_List.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_Patient_List.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        connection.close()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1698, 906)
        MainWindow.setMinimumSize(QtCore.QSize(1698, 906))
        MainWindow.setMaximumSize(QtCore.QSize(1698, 906))
        # MainWindow.setStyleSheet("""QTableWidget {alternate-row-color: green;}""")
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(359, 9, 1331, 551))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_Patient_list = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_Patient_list.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_Patient_list.setObjectName("gridLayout_Patient_list")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.gridLayoutWidget)
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.gridLayout_Patient_list.addWidget(self.verticalScrollBar, 0, 1, 1, 1)
        self.tableWidget_Patient_List = QtWidgets.QTableWidget(self.gridLayoutWidget)
        self.tableWidget_Patient_List.setRowCount(20)
        self.tableWidget_Patient_List.setColumnCount(12)
        self.tableWidget_Patient_List.setObjectName("tableWidget_Patient_List")
        self.tableWidget_Patient_List.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        self.tableWidget_Patient_List.setAlternatingRowColors(True)
        self.tableWidget_Patient_List.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_Patient_List.setHorizontalHeaderLabels(['HASTA ADI', 'SOYADI', 'DOĞUM TARİHİ', 'UYRUK','TCKN','PASSAPORT','CİNSİYET','ANNE ADI','BABA ADI','E-POSTA','TELEFON','EV ADRESİ'])
        # self.tableWidget_Patient_List.setDragEnabled(True)
        # self.tableWidget_Patient_List.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        # self.tableWidget_Patient_List.setDefaultDropAction(QtCore.Qt.LinkAction)
        self.gridLayout_Patient_list.addWidget(self.tableWidget_Patient_List, 0, 0, 1, 1)

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(340, 10, 20, 871))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(360, 600, 1331, 281))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_Patient_Files = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_Patient_Files.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_Patient_Files.setObjectName("gridLayout_Patient_Files")
        self.verticalScrollBar_2 = QtWidgets.QScrollBar(self.gridLayoutWidget_2)
        self.verticalScrollBar_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_2.setObjectName("verticalScrollBar_2")
        self.gridLayout_Patient_Files.addWidget(self.verticalScrollBar_2, 0, 1, 1, 1)
        self.tableWidget_Patient_File = QtWidgets.QTableWidget(self.gridLayoutWidget_2)
        self.tableWidget_Patient_File.setRowCount(1)
        self.tableWidget_Patient_File.setColumnCount(1)
        self.tableWidget_Patient_File.setObjectName("tableWidget_Patient_File")
        self.gridLayout_Patient_Files.addWidget(self.tableWidget_Patient_File, 0, 0, 1, 1)
        self.lineEdit_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_name.setGeometry(QtCore.QRect(150, 50, 181, 31))
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(10, 60, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_name.setFont(font)
        self.label_name.setObjectName("label_name")
        self.label_surname = QtWidgets.QLabel(self.centralwidget)
        self.label_surname.setGeometry(QtCore.QRect(10, 110, 71, 21))
        self.label_surname.setObjectName("label_surname")
        self.lineEdit_Surname = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Surname.setGeometry(QtCore.QRect(150, 100, 181, 31))
        self.lineEdit_Surname.setObjectName("lineEdit_Surname")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(150, 150, 181, 31))
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(1950, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setMinimumDate(QtCore.QDate(1900, 9, 14))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.label_birtday = QtWidgets.QLabel(self.centralwidget)
        self.label_birtday.setGeometry(QtCore.QRect(10, 160, 131, 21))
        self.label_birtday.setObjectName("label_birtday")
        self.label_nationality = QtWidgets.QLabel(self.centralwidget)
        self.label_nationality.setGeometry(QtCore.QRect(10, 210, 71, 16))
        self.label_nationality.setObjectName("label_nationality")
        self.lineEdit_Nationality = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Nationality.setGeometry(QtCore.QRect(150, 200, 181, 31))
        self.lineEdit_Nationality.setObjectName("lineEdit_Nationality")
        self.label_tcno = QtWidgets.QLabel(self.centralwidget)
        self.label_tcno.setGeometry(QtCore.QRect(10, 260, 61, 16))
        self.label_tcno.setObjectName("label_tcno")
        self.lineEdit_TcNo = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_TcNo.setGeometry(QtCore.QRect(150, 250, 181, 31))
        self.lineEdit_TcNo.setObjectName("lineEdit_TcNo")
        self.label_pasaport = QtWidgets.QLabel(self.centralwidget)
        self.label_pasaport.setGeometry(QtCore.QRect(10, 310, 101, 16))
        self.label_pasaport.setObjectName("label_pasaport")
        self.lineEdit_Pasaport = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Pasaport.setGeometry(QtCore.QRect(150, 300, 181, 31))
        self.lineEdit_Pasaport.setObjectName("lineEdit_Pasaport")
        self.label_sex = QtWidgets.QLabel(self.centralwidget)
        self.label_sex.setGeometry(QtCore.QRect(10, 360, 81, 16))
        self.label_sex.setObjectName("label_sex")
        self.lineEdit_Sex = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Sex.setGeometry(QtCore.QRect(150, 350, 181, 31))
        self.lineEdit_Sex.setObjectName("lineEdit_Sex")
        self.label_anne_adi = QtWidgets.QLabel(self.centralwidget)
        self.label_anne_adi.setGeometry(QtCore.QRect(10, 410, 91, 16))
        self.label_anne_adi.setObjectName("label_anne_adi")
        self.lineEdit_Mother_Name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Mother_Name.setGeometry(QtCore.QRect(150, 400, 181, 31))
        self.lineEdit_Mother_Name.setObjectName("lineEdit_Mother_Name")
        self.label_baba_adi = QtWidgets.QLabel(self.centralwidget)
        self.label_baba_adi.setGeometry(QtCore.QRect(10, 460, 91, 16))
        self.label_baba_adi.setObjectName("label_baba_adi")
        self.lineEdit_Father_Name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Father_Name.setGeometry(QtCore.QRect(150, 450, 181, 31))
        self.lineEdit_Father_Name.setObjectName("lineEdit_Father_Name")
        self.pushButton_Find = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Find.setGeometry(QtCore.QRect(10, 500, 321, 31))
        self.pushButton_Find.setObjectName("pushButton_Find")
        self.pushButton_Find.clicked.connect(self.connect_data)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 30, 331, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_header = QtWidgets.QLabel(self.centralwidget)
        self.label_header.setGeometry(QtCore.QRect(10, 10, 311, 16))
        self.label_header.setObjectName("label_header")
        self.pushButton_Create_New_Patient_Folder = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Create_New_Patient_Folder.setGeometry(QtCore.QRect(360, 560, 1331, 41))
        self.pushButton_Create_New_Patient_Folder.setObjectName("pushButton_Create_New_Patient_Folder")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 540, 321, 31))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AYAKTAN VE YATAN HASTA ARAMA "))
        self.label_name.setText(_translate("MainWindow", "ADI :"))
        self.label_surname.setText(_translate("MainWindow", "SOYADI :"))
        self.label_birtday.setText(_translate("MainWindow", "DOĞUM TARİHİ :"))
        self.label_nationality.setText(_translate("MainWindow", "UYRUK :"))
        self.label_tcno.setText(_translate("MainWindow", "TC NO :"))
        self.label_pasaport.setText(_translate("MainWindow", "PASAPORT:"))
        self.label_sex.setText(_translate("MainWindow", "CİNSİYET :"))
        self.label_anne_adi.setText(_translate("MainWindow", "ANNE ADI :"))
        self.label_baba_adi.setText(_translate("MainWindow", "BABA ADI :"))
        self.pushButton_Find.setText(_translate("MainWindow", "ARA"))
        self.label_header.setText(_translate("MainWindow", "HASTA TAKİP"))
        self.pushButton_Create_New_Patient_Folder.setText(_translate("MainWindow", "SEÇİLİ HASTAYA YENİ DOSYA OLUŞTUR"))
        self.pushButton.setText(_translate("MainWindow", "TEMİZLE"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
