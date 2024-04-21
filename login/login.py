from PyQt5 import QtCore, QtGui, QtWidgets
from mainMenu.admin import Ui_MainWindowAdmin
from mainMenu.gest import Ui_MainWindowGest
import mysql.connector

class Ui_DialogLogin(object):
    def setupUi(self, DialogLogin):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="oussama",
            password="projet2cp",
            database="projet2cp",
            port="3306"
        )
        DialogLogin.setObjectName("DialogLogin")
        DialogLogin.resize(1200, 800)
        DialogLogin.setMinimumSize(QtCore.QSize(1200, 800))
        DialogLogin.setMaximumSize(QtCore.QSize(1200, 800))
        self.verticalLayout = QtWidgets.QVBoxLayout(DialogLogin)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(DialogLogin)
        self.widget.setMinimumSize(QtCore.QSize(1200, 800))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.widget.setFont(font)
        self.widget.setStyleSheet("QWidget#widget{\n"
                                  "border-image: url(:/resources_login/image 1.png);\n"
                                  "background-position: center;\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton#pushButton:hover{\n"
                                  "    \n"
                                  "    background-color: rgb(38, 92, 179);\n"
                                  "}\n"
                                  "\n"
                                  "\n"
                                  "")
        self.widget.setObjectName("widget")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(420, 180, 400, 401))
        self.widget_2.setMinimumSize(QtCore.QSize(400, 400))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.widget_2.setFont(font)
        self.widget_2.setStyleSheet("\n"
                                    "background-color: rgb(249, 249, 249);\n"
                                    "border-radius:20px;\n"
                                    "\n"
                                    "")
        self.widget_2.setObjectName("widget_2")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(78, 20, 245, 58))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(29)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(26, 61, 119);")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit.setGeometry(QtCore.QRect(73, 110, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(211, 211, 211);\n"
                                    "border-radius: 10px;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(73, 180, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgb(211, 211, 211);\n"
                                      "border-radius: 10px;")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        self.pushButton.setGeometry(QtCore.QRect(118, 250, 161, 35))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "border-radius: 10px;\n"
                                      "\n"
                                      "\n"
                                      "    background-color: rgb(26, 61, 119);\n"
                                      "\n"
                                      "\n"
                                      "")
        self.pushButton.setCheckable(True)
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(130, 300, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_2.setStyleSheet("color: rgb(122, 122, 122);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setGeometry(QtCore.QRect(22, 110, 40, 40))
        self.label_3.setStyleSheet("background-color: rgba(102, 102, 102,0.1);")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/resources_login/user.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setGeometry(QtCore.QRect(22, 180, 40, 40))
        self.label_4.setStyleSheet("background-color: rgba(102, 102, 102,0.1);")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/resources_login/key.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(DialogLogin)
        QtCore.QMetaObject.connectSlotsByName(DialogLogin)
        self.pushButton.clicked.connect(self.login)
        # modify dialog login icon
        DialogLogin.setWindowIcon(QtGui.QIcon('../resourcesGenerales/iconGC.png'))

    def retranslateUi(self, DialogLogin):
        _translate = QtCore.QCoreApplication.translate
        DialogLogin.setWindowTitle(_translate("DialogLogin", "Dialog"))
        self.label.setText(_translate("DialogLogin", "Connectez-vous"))
        self.lineEdit.setPlaceholderText(_translate("DialogLogin", " Nom d\'utilisateur"))
        self.lineEdit_2.setPlaceholderText(_translate("DialogLogin", " Mot de passe"))
        self.pushButton.setText(_translate("DialogLogin", "Se connecter"))
        self.label_2.setText(_translate("DialogLogin", "Mot de passe oublié ? "))

    def login(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        if self.pushButton.isChecked() and self.verify_admin(username, password):
            DialogLogin.accept()
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindowAdmin()
            self.ui.setupUi(self.window)
            self.window.show()
            self.lineEdit.setText("")
            self.lineEdit_2.setText("")
        elif self.pushButton.isChecked() and self.verify_gestionnaire(username, password):
            DialogLogin.accept()
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindowGest()
            self.ui.setupUi(self.window)
            self.window.show()
            self.lineEdit.setText("")
            self.lineEdit_2.setText("")
        elif self.lineEdit.text() == "" or self.lineEdit_2.text() == "":
            # show a message box to the user that the username or password is empty
            self.msg = QtWidgets.QMessageBox()
            self.msg.setIcon(QtWidgets.QMessageBox.Critical)
            self.msg.setText("Veuillez remplir tous les champs.")
            self.msg.setWindowTitle("Erreur")
            # set message box icon
            self.msg.setWindowIcon(QtGui.QIcon('../resourcesGenerales/iconGC.png'))
            self.msg.exec_()
        else:
            # show a message box to the user that the username or password is incorrect
            self.msg = QtWidgets.QMessageBox()
            self.msg.setIcon(QtWidgets.QMessageBox.Critical)
            self.msg.setText("Nom d'utilisateur ou mot de passe incorrect veuillez réessayer.")
            self.msg.setWindowTitle("Erreur")
            self.msg.setWindowIcon(QtGui.QIcon('../resourcesGenerales/iconGC.png'))
            self.msg.exec_()
            self.lineEdit.setText("")
            self.lineEdit_2.setText("")

    def verify_admin(self, username, password):
        mycursor = self.mydb.cursor()
        query = " SELECT * FROM admin WHERE nom = %s AND mot_de_passe = %s "
        values = (username, password)
        mycursor.execute(query, values)
        result = mycursor.fetchall()
        mycursor.close()
        return bool(result)
    def verify_gestionnaire(self, username, password):
        mycursor = self.mydb.cursor()
        query = " SELECT * FROM gestionnaire WHERE nom = %s AND mot_de_passe = %s "
        values = (username, password)
        mycursor.execute(query, values)
        result = mycursor.fetchall()
        mycursor.close()
        return bool(result)

import resources_login_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogLogin = QtWidgets.QDialog()
    ui = Ui_DialogLogin()
    ui.setupUi(DialogLogin)
    DialogLogin.show()
    sys.exit(app.exec_())