import os
import sqlite3
# import cv2
import numpy as np
# from AI_login import Ui_MainWindow

from PyQt5 import QtCore, QtGui, QtWidgets


class saver_UserWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        MainWindow.setMinimumSize(QtCore.QSize(600, 400))
        MainWindow.setMaximumSize(QtCore.QSize(600, 400))
        MainWindow.setWindowIcon(QtGui.QIcon("icons/add-f.png"))
        MainWindow.setStyleSheet("""QLineEdit {
                            border-style: outset;
                            border-width: 2px;
                            border-radius: 10px;
                            border-color: black;
                            font: bold 15px;
                            min-width: 10em;
                            padding: 6px;
                            }QPushButton {background-color: white; border-style: outset;border-width: 2px;border-radius: 10px;border-color: black;}
                            QPushButton:hover:!pressed{border: 1px solid green;}
                            QLineEdit:hover:!pressed{border: 1px solid green;}
                            QDateEdit:hover:!pressed{border: 1px solid green;}""")


        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.user_save_label = QtWidgets.QLabel(self.centralwidget)
        self.user_save_label.setGeometry(QtCore.QRect(195, 10, 300, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.user_save_label.setFont(font)
        self.user_save_label.setObjectName("user_save_label")

        pic1 = QtWidgets.QLabel(self.centralwidget)
        pic1.setGeometry(130, 70, 50, 100)
        pic1.setPixmap(QtGui.QPixmap(os.getcwd() + "/icons/qwert.png"))

        pic3 = QtWidgets.QLabel(self.centralwidget)
        pic3.setGeometry(130, 115, 50, 100)
        pic3.setPixmap(QtGui.QPixmap(os.getcwd() + "/icons/password2.png"))


        self.new_user_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.new_user_lineEdit.setGeometry(QtCore.QRect(170, 100, 300, 40))
        self.new_user_lineEdit.setObjectName("new_user_lineEdit")


        self.new_password_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.new_password_lineEdit.setGeometry(QtCore.QRect(170, 145, 300, 40))
        self.new_password_lineEdit.setObjectName("new_password_lineEdit")
        self.new_password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)

        self.okey_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.okey_checkBox.setGeometry(QtCore.QRect(170, 200, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.okey_checkBox.setFont(font)
        self.okey_checkBox.setObjectName("okey_checkBox")

        self.save_buton = QtWidgets.QPushButton(self.centralwidget)
        self.save_buton.setGeometry(QtCore.QRect(165, 250, 100, 40))
        self.save_buton.setObjectName("save_buton")
        self.save_buton.clicked.connect(self.save_me)
        self.save_buton.setIcon(QtGui.QIcon("icons/file.png"))

        self.mainmenu_buton = QtWidgets.QPushButton(self.centralwidget)
        self.mainmenu_buton.setGeometry(QtCore.QRect(268, 250, 200, 40))
        self.mainmenu_buton.setObjectName("mainmenu_buton")
        self.mainmenu_buton.clicked.connect(MainWindow.close)
        self.mainmenu_buton.setIcon(QtGui.QIcon("icons/main_page.png"))

        self.msg_box = QtWidgets.QMessageBox()
        self.msg_box.setIcon(QtWidgets.QMessageBox.Information)
        self.msg_box.setWindowTitle("Uyarı !")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Kaydol"))
        self.user_save_label.setText(_translate("MainWindow", "YENİ KULLANICI KAYDET"))

        self.okey_checkBox.setText(_translate("MainWindow", "Onaylıyorum"))
        self.save_buton.setText(_translate("MainWindow", "Kaydet"))
        self.mainmenu_buton.setText(_translate("MainWindow","Anasayfaya Dön"))

    def message_func(self):
        self.msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
        self.returnValue = self.msg_box.exec()

    # def sql(self):
    #     self.cursor.execute("Select * From users Where user_name = ? and password = ?",
    #                         (user_name_text, password_text))
    #     data = self.cursor.fetchall()

    def save_me(self):
        add_user = self.new_user_lineEdit.text()
        add_password = self.new_password_lineEdit.text()



        if len(add_user) != 0:
            if len(add_password) != 0:
                if self.okey_checkBox.isChecked():
                    self.msg_box = QtWidgets.QMessageBox()
                    self.msg_box.setIcon(QtWidgets.QMessageBox.Information)
                    self.msg_box.setText("Kayıt Başarılı ..")
                    self.msg_box.setWindowTitle("Bilgi ")
                    self.msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
                    self.returnValue = self.msg_box.exec()
                    # self.yazi_labeli.setText("Kayıt başarıyla oluşturulmuştur")
                    connection = sqlite3.connect("sqlite/patient_info.sqlite")
                    connection.execute("INSERT INTO users VALUES (?,?)", (add_user, add_password))
                    connection.commit()
                    connection.close()
                else:
                    self.msg_box.setText("Lütfen onaylayınız !")
                    self.message_func()
            else:
                self.msg_box.setText("Lütfen şifre giriniz ! ")
                self.message_func()
        else:
            self.msg_box.setText("Lütfen kullanıcı adı giriniz")
            self.message_func()








if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = saver_UserWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
