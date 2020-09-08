# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hasta_kayit.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import sqlite3
import datetime
from playsound import playsound
from gtts import gTTS
from PyQt5 import QtCore, QtGui, QtWidgets
import re


class Ui_hasta_kayit_window(object):
    def baglanti_olustur_3(self):
        baglanti = sqlite3.connect("sqlite/patient_info.sqlite")
        self.cursor = baglanti.cursor()
        self.cursor.execute(
            "Create Table If not exists patients_inf(hasta_adi TEXT,hasta_soyadi TEXT,dogum_tarihi INT,uyruk TEXT,TCKN INT,passaport INT,cinsiyet TEXT,anne_adi TEXT,baba_adi TEXT,e_posta TEXT,telefon INT,ev_adresi TEXT,TCKN_NEDEN_YOK TEXT)")
        baglanti.commit()

        # patient_name, patient_surname, patient_birtday,
        # patient_nationality, patient_TCKN,
        # patient_passaport, patient_cinsiyet,
        # patient_mother_name, patient_father_name,
        # patient_e_posta, patient_phone, patient_adress,))

    def setupUi(self, MainWindow):
        # region MAİNWİNDOW
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 550)
        MainWindow.setMinimumSize(QtCore.QSize(800, 550))
        MainWindow.setMaximumSize(QtCore.QSize(805, 555))
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(False)
        MainWindow.setStyleSheet("""QLineEdit {
                                            border-style: outset;
                                            border-width: 2px;
                                            # border-radius: 10px;
                                            # border-color: black;
                                            font: bold 15px;
                                            min-width: 10em;
                                            padding: 6px;
                                            
                                            }QPushButton {background-color: white; border-style: outset;border-width: 2px;border-radius: 10px;border-color: black;}
                                            QPushButton:hover:!pressed{border: 1px solid green;}
                                            QDateEdit:hover:!pressed{border: 1px solid green;}""")
        self.baglanti_olustur_3()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # endregion MAINWINDOW

        # region UYRUK
        self.label_uyruk = QtWidgets.QLabel(self.centralwidget)
        self.label_uyruk.setGeometry(QtCore.QRect(10, 30, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_uyruk.setFont(font)
        self.label_uyruk.setObjectName("label_uyruk")
        self.comboBox_uyruk = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_uyruk.setGeometry(QtCore.QRect(160, 30, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_uyruk.setFont(font)
        self.comboBox_uyruk.setInputMethodHints(QtCore.Qt.ImhPreferUppercase)
        self.comboBox_uyruk.setCurrentText("")
        self.comboBox_uyruk.setMaxCount(2147483647)
        self.comboBox_uyruk.setObjectName("comboBox_uyruk")
        self.comboBox_uyruk_list = ["", "Arjantin", "Angola", "Arabistan", "Brezilya",
                                    "Belçika", "Çin",
                                    "Danimarka", "Diğer"]
        self.comboBox_uyruk.addItems(self.comboBox_uyruk_list)
        self.comboBox_uyruk.setCurrentIndex(0)
        self.comboBox_uyruk.setDisabled(True)
        # endregion UYRUK

        # region TC KİMLİK NO
        self.label_Tc = QtWidgets.QLabel(self.centralwidget)
        self.label_Tc.setGeometry(QtCore.QRect(10, 70, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_Tc.setFont(font)
        self.label_Tc.setObjectName("label_Tc")
        self.lineEdit_Tc_Kimlik_No = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Tc_Kimlik_No.setGeometry(QtCore.QRect(160, 70, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_Tc_Kimlik_No.setFont(font)
        # self.lineEdit_Tc_Kimlik_No.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly | QtCore.Qt.ImhPreferNumbers)
        self.lineEdit_Tc_Kimlik_No.setObjectName("lineEdit_Tc_Kimlik_No")

        self.lineEdit_Tc_Kimlik_No.setMaxLength(11)
        self.rxt = QtCore.QRegExp("\d+")
        self.lineEdit_Tc_Kimlik_No.setValidator(QtGui.QRegExpValidator(self.rxt))
        # endregion

        # region YABANCI HASTA
        self.checkBox_Yabanci_Hasta = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_Yabanci_Hasta.setGeometry(QtCore.QRect(380, 30, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_Yabanci_Hasta.setFont(font)
        self.checkBox_Yabanci_Hasta.setObjectName("checkBox_Yabanci_Hasta")
        self.checkBox_Yabanci_Hasta.clicked.connect(self.check_yabanci)
        # endregion YABANCI HASTA

        # region KİMLİK YOK
        self.checkBox_Kimlik_Yok = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_Kimlik_Yok.setGeometry(QtCore.QRect(560, 40, 180, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_Kimlik_Yok.setFont(font)
        self.checkBox_Kimlik_Yok.setObjectName("checkBox_Kimlik_Yok")
        self.checkBox_Kimlik_Yok.clicked.connect(self.check_TC_yok)

        self.label_kimlik_yok_nedeni = QtWidgets.QLabel(self.centralwidget)
        self.label_kimlik_yok_nedeni.setGeometry(QtCore.QRect(10, 110, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_kimlik_yok_nedeni.setFont(font)
        self.label_kimlik_yok_nedeni.setObjectName("label_kimlik_yok_nedeni")
        self.comboBox_Kimlik_Yok_Neden = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_Kimlik_Yok_Neden.setGeometry(QtCore.QRect(160, 110, 621, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_Kimlik_Yok_Neden.setFont(font)
        # self.comboBox_Kimlik_Yok_Neden.setInputMethodHints(QtCore.Qt.ImhPreferUppercase)
        self.comboBox_Kimlik_Yok_Neden.setObjectName("comboBox_Kimlik_Yok_Neden")
        self.comboBox_Kimlik_Yok_Neden_list = ["", "Kayıp", "Tüzel Kişi", "Devlet Görevlisi",
                                               "Diğer"]
        self.comboBox_Kimlik_Yok_Neden.addItems(self.comboBox_Kimlik_Yok_Neden_list)
        self.comboBox_Kimlik_Yok_Neden.setDisabled(True)
        # endregion KİMLİK YOK

        # region AD
        self.label_adi = QtWidgets.QLabel(self.centralwidget)
        self.label_adi.setGeometry(QtCore.QRect(10, 150, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_adi.setFont(font)
        self.label_adi.setObjectName("label_adi")
        self.lineEdit_Adi = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Adi.setGeometry(QtCore.QRect(160, 150, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_Adi.setFont(font)
        # self.lineEdit_Adi.setInputMethodHints(QtCore.Qt.ImhPreferUppercase | QtCore.Qt.ImhUppercaseOnly)
        self.lineEdit_Adi.setObjectName("lineEdit_Adi")
        # self.rxt_2 = QtCore.QRegExp(r">AAAAA-AAAAA-AAAAA-AAAAA-AAAAA;#")
        # self.lineEdit_Adi.setValidator(QtGui.QRegExpValidator(self.rxt_2))

        # endregion AD

        # region SOYAD
        self.label_soyadi = QtWidgets.QLabel(self.centralwidget)
        self.label_soyadi.setGeometry(QtCore.QRect(380, 150, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_soyadi.setFont(font)
        self.label_soyadi.setObjectName("label_soyadi")
        self.lineEdit_Soyadi = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Soyadi.setGeometry(QtCore.QRect(500, 150, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_Soyadi.setFont(font)
        self.lineEdit_Soyadi.setInputMethodHints(QtCore.Qt.ImhUppercaseOnly)
        self.lineEdit_Soyadi.setObjectName("lineEdit_Soyadi")
        # endregion SOYAD

        # region CİNSİYET
        self.label_cinsiyet = QtWidgets.QLabel(self.centralwidget)
        self.label_cinsiyet.setGeometry(QtCore.QRect(10, 200, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_cinsiyet.setFont(font)
        self.label_cinsiyet.setObjectName("label_cinsiyet")
        # endregion CİNSİYET

        # region PASSAPORT
        self.label_passaport = QtWidgets.QLabel(self.centralwidget)
        self.label_passaport.setGeometry(QtCore.QRect(380, 70, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_passaport.setFont(font)
        self.label_passaport.setObjectName("label_passaport")
        self.lineEdit_Passaport_No = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Passaport_No.setGeometry(QtCore.QRect(500, 70, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_Passaport_No.setFont(font)
        self.lineEdit_Passaport_No.setInputMethodHints(QtCore.Qt.ImhPreferUppercase)
        self.lineEdit_Passaport_No.setObjectName("lineEdit_Passaport_No")
        self.lineEdit_Passaport_No.setMaxLength(9)
        self.lineEdit_Passaport_No.setDisabled(True)
        # endregion PASSAPORT

        # region CİNSİYET
        self.comboBox_Cinsiyet = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_Cinsiyet.setGeometry(QtCore.QRect(160, 190, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_Cinsiyet.setFont(font)
        self.comboBox_Cinsiyet.setObjectName("comboBox_Cinsiyet")
        self.comboBox_Cinsiyet_list = ["", "Erkek", "Kadın"]
        self.comboBox_Cinsiyet.addItems(self.comboBox_Cinsiyet_list)
        # endregion CİNSİYET

        # region DOĞUM TARİHİ
        self.label_dogum_tarihi = QtWidgets.QLabel(self.centralwidget)
        self.label_dogum_tarihi.setGeometry(QtCore.QRect(380, 190, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_dogum_tarihi.setFont(font)
        self.label_dogum_tarihi.setObjectName("label_dogum_tarihi")
        self.dateEdit_Dogum_Tarihi = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_Dogum_Tarihi.setGeometry(QtCore.QRect(500, 190, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dateEdit_Dogum_Tarihi.setFont(font)
        self.dateEdit_Dogum_Tarihi.setDateTime(QtCore.QDateTime(QtCore.QDate(1970, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_Dogum_Tarihi.setMinimumDateTime(
            QtCore.QDateTime(QtCore.QDate(1900, 9, 14), QtCore.QTime(0, 0, 0)))
        self.dateEdit_Dogum_Tarihi.setCalendarPopup(True)
        self.dateEdit_Dogum_Tarihi.setObjectName("dateEdit_Dogum_Tarihi")
        # endregion DOĞUM TARİHİ

        # region ANNE ADI
        self.label_anne_adi = QtWidgets.QLabel(self.centralwidget)
        self.label_anne_adi.setGeometry(QtCore.QRect(10, 240, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_anne_adi.setFont(font)
        self.label_anne_adi.setObjectName("label_anne_adi")
        self.lineEdit_Anne_Adi = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Anne_Adi.setGeometry(QtCore.QRect(160, 230, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_Anne_Adi.setFont(font)
        # self.lineEdit_Anne_Adi.setInputMethodHints(QtCore.Qt.ImhPreferUppercase | QtCore.Qt.ImhUppercaseOnly)
        self.lineEdit_Anne_Adi.setObjectName("lineEdit_Anne_Adi")
        # endregion ANNE ADI

        # region BABA ADI
        self.label_baba_adi = QtWidgets.QLabel(self.centralwidget)
        self.label_baba_adi.setGeometry(QtCore.QRect(380, 240, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_baba_adi.setFont(font)
        self.label_baba_adi.setObjectName("label_baba_adi")
        self.lineEdit_Baba_Adi = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Baba_Adi.setGeometry(QtCore.QRect(500, 231, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_Baba_Adi.setFont(font)
        self.lineEdit_Baba_Adi.setInputMethodHints(QtCore.Qt.ImhUppercaseOnly)
        self.lineEdit_Baba_Adi.setObjectName("lineEdit_Baba_Adi")
        # endregion BABA ADI

        # region E_POSTA
        self.label_e_posta = QtWidgets.QLabel(self.centralwidget)
        self.label_e_posta.setGeometry(QtCore.QRect(10, 280, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_e_posta.setFont(font)
        self.label_e_posta.setObjectName("label_e_posta")
        self.lineEdit_Eposta = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Eposta.setGeometry(QtCore.QRect(160, 270, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_Eposta.setFont(font)
        self.lineEdit_Eposta.setInputMethodHints(QtCore.Qt.ImhEmailCharactersOnly)
        self.lineEdit_Eposta.setObjectName("lineEdit_Eposta")

        self.my_regex = QtCore.QRegExp(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
        self.my_validator = QtGui.QRegExpValidator(self.my_regex, self.lineEdit_Eposta)
        self.lineEdit_Eposta.setValidator(self.my_validator)

        # endregion E_POSTA

        # region CEP TELEFONU
        self.label_cep_telefonu = QtWidgets.QLabel(self.centralwidget)
        self.label_cep_telefonu.setGeometry(QtCore.QRect(380, 280, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_cep_telefonu.setFont(font)
        self.label_cep_telefonu.setObjectName("label_cep_telefonu")
        self.lineEdit_Cep_Telefonu = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Cep_Telefonu.setGeometry(QtCore.QRect(500, 270, 281, 31))
        # self.lineEdit_Cep_Telefonu.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly | QtCore.Qt.ImhPreferNumbers)
        self.lineEdit_Cep_Telefonu.setObjectName("lineEdit_Cep_Telefonu")

        self.lineEdit_Cep_Telefonu.setMaxLength(10)
        self.rx = QtCore.QRegExp("\d+")
        self.lineEdit_Cep_Telefonu.setValidator(QtGui.QRegExpValidator(self.rx))

        # endregion CEP TELEFONU

        # region EV ADRESİ
        self.label_ev_adresi = QtWidgets.QLabel(self.centralwidget)
        self.label_ev_adresi.setGeometry(QtCore.QRect(10, 340, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_ev_adresi.setFont(font)
        self.label_ev_adresi.setObjectName("label_ev_adresi")

        self.textEdit_Ev_Adresi = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_Ev_Adresi.setGeometry(QtCore.QRect(160, 320, 621, 141))
        # self.textEdit_Ev_Adresi.setInputMethodHints(QtCore.Qt.ImhUppercaseOnly)
        # self.textEdit_Ev_Adresi.setMaxLength(70000)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit_Ev_Adresi.setFont(font)
        self.textEdit_Ev_Adresi.setObjectName("TextEdit_Ev_Adresi")
        # endregion EV ADRESİ

        # region KAYDET BUTONU
        self.pushButton_Kaydet = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Kaydet.setGeometry(QtCore.QRect(360, 490, 201, 28))
        self.pushButton_Kaydet.setObjectName("pushButton_Kaydet")
        self.pushButton_Kaydet.clicked.connect(self.kaydet)
        # endregion KAYDET BUTONU

        # region TEMİZLE BUTONU
        self.pushButton_Temizle = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Temizle.setGeometry(QtCore.QRect(160, 490, 191, 28))
        self.pushButton_Temizle.setWhatsThis("")
        self.pushButton_Temizle.setAccessibleDescription("")
        self.pushButton_Temizle.setObjectName("pushButton_Temizle")
        self.pushButton_Temizle.clicked.connect(self.alanlari_temizle)
        # endregion TEMİZLE BUTONU

        # region ÇIKIŞ BUTONU
        self.pushButton_Cikis = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Cikis.setGeometry(QtCore.QRect(570, 490, 211, 28))
        self.pushButton_Cikis.setWhatsThis("")
        self.pushButton_Cikis.setAccessibleDescription("")
        self.pushButton_Cikis.setObjectName("pushButton_Cikis")
        self.pushButton_Cikis.clicked.connect(MainWindow.close)
        # endregion

        # region MAINWİNDOW Statue
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # endregion

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hasta Kayıt Formu"))
        self.label_uyruk.setText(_translate("MainWindow", "Uyruk"))
        self.label_Tc.setText(_translate("MainWindow", "Tc Kimlik No"))
        self.checkBox_Yabanci_Hasta.setText(_translate("MainWindow", "Yabancı Hasta"))
        self.checkBox_Kimlik_Yok.setText(_translate("MainWindow", "Türk Ama Kimlik Yok"))
        self.label_kimlik_yok_nedeni.setText(_translate("MainWindow", "Kimlik Yok Nedeni"))
        self.label_adi.setText(_translate("MainWindow", "Adı"))
        self.label_soyadi.setText(_translate("MainWindow", "Soyadı"))
        self.label_cinsiyet.setText(_translate("MainWindow", "Cinsiyet"))
        self.label_passaport.setText(_translate("MainWindow", "Passaport No"))
        self.label_dogum_tarihi.setText(_translate("MainWindow", "Doğum Tarihi"))
        self.label_anne_adi.setText(_translate("MainWindow", "Anne Adı"))
        self.label_baba_adi.setText(_translate("MainWindow", "Baba Adı"))
        self.label_e_posta.setText(_translate("MainWindow", "E-Posta"))
        self.label_cep_telefonu.setText(_translate("MainWindow", "Cep Telefonu"))
        self.label_ev_adresi.setText(_translate("MainWindow", "Ev Adresi"))
        self.pushButton_Kaydet.setText(_translate("MainWindow", "Kaydet"))
        self.pushButton_Temizle.setText(_translate("MainWindow", "Temizle"))
        self.pushButton_Cikis.setText(_translate("MainWindow", "Çıkış"))

    def check_yabanci(self):
        if self.checkBox_Yabanci_Hasta.isChecked():
            self.comboBox_uyruk.setEnabled(True)
            self.lineEdit_Passaport_No.setEnabled(True)
            self.lineEdit_Tc_Kimlik_No.setEnabled(False)
            self.lineEdit_Tc_Kimlik_No.clear()
            self.checkBox_Kimlik_Yok.setDisabled(True)
            self.comboBox_uyruk.setCurrentIndex(0)
            # self.comboBox_uyruk.isHidden()
        else:
            self.comboBox_uyruk.setEnabled(False)
            self.lineEdit_Passaport_No.setEnabled(False)
            self.lineEdit_Passaport_No.clear()
            self.comboBox_uyruk.setCurrentIndex(0)
            self.lineEdit_Tc_Kimlik_No.setEnabled(True)
            self.checkBox_Kimlik_Yok.setDisabled(False)

    def check_TC_yok(self):
        if self.checkBox_Kimlik_Yok.isChecked():
            self.comboBox_Kimlik_Yok_Neden.setEnabled(True)
            self.lineEdit_Tc_Kimlik_No.setText("11111111111")
            self.lineEdit_Tc_Kimlik_No.setEnabled(False)
            self.checkBox_Yabanci_Hasta.setDisabled(True)
            self.comboBox_uyruk.setCurrentIndex(0)
        else:
            self.comboBox_Kimlik_Yok_Neden.setEnabled(False)
            self.comboBox_Kimlik_Yok_Neden.setCurrentIndex(0)
            self.lineEdit_Tc_Kimlik_No.clear()
            self.checkBox_Yabanci_Hasta.setDisabled(False)
            self.lineEdit_Tc_Kimlik_No.setDisabled(False)

    def register_done(self):
        self.info()
        self.msg_box = QtWidgets.QMessageBox()
        self.msg_box.setIcon(QtWidgets.QMessageBox.Information)
        self.msg_box.setText("Kayıt Başarılı ! ")
        self.msg_box.setWindowTitle("Bilgi ")
        self.msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
        self.returnValue = self.msg_box.exec()

    def info(self):
        self.msg_box = QtWidgets.QMessageBox()
        self.msg_box.setIcon(QtWidgets.QMessageBox.Information)
        self.msg_box.setText("Kaydetmek istiyor musunuz ? ")
        self.msg_box.setWindowTitle("Bilgi Ekranı")

    def uyari_msg(self):
        self.msg_box = QtWidgets.QMessageBox()
        self.msg_box.setIcon(QtWidgets.QMessageBox.Information)
        self.msg_box.setText(self.uyari_msg_text)
        self.msg_box.setWindowTitle("UYARI !")
        self.msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
        self.returnValue = self.msg_box.exec()

    def alanlari_temizle(self):
        self.lineEdit_Adi.clear()
        self.lineEdit_Soyadi.clear()
        self.comboBox_uyruk.setCurrentIndex(0)
        self.lineEdit_Tc_Kimlik_No.clear()
        self.lineEdit_Passaport_No.clear()
        self.comboBox_Cinsiyet.setCurrentIndex(0)
        self.lineEdit_Anne_Adi.clear()
        self.lineEdit_Baba_Adi.clear()
        self.lineEdit_Eposta.clear()
        self.lineEdit_Cep_Telefonu.clear()
        self.textEdit_Ev_Adresi.clear()
        self.comboBox_Kimlik_Yok_Neden.setCurrentIndex(0)
        self.checkBox_Kimlik_Yok.setChecked(False)
        self.checkBox_Yabanci_Hasta.setChecked(False)
        self.checkBox_Kimlik_Yok.setDisabled(False)
        self.checkBox_Yabanci_Hasta.setEnabled(True)
        self.lineEdit_Tc_Kimlik_No.setEnabled(True)
        self.comboBox_uyruk.setEnabled(False)
        self.comboBox_Kimlik_Yok_Neden.setEnabled(False)
        self.lineEdit_Passaport_No.setEnabled(False)

    def kaydet(self):
        patient_name = self.lineEdit_Adi.text()
        patient_surname = self.lineEdit_Soyadi.text()
        patient_nationality = self.comboBox_uyruk.currentText()
        patient_TCKN = self.lineEdit_Tc_Kimlik_No.text()
        patient_passaport = self.lineEdit_Passaport_No.text()
        patient_TC_yok = self.comboBox_Kimlik_Yok_Neden.currentText()
        patient_cinsiyet = self.comboBox_Cinsiyet.currentText()
        patient_mother_name = self.lineEdit_Anne_Adi.text()
        patient_father_name = self.lineEdit_Baba_Adi.text()
        patient_e_posta = self.lineEdit_Eposta.text()
        patient_phone = self.lineEdit_Cep_Telefonu.text()
        patient_adress = self.textEdit_Ev_Adresi.toPlainText()
        patient_birtday = self.dateEdit_Dogum_Tarihi.text()
        patient_date = self.dateEdit_Dogum_Tarihi.date().year()
        a = patient_date
        now = datetime.datetime.now()
        b = now.strftime("%Y")

        # region Yabanci hasta ise
        if self.checkBox_Yabanci_Hasta.isChecked():
            if len(patient_name) != 0:
                if len(patient_surname) != 0:
                    if int(a) < int(b):
                        if int(a) > 1900:
                            if patient_nationality != "" and patient_nationality != "Türkiye":
                                if len(patient_passaport) == 9:
                                    if patient_cinsiyet != "":
                                        if patient_mother_name != 0:
                                            if patient_father_name != 0:
                                                if patient_e_posta != 0 and re.search("@", patient_e_posta):
                                                    if len(patient_phone) >= 9 and len(patient_phone) <= 12:
                                                        if len(patient_adress) > 20:

                                                            if re.search("com", patient_e_posta):
                                                                connection = sqlite3.connect(
                                                                    "sqlite/patient_info.sqlite")
                                                                connection.execute(
                                                                    "INSERT INTO patients_inf VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
                                                                    (
                                                                        patient_name.upper(),
                                                                        patient_surname.upper(),
                                                                        patient_birtday,
                                                                        patient_nationality, patient_TCKN,
                                                                        patient_passaport.upper(),
                                                                        patient_cinsiyet.upper(),
                                                                        patient_mother_name.upper(),
                                                                        patient_father_name.upper(),
                                                                        patient_e_posta, patient_phone,
                                                                        patient_adress.upper(), patient_TC_yok.upper()))
                                                                connection.commit()
                                                                connection.close()

                                                                self.register_done()
                                                            else:
                                                                self.uyari_msg_text = "Hatalı Yada Eksik E-POSTA"
                                                                self.uyari_msg()

                                                        else:
                                                            self.uyari_msg_text = "Hatalı Yada Eksik ADRES"
                                                            self.uyari_msg()
                                                    else:
                                                        self.uyari_msg_text = "Hatalı Yada Eksik TELEFON NUMARASI"
                                                        self.uyari_msg()
                                                else:
                                                    self.uyari_msg_text = "Hatalı Yada Eksik E-POSTA"
                                                    self.uyari_msg()
                                            else:
                                                self.uyari_msg_text = "Hatalı Yada Eksik BABA ADI"
                                                self.uyari_msg()
                                        else:
                                            self.uyari_msg_text = "Hatalı Yada Eksik ANNE ADI"
                                            self.uyari_msg()
                                    else:
                                        self.uyari_msg_text = "Hatalı Yada Eksik CİNSİYET"
                                        self.uyari_msg()
                                else:
                                    self.uyari_msg_text = "Hatalı Yada Eksik PASAPORT"
                                    self.uyari_msg()
                            else:
                                self.uyari_msg_text = "Hatalı Yada Yanlış UYRUK SEÇTİNİZ"
                                self.uyari_msg()
                        else:
                            self.uyari_msg_text = "Hatalı Yada Eksik DOĞUM TARİHİ"
                            self.uyari_msg()
                    else:
                        self.uyari_msg_text = "Hatalı Yada Eksik DOĞUM TARİHİ"
                        self.uyari_msg()
                else:
                    self.uyari_msg_text = "Hatalı Yada Eksik SOYAD"
                    self.uyari_msg()
            else:
                self.uyari_msg_text = "Hatalı Yada Eksik AD"
                self.uyari_msg()
        #         endregion

        # region TC-vatandaşı fakat kimlik yok
        if self.checkBox_Kimlik_Yok.isChecked():

            if len(patient_name) != 0:
                if len(patient_surname) != 0:
                    if int(a) < int(b):
                        if int(a) > 1900:
                            if patient_cinsiyet != "Cinsiyet Seçiniz":
                                if patient_mother_name != 0:
                                    if patient_father_name != 0:
                                        if patient_e_posta != 0 and re.search("@", patient_e_posta):
                                            if len(patient_phone) == 10:
                                                if len(patient_adress) > 20:
                                                    if re.search("com", patient_e_posta):
                                                        if patient_TC_yok != "":
                                                            connection = sqlite3.connect("sqlite/patient_info.sqlite")
                                                            connection.execute(
                                                                "INSERT INTO patients_inf VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
                                                                (
                                                                    patient_name.upper(), patient_surname.upper(),
                                                                    patient_birtday,
                                                                    patient_nationality, patient_TCKN,
                                                                    patient_passaport.upper(), patient_cinsiyet.upper(),
                                                                    patient_mother_name.upper(),
                                                                    patient_father_name.upper(),
                                                                    patient_e_posta, patient_phone,
                                                                    patient_adress.upper(), patient_TC_yok.upper()))
                                                            connection.commit()
                                                            connection.close()

                                                            self.register_done()
                                                        else:
                                                            self.uyari_msg_text = "Hatalı Yada Eksik KİMLİK NEDENİ"
                                                            self.uyari_msg()

                                                    else:
                                                        self.uyari_msg_text = "Hatalı Yada Eksik E-POSTA"
                                                        self.uyari_msg()
                                                else:
                                                    self.uyari_msg_text = "Hatalı Yada Eksik ADRES"
                                                    self.uyari_msg()
                                            else:
                                                self.uyari_msg_text = "Hatalı Yada Eksik TELEFON NUMARASI"
                                                self.uyari_msg()
                                        else:
                                            self.uyari_msg_text = "Hatalı Yada Eksik E-POSTA"
                                            self.uyari_msg()
                                    else:
                                        self.uyari_msg_text = "Hatalı Yada Eksik BABA ADI"
                                        self.uyari_msg()
                                else:
                                    self.uyari_msg_text = "Hatalı Yada Eksik ANNE ADI"
                                    self.uyari_msg()
                            else:
                                self.uyari_msg_text = "Hatalı Yada Eksik CİNSİYET BİLGİSİ"
                                self.uyari_msg()
                        else:
                            self.uyari_msg_text = "Hatalı Yada Eksik DOĞUM TARİHİ"
                            self.uyari_msg()
                    else:
                        self.uyari_msg_text = "Hatalı Yada Eksik DOĞUM TARİHİ"
                        self.uyari_msg()
                else:
                    self.uyari_msg_text = "Hatalı Yada Eksik SOYAD"
                    self.uyari_msg()
            else:
                self.uyari_msg_text = "Hatalı Yada Eksik AD"
                self.uyari_msg()
        #         endregion

        # region Tc vatandaşı ise
        if not self.checkBox_Kimlik_Yok.isChecked() and not self.checkBox_Yabanci_Hasta.isChecked():

            if len(patient_name) != 0:
                if len(patient_surname) != 0:
                    if int(a) < int(b):
                        if int(a) > 1900:
                            if patient_cinsiyet != "Cinsiyet Seçiniz":
                                if patient_mother_name != 0:
                                    if patient_father_name != 0:
                                        if patient_e_posta != 0 and re.search("@", patient_e_posta):
                                            if re.search("com", patient_e_posta):
                                                if len(patient_phone) == 10:
                                                    if len(patient_adress) > 20:
                                                        if len(patient_TCKN) == 11:
                                                            connection = sqlite3.connect("sqlite/patient_info.sqlite")
                                                            connection.execute(
                                                                "INSERT INTO patients_inf VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
                                                                (
                                                                    patient_name.upper(), patient_surname.upper(),
                                                                    patient_birtday,
                                                                    patient_nationality, patient_TCKN,
                                                                    patient_passaport.upper(), patient_cinsiyet.upper(),
                                                                    patient_mother_name.upper(),
                                                                    patient_father_name.upper(),
                                                                    patient_e_posta, patient_phone,
                                                                    patient_adress.upper(), patient_TC_yok.upper()))
                                                            connection.commit()
                                                            connection.close()

                                                            self.register_done()
                                                        else:
                                                            self.uyari_msg_text = "Hatalı Yada Eksik TC NO"
                                                            self.uyari_msg()
                                                    else:
                                                        self.uyari_msg_text = "Hatalı Yada Eksik ADRES"
                                                        self.uyari_msg()
                                                else:
                                                    self.uyari_msg_text = "Hatalı Yada Eksik TELEFON NUMARASI"
                                                    self.uyari_msg()
                                            else:
                                                self.uyari_msg_text = "Hatalı Yada Eksik E-POSTA"
                                                self.uyari_msg()
                                        else:
                                            self.uyari_msg_text = "Hatalı Yada Eksik E-POSTA"
                                            self.uyari_msg()
                                    else:
                                        self.uyari_msg_text = "Hatalı Yada Eksik BABA ADI"
                                        self.uyari_msg()
                                else:
                                    self.uyari_msg_text = "Hatalı Yada Eksik ANNE ADI"
                                    self.uyari_msg()
                            else:
                                self.uyari_msg_text = "Hatalı Yada Eksik CİNSİYET BİLGİSİ"
                                self.uyari_msg()
                        else:
                            self.uyari_msg_text = "Hatalı Yada Eksik DOĞUM TARİHİ"
                            self.uyari_msg()
                    else:
                        self.uyari_msg_text = "Hatalı Yada Eksik DOĞUM TARİHİ"
                        self.uyari_msg()
                else:
                    self.uyari_msg_text = "Hatalı Yada Eksik SOYAD"
                    self.uyari_msg()
            else:
                self.uyari_msg_text = "Hatalı yada eksik İSİM"
                self.uyari_msg()

        # endregion


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_hasta_kayit_window()
    ui.setupUi(MainWindow)
    MainWindow.setWindowIcon(QtGui.QIcon("icons/patient.png"))
    MainWindow.show()

    sys.exit(app.exec_())
