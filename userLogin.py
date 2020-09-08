import os
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon

# from new_users_page import *

from patientRegister import *
from userRegister import *
import warnings
warnings.simplefilter("ignore")
from PyQt5.QtGui import QIcon, QPixmap, QPalette, QImage, QBrush


class Ui_MainWindow(object):

    def baglanti_olustur(self):
        baglanti = sqlite3.connect("sqlite/patient_info.sqlite")
        self.cursor = baglanti.cursor()
        self.cursor.execute("Create Table If not exists users(user_name TEXT,password TEXT)")
        baglanti.commit()


    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(600, 450)
        MainWindow.setStyleSheet("""QLineEdit {
                    border-style: outset;
                    border-width: 2px;
                    border-radius: 10px;
                    border-color: black;
                    
                    font: bold 15px;
                    min-width: 10em;
                    padding: 6px;
                    }QPushButton {background-color: white; border-style: outset;border-width: 2px;border-radius: 10px;border-color: black; }
                    QPushButton:hover:!pressed{border: 1px solid green;}
                    QLineEdit:hover:!pressed{border: 1px solid green;}
                    QDateEdit:hover:!pressed{border: 1px solid green;}
                    QCheckBox::hover:!pressed{border: 1px }""")

        # oImage = QImage("saydam2.jpg")
        # sImage = oImage.scaled(QtCore.QSize(600, 450))
        # palette = QPalette()
        # palette.setBrush(QPalette.Window, QtGui.QBrush(sImage))
        # MainWindow.setPalette(palette)

        self.baglanti_olustur()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.header_label = QtWidgets.QLabel(self.centralwidget)
        self.header_label.setGeometry(QtCore.QRect(110, 20, 500, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.header_label.setFont(font)
        self.header_label.setTextFormat(QtCore.Qt.PlainText)
        self.header_label.setObjectName("header_label")
        self.header_label.setStyleSheet('QLabel{color: darkblack}')

        # self.background_label = QtWidgets.QLabel(self.centralwidget)
        # self.background_label.setPixmap(QPixmap("arka.png"))
        # self.background_label.setGeometry(1, 1, 600, 100)

        pic = QtWidgets.QLabel(self.centralwidget)
        pic.setGeometry(105, 80, 50, 100)
        # use full ABSOLUTE path to the image, not relative
        pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/icons/qwert.png"))

        self.user_name_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.user_name_edit.setGeometry(QtCore.QRect(140, 113, 360, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.user_name_edit.setFont(font)

        self.user_name_edit.setObjectName("user_name_edit")

        self.password_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.password_edit.setGeometry(QtCore.QRect(140, 160, 360, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.password_edit.setFont(font)
        self.password_edit.setObjectName("password_edit")
        self.password_edit.setEchoMode(QtWidgets.QLineEdit.Password)


        pic2 = QtWidgets.QLabel(self.centralwidget)
        pic2.setGeometry(105, 132, 30, 100)
        pic2.setPixmap(QtGui.QPixmap(os.getcwd() + "/icons/password2.png"))

        self.robot_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.robot_checkbox.setGeometry(QtCore.QRect(325, 200, 250, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.robot_checkbox.setFont(font)
        self.robot_checkbox.setObjectName("robot_checkbox")
        self.robot_checkbox.setIcon(QtGui.QIcon("icons/robot2.png"))

        self.login_buton = QtWidgets.QPushButton(self.centralwidget)
        self.login_buton.setGeometry(QtCore.QRect(100, 230, 165, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.login_buton.setFont(font)
        self.login_buton.setObjectName("login_buton")
        self.login_buton.clicked.connect(self.log_in)
        self.login_buton.setIcon(QtGui.QIcon("icons/enter.png"))

        self.webcam_login = QtWidgets.QPushButton(self.centralwidget)
        self.webcam_login.setGeometry(QtCore.QRect(270, 230, 235, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.webcam_login.setFont(font)
        self.webcam_login.setObjectName("webcam_Login")
        self.webcam_login.clicked.connect(self.webcam_login_ol)
        self.webcam_login.setIcon(QtGui.QIcon("icons/video-call.png"))

        # self.yazi_alani = QtWidgets.QLabel(self.centralwidget)
        # self.yazi_alani.setGeometry(80, 370, 500, 60)
        # font = QtGui.QFont()
        #
        # self.yazi_alani.setFont(QtGui.QFont('SansSerif', 13))
        # self.yazi_alani.setObjectName("yazi_alani")

        self.new_user = QtWidgets.QPushButton(self.centralwidget)
        self.new_user.setGeometry(QtCore.QRect(100, 285, 405, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.new_user.setFont(font)
        self.new_user.setObjectName("new_user")
        self.new_user.clicked.connect(self.new_user_add)
        self.new_user.setIcon(QtGui.QIcon("icons/plus.png"))

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "KULLANICI GİRİŞİ"))
        self.header_label.setText(_translate("MainWindow", "AUROLAB SİSTEMİNE GİRİŞ"))
        self.robot_checkbox.setText(_translate("MainWindow", "Ben robot değilim"))
        self.login_buton.setText(_translate("MainWindow", "GİRİŞ YAP"))

        self.new_user.setText(_translate("MainWindow", "ÜYE OL"))
        self.webcam_login.setText(_translate("MainWindow", "KAMERA İLE GİRİŞ YAP"))
        # self.yazi_alani.setText(_translate("MainWindow", ""))

    def after_entered(self):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setIcon(QtWidgets.QMessageBox.Information)
        msg_box.setText("Yeni hasta eklemek istermisiniz ? ")
        msg_box.setWindowTitle("Uyarı Ekranı")

        msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)

        returnValue = msg_box.exec()
        if returnValue == msg_box.Ok:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_hasta_kayit_window()

            self.ui.setupUi(self.window)
            self.window.show()
        else:
            print("yeni sayfa yakında gelecek")

    def log_in(self):

        user_name_text = self.user_name_edit.text()

        password_text = self.password_edit.text()
        self.cursor.execute("Select * From users Where user_name = ? and password = ?",
                            (user_name_text, password_text))
        data = self.cursor.fetchall()

        if len(data) != 0:
            if self.robot_checkbox.isChecked():
                MainWindow.hide()
                # self.robot_ui()
                self.after_entered()

            else:

                self.msg_box = QtWidgets.QMessageBox()

                self.msg_box.setIcon(QtWidgets.QMessageBox.Information)

                self.msg_box.setText("Lütfen robot değilim seçeneğini aktif ediniz")

                self.msg_box.setWindowTitle("Uyarı !")

                self.msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)

                self.returnValue = self.msg_box.exec()


        else:

            self.msg_box = QtWidgets.QMessageBox()

            self.msg_box.setIcon(QtWidgets.QMessageBox.Information)

            self.msg_box.setText("Hatalı yada eksik giriş yaptınız ! ")

            self.msg_box.setWindowTitle("Uyarı !")

            self.msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)

            self.returnValue = self.msg_box.exec()

            # self.yazi_alani.setText("Hatalı işlem yaptınız Lütfen tekrar deneyiniz")

    def new_user_add(self):
        self.msg_box = QtWidgets.QMessageBox()
        self.msg_box.setIcon(QtWidgets.QMessageBox.Information)
        self.msg_box.setText("Yüz tarama ile üye olmak ister misiniz ? ")
        self.msg_box.setWindowTitle("Bilgi Ekranı")

        self.msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)

        self.returnValue = self.msg_box.exec()
        if self.returnValue == self.msg_box.Ok:
            import photoMaster
            photoMaster
            import modelTrain
            modelTrain
        else:
            self.window = QtWidgets.QMainWindow()
            self.ui = saver_UserWindow()
            self.ui.setupUi(self.window)
            self.window.show()

    def webcam_login_ol(self):
        import photoResult
        photoResult
        MainWindow.hide()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setWindowIcon(QtGui.QIcon("user-1.png"))

    MainWindow.show()
    sys.exit(app.exec_())
